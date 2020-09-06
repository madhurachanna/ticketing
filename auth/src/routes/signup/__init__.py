from flask import Blueprint
import src.routes.signup.handlers as H

signup = Blueprint("signup", __name__)


signup.route("/api/users/signup", methods=["POST"])(H.signup)
