from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import redis

from src.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
session = db.session
jwt = JWTManager()
revoked_store = redis.StrictRedis(
    host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=0, decode_responses=True
)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()

    from src.middleware.error_handler import errors
    from src.routes.new_ticket import new_ticket
    from src.routes.get_tickets import get_tickets

    app.register_blueprint(new_ticket)
    app.register_blueprint(get_tickets)
    app.register_blueprint(errors)

    return app


from src.models import *
