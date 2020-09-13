from functools import wraps
from flask_jwt_extended import verify_jwt_in_request

from src import jwt, revoked_store


@jwt.token_in_blacklist_loader
def check_if_token_is_revoked(decrypted_token):
    jti = decrypted_token["jti"]
    return revoked_store.exists(jti)


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        return fn(*args, **kwargs)

    return wrapper
