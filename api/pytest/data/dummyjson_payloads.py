"""
TR: DummyJSON testleri için yeniden kullanılabilir veri paketleri (payloads) ve beklenen değerler.
EN: Reusable payloads and expected values for DummyJSON tests.
"""

from env_loader import get_required_env


def get_login_payload():
    """
    TR: Giriş yapmak için kullanılacak kullanıcı bilgilerini çalışma zamanında döndürür.
    EN: Return login credentials at runtime.
    """
    return {
        "username": get_required_env("DUMMYJSON_USERNAME"),
        "password": get_required_env("DUMMYJSON_PASSWORD"),
    }


def get_expected_username():
    """
    TR: Giriş sonrası doğrulanacak beklenen kullanıcı adını çalışma zamanında döndürür.
    EN: Return the expected username at runtime.
    """
    return get_required_env("DUMMYJSON_EXPECTED_USERNAME")


def get_wrong_access_token():
    """
    TR: Hata durumlarını test etmek için yanlış token değerini çalışma zamanında döndürür.
    EN: Return the wrong token used for error scenarios at runtime.
    """
    return get_required_env("DUMMYJSON_WRONG_ACCESS_TOKEN")

# Yetki hataları için beklenen HTTP durum kodları.
# Expected HTTP status codes for authorization errors.
AUTH_ERROR_STATUS_CODES = (401, 403)

# Ürün listeleme testi için limit değeri.
# Limit value for product listing test.
PRODUCTS_LIMIT = 5

# Sepet işlemleri için örnek ID.
# Sample ID for cart operations.
CART_ID = 1

# Sepete ürün eklemek için gönderilecek veri yapısı.
# The data structure to be sent to the API when adding items to a cart.
ADD_CART_PAYLOAD = {
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

# Sepetteki toplam beklenen ürün adedi.
# Total expected quantity of items in the cart.
EXPECTED_CART_TOTAL_QUANTITY = 3

# Var olmayan bir sepet için ID.
NON_EXISTENT_CART_ID = 999
