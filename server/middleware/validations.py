""" Module that holds middleware validators. """
from errors import ClientError
from re import compile, match
from models import Request

URL_REGEX = compile(r"^(http(s)?:\/\/)?[-a-zA-Z0-9@:%._\+~#=]{2,256}"
                    r"\.[a-z]{2,6\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$")


def validate_url(url):
    """
    Checks if argument is a valid url string.

    Args:
        app (Flask): flask application.

    Raises:
        ClientError: if not valid url.
    """
    if len(url) < 3 and not match(URL_REGEX, url):
        raise ClientError('invalid url syntax')


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


def validate_product_area(product_area):
    """
    Checks if argument is one of the expected values.

    Args:
        product_area (str): area of product.

    Raises:
        ClientError: if argument is not one of the expected values.
    """
    expected_values = ['POLICIES', 'BILLING', 'CLAIMS', 'REPORTS']

    if product_area not in expected_values:
        raise ClientError(f'product_area can only be one of {expected_values}')


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
        raise ClientError('priority number already exists for client')


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
