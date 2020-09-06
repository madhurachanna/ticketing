from flask import Blueprint
from src.errors.request_validation_error import RequestValidationError

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(RequestValidationError)
def handler_bad_request(e):
    return {"errors": e.serialize_errors()}, e.status_code
