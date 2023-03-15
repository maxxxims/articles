from flask import Blueprint, render_template, abort, request
from model.model import CLASSIFIER, test

DOMAIN = 'http://127.0.0.1:5000'
PATH_TO_MODEL = 'model/catboost_model'

mainpage = Blueprint('main_page', __name__, template_folder='templates')
model = CLASSIFIER(path=PATH_TO_MODEL)


def get_context() -> dict:
    category_url = DOMAIN + '/predict_category'
    context = {
        'category_url': category_url
            }
    return context


@mainpage.route("/")
def index():
    context = get_context()
    return render_template('index.html', **context)


@mainpage.route("/predict_category", methods=["POST"])
def predict():
    r = request.json
    category, proba = model.predict(r.get('title', ' '), r.get('text', ' '))
    return {'msg': 'ok', 'category': category, 'proba': proba}