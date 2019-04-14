""" Module for flask app configuration """
from flask import Flask, jsonify
from extensions import cors, migrate, debug_toolbar
from config.blueprints import api_v1_blueprint
from config.config import apply_configuration
from models.db import db
from views.api import api
from views import serve_index, serve_files
from errors import ApplicationError
from cli import db_cli


def create_app():
    """
    Creates app and sets it up with necessary configuration

    Parameters:
        app (Flask): flask application
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
    Adds routes for serving static files

    Parameters:
        app (Flask): flask application
    """
    app.add_url_rule('/', 'home', view_func=serve_index)
    app.add_url_rule('/<path:path>', 'files', view_func=serve_files)


def register_cli_commands(app):
    app.cli.add_command(db_cli)


def initialize_extensions(app):
    """
    Initializes flask extensions

    Parameters:
        app (Flask): flask application
    """
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    debug_toolbar.init_app(app)


@api.errorhandler(ApplicationError)
def register_error_handler(error):
    """
    Handles all errors from the app

    Parameters:
        error (ApplicationError): the error returned by the app
    """
    response = jsonify(error.error)
    response.status_code = error.status_code
    return response
