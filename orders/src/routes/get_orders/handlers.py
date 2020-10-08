from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from common.errors.not_found_error import NotFoundError

from src.crud import get_orders_by_user_id, get_order_by_user_id
from src.serializers import serialize_orders_by_user_id


@jwt_required
def get_orders():
    user_id = get_jwt_identity()["id"]

    orders = get_orders_by_user_id(user_id)
    orders = serialize_orders_by_user_id(orders)

    return jsonify(orders)


@jwt_required
def get_order(order_id):
    user_id = get_jwt_identity()["id"]

    order = get_order_by_user_id(user_id, order_id)
    if not order:
        raise NotFoundError("Order not found!")

    order = serialize_orders_by_user_id([order])

    return jsonify(order[0])
