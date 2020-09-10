from flask import request
from pydantic import ValidationError
from flask_jwt_extended import create_access_token

from src.validators.user import SignInValid
from src.errors.request_validation_error import RequestValidationError
from src.errors.authentication_error import AuthenticationError
import src.crud as C


def signin():
    try:
        usr = SignInValid(**(request.get_json() or {}))

        existing_usr = C.get_user_by_email(usr.email)
        if(not existing_usr or not existing_usr.check_password(usr.password)):
            raise AuthenticationError('incorrect username or password')

        return {'access_token': create_access_token(existing_usr.dict())}

    except ValidationError as e:
        raise RequestValidationError(e.errors())
