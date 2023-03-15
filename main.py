from flask import Flask
from blueprints.mainpage import mainpage


app = Flask(__name__)
app.register_blueprint(mainpage)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run()