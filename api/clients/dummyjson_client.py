"""
Client for DummyJSON API endpoints.
"""

from api.clients.base_client import BaseClient
from api.config.settings import DUMMYJSON_BASE_URL


class DummyJsonClient(BaseClient):
    """
    API client for DummyJSON authentication, user, product, and cart endpoints.
    """

    def __init__(self):
        super().__init__(DUMMYJSON_BASE_URL)

    @staticmethod
    def _build_auth_headers(access_token):
        """
        Build Bearer token headers for protected endpoints.
        """
        return {
            "Authorization": f"Bearer {access_token}",
        }

    def login(self, payload):
        """
        Log in with username and password.
        """
        return self.post("/user/login", json=payload)

    def get_current_user(self, access_token=None):
        """
        Get the current authenticated user.

        If access_token is not provided, the request is sent without Authorization header.
        """
        headers = None

        if access_token is not None:
            headers = self._build_auth_headers(access_token)

        return self.get("/user/me", headers=headers)

    def get_products(self, limit):
        """
        Get products with a limit query parameter.
        """
        return self.get(
            "/products",
            params={"limit": limit},
        )

    def add_cart(self, payload):
        """
        Create a cart.
        """
        return self.post("/carts/add", json=payload)

    def delete_cart(self, cart_id):
        """
        Delete a cart by ID.
        """
        return self.delete(f"/carts/{cart_id}")