from flask import request
from flask_jwt_extended import create_access_token, jwt_required
from common.errors.bad_request_error import BadRequestError
from common.middleware.request_validator import request_validator


from src.validators.signup import SignUpValidator
import src.crud as C


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
    return "protected"
