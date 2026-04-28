import pytest

from api.clients.jsonplaceholder_client import JsonPlaceholderClient
from api.data.jsonplaceholder_payloads import (
    POST_ID,
    USER_ID,
    CREATE_POST_PAYLOAD,
    UPDATE_POST_PAYLOAD,
)


@pytest.fixture
def jsonplaceholder_client():
    """
    Provide a JSONPlaceholder API client for tests.
    """
    return JsonPlaceholderClient()


@pytest.mark.smoke
@pytest.mark.regression
def test_jsonplaceholder_get_single_post_returns_expected_fields(jsonplaceholder_client):
    """
    Verify that a single post can be retrieved and contains the expected fields.
    """
    response = jsonplaceholder_client.get_post(POST_ID)

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert body["id"] == POST_ID
    assert isinstance(body["id"], int)
    assert body["userId"] == USER_ID
    assert isinstance(body["userId"], int)
    assert isinstance(body["title"], str)
    assert body["title"].strip() != ""
    assert isinstance(body["body"], str)
    assert body["body"].strip() != ""


@pytest.mark.smoke
@pytest.mark.regression
def test_jsonplaceholder_get_users_returns_non_empty_list(jsonplaceholder_client):
    """
    Verify that the users endpoint returns a non-empty list with valid user fields.
    """
    response = jsonplaceholder_client.get_users()

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, list)
    assert len(body) > 0

    first_user = body[0]

    assert isinstance(first_user, dict)
    assert isinstance(first_user["email"], str)
    assert first_user["email"].strip() != ""
    assert isinstance(first_user["username"], str)
    assert first_user["username"].strip() != ""
    assert isinstance(first_user["name"], str)
    assert first_user["name"].strip() != ""


@pytest.mark.regression
def test_jsonplaceholder_create_post_returns_201_and_created_fields(jsonplaceholder_client):
    """
    Verify that creating a post returns 201 Created and echoes the submitted payload.
    """
    response = jsonplaceholder_client.create_post(CREATE_POST_PAYLOAD)

    assert response.status_code == 201

    body = response.json()

    assert isinstance(body, dict)
    assert body["title"] == CREATE_POST_PAYLOAD["title"]
    assert body["body"] == CREATE_POST_PAYLOAD["body"]
    assert body["userId"] == CREATE_POST_PAYLOAD["userId"]
    assert "id" in body
    assert isinstance(body["id"], int)


@pytest.mark.regression
def test_jsonplaceholder_update_post_returns_200_and_updated_fields(jsonplaceholder_client):
    """
    Verify that updating a post returns 200 OK and the updated payload fields.
    """
    response = jsonplaceholder_client.update_post(POST_ID, UPDATE_POST_PAYLOAD)

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert body["id"] == UPDATE_POST_PAYLOAD["id"]
    assert body["title"] == UPDATE_POST_PAYLOAD["title"]
    assert body["body"] == UPDATE_POST_PAYLOAD["body"]
    assert body["userId"] == UPDATE_POST_PAYLOAD["userId"]


@pytest.mark.regression
def test_jsonplaceholder_delete_post_returns_200_and_empty_body(jsonplaceholder_client):
    """
    Verify JSONPlaceholder's fake DELETE contract for an existing post.
    """
    response = jsonplaceholder_client.delete_post(POST_ID)

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert len(body) == 0