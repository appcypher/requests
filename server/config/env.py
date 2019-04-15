""" Module for getting environment variables. """
from os import path, environ
from dotenv import load_dotenv

# Loads environment variables from .env file
load_dotenv(path.join(path.dirname(__file__), '.env'))

# Needed to know if app is running as a test or not
TESTING = environ.get("TESTING")

# Secret key for variosus stuff
SECRET_KEY = environ.get("SECRET_KEY")

# Test database URI
SQLALCHEMY_DATABASE_URI_TESTING = environ.get(
    "SQLALCHEMY_DATABASE_URI_TESTING")

# Development database URI
SQLALCHEMY_DATABASE_URI_DEVELOPMENT = environ.get(
    "SQLALCHEMY_DATABASE_URI_DEVELOPMENT")
