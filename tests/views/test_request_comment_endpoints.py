from urls import request_comments_url


def test_get_request_comments_succeeds_with_valid_request_id_in_params(
    valid_comment_model, client, request_headers
):
    """
    Tests that response is okay when request id exists.

    Args:
        valid_client_model (Model): a valid model created by a fixture.
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.get(request_comments_url(1), headers=request_headers)
    response = res.get_json()

    assert response['success']
    assert response['message'] == 'comments fetched successfully'
    assert len(response['data']) == 1
    assert res.status_code == 200


def test_get_request_comments_succeeds_with_non_existent_request_id_in_params(
    client, request_headers
):
    """
    Tests that response is okay when request id exists.

    Args:
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.get(request_comments_url(1), headers=request_headers)
    response = res.get_json()

    assert not response['success']
    assert response['message'] == 'cannot find specified request'
    assert res.status_code == 404


def test_post_request_comments_succeeds_with_valid_comment_body(
    valid_comment_body, client, request_headers
):
    """
    Tests that response is okay when comment body is valid.

    Args:
        valid_comment_body (dict): a valid comment body created by a fixture.
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.post(
        request_comments_url(1),
        headers=request_headers,
        json=valid_comment_body
    )
    response = res.get_json()

    assert response['success']
    assert response['message'] == 'comment created successfully'
    assert response['data']['message'] == 'I will be working on this soon'
    assert res.status_code == 201


def test_post_request_comments_fails_with_missing_fields_in_body(
    invalid_comment_body_with_missing_fields, client, request_headers
):
    """
    Tests that response shows failure when comment body has missing fields.

    Args:
        invalid_comment_body_with_missing_fields (dict): a comment body with
            missing fields created by a fixture.
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.post(
        request_comments_url(1),
        headers=request_headers,
        json=invalid_comment_body_with_missing_fields
    )
    response = res.get_json()

    assert not response['success']
    assert (
        response['message']['message'][0] == 'Missing data for required field.'
    )
    assert res.status_code == 400


def test_post_request_comments_fails_with_non_existent_request_in_body(
    invalid_comment_body_with_non_existent_request, client, request_headers
):
    """
    Tests that response shows failure when comment body has non-existent
    request id.

    Args:
        invalid_comment_body_with_non_existent_client (dict): a comment body
            with non-existent request id
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.post(
        request_comments_url(1),
        headers=request_headers,
        json=invalid_comment_body_with_non_existent_request
    )
    response = res.get_json()

    assert not response['success']
    assert response['message'] == 'cannot find specified request'
    assert res.status_code == 404


def test_post_request_comments_fails_with_non_existent_staff_in_body(
    invalid_comment_body_with_non_existent_staff, client, request_headers
):
    """
    Tests that response shows failure when comment body has non-existent
    staff id.

    Args:
        invalid_comment_body_with_non_existent_staff (dict): a comment body
            with non-existent staff id
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.post(
        request_comments_url(1),
        headers=request_headers,
        json=invalid_comment_body_with_non_existent_staff
    )
    response = res.get_json()

    assert not response['success']
    assert response['message'] == 'cannot find specified staff'
    assert res.status_code == 404


def test_post_request_comments_fails_with_bad_json_in_body(
    bad_comment_json_string, client, request_headers
):
    """
    Tests that response shows failure when comment body has conflicting
    priority.

    Args:
        invalid_comment_body_with_conflicting_priority (dict): a comment body
            with conflicting priority
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """

    res = client.post(
        request_comments_url(1),
        headers=request_headers,
        data=bad_comment_json_string
    )
    response = res.get_json()

    assert not response['success']
    assert res.status_code == 400
