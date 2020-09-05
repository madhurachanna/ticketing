from flask import Blueprint
import src.routes.hello.handlers as H

hello = Blueprint("users", __name__)

hello.route("/hello", methods=["GET"])(H.say_hello)