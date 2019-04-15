""" Module for flask app configuration. """
from flask import Flask
from extensions import cors, migrate, debug_toolbar
from werkzeug.exceptions import HTTPException
from config.blueprints import api_v1_blueprint
from config.config import apply_configuration
from models.db import db
from views.api import api
from views import serve_index, serve_files
from errors import ApplicationError
from cli import db_cli


def create_app():
    """
    Creates app and sets it up with necessary configuration.

    Args:
        app (Flask): flask application.
    """
    app = Flask(__name__)
    apply_configuration(app)
    add_rules(app)
    register_blueprints(app)
    initialize_extensions(app)
    register_cli_commands(app)
    return app


def register_blueprints(app):
    app.register_blueprint(api_v1_blueprint)


def add_rules(app):
    """
    Adds routes for serving static files.

    Args:
        app (Flask): flask application.
    """
    app.add_url_rule('/', 'home', view_func=serve_index)
    app.add_url_rule('/<path:path>', 'files', view_func=serve_files)


def register_cli_commands(app):
    app.cli.add_command(db_cli)


def initialize_extensions(app):
    """
    Initializes flask extensions.

    Args:
        app (Flask): flask application.
    """
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    debug_toolbar.init_app(app)


@api.errorhandler(Exception)
@api_v1_blueprint.errorhandler(Exception)
def register_error_handler(error):
    """
    Handles all errors from the app.

    Args:
        error (Exception): the error returned by the app.
    """
    error_type = type(error)
    response = {'success': False, 'message': str(error)}
    status_code = 500

    # Get application exceptions
    if issubclass(error_type, ApplicationError):
        status_code = error.status_code
        response['message'] = error.message
    # Get flask exceptions
    elif issubclass(error_type, HTTPException):
        error_response = error.get_response()
        status_code = error_response._status_code
        response['message'] = error.description

    return response, status_code
