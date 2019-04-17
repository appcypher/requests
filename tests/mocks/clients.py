from pytest import fixture
from models import Client


@fixture(scope='function')
def valid_client_model(initialize_db):
    """
    A fixture for creating a valid client model.

    Args:
        initialize_db (None): initializes the database and drops tables when
            test function finishes.
    """
    return Client(username='Leroy Jenkins', avatar_url='').save()


@fixture(scope='function')
def valid_client_model_no_save(initialize_db):
    """
    A fixture for creating a valid client model without saving it to the db.

    Args:
        initialize_db (None): initializes the database and drops tables when
            test function finishes.
    """
    return Client(username='Leroy Jenkins', avatar_url='')


@fixture(scope='function')
def multiple_valid_client_models(initialize_db):
    """
    A fixture for creating a multiple valid clients.

    Args:
        initialize_db (None): initializes the database and drops tables when
            test function finishes.
    """
    clients = [
        Client(username='Leroy Jenkins', avatar_url='').save(),
        Client(username='James Waldo', avatar_url='').save(),
        Client(username='Anu Johnson', avatar_url='').save(),
    ]

    return clients


@fixture(scope='function')
def valid_client_request_body(initialize_db):
    """
    A fixture for creating a valid client model.

    Args:
        initialize_db (None): initializes the database and drops tables when
            test function finishes.
    """
    return {'username': 'Leroy Jenkins', 'avatar_url': ''}
