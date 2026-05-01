"""
TR: DummyJSON testleri için yeniden kullanılabilir veri paketleri (payloads) ve beklenen değerler.
EN: Reusable payloads and expected values for DummyJSON tests.
"""

from env_loader import get_required_env


# Giriş yapmak için kullanılacak kullanıcı bilgileri.
# User credentials to be used for login.
LOGIN_PAYLOAD = {
    "username": get_required_env("DUMMYJSON_USERNAME"),
    "password": get_required_env("DUMMYJSON_PASSWORD"),
}

# Giriş sonrası doğrulanacak beklenen kullanıcı adı.
# Expected username to verify after login.
EXPECTED_USERNAME = get_required_env("DUMMYJSON_EXPECTED_USERNAME")

# Hata durumlarını test etmek için yanlış token.
# Wrong token for testing error scenarios.
WRONG_ACCESS_TOKEN = get_required_env("DUMMYJSON_WRONG_ACCESS_TOKEN")

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
