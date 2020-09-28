from flask import request
from flask_jwt_extended import create_access_token, jwt_required
from common.errors.bad_request_error import BadRequestError
from common.middleware.request_validator import request_validator
import pika

from src.validators.signup import SignUpValidator
import src.crud as C
from src.config import Config


@request_validator(SignUpValidator)
def signup():
    usr = request.valid_req

    existing_usr = C.get_user_by_email(usr.email)
    if existing_usr:
        raise BadRequestError("User already exists")

    newUsr = C.add_new_user(usr)
    return {"access_token": create_access_token(newUsr)}, 201


@jwt_required
def protected():
    URL = Config.BROKER
    print(URL)
    connection = pika.BlockingConnection(pika.URLParameters(URL))
    channel = connection.channel()
    channel.queue_declare(queue="hello")
    channel.basic_publish(exchange="", routing_key="hello", body="Hello")
    print(" [x] Sent 'Hello World!'", flush=True)
    connection.close()
    return "protected"
