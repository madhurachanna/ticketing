from functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from src.errors.authentication_error import AuthenticationError


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args, **kwargs)
        except:
            raise AuthenticationError()
    return wrapper
