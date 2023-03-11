from flask import Flask


flask_app = Flask(__name__)

@flask_app.route("/")
def home_route():
    return "Hello World !"