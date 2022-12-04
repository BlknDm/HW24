from flask import Flask

from views import main_blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    return app
