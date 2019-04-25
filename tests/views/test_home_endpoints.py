from urls import base_url


def test_get_index_succeeds(client, request_headers):
    """
    Tests that response is okay when home route is requested.

    Args:
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """

    res = client.get(base_url, headers=request_headers, follow_redirects=True)

    assert res.status_code == 200
    assert res.data.startswith(b'<!DOCTYPE html>\n<html lang="en">')


def test_get_file_succeeds_with_valid_resource_path(client, request_headers):
    """
    Tests that response is okay when valid resource path is requested.

    Args:
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """

    res = client.get(
        f'{base_url}/dist/bundle.min.js',
        headers=request_headers,
        follow_redirects=True
    )

    assert res.status_code == 200
    assert b'function' in res.data


def test_get_file_succeeds_with_invalid_resource_path(client, request_headers):
    """
    Tests that response shows failure when invalid resource path is requested.

    Args:
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """

    res = client.get(
        f'{base_url}/non-existent.css',
        headers=request_headers,
        follow_redirects=True
    )

    assert res.status_code == 404
