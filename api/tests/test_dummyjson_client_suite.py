import pytest


from api.data.dummyjson_payloads import (
    get_login_payload,
    get_expected_username,
    get_wrong_access_token,
    AUTH_ERROR_STATUS_CODES,
    PRODUCTS_LIMIT,
    CART_ID,
    ADD_CART_PAYLOAD,
    EXPECTED_CART_TOTAL_QUANTITY,
    NON_EXISTENT_CART_ID,
)


def _assert_non_empty_string(value):
    assert isinstance(value, str)
    assert value.strip() != ""


def _assert_valid_access_token(body):
    assert "accessToken" in body
    _assert_non_empty_string(body["accessToken"])


def _assert_error_message_body(body):
    assert isinstance(body, dict)
    assert "message" in body
    _assert_non_empty_string(body["message"])


def _get_dummyjson_access_token(dummyjson_client):
    """
    TR: Yardımcı fonksiyon: DummyJSON'a giriş yapar ve yetkili istekler için geçerli bir access token döndürür.
    EN: Helper function: Log in to DummyJSON and return a valid access token for authorized requests.
    """
    response = dummyjson_client.login(get_login_payload())

    assert response.status_code == 200

    body = response.json()

    # Token'ın varlığını ve formatını kontrol ediyoruz.
    # Checking for token existence and its format.
    assert isinstance(body, dict)
    _assert_valid_access_token(body)

    return body["accessToken"]


@pytest.mark.smoke
@pytest.mark.regression
def test_dummyjson_login_success_returns_access_and_refresh_tokens(dummyjson_client):
    """
    TR: Başarılı bir girişin access ve refresh token döndürdüğünü doğrular.
    EN: Verify that a successful login returns access and refresh tokens.
    """
    login_payload = get_login_payload()
    response = dummyjson_client.login(login_payload)

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    _assert_valid_access_token(body)

    # Refresh token genellikle daha uzun süreli oturumlar için kullanılır.
    # Refresh tokens are usually used for longer-lived sessions.
    assert "refreshToken" in body
    _assert_non_empty_string(body["refreshToken"])

    assert body["username"] == login_payload["username"]


@pytest.mark.smoke
@pytest.mark.regression
def test_dummyjson_get_current_user_with_bearer_token_returns_200(dummyjson_client):
    """
    TR: Geçerli bir Bearer token ile korumalı bir uç noktaya (me) erişilebildiğini doğrular.
    EN: Verify that a valid Bearer token can access the protected current user endpoint.
    """
    # Önce giriş yapıp token alıyoruz.
    # First, login and get a token.
    access_token = _get_dummyjson_access_token(dummyjson_client)

    # Aldığımız token'ı kullanarak profil bilgilerini çekiyoruz.
    # Fetching profile info using the obtained token.
    response = dummyjson_client.get_current_user(access_token)

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert body["username"] == get_expected_username()
    assert "email" in body
    _assert_non_empty_string(body["email"])


@pytest.mark.regression
def test_dummyjson_get_current_user_without_bearer_token_returns_auth_error(dummyjson_client):
    """
    TR: Negatif Test: Token olmadan korumalı uç noktaya erişimin reddedildiğini doğrular.
    EN: Negative Test: Verify that the protected current user endpoint rejects requests without a token.
    """
    response = dummyjson_client.get_current_user()

    # 401 (Unauthorized) veya 403 (Forbidden) dönmesi beklenir.
    # Expected to return 401 (Unauthorized) or 403 (Forbidden).
    assert response.status_code in AUTH_ERROR_STATUS_CODES

    body = response.json()

    _assert_error_message_body(body)


@pytest.mark.regression
def test_dummyjson_get_current_user_with_wrong_bearer_token_returns_auth_error(dummyjson_client):
    """
    TR: Negatif Test: Yanlış bir Bearer token ile erişimin reddedildiğini doğrular.
    EN: Negative Test: Verify that the protected current user endpoint rejects an invalid Bearer token.
    """
    response = dummyjson_client.get_current_user(get_wrong_access_token())

    assert response.status_code in AUTH_ERROR_STATUS_CODES

    body = response.json()

    _assert_error_message_body(body)


@pytest.mark.smoke
@pytest.mark.regression
def test_dummyjson_get_products_returns_limited_product_list(dummyjson_client):
    """
    TR: Ürünler uç noktasının sınırlı sayıda (limit) ürün döndürdüğünü doğrular.
    EN: Verify that the products endpoint returns a limited list with valid product fields.
    """
    response = dummyjson_client.get_products(PRODUCTS_LIMIT)

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert "products" in body
    assert isinstance(body["products"], list)
    # Dönen ürün sayısının gönderdiğimiz limit ile aynı olduğunu kontrol ediyoruz.
    # Checking if the returned product count matches the limit we sent.
    assert len(body["products"]) == PRODUCTS_LIMIT

    first_product = body["products"][0]

    assert isinstance(first_product, dict)
    assert isinstance(first_product["id"], int)
    assert first_product["id"] > 0
    _assert_non_empty_string(first_product["title"])
    assert isinstance(first_product["price"], (int, float))
    assert first_product["price"] > 0


@pytest.mark.regression
def test_dummyjson_add_cart_returns_created_cart_fields(dummyjson_client):
    """
    TR: Yeni bir sepet oluşturmanın beklenen veri yapısını döndürdüğünü doğrular.
    EN: Verify that creating a cart returns the expected cart contract.
    """
    response = dummyjson_client.add_cart(ADD_CART_PAYLOAD)

    # Not: Bazı API'lar yeni kaynak için 201 döndürür, DummyJSON 201 veya 200 dönebilir.
    # Note: Some APIs return 201 for new resources; DummyJSON might return 201 or 200.
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
    # Toplam ürün miktarının doğruluğunu kontrol ediyoruz.
    # Verifying the correctness of the total quantity.
    assert body["totalQuantity"] == EXPECTED_CART_TOTAL_QUANTITY


@pytest.mark.regression
def test_dummyjson_delete_cart_returns_deleted_marker_fields(dummyjson_client):
    """
    TR: Bir sepeti silmenin silinme işaretlerini (isDeleted) döndürdüğünü doğrular.
    EN: Verify that deleting a cart returns simulated deletion marker fields.
    """
    response = dummyjson_client.delete_cart(CART_ID)

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert body["id"] == CART_ID
    # DummyJSON gerçek silme yapmaz, silindiğine dair bayrak döner.
    # DummyJSON doesn't perform a real delete; it returns a flag indicating deletion.
    assert body["isDeleted"] is True
    assert "deletedOn" in body
    _assert_non_empty_string(body["deletedOn"])

@pytest.mark.regression
def test_dummyjson_delete_cart_returns_404_for_non_existing_cart(dummyjson_client):
    """
    TR: Negatif Test: Var olmayan bir sepeti silme denemesinin 404 (Not Found) döndürdüğünü doğrular.
    EN: Negative Test: Verify that attempting to delete a non-existent cart returns 404.
    """
    response = dummyjson_client.delete_cart(NON_EXISTENT_CART_ID)

    assert response.status_code == 404

    body = response.json()
    _assert_error_message_body(body)
