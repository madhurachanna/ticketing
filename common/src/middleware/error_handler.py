from flask import Blueprint

from ..errors.custom_error import CustomError

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(Exception)
def handler_bad_request(e):
    print("Error:Common", e)
    if isinstance(e, CustomError):
        return {"errors": e.serialize_errors()}, e.status_code
    return {"errors": [{"message": "Something went wrong"}]}, 400
