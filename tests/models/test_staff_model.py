from models import Staff
from errors import ClientError
from pytest import raises


def test_staff_model_saves_with_valid_data(valid_staff_model):
    """
    Tests that data is saved in the db when model has valid data.

    Args:
        valid_staff_model (Model): a valid model created by a fixture
    """
    query = Staff.query
    count = query.count()
    staff = query.all()[0]

    assert staff.username == 'Leroy Jenkins'
    assert staff.avatar_url == ''
    assert count == 1


def test_staff_model_finds_row_if_it_exists(valid_staff_model):
    """
    Tests that model finds row correctly if it exists in the db.

    Args:
        valid_staff_model (Model): a valid model created by a fixture.
    """
    staff = Staff.find_by_id(1)

    assert staff.username == 'Leroy Jenkins'
    assert staff.avatar_url == ''


def test_staff_model_does_not_find_row_if_it_does_not_exist(initialize_db):
    """
    Tests that model does not find row correctly if it does not exist in
    the db.

    Args:
        initialize_db (None): initializes the database and drops tables when
            test function finishes.
    """
    with raises(ClientError) as err:
        Staff.find_by_id(1)

    assert err.value.message == 'cannot find specified staff'
    assert err.value.status_code == 404


def test_staff_model_gets_all_rows_correctly_after_saving(valid_staff_model):
    """
    Tests that model gets correct number of rows when there is data in the
    table.

    Args:
        valid_staff_model (Model): a valid model created by a fixture.
    """
    staffs = Staff.get_all()

    assert staffs[0].username == 'Leroy Jenkins'
    assert staffs[0].avatar_url == ''
    assert len(staffs) == 1


def test_staff_model_repr_shows_correctly_if_it_exists(
    valid_staff_model_no_save
):
    """
    Tests that model __repr__ row correctly.

    Args:
        valid_staff_model (Model): a valid model created by a fixture.
    """
    rep = repr(valid_staff_model_no_save)

    assert rep == "Staff {'username': 'Leroy Jenkins', 'avatar_url': ''}"


def test_staff_model_updates_correctly_if_it_exists(valid_staff_model):
    """
    Tests that model __repr__ row correctly.

    Args:
        valid_staff_model (Model): a valid model created by a fixture.
    """
    valid_staff_model.update(username="Leroy Jenkins")

    updated_staff = Staff.find_by_id(1)

    assert updated_staff.username == 'Leroy Jenkins'
