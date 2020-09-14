from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import jsonify


@jwt_required
def current_user():
    return jsonify(get_jwt_identity())
