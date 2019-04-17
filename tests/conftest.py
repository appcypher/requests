from mocks import *
from models.db import db
from pytest import yield_fixture, fixture
from app import create_app


@fixture(scope='session')
def request_headers():
    """
    Fixture for creating a request header.
    """
    return {'Content-Type': 'application/json', 'Accept': 'application/json'}


@yield_fixture(scope="session")
def app():
    """
    Fixture that starts the flask application.
    """
    # Start flask app.
    flask_app = create_app(test_env=True)

    # Run tests with application context.
    with flask_app.app_context():
        yield flask_app


@yield_fixture(scope="function")
def initialize_db(app):
    """
    Fixture for creating tables in the database.
    Drops tables after each function.

    Args:
        app (Flask): a flask application instance.
    """
    # Create tables
    db.create_all()

    yield app

    # Close connection. Postgres needs it to release locks
    db.session.close()

    # Drop all tables
    db.drop_all()


@fixture(scope="function")
def client(initialize_db):
    """
    Fixture for creating a request maker.

    Args:
        initialize_db (None): initializes the database and drops tables when
            test function finishes.
    """
    # `initialize_db` fixture returns the flask app
    flask_app = initialize_db

    return flask_app.test_client()


@yield_fixture(scope="function")
def cli_app():
    """
    Fixture for creating a flask app and app context specifically for testing
    the custom flask cli.

    Note:
        We can't use the existing `app` fixture first because we need a per
        function scope. Secondly, we need to pass yield a factory function
        instead of the app itself
    """
    # Declaring app context so that it can be popped outside the app closure.
    flask_app_context = None

    # Closure for creating flask app and context.
    def app(info):
        # Use the variable the defined outside the closure.
        nonlocal flask_app_context

        # Create flask application.
        flask_app = create_app(test_env=True)

        # Create application context
        flask_app_context = flask_app.app_context()

        # Push it onto the context stack.
        flask_app_context.push()

        # Create the tables.
        db.create_all()

        return flask_app

    yield app

    # Close connection. Postgres needs it to release locks.
    db.session.close()

    # Drop all the tables.
    db.drop_all()

    # Pop application context
    flask_app_context.pop()
