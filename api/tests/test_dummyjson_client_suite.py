import pytest

from api.clients.dummyjson_client import DummyJsonClient
from api.data.dummyjson_payloads import (
    LOGIN_PAYLOAD,
    EXPECTED_USERNAME,
    WRONG_ACCESS_TOKEN,
    AUTH_ERROR_STATUS_CODES,
    PRODUCTS_LIMIT,
    CART_ID,
    ADD_CART_PAYLOAD,
    EXPECTED_CART_TOTAL_QUANTITY,
)


@pytest.fixture
def dummyjson_client():
    """
    Provide a DummyJSON API client for tests.
    """
    return DummyJsonClient()


def _get_dummyjson_access_token(dummyjson_client):
    """
    Log in to DummyJSON and return a valid access token for authorized requests.
    """
    response = dummyjson_client.login(LOGIN_PAYLOAD)

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert "accessToken" in body
    assert isinstance(body["accessToken"], str)
    assert body["accessToken"].strip() != ""

    return body["accessToken"]


@pytest.mark.smoke
@pytest.mark.regression
def test_dummyjson_login_success_returns_access_and_refresh_tokens(dummyjson_client):
    """
    Verify that a successful login returns access and refresh tokens.
    """
    response = dummyjson_client.login(LOGIN_PAYLOAD)

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert "accessToken" in body
    assert isinstance(body["accessToken"], str)
    assert body["accessToken"].strip() != ""

    assert "refreshToken" in body
    assert isinstance(body["refreshToken"], str)
    assert body["refreshToken"].strip() != ""

    assert body["username"] == LOGIN_PAYLOAD["username"]


@pytest.mark.smoke
@pytest.mark.regression
def test_dummyjson_get_current_user_with_bearer_token_returns_200(dummyjson_client):
    """
    Verify that a valid Bearer token can access the protected current user endpoint.
    """
    access_token = _get_dummyjson_access_token(dummyjson_client)

    response = dummyjson_client.get_current_user(access_token)

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert body["username"] == EXPECTED_USERNAME
    assert "email" in body
    assert isinstance(body["email"], str)
    assert body["email"].strip() != ""


@pytest.mark.regression
def test_dummyjson_get_current_user_without_bearer_token_returns_auth_error(dummyjson_client):
    """
    Verify that the protected current user endpoint rejects requests without a token.
    """
    response = dummyjson_client.get_current_user()

    assert response.status_code in AUTH_ERROR_STATUS_CODES

    body = response.json()

    assert isinstance(body, dict)
    assert "message" in body
    assert isinstance(body["message"], str)
    assert body["message"].strip() != ""


@pytest.mark.regression
def test_dummyjson_get_current_user_with_wrong_bearer_token_returns_auth_error(dummyjson_client):
    """
    Verify that the protected current user endpoint rejects an invalid Bearer token.
    """
    response = dummyjson_client.get_current_user(WRONG_ACCESS_TOKEN)

    assert response.status_code in AUTH_ERROR_STATUS_CODES

    body = response.json()

    assert isinstance(body, dict)
    assert "message" in body
    assert isinstance(body["message"], str)
    assert body["message"].strip() != ""


@pytest.mark.smoke
@pytest.mark.regression
def test_dummyjson_get_products_returns_limited_product_list(dummyjson_client):
    """
    Verify that the products endpoint returns a limited list with valid product fields.
    """
    response = dummyjson_client.get_products(PRODUCTS_LIMIT)

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert "products" in body
    assert isinstance(body["products"], list)
    assert len(body["products"]) == PRODUCTS_LIMIT

    first_product = body["products"][0]

    assert isinstance(first_product, dict)
    assert isinstance(first_product["id"], int)
    assert first_product["id"] > 0
    assert isinstance(first_product["title"], str)
    assert first_product["title"].strip() != ""
    assert isinstance(first_product["price"], (int, float))
    assert first_product["price"] > 0


@pytest.mark.regression
def test_dummyjson_add_cart_returns_created_cart_fields(dummyjson_client):
    """
    Verify that creating a cart returns the expected cart contract.
    """
    response = dummyjson_client.add_cart(ADD_CART_PAYLOAD)

    assert response.status_code == 201

    body = response.json()

    assert isinstance(body, dict)
    assert "id" in body
    assert isinstance(body["id"], int)

    assert body["userId"] == ADD_CART_PAYLOAD["userId"]

    assert "products" in body
    assert isinstance(body["products"], list)
    assert len(body["products"]) == len(ADD_CART_PAYLOAD["products"])

    assert "total" in body
    assert isinstance(body["total"], (int, float))
    assert body["total"] > 0

    assert "totalQuantity" in body
    assert isinstance(body["totalQuantity"], int)
    assert body["totalQuantity"] == EXPECTED_CART_TOTAL_QUANTITY


@pytest.mark.regression
def test_dummyjson_delete_cart_returns_deleted_marker_fields(dummyjson_client):
    """
    Verify that deleting a cart returns simulated deletion marker fields.
    """
    response = dummyjson_client.delete_cart(CART_ID)

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert body["id"] == CART_ID
    assert body["isDeleted"] is True
    assert "deletedOn" in body
    assert isinstance(body["deletedOn"], str)
    assert body["deletedOn"].strip() != ""