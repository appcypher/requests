from flask import Flask, jsonify
from extensions import cors, migrate, debug_toolbar
from blueprints import api_v1_blueprint
from models.db import db
from views.api import api
from config import apply_configuration
from errors import ApplicationError
from cli import db_cli


def create_app():
    app = Flask(__name__)
    apply_configuration(app)
    register_blueprints(app)
    initialize_extensions(app)
    register_cli_commands(app)
    return app


def register_blueprints(app):
    app.register_blueprint(api_v1_blueprint)


def register_cli_commands(app):
    app.cli.add_command(db_cli)


def initialize_extensions(app):
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    debug_toolbar.init_app(app)


@api.errorhandler(ApplicationError)
def register_error_handler(error):
    response = jsonify(error.error)
    response.status_code = error.status_code
    return response
