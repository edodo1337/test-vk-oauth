from flask import Flask, url_for
from .config import Config


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    from backend.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from backend.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
