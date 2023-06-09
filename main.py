from flask import Flask
from blueprints.blueprint import mainpage, PORT


app = Flask(__name__)
app.register_blueprint(mainpage)


if __name__ == '__main__':
    app.run(port=PORT)