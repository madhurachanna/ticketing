from flask import Blueprint
import src.routes.current_user.handlers as H

current_user = Blueprint("current_user", __name__)


current_user.route("/api/users/me", methods=["GET"])(H.current_user)
