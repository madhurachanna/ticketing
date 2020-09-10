from flask import Blueprint

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(Exception)
def handler_bad_request(e):
    return {"errors": e.serialize_errors()}, e.status_code
