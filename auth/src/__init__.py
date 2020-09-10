from flask import Flask
from src.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
session = db.session
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()

    from src.middleware.error_handler import errors
    from src.routes.signup import signup
    from src.routes.signin import signin
    app.register_blueprint(errors)
    app.register_blueprint(signup)
    app.register_blueprint(signin)

    return app


from src.models import *