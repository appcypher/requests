from os import path, environ
from dotenv import load_dotenv

load_dotenv(path.join(path.dirname(__file__), '.env'))

TESTING = environ.get("TESTING")
SECRET_KEY = environ.get("SECRET_KEY")
SQLALCHEMY_DATABASE_URI_TESTING = environ.get(
    "SQLALCHEMY_DATABASE_URI_TESTING")
SQLALCHEMY_DATABASE_URI_DEVELOPMENT = environ.get(
    "SQLALCHEMY_DATABASE_URI_DEVELOPMENT")
