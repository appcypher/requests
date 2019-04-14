""" Module that holds middleware validators """
from errors import ClientError
from re import compile, match

URL_REGEX = compile(
    r"^(http(s)?:\/\/)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9"
    r"@:%_\+.~#?&//=]*)$")


def validate_url(url):
    """
    Checks if argument is a valid url string

    Parameters:
        app (Flask): flask application

    Raises:
        ClientError: if not valid url
    """
    if len(url) < 3 and not match(URL_REGEX, url):
        raise ClientError('invalid url syntax')


def validate_string_length(length):
    """
    Checks if argument has the specified length

    Parameters:
        length (int): length of string

    Raises:
        ClientError: if length of argument exceeds specified length
    """
    def validate(string):
        if len(string) > length:
            raise ClientError(f'string cannot be longer than {length}')

    return validate


def validate_product_area(product_area):
    """
    Checks if argument is one of the expected values

    Parameters:
        product_area (str): area of product

    Raises:
        ClientError: if argument is not one of the expected values
    """
    expected_values = ['POLICIES', 'BILLING', 'CLAIMS', 'REPORTS']

    if product_area not in expected_values:
        raise ClientError(f'product_area can only be one of {expected_values}')


def validate_priority(priority):
    """
    TODO
    ...
    """
    # TODO: A client can't have duplicate priority values
    pass
