from seeders import (seed_client, seed_staff, seed_request, seed_comment)
from models import (Client, Staff, Request, Comment)


def test_seed_client_saves_clients_to_db(initialize_db):
    """
    Tests that `seed_client` function stores clients in the db.

    Args:
        initialize_db (None): initializes the database and drops tables when
            test function finishes.
    """
    seed_client()

    clients = Client.get_all()

    assert clients[0].username == 'Client A'
    assert clients[1].username == 'Client B'
    assert clients[2].username == 'Client C'
    assert len(clients) == 3


def test_seed_staff_saves_staffs_to_db(initialize_db):
    """
    Tests that `seed_staff` function stores staffs in the db.

    Args:
        initialize_db (None): initializes the database and drops tables when
            test function finishes.
    """
    seed_staff()

    staff = Staff.get_all()

    assert staff[0].username == 'Steve Akinyemi'
    assert staff[1].username == 'Anu Johnson'
    assert staff[2].username == 'James Waldo'
    assert len(staff) == 3


def test_seed_comment_saves_comments_to_db(multiple_valid_request_models):
    """
    Tests that `seed_comment` function stores comments in the db.

    Args:
        multiple_valid_request_models (list): a list of valid request models
            created by a fixture.
    """
    seed_comment()

    comments = Comment.get_all()

    assert comments[0].message == 'I will be working on this soon'
    assert comments[1].message == 'I think we should wait for confirmation'
    assert comments[2].message == 'How long will the Paypal support take?'
    assert len(comments) == 14


def test_seed_request_saves_requests_to_db(
    multiple_valid_staff_models, multiple_valid_client_models
):
    """
    Tests that `seed_request` function stores requests in the db.

    Args:
        multiple_valid_staff_models (list): a list of valid staff models
            created by a fixture.
        multiple_valid_client_models (list): a list of valid client models
            created by a fixture.
    """
    seed_request()

    requests = Request.get_all()

    assert requests[0].title == (
        'Add option for clearing transactions or archiving them'
        ' transactions'
    )
    assert requests[1].title == (
        'Improve customer care services to reduce client churn'
    )
    assert requests[2].title == (
        'Fix issue with the customisation section. It hangs'
        ' sometimes and breaks immersion'
    )
    assert len(requests) == 12
