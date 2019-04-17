from pytest import fixture
from models import Staff


@fixture(scope='function')
def valid_staff_model(initialize_db):
    """
    A fixture for creating a valid staff model.

    Args:
        initialize_db (None): initializes the database and drops tables when
            test function finishes.
    """
    return Staff(username='Leroy Jenkins', avatar_url='').save()


@fixture(scope='function')
def valid_staff_model_no_save(initialize_db):
    """
    A fixture for creating a valid staff model without saving it to the db.

    Args:
        initialize_db (None): initializes the database and drops tables when
            test function finishes.
    """
    return Staff(username='Leroy Jenkins', avatar_url='')


@fixture(scope='function')
def multiple_valid_staff_models(initialize_db):
    """
    A fixture for creating a multiple valid staff.

    Args:
        initialize_db (None): initializes the database and drops tables when
            test function finishes.
    """
    staff = [
        Staff(username='Leroy Jenkins', avatar_url='').save(),
        Staff(username='James Waldo', avatar_url='').save(),
        Staff(username='Anu Johnson', avatar_url='').save(),
    ]

    return staff


@fixture(scope='function')
def valid_staff_request_body(initialize_db):
    """
    A fixture for creating a valid staff request_body.

    Args:
        initialize_db (None): initializes the database and drops tables when
            test function finishes.
    """
    return {'username': 'Leroy Jenkins', 'avatar_url': ''}
