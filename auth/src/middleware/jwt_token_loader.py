from src import jwt
from src import revoked_store


@jwt.expired_token_loader
def expired_token_cb(expired_token):
    return {"errors": [{"message": "Unauthorized"}]}, 401


@jwt.invalid_token_loader
def invalid_token_cb(expired_token):
    return {"errors": [{"message": "Unauthorized"}]}, 401


@jwt.unauthorized_loader
def unauthorized_cb(expired_token):
    return {"errors": [{"message": "Unauthorized"}]}, 401


@jwt.revoked_token_loader
def revoked_token_cb():
    return {"errors": [{"message": "Unauthorized"}]}, 401


@jwt.token_in_blacklist_loader
def check_if_token_is_revoked(decrypted_token):
    jti = decrypted_token["jti"]
    return revoked_store.exists(jti)
