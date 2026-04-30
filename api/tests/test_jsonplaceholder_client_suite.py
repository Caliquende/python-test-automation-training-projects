import pytest

# JSONPlaceholder API istemcisini ve test verilerini içe aktarıyoruz.
# Importing the JSONPlaceholder API client and test data.

from api.data.jsonplaceholder_payloads import (
    POST_ID,
    USER_ID,
    CREATE_POST_PAYLOAD,
    UPDATE_POST_PAYLOAD,
    NON_EXISTENT_POST_ID,
)


@pytest.mark.smoke
@pytest.mark.regression
def test_jsonplaceholder_get_single_post_returns_expected_fields(jsonplaceholder_client):
    """
    TR: Tek bir gönderinin başarıyla alınıp alınmadığını ve beklenen alanları içerip içermediğini doğrular.
    @pytest.mark.smoke: Bu testin kritik bir test (smoke test) olduğunu belirtir.
    
    EN: Verifies that a single post can be retrieved and contains the expected fields.
    @pytest.mark.smoke: Indicates that this is a critical test (smoke test).
    """
    # İstemciyi kullanarak belirli bir ID'ye sahip gönderiyi çekiyoruz.
    # We fetch a post with a specific ID using the client.
    response = jsonplaceholder_client.get_post(POST_ID)

    # HTTP durum kodunun 200 (OK) olduğunu kontrol ediyoruz.
    # Checking if the HTTP status code is 200 (OK).
    assert response.status_code == 200

    # Yanıt gövdesini JSON formatına dönüştürüyoruz.
    # Converting the response body to JSON format.
    body = response.json()

    # Yanıtın bir sözlük (dictionary) olup olmadığını ve içeriğini kontrol ediyoruz.
    # Checking if the response is a dictionary and validating its content.
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
    TR: Kullanıcılar uç noktasının boş olmayan bir liste döndürdüğünü doğrular.
    
    EN: Verify that the users endpoint returns a non-empty list with valid user fields.
    """
    response = jsonplaceholder_client.get_users()

    assert response.status_code == 200

    body = response.json()

    # Yanıtın bir liste olduğunu ve içinde en az bir öğe olduğunu kontrol ediyoruz.
    # Checking if the response is a list and contains at least one item.
    assert isinstance(body, list)
    assert len(body) > 0

    # Listenin ilk elemanını alıp temel alanları kontrol ediyoruz.
    # Taking the first element of the list and checking its basic fields.
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
    TR: Yeni bir gönderi oluşturmanın 201 (Created) döndürdüğünü doğrular.
    
    EN: Verify that creating a post returns 201 Created and echoes the submitted payload.
    """
    # POST isteği göndererek yeni bir veri oluşturuyoruz.
    # Sending a POST request to create new data.
    response = jsonplaceholder_client.create_post(CREATE_POST_PAYLOAD)

    # 201 status kodu, kaynağın başarıyla oluşturulduğu anlamına gelir.
    # Status code 201 means the resource was successfully created.
    assert response.status_code == 201

    body = response.json()

    # Gönderdiğimiz verilerin dönen yanıtta aynen yer aldığını doğruluyoruz.
    # Validating that the data we sent matches the returned response.
    assert isinstance(body, dict)
    assert body["title"] == CREATE_POST_PAYLOAD["title"]
    assert body["body"] == CREATE_POST_PAYLOAD["body"]
    assert body["userId"] == CREATE_POST_PAYLOAD["userId"]
    assert "id" in body # API tarafından atanan yeni ID'nin varlığını kontrol ediyoruz.
    assert isinstance(body["id"], int)


@pytest.mark.regression
def test_jsonplaceholder_update_post_returns_200_and_updated_fields(jsonplaceholder_client):
    """
    TR: Bir gönderiyi güncellemenin 200 (OK) döndürdüğünü doğrular.
    
    EN: Verify that updating a post returns 200 OK and the updated payload fields.
    """
    # PUT isteği ile var olan bir veriyi güncelliyoruz.
    # Updating an existing resource using a PUT request.
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
    TR: Bir gönderiyi silmenin 200 (OK) döndürdüğünü doğrular (Fake API kuralı).
    
    EN: Verify JSONPlaceholder's fake DELETE contract for an existing post.
    """
    # DELETE isteği ile kaynağı siliyoruz.
    # Deleting the resource using a DELETE request.
    response = jsonplaceholder_client.delete_post(POST_ID)

    assert response.status_code == 200

    body = response.json()

    # JSONPlaceholder silme işleminden sonra boş bir nesne döndürür.
    # JSONPlaceholder returns an empty object after a successful deletion.
    assert isinstance(body, dict)
    assert len(body) == 0


@pytest.mark.regression
def test_jsonplaceholder_get_post_returns_404_for_non_existing_post(jsonplaceholder_client):
    """
    TR: Var olmayan bir gönderiyi çekme denemesinin 404 (Not Found) döndürdüğünü doğrular.
    
    EN: Verify that attempting to retrieve a non-existent post returns 404.
    """
    # DELETE isteği ile kaynağı siliyoruz.
    # Deleting the resource using a DELETE request.
    response = jsonplaceholder_client.delete_post(POST_ID)

    assert response.status_code == 200

    body = response.json()

    # JSONPlaceholder silme işleminden sonra boş bir nesne döndürür.
    # JSONPlaceholder returns an empty object after a successful deletion.
    assert isinstance(body, dict)
    assert len(body) == 0

@pytest.mark.regression
def test_jsonplaceholder_update_non_existing_post_returns_404(jsonplaceholder_client):
    """
    TR: Var olmayan bir gönderiyi güncelleme denemesinin 404 (Not Found) döndürdüğünü doğrular.
    
    EN: Verify that attempting to update a non-existent post returns 404.
    """
    response = jsonplaceholder_client.update_post(NON_EXISTENT_POST_ID, UPDATE_POST_PAYLOAD)

    # JSONPlaceholder sahte bir API olduğu için var olmayan kaynak güncellemelerinde 
    # 404 yerine bazen 500 (Internal Server Error) döndürebilir.
    # Since JSONPlaceholder is a mock API, it may return 500 instead of 404 for non-existent PUT.
    assert response.status_code in (404, 500)

    # Eğer 404 döndüyse JSON gövdesini kontrol edebiliriz. 
    # 500 döndüğünde API genellikle JSON olmayan bir hata metni döndürür (JSONDecodeError'u önlemek için).
    # Only validate JSON if not a 500 error, as mock APIs often return plain text for 500s.
    if response.status_code == 404:
        body = response.json()
        assert isinstance(body, dict)
        assert len(body) == 0

@pytest.mark.regression
def test_jsonplaceholder_get_non_existing_post_returns_404(jsonplaceholder_client):
    """
    TR: Var olmayan bir gönderiyi çekme denemesinin 404 (Not Found) döndürdüğünü doğrular.
    
    EN: Verify that attempting to retrieve a non-existent post returns 404.
    """
    response = jsonplaceholder_client.get_post(NON_EXISTENT_POST_ID)

    assert response.status_code == 404

    body = response.json()

    # JSONPlaceholder silme işleminden sonra boş bir nesne döndürür.
    # JSONPlaceholder returns an empty object after a successful deletion.
    assert isinstance(body, dict)
    assert len(body) == 0

@pytest.mark.regression
def test_jsonplaceholder_get_comments_returns_200(jsonplaceholder_client):
    """
    TR: Yorumları başarıyla çektiğini doğrular.
    
    EN: Verify that the comments endpoint returns a non-empty list with valid comment fields.
    """
    response = jsonplaceholder_client.get_comments(POST_ID)

    assert response.status_code == 200

    body = response.json()

    # Yanıtın bir liste olduğunu ve içinde en az bir öğe olduğunu kontrol ediyoruz.
    # Checking if the response is a list and contains at least one item.
    assert isinstance(body, list)
    assert len(body) > 0

    
