from flask import Blueprint

auth_routes = Blueprint("auth_routes", __name__)


@auth_routes.route('/')
def welcome():
    test_var= "Hello"
    return {
        "message": "Welcome to your awesome auth endpoint",
        "success": True
    }
