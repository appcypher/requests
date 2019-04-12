from errors import ClientError
from re import compile, match

URL_REGEX = compile(
    r"^(http(s)?:\/\/)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9"
    r"@:%_\+.~#?&//=]*)$")


def validate_url(url):
    if not len(url) > 0:
        raise ClientError('invalid url syntax')
    elif not match(URL_REGEX, url):
        raise ClientError('invalid url syntax')


def validate_string_length(length):
    def validate(string):
        if len(string) > length:
            raise ClientError(f'string cannot be longer than {length}')

    return validate


def validate_product_area(product_area):
    expected_values = ['POLICIES', 'BILLING', 'CLAIMS', 'REPORTS']

    if product_area not in expected_values:
        raise ClientError(f'product_area can only be one of {expected_values}')


def validate_priority(priority):
    # TODO: A client can't have duplicate priority values
    pass
