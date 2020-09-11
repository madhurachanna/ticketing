from flask_jwt_extended import get_jwt_identity

from src.utils.jwt_required import jwt_required


@jwt_required
def current_user():
    return {"currentUser": get_jwt_identity()}
