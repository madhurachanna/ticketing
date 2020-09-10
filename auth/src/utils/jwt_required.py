from functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from src.errors.jwt_token_validation_error import JwtTokenValidationError


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args, **kwargs)
        except:
            raise JwtTokenValidationError()
    return wrapper
