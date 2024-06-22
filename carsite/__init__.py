from flask import Flask


def create_app():
    app = Flask(__name__)
    app.debug = True
    from .templates import views

    app.register_blueprint(views.bp)

    return app
