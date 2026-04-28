"""
Client for JSONPlaceholder API endpoints.
"""

from api.clients.base_client import BaseClient
from api.config.settings import JSONPLACEHOLDER_BASE_URL


class JsonPlaceholderClient(BaseClient):
    """
    API client for JSONPlaceholder post and user endpoints.
    """

    def __init__(self):
        super().__init__(JSONPLACEHOLDER_BASE_URL)

    def get_post(self, post_id):
        """
        Get a single post by ID.
        """
        return self.get(f"/posts/{post_id}")

    def get_users(self):
        """
        Get all users.
        """
        return self.get("/users")

    def create_post(self, payload):
        """
        Create a post.
        """
        return self.post("/posts", json=payload)

    def update_post(self, post_id, payload):
        """
        Update a post by ID.
        """
        return self.put(f"/posts/{post_id}", json=payload)

    def delete_post(self, post_id):
        """
        Delete a post by ID.
        """
        return self.delete(f"/posts/{post_id}")