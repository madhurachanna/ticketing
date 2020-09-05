from flask import Blueprint
import src.routes.users.handlers as H

users = Blueprint("users", __name__)

users.route("/api/users/hello", methods=["GET"])(H.say_hello)