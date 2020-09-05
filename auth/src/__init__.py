from flask import Flask

app = Flask(__name__)


def create_app():
    app = Flask(__name__)

    from src.routes.hello.api import hello

    app.register_blueprint(hello)

    return app