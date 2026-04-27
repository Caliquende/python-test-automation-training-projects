import requests

JSONPLACEHOLDER_BASE_URL = "https://jsonplaceholder.typicode.com"
DUMMYJSON_BASE_URL = "https://dummyjson.com"


def get_dummyjson_access_token():
    """
    Log in to DummyJSON and return a valid access token for authorized requests.
    """
    payload = {
        "username": "emilys",
        "password": "emilyspass",
    }

    response = requests.post(
        f"{DUMMYJSON_BASE_URL}/user/login",
        json=payload,
        timeout=5,
    )

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert "accessToken" in body
    assert isinstance(body["accessToken"], str)
    assert body["accessToken"].strip() != ""

    return body["accessToken"]


def test_jsonplaceholder_get_single_post_returns_expected_fields():
    """
    Verify that a single post can be retrieved and contains the expected fields.
    """
    response = requests.get(
        f"{JSONPLACEHOLDER_BASE_URL}/posts/1",
        timeout=5,
    )

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert body["id"] == 1
    assert isinstance(body["id"], int)
    assert body["userId"] == 1
    assert isinstance(body["userId"], int)
    assert isinstance(body["title"], str)
    assert body["title"].strip() != ""
    assert isinstance(body["body"], str)
    assert body["body"].strip() != ""


def test_jsonplaceholder_get_users_returns_non_empty_list():
    """
    Verify that the users endpoint returns a non-empty list with valid user fields.
    """
    response = requests.get(
        f"{JSONPLACEHOLDER_BASE_URL}/users",
        timeout=5,
    )

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


def test_jsonplaceholder_create_post_returns_201_and_created_fields():
    """
    Verify that creating a post returns 201 Created and echoes the submitted payload.
    """
    payload = {
        "title": "test title",
        "body": "test body",
        "userId": 1,
    }

    response = requests.post(
        f"{JSONPLACEHOLDER_BASE_URL}/posts",
        json=payload,
        timeout=5,
    )

    assert response.status_code == 201

    body = response.json()

    assert isinstance(body, dict)
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    assert "id" in body
    assert isinstance(body["id"], int)


def test_jsonplaceholder_update_post_returns_200_and_updated_fields():
    """
    Verify that updating a post returns 200 OK and the updated payload fields.
    """
    payload = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1,
    }

    response = requests.put(
        f"{JSONPLACEHOLDER_BASE_URL}/posts/1",
        json=payload,
        timeout=5,
    )

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert body["id"] == payload["id"]
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]


def test_jsonplaceholder_delete_post_returns_200_and_empty_body():
    """
    Verify JSONPlaceholder's fake DELETE contract for an existing post.
    """
    response = requests.delete(
        f"{JSONPLACEHOLDER_BASE_URL}/posts/1",
        timeout=5,
    )

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert len(body) == 0


def test_dummyjson_login_success_returns_access_and_refresh_tokens():
    """
    Verify that a successful login returns access and refresh tokens.
    """
    payload = {
        "username": "emilys",
        "password": "emilyspass",
    }

    response = requests.post(
        f"{DUMMYJSON_BASE_URL}/user/login",
        json=payload,
        timeout=5,
    )

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert "accessToken" in body
    assert isinstance(body["accessToken"], str)
    assert body["accessToken"].strip() != ""

    assert "refreshToken" in body
    assert isinstance(body["refreshToken"], str)
    assert body["refreshToken"].strip() != ""

    assert body["username"] == payload["username"]


def test_dummyjson_get_current_user_with_bearer_token_returns_200():
    """
    Verify that a valid Bearer token can access the protected current user endpoint.
    """
    access_token = get_dummyjson_access_token()

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(
        f"{DUMMYJSON_BASE_URL}/user/me",
        headers=headers,
        timeout=5,
    )

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert body["username"] == "emilys"
    assert "email" in body
    assert isinstance(body["email"], str)
    assert body["email"].strip() != ""


def test_dummyjson_get_current_user_without_bearer_token_returns_auth_error():
    """
    Verify that the protected current user endpoint rejects requests without a token.
    """
    response = requests.get(
        f"{DUMMYJSON_BASE_URL}/user/me",
        timeout=5,
    )

    assert response.status_code in (401, 403)

    body = response.json()

    assert isinstance(body, dict)
    assert "message" in body
    assert isinstance(body["message"], str)
    assert body["message"].strip() != ""


def test_dummyjson_get_current_user_with_wrong_bearer_token_returns_auth_error():
    """
    Verify that the protected current user endpoint rejects an invalid Bearer token.
    """
    headers = {
        "Authorization": "Bearer wrong_token",
    }

    response = requests.get(
        f"{DUMMYJSON_BASE_URL}/user/me",
        headers=headers,
        timeout=5,
    )

    assert response.status_code in (401, 403)

    body = response.json()

    assert isinstance(body, dict)
    assert "message" in body
    assert isinstance(body["message"], str)
    assert body["message"].strip() != ""


def test_dummyjson_get_products_returns_limited_product_list():
    """
    Verify that the products endpoint returns a limited list with valid product fields.
    """
    response = requests.get(
        f"{DUMMYJSON_BASE_URL}/products",
        params={"limit": 5},
        timeout=5,
    )

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert "products" in body
    assert isinstance(body["products"], list)
    assert len(body["products"]) == 5

    first_product = body["products"][0]

    assert isinstance(first_product, dict)
    assert isinstance(first_product["id"], int)
    assert first_product["id"] > 0
    assert isinstance(first_product["title"], str)
    assert first_product["title"].strip() != ""
    assert isinstance(first_product["price"], (int, float))
    assert first_product["price"] > 0


def test_dummyjson_add_cart_returns_created_cart_fields():
    """
    Verify that creating a cart returns the expected cart contract.
    """
    payload = {
        "userId": 1,
        "products": [
            {
                "id": 1,
                "quantity": 2,
            },
            {
                "id": 2,
                "quantity": 1,
            },
        ],
    }

    response = requests.post(
        f"{DUMMYJSON_BASE_URL}/carts/add",
        json=payload,
        timeout=5,
    )

    assert response.status_code == 201

    body = response.json()

    assert isinstance(body, dict)
    assert "id" in body
    assert isinstance(body["id"], int)

    assert body["userId"] == payload["userId"]

    assert "products" in body
    assert isinstance(body["products"], list)
    assert len(body["products"]) == len(payload["products"])

    assert "total" in body
    assert isinstance(body["total"], (int, float))
    assert body["total"] > 0

    assert "totalQuantity" in body
    assert isinstance(body["totalQuantity"], int)
    assert body["totalQuantity"] == 3


def test_dummyjson_delete_cart_returns_deleted_marker_fields():
    """
    Verify that deleting a cart returns simulated deletion marker fields.
    """
    response = requests.delete(
        f"{DUMMYJSON_BASE_URL}/carts/1",
        timeout=5,
    )

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert body["id"] == 1
    assert body["isDeleted"] is True
    assert "deletedOn" in body
    assert isinstance(body["deletedOn"], str)
    assert body["deletedOn"].strip() != ""