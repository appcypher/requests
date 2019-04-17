from urls import clients_url


def test_get_clients_succeeds_with_valid_client_id_in_params(
    valid_client_model, client, request_headers
):
    """
    Tests that response is okay when client id exists.

    Args:
        valid_client_model (Model): a valid model created by a fixture.
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.get(clients_url(1), headers=request_headers)
    response = res.get_json()

    assert response['success']
    assert response['message'] == 'client fetched successfully'
    assert response['data']['username'] == 'Leroy Jenkins'
    assert res.status_code == 200


def test_get_clients_succeeds_with_non_existent_client_id_in_params(
    client, request_headers
):
    """
    Tests that response is okay when client id exists.

    Args:
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.get(clients_url(1), headers=request_headers)
    response = res.get_json()

    assert not response['success']
    assert response['message'] == 'cannot find specified client'
    assert res.status_code == 404
