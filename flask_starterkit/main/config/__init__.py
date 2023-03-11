from flask import Flask

def create_app():
    """This function will create the instance of the flask application. You can also pass any config, blueprints or commands inside this functions

    Returns:
        Flask: The configured instance of the flask application
    """
    app_instance = Flask(__name__)
    app_instance.config["YOUR_AWESOME_CONFIG_ENV"] = "your awesome non sensitive value"
    return app_instance