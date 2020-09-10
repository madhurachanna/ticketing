from flask_jwt_extended import get_raw_jwt

from src.utils.jwt_required import jwt_required
from src.utils.jwt_access_revoke import set_jwt_access_revoke


@jwt_required
def signout():
    jti = get_raw_jwt()["jti"]
    set_jwt_access_revoke(jti, "true")
    return "Logout successful", 200
