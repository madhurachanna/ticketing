from functools import wraps
from pydantic import BaseModel, confloat, ValidationError
from flask import request

from src.errors.request_validation_error import RequestValidationError


class Ticket(BaseModel):
    title: str
    price: confloat(gt=0)

    class Config:
        extra = "forbid"


def new_ticket_req_validate(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            req = request.get_json() or {}
            request.valid_req = Ticket(**req)
            return fn(*args, **kwargs)
        except ValidationError as e:
            raise RequestValidationError(e.errors())

    return wrapper
