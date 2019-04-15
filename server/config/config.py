""" Module for flask application configuration. """
from .env import (TESTING, SECRET_KEY, SQLALCHEMY_DATABASE_URI_TESTING,
                  SQLALCHEMY_DATABASE_URI_DEVELOPMENT)


def apply_configuration(app):
    """
    Adds configuration values to flask app.

    Args:
        app(Flask): flask application.
    """

    SQLALCHEMY_DATABASE_URI = (SQLALCHEMY_DATABASE_URI_TESTING if TESTING else
                               SQLALCHEMY_DATABASE_URI_DEVELOPMENT)

    # Secret key fro various stuff
    app.config['SECRET_KEY'] = SECRET_KEY

    # The postgres database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

    # A deprecated SQLAlchelmy feature that needs to be turned off
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Prevents flask restful from appending message to 404 response
    app.config['ERROR_404_HELP'] = False
