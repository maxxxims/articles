from flask import Blueprint, render_template, abort, request
from model.model import CLASSIFIER, test

mainpage = Blueprint('main_page', __name__,
                        template_folder='templates')

path_to_model = 'model/catboost_model'
model = CLASSIFIER(path=path_to_model)


@mainpage.route("/main")
def index():
    
    return render_template('index.html')


@mainpage.route("/predict_category", methods=["GET", "POST"])
def predict():
    r = request.json
    print(r)
    category, proba = model.predict(r.get('title', ' '), r.get('text', ' '))
    return {'msg': 'ok', 'category': category, 'proba': proba}