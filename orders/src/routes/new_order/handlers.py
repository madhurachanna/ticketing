from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from common.errors.not_found_error import NotFoundError
from common.errors.bad_request_error import BadRequestError
from common.middleware.request_validator import request_validator

from src.crud import order_by_reserved_ticket_id, ticket_by_id, create_order
from src.validators.new_order import NewOrderValidatior


# @jwt_required
# @request_validator(NewOrderValidatior)
def create_new_order():
    req = request.get_json() or {}

    ticket = ticket_by_id(req["ticket_id"])
    if not ticket:
        raise NotFoundError("Ticket not found")

    is_reserved = order_by_reserved_ticket_id(ticket.id)
    if is_reserved:
        raise BadRequestError("Ticket is already reserved")

    print("is_reserved", is_reserved, flush=True)

    # user_id = get_jwt_identity()["id"]
    order = create_order({**req, "user_id": "zyz"})

    return order.serialize(), 201
