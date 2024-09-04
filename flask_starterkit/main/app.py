from flask import Flask
from flask_starterkit.main.config import create_app

flask_app = create_app()


@flask_app.route("/_status")
def home_route():
    return {
        "message":  "Ok.",
        "success": True
    }
