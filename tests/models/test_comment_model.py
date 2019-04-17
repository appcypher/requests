from models import Comment
from errors import ClientError
from pytest import raises


def test_comment_model_saves_with_valid_data(valid_comment_model):
    """
    Tests that data is saved in the db when model has valid data.

    Args:
        valid_comment_model (Model): a valid model created by a fixture.
    """
    query = Comment.query
    count = query.count()
    comment = query.all()[0]

    assert comment.message == 'I will be working on this soon'
    assert comment.staff_id == 1
    assert comment.request_id == 1
    assert count == 1


def test_comment_model_finds_row_if_it_exists(valid_comment_model):
    """
    Tests that model finds row correctly if it exists in the db.

    Args:
        valid_comment_model (Model): a valid model created by a fixture.
    """
    comment = Comment.find_by_id(1)

    assert comment.message == 'I will be working on this soon'
    assert comment.staff_id == 1
    assert comment.request_id == 1


def test_comment_model_does_not_find_row_if_it_does_not_exist(initialize_db):
    """
    Tests that model does not find row correctly if it does not exist in
    the db.

    Args:
        initialize_db (None): initializes the database and drops tables when
            test function finishes.
    """
    with raises(ClientError) as err:
        Comment.find_by_id(1)

    assert err.value.message == 'cannot find specified comment'
    assert err.value.status_code == 404


def test_comment_model_get_all_rows_correctly_after_saving(
        valid_comment_model):
    """
    Tests that model gets correct number of rows when there is data in the
    table.

    Args:
        valid_comment_model (Model): a valid model created by a fixture.
    """
    comments = Comment.get_all()

    assert comments[0].message == 'I will be working on this soon'
    assert comments[0].staff_id == 1
    assert comments[0].request_id == 1


def test_comment_model_repr_shows_correctly_if_it_exists(
        valid_comment_model_no_save):
    """
    Tests that model __repr__ row correctly.

    Args:
        valid_comment_model (Model): a valid model created by a fixture.
    """
    rep = repr(valid_comment_model_no_save)

    assert rep == ("Comment {'message': 'I will be working on this soon', "
                   "'request_id': 1, 'staff_id': 1}")


def test_comment_model_updates_correctly_if_it_exists(valid_comment_model):
    """
    Tests that model __repr__ row correctly.

    Args:
        valid_comment_model (Model): a valid model created by a fixture.
    """
    valid_comment_model.update(message='Related to #0')

    updated_comment = Comment.find_by_id(1)

    assert updated_comment.message == 'Related to #0'
