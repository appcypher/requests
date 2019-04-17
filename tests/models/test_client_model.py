from models import Client
from errors import ClientError
from pytest import raises


def test_client_model_saves_with_valid_data(valid_client_model):
    """
    Tests that data is saved in the db when model has valid data.

    Args:
        valid_client_model (Model): a valid model created by a fixture.
    """
    query = Client.query
    count = query.count()
    client = query.all()[0]

    assert client.username == 'Leroy Jenkins'
    assert client.avatar_url == ''
    assert count == 1


def test_client_model_finds_row_if_it_exists(valid_client_model):
    """
    Tests that model finds row correctly if it exists in the db.

    Args:
        valid_client_model (Model): a valid model created by a fixture.
    """
    client = Client.find_by_id(1)

    assert client.username == 'Leroy Jenkins'
    assert client.avatar_url == ''


def test_client_model_does_not_find_row_if_it_does_not_exist(initialize_db):
    """
    Tests that model does not find row correctly if it does not exist in
    the db.

    Args:
        initialize_db (None): initializes the database and drops tables when
            test function finishes.
    """
    with raises(ClientError) as err:
        Client.find_by_id(1)

    assert err.value.message == 'cannot find specified client'
    assert err.value.status_code == 404


def test_client_model_gets_all_rows_correctly_after_saving(valid_client_model):
    """
    Tests that model gets correct number of rows when there is data in the
    table.

    Args:
        valid_client_model (Model): a valid model created by a fixture.
    """
    clients = Client.get_all()

    assert clients[0].username == 'Leroy Jenkins'
    assert clients[0].avatar_url == ''
    assert len(clients) == 1


def test_client_model_repr_shows_correctly_if_it_exists(
    valid_client_model_no_save
):
    """
    Tests that model __repr__ row correctly.

    Args:
        valid_client_model (Model): a valid model created by a fixture.
    """
    rep = repr(valid_client_model_no_save)

    assert rep == "Client {'username': 'Leroy Jenkins', 'avatar_url': ''}"


def test_client_model_updates_correctly_if_it_exists(valid_client_model):
    """
    Tests that model __repr__ row correctly.

    Args:
        valid_client_model (Model): a valid model created by a fixture.
    """
    valid_client_model.update(username="Linus Torvalds")

    updated_client = Client.find_by_id(1)

    assert updated_client.username == 'Linus Torvalds'
