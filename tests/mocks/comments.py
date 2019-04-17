from pytest import fixture
from models import Comment


@fixture(scope='function')
def valid_comment_model(valid_request_model):
    """
    A fixture for creating a valid comment model.

    Args:
        valid_request_model (Model): a valid request model created by a
            fixture.
    """
    return Comment(
        message='I will be working on this soon', request_id=1, staff_id=1
    ).save()


@fixture(scope='function')
def valid_comment_model_no_save(valid_request_model):
    """
    A fixture for creating a valid comment model without saving it to the db.

    Args:
        valid_request_model (Model): a valid request model created by a
            fixture.
    """
    return Comment(
        message='I will be working on this soon', request_id=1, staff_id=1
    )


@fixture(scope='function')
def valid_comment_body(valid_request_model):
    """
    A fixture for creating a valid comment body.

    Args:
        valid_request_model (Model): a valid request model created by a
            fixture.
    """
    return {
        'message': 'I will be working on this soon',
        'request_id': 1,
        'staff_id': 1,
    }


@fixture(scope='function')
def invalid_comment_body_with_missing_fields(valid_request_model):
    """
    A fixture for creating a comment body with missing fields.

    Args:
        valid_request_model (Model): a valid request model created by a
            fixture.
    """
    return {
        'staff_id': 1,
    }


@fixture(scope='function')
def invalid_comment_body_with_non_existent_request(valid_staff_model):
    """
    A fixture for creating a comment body with non-existent client id.

    Args:
        valid_staff_model (Model): a valid staff model created by a fixture.
    """
    return {
        'message': 'I will be working on this soon',
        'request_id': 1,
        'staff_id': 1,
    }


@fixture(scope='function')
def invalid_comment_body_with_non_existent_staff(valid_request_model):
    """
    A fixture for creating a comment body with non-existent staff id.

    Args:
        valid_request_model (Model): a valid request model created by a
            fixture.
    """
    return {
        'message': 'I will be working on this soon',
        'request_id': 1,
        'staff_id': 2,
    }


@fixture(scope='function')
def bad_comment_json_string(valid_request_model):
    """
    A fixture for creating a bad comment body.

    Args:
        valid_request_model (Model): a valid request model created by a
            fixture.
    """
    # Json string contains an extra comma.
    return (
        """
        {
            "message": "I will be working on this soon",
            "request_id": 1,
            "staff_id": 2,
        }
        """
    )
