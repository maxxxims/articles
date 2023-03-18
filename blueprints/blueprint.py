from flask import Blueprint, render_template, request
from model.model import CLASSIFIER
import json


#############           INIT                 #############
with open('constants.txt', 'r', encoding='utf-8') as file:
    data = json.loads(file.read())
    DOMAIN = data['DOMAIN']
    PORT = data['PORT']
    PATH_TO_MODEL = data['PATH_TO_MODEL']
    PATH_TO_CSV = data['PATH_TO_CSV']


mainpage = Blueprint('main_page', __name__, template_folder='templates')
model = CLASSIFIER(path_to_model=PATH_TO_MODEL, path_to_csv=PATH_TO_CSV)


def get_context() -> dict:
    category_url = DOMAIN + '/predict_category'
    media_url = DOMAIN + '/predict_media'
    media_profile_url = DOMAIN + '/find_media'
    context = {
        'category_url': category_url,
        'media_url':    media_url,
        'media_profile_url': media_profile_url,
            }
    return context


@mainpage.route("/")
def index():
    context = get_context()
    return render_template('index2.html', **context)


@mainpage.route("/predict_category", methods=["POST"])
def predict():
    r = request.json
    category, proba = model.predict(r.get('title', ' '), r.get('text', ' '))
    return {'status': 200, 'category': category, 'proba': proba}


@mainpage.route("/predict_media", methods=["POST"])
def predict_media():
    r = request.json
    category = model.predict_media(r.get('media', ' '))
    if not category:
        return {'status': 404, 'category': category}
    else:
        return {'status': 200, 'category': category}
    

@mainpage.route("/find_media", methods=["POST"])
def find_media():
    r = request.json
    data = model.find_in_table(r.get('media', ' '))
    if not data:
        return {'status': 404, 'category': data}
    return {'status': 200, 'data': data}