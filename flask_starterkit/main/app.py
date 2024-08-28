from flask import Flask
from flask_starterkit.main.config import create_app

flask_app = create_app()


@flask_app.route("/")
def home_route():
    return "GitHub hook is working!"
