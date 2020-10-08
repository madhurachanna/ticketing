from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from common.errors.not_found_error import NotFoundError

from src.crud import get_order, delete_order
from src.serializers import serialize_orders_by_user_id


@jwt_required
def del_order(order_id):
    user_id = get_jwt_identity()["id"]

    order = get_order(user_id, order_id)
    if not order:
        raise NotFoundError("Order not found!")

    order = delete_order(order.Order)
    order = serialize_orders_by_user_id([order])

    return jsonify(order[0]), 200
