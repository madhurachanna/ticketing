from flask import Blueprint, request

# from src.models.tickets import Ticket
from src.crud import get_all_tickets, create_ticket as ct

tests = Blueprint("tests", __name__)


@tests.route("/api/orders/tickets", methods=["GET"])
def get_tickets():
    tickets = get_all_tickets()
    print("ticket", tickets, flush=True)
    tickets = [i.serialize() for i in tickets]
    return {"tickets": tickets}


@tests.route("/api/orders/tickets", methods=["POST"])
def create_ticket():
    print("creat ticket", flush=True)
    req = request.get_json()
    print("req", req)
    tickets = ct(req)
    print("ticket", tickets.serialize(), flush=True)
    return tickets.serialize()
