from flask import request
from pydantic import ValidationError

from src.models.validators.user import User
from src.errors.request_validation_error import RequestValidationError


def signup():
    try:
        req = request.get_json() or {}
        User(**req)
    except ValidationError as e:
        raise RequestValidationError(e.errors())

    return "Signup"
