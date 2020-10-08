from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from src.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
session = db.session
jwt = JWTManager()
# revoked_store = redis.StrictRedis(
#   host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=0, decode_responses=True
# )

from src.models import *


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()

    from common.middleware.error_handler import errors

    from src.routes.new_order import new_order
    from src.routes.get_orders import get_orders
    from src.routes.del_order import del_order
    from src.tests import tests

    app.register_blueprint(new_order)
    app.register_blueprint(get_orders)
    app.register_blueprint(del_order)
    app.register_blueprint(errors)
    app.register_blueprint(tests)

    return app


import src.middleware.jwt_token_loader
