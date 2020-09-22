import functools
from flask import request
from pydantic import ValidationError


from ..errors.request_validation_error import RequestValidationError


def request_validator(ValidatorSchema):
    def wrapper(func):
        @functools.wraps(func)
        def validate(*args, **kwargs):
            try:
                req = request.get_json() or {}
                request.valid_req = ValidatorSchema(**req)
            except ValidationError as e:
                raise RequestValidationError(e.errors())

            return func(*args, **kwargs)

        return validate

    return wrapper
