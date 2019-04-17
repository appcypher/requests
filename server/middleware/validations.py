""" Module that holds middleware validators. """
from errors import ClientError
from models import Request


def validate_string_length(length):
    """
    Checks if argument has the specified length.

    Args:
        length (int): length of string.

    Raises:
        ClientError: if length of argument exceeds specified length.
    """

    def validate(string):
        if len(string) > length:
            raise ClientError(f'string cannot be longer than {length}')

    return validate


def validate_priority(client_id, priority):
    """
    Checks if client is already given the priority.

    Args:
        client_id (int): client id.
        priority (int): priority value.

    Raises:
        ClientError: if priority already exists for client.
    """
    result = Request.query.filter_by(client_id=client_id,
                                     priority=priority).all()

    if result:
        raise ClientError('priority number already exists for client', 409)


def validate_id(model):
    """
    Checks if a row with specified id exists for a model.

    Args:
        model (Model): table of interest.
        id (int): id to check for.

    Raises:
        ClientError: if row does not exist.
    """

    return lambda id: model.find_by_id(id)
