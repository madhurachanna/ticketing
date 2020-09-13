from flask import request

# from utils.jwt_required import jwt_required
from src.validators.new_ticket import new_ticket_req_validate


@new_ticket_req_validate
def create_new_ticket():
    # req = request.valid_req
    # print(x)
    return "New tickett"
