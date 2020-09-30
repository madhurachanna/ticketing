from flask import Blueprint
import src.routes.new_order.handlers as H

new_order = Blueprint("new_order", __name__)


new_order.route("/api/orders", methods=["POST"])(H.create_new_order)
