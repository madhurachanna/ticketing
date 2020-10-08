from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from src.crud import get_orders_by_user_id
from src.serializers import serialize_orders_by_user_id


@jwt_required
def get_orders():
    user_id = get_jwt_identity()["id"]

    orders = get_orders_by_user_id(user_id)
    orders = serialize_orders_by_user_id(orders)

    return jsonify(orders)
