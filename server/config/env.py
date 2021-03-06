""" Module for getting environment variables. """
from os import environ

# Secret key for variosus stuff
SECRET_KEY = environ.get("SECRET_KEY")

# Test database URI
SQLALCHEMY_DATABASE_URI_TESTING = environ.get(
    "SQLALCHEMY_DATABASE_URI_TESTING"
)

# Development/production database URI
SQLALCHEMY_DATABASE_URI = environ.get(
    "SQLALCHEMY_DATABASE_URI"
)

# Secret key for variosus stuff
TESTING = environ.get("TESTING")
