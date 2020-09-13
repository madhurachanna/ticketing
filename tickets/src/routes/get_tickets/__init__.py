from flask import Blueprint
import src.routes.get_tickets.handlers as H

get_tickets = Blueprint("get_tickets", __name__)


get_tickets.route("/api/tickets", methods=["GET"])(H.get_tickets)
get_tickets.route("/api/tickets/<ticket_id>", methods=["GET"])(H.get_ticket)
