from pydantic import BaseModel, constr, validator, ValidationError
from flask import request
from functools import wraps
import re

from src.errors.request_validation_error import RequestValidationError


class SignUpValid(BaseModel):
    email: str
    username: str
    password: constr(min_length=4, max_length=20)

    @validator("email")
    def email_validation(cls, v):
        regex = "^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$"
        if not re.search(regex, v):
            raise ValueError("must be valid email")
        return v

    class Config:
        extra = "forbid"


def signup_req_validate(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            req = request.get_json() or {}
            request.valid_req = SignUpValid(**req)
            return fn(*args, **kwargs)
        except ValidationError as e:
            raise RequestValidationError(e.errors())

    return wrapper
