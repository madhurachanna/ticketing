from flask import request
from pydantic import ValidationError
from flask_jwt_extended import (
    create_access_token,  get_jwt_identity
)

from src.validators.user import SignUpValid
from src.errors.request_validation_error import RequestValidationError
from src.errors.bad_request_error import BadRequestError
from src.utils.jwt_required import jwt_required
import src.crud as C


def signup():
    try:
        usr = SignUpValid(**(request.get_json() or {}))

        existing_usr = C.get_user_by_email(usr.email)
        if(existing_usr):
            raise BadRequestError('user already exists')

        newUsr = C.add_new_user(usr)
        print(newUsr)
        return {'access_token': create_access_token(newUsr)}

    except ValidationError as e:
        raise RequestValidationError(e.errors())

    return "Signup"


@jwt_required
def protected():
    return 'protected'
