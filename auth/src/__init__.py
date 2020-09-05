from flask import Flask

app = Flask(__name__)


def create_app():
    app = Flask(__name__)

    from src.routes.users import users

    app.register_blueprint(users)

    return app