from flask import Blueprint, request, jsonify

auth_routes = Blueprint("auth_routes", __name__)
auth_bp = Blueprint('auth', __name__)


@auth_routes.route('/')
def welcome():
    return {
        "message":  " lint Welcome to your awesome auth endpoint",
        "success": True
    }

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == "admin" and password == "secret":
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401
