from flask_jwt_extended import get_raw_jwt, jwt_required

from src.utils.jwt_token_blacklist import add_token_to_blacklist


@jwt_required
def signout():
    jti = get_raw_jwt()["jti"]
    add_token_to_blacklist(jti, "true")
    return "Logout successful", 200
