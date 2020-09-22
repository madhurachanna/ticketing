from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import redis

from src.config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
session = db.session
bcrypt = Bcrypt()
jwt = JWTManager()
revoked_store = redis.StrictRedis(
    host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=0, decode_responses=True
)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()

    from common.middleware.error_handler import errors
    from src.routes.signup import signup
    from src.routes.signin import signin
    from src.routes.signout import signout
    from src.routes.current_user import current_user

    app.register_blueprint(errors)
    app.register_blueprint(signup)
    app.register_blueprint(signin)
    app.register_blueprint(signout)
    app.register_blueprint(current_user)

    return app


import src.middleware.jwt_token_loader
from src.models import *
