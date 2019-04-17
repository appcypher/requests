from models import Request
from errors import ClientError
from pytest import raises
from models.request import ProductArea


def test_request_model_saves_with_valid_data(valid_request_model):
    """
    Tests that data is saved in the db when model has valid data.

    Args:
        valid_request_model (Model): a valid model created by a fixture.
    """
    query = Request.query
    count = query.count()
    request = query.all()[0]

    assert request.title == 'Improve customer care services'
    assert request.staff_id == 1
    assert request.product_area == ProductArea.POLICIES
    assert count == 1


def test_request_model_finds_row_if_it_exists(valid_request_model):
    """
    Tests that model finds row correctly if it exists in the db.

    Args:
        valid_request_model (Model): a valid model created by a fixture.
    """
    request = Request.find_by_id(1)

    assert request.title == 'Improve customer care services'
    assert request.staff_id == 1
    assert request.product_area == ProductArea.POLICIES


def test_request_model_does_not_find_row_if_it_does_not_exist(initialize_db):
    """
    Tests that model does not find row correctly if it does not exist in
    the db.

    Args:
        initialize_db (None): initializes the database and drops tables when
            test function finishes.
    """
    with raises(ClientError) as err:
        Request.find_by_id(1)

    assert err.value.message == 'cannot find specified request'
    assert err.value.status_code == 404


def test_request_model_get_all_rows_correctly_after_saving(
        valid_request_model):
    """
    Tests that model gets correct number of rows when there is data in the
    table.

    Args:
        valid_request_model (Model): a valid model created by a fixture.
    """
    requests = Request.get_all()

    assert requests[0].title == 'Improve customer care services'
    assert requests[0].staff_id == 1
    assert requests[0].product_area == ProductArea.POLICIES
    assert len(requests) == 1


def test_request_model_repr_shows_correctly_if_it_exists(
        valid_request_model_no_save):
    """
    Tests that model __repr__ row correctly.

    Args:
        valid_request_model (Model): a valid model created by a fixture.
    """
    rep = repr(valid_request_model_no_save)

    assert rep.startswith(
        "Request {'title': 'Improve customer care services', "
        "'description': 'The current customer care services are reported to ")


def test_request_model_updates_correctly_if_it_exists(valid_request_model):
    """
    Tests that model __repr__ row correctly.

    Args:
        valid_request_model (Model): a valid model created by a fixture.
    """
    valid_request_model.update(title="Restruture customer care")

    updated_request = Request.find_by_id(1)

    assert updated_request.title == 'Restruture customer care'
