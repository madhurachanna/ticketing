from flask import request
from flask_jwt_extended import create_access_token

from src.validators.signin import signin_req_validate
from src.errors.authentication_error import AuthenticationError
import src.crud as C


@signin_req_validate
def signin():
    usr = request.valid_req

    existing_usr = C.get_user_by_email(usr.email)
    if not existing_usr or not existing_usr.check_password(usr.password):
        raise AuthenticationError("Incorrect username or password")

    return {"access_token": create_access_token(existing_usr.dict())}
