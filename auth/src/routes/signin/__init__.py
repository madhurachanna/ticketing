from flask import Blueprint
import src.routes.signin.handlers as H

signin = Blueprint("signin", __name__)


signin.route("/api/users/signin", methods=["POST"])(H.signin)
