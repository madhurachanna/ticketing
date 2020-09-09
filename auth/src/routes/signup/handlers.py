from flask import request
from pydantic import ValidationError

from src.validators.user import User
from src.errors.request_validation_error import RequestValidationError
import src.crud as C


def signup():
    try:
        req = request.get_json() or {}
        User(**req)
        user = C.get_user_by_email(req['email'])

    except ValidationError as e:
        raise RequestValidationError(e.errors())

    return "Signup"
