from flask import Flask
from blueprints.blueprint import mainpage


app = Flask(__name__)
app.register_blueprint(mainpage)


if __name__ == '__main__':
    app.run()