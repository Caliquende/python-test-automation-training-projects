"""
Reusable payloads and expected values for DummyJSON tests.
"""

LOGIN_PAYLOAD = {
    "username": "emilys",
    "password": "emilyspass",
}

EXPECTED_USERNAME = "emilys"

WRONG_ACCESS_TOKEN = "wrong_token"

AUTH_ERROR_STATUS_CODES = (401, 403)

PRODUCTS_LIMIT = 5

CART_ID = 1

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

EXPECTED_CART_TOTAL_QUANTITY = 3