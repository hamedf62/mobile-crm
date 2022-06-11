from flask import Flask, jsonify, Blueprint
from datetime import datetime, timedelta, time, date

from flask_jwt_extended import JWTManager
from app.routes import blueprint


def register_blueprints(app):

    app.register_blueprint(blueprint, url_prefix="/api/v1")


def configure_database(app):
    # @app.before_first_request
    # def create_db():
    #     initialize_database()

    @app.teardown_request
    def shutdown_session(exception=None):
        # dbsession.remove()
        # Session.remove()
        # dbsession.close()
        # engine.dispose()
        pass


def after_request(app):
    @app.after_request
    def add_header(r):
        """
        Add headers to both force latest IE rendering engine or Chrome Frame,
        and also to cache the rendered page for 10 minutes.
        """
        # r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        # r.headers["Pragma"] = "no-cache"
        # r.headers["Expires"] = "0"
        r.headers["Last-Modified"] = datetime.now()
        r.headers[
            "Cache-Control"
        ] = "no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "-1"
        # r.headers["Cache-Control"] = "public, max-age=0"
        return r


def create_app(config):
    app = Flask(__name__, static_folder=None)
    # CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(config)

    app.config["JWT_SECRET_KEY"] = "hmft1362"  # Change this!
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=60)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(hours=48)
    app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
    JWTManager(app)

    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    # Session(app)

    # error_handler(app)
    register_blueprints(app)
    configure_database(app)
    # before_request(app)
    after_request(app)

    return app
