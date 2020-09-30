from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from common.errors.not_found_error import NotFoundError
from common.errors.bad_request_error import BadRequestError
from common.middleware.request_validator import request_validator

from src.crud.tickets import ticket_by_id
from src.crud.orders import create_new_order as new_order
from src.validators.new_order import NewOrderValidatior


@jwt_required
@request_validator(NewOrderValidatior)
def create_new_order():
    req = request.get_json() or {}

    ticket = ticket_by_id(req["ticket_id"])
    if not ticket:
        raise NotFoundError("Ticket not found")

    is_reserved = ticket.is_reserved()
    if is_reserved:
        raise BadRequestError("Ticket is already reserved")

    user_id = get_jwt_identity()["id"]
    order = new_order({**req, "user_id": user_id})

    return order.serialize(), 201
