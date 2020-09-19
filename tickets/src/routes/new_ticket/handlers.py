from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

from src.validators.new_ticket import NewTicketValidator
from src.crud import add_new_ticket
from src.middleware.request_validator import request_validator


@jwt_required
@request_validator(NewTicketValidator)
def create_new_ticket():
    user_id = get_jwt_identity()["id"]
    ticket = add_new_ticket({**request.get_json(), "user_id": user_id})
    return ticket, 201
