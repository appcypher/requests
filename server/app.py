""" Module for flask app configuration. """
from flask import Flask
from extensions import cors, migrate
from werkzeug.exceptions import HTTPException
from config.blueprints import api_v1_blueprint
from config.config import apply_configuration
from models.db import db
from views.api import api
from views import serve_index, serve_files
from errors import ApplicationError
from cli import db_cli


def create_app(test_env=False):
    """
    Creates app and sets it up with necessary configuration.

    Args:
        app (Flask): flask application.
    """
    # Start and create flask app instance.
    app = Flask(__name__)

    # Apply flask configurations.
    apply_configuration(app, test_env)

    # Add additional endpoints to app.
    add_rules(app)

    # Register application blueprint.
    register_blueprints(app)

    # Initiatze extensions.
    initialize_extensions(app)

    # Add cli commands like `flask seed model`.
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
    # Serve `index.html` on '/' root route.
    app.add_url_rule('/', 'home', view_func=serve_index)

    # Serve from other files from `client/dist` folder.
    app.add_url_rule('/<path:path>', 'files', view_func=serve_files)


def register_cli_commands(app):
    app.cli.add_command(db_cli)


def initialize_extensions(app):
    """
    Initializes flask extensions.

    Args:
        app (Flask): flask application.
    """
    # Initialize SQLAlchemy instance.
    db.init_app(app)

    # Allow cross-origin requests.
    cors.init_app(app)

    # Apply database migrations.
    migrate.init_app(app, db)


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
