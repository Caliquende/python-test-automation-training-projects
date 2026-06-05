"""
TR: DummyJSON API uç noktaları için istemci (client).
EN: Client for DummyJSON API endpoints.
"""

from api.pytest.clients.base_client import BaseClient
from api.pytest.config.settings import DUMMYJSON_BASE_URL


class DummyJsonClient(BaseClient):
    """
    TR: DummyJSON kimlik doğrulama (auth), kullanıcı, ürün ve sepet uç noktaları için API istemcisi.
    EN: API client for DummyJSON authentication, user, product, and cart endpoints.
    """

    def __init__(self):
        # BaseClient'ı DummyJSON'ın temel URL'i ile başlatıyoruz.
        # Initializing BaseClient with the DummyJSON base URL.
        super().__init__(DUMMYJSON_BASE_URL)

    @staticmethod
    def _build_auth_headers(access_token):
        """
        TR: Korumalı uç noktalar için Bearer token başlıklarını oluşturur.
        EN: Build Bearer token headers for protected endpoints.
        """
        return {
            "Authorization": f"Bearer {access_token}",
        }

    def login(self, payload):
        """
        TR: Kullanıcı adı ve şifre ile giriş yapar.
        EN: Log in with username and password.
        """
        return self.post("/user/login", json=payload)

    def get_current_user(self, access_token=None):
        """
        TR: O anki oturum açmış kullanıcı bilgilerini çeker.
        Access token sağlanmazsa istek yetkisiz (unauthorized) olarak gönderilir.
        
        EN: Get the current authenticated user.
        If access_token is not provided, the request is sent without Authorization header.
        """
        headers = None

        if access_token is not None:
            headers = self._build_auth_headers(access_token)

        return self.get("/user/me", headers=headers)

    def get_products(self, limit):
        """
        TR: Belirli bir limit ile ürünleri listeler (Query parameter kullanımı).
        EN: Get products with a limit query parameter.
        """
        return self.get(
            "/products",
            params={"limit": limit},
        )

    def add_cart(self, payload):
        """
        TR: Yeni bir sepet oluşturur.
        EN: Create a cart.
        """
        return self.post("/carts/add", json=payload)

    def delete_cart(self, cart_id):
        """
        TR: ID'ye göre bir sepeti siler.
        EN: Delete a cart by ID.
        """
        return self.delete(f"/carts/{cart_id}")
