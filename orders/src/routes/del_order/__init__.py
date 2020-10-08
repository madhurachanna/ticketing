from flask import Blueprint
import src.routes.del_order.handlers as H

del_order = Blueprint("del_order", __name__)


del_order.route("/api/orders/<order_id>", methods=["DELETE"])(H.del_order)
