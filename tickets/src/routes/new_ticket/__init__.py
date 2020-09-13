from flask import Blueprint
import src.routes.new_ticket.handlers as H

new_ticket = Blueprint("new_ticket", __name__)


new_ticket.route("/api/tickets", methods=["POST"])(H.create_new_ticket)
