from flask import Blueprint
import src.routes.signout.handlers as H

signout = Blueprint("signout", __name__)


signout.route("/api/users/signout", methods=["POST"])(H.signout)
