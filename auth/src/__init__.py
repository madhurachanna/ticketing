from flask import Flask

app = Flask(__name__)


def create_app():
    app = Flask(__name__)

    from src.routes.signup import signup
    from src.middleware.error_handler import errors

    app.register_blueprint(errors)
    app.register_blueprint(signup)

    return app
