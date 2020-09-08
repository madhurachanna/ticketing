from flask import Flask
from src.config import Config
from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db = SQLAlchemy()
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from src.routes.signup import signup
    from src.middleware.error_handler import errors
    app.register_blueprint(errors)
    app.register_blueprint(signup)

    return app
