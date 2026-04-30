"""
TR: JSONPlaceholder API uç noktaları için istemci (client).
EN: Client for JSONPlaceholder API endpoints.
"""

from api.clients.base_client import BaseClient
from api.config.settings import JSONPLACEHOLDER_BASE_URL


class JsonPlaceholderClient(BaseClient):
    """
    TR: JSONPlaceholder gönderi (post) ve kullanıcı (user) uç noktaları için API istemcisi.
    BaseClient sınıfından türetilmiştir (Inheritance), böylece temel HTTP metodlarını kullanabilir.
    
    EN: API client for JSONPlaceholder post and user endpoints.
    Inherits from BaseClient to use basic HTTP methods.
    """

    def __init__(self):
        # BaseClient'ı JSONPlaceholder'ın temel URL'i ile başlatıyoruz.
        # Initializing BaseClient with the JSONPlaceholder base URL.
        super().__init__(JSONPLACEHOLDER_BASE_URL)

    def get_post(self, post_id):
        """
        TR: ID'ye göre tek bir gönderi çeker.
        EN: Get a single post by ID.
        """
        return self.get(f"/posts/{post_id}")

    def get_users(self):
        """
        TR: Tüm kullanıcıları listeler.
        EN: Get all users.
        """
        return self.get("/users")

    def create_post(self, payload):
        """
        TR: Yeni bir gönderi oluşturur (POST).
        EN: Create a post (POST).
        """
        return self.post("/posts", json=payload)

    def update_post(self, post_id, payload):
        """
        TR: Mevcut bir gönderiyi günceller (PUT).
        EN: Update a post by ID (PUT).
        """
        return self.put(f"/posts/{post_id}", json=payload)

    def delete_post(self, post_id):
        """
        TR: Bir gönderiyi siler (DELETE).
        EN: Delete a post by ID (DELETE).
        """
        return self.delete(f"/posts/{post_id}")

    def get_comments(self, post_id):
        """
        TR: Belirli bir gönderiye ait yorumları çeker.
        EN: Get comments for a specific post.
        """
        return self.get(f"/posts/{post_id}/comments")