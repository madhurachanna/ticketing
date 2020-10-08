from flask import Blueprint
import src.routes.get_orders.handlers as H

get_orders = Blueprint("get_orders", __name__)


get_orders.route("/api/orders", methods=["GET"])(H.get_orders)
get_orders.route("/api/orders/<order_id>", methods=["GET"])(H.get_order_by_id)
