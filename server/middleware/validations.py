""" Module that holds middleware validators. """
from errors import ClientError
from marshmallow import ValidationError
from datetime import datetime


def validate_date(date):
    """
    Checks if date is a time in the future..

    Args:
        date (datetime): date input.

    Raises:
        ValidationError: if date is not a time in the future.
    """
    present = datetime.now()

    if date.date() < present.date():
        raise ValidationError('date can only be a later time in the future')


def validate_string_length(length):
    """
    Checks if argument has the specified length.

    Args:
        length (int): length of string.

    Raises:
        ClientError: if length of argument exceeds specified length.
    """

    def validate(string):
        if not string or len(string) > length:
            raise ValidationError(f'string cannot be longer than {length}')

    return validate


def validate_priority(client_id, priority):
    """
    Checks if priority is invalid.

    Args:
        client_id (int): client id.
        priority (int): priority value.

    Raises:
        ClientError: if priority value is not between 0 and 100.
    """

    if priority > 99 or priority < 1:
        raise ClientError('priority value must be between 0 and 100', 400)


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
