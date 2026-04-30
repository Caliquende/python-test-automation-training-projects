"""
TR: Yeniden kullanılabilir HTTP istek mantığı için temel API istemcisi.
EN: Base API client for reusable HTTP request logic.
"""

import requests

from api.config.settings import DEFAULT_TIMEOUT


class BaseClient:
    """
    TR: API servis istemcileri için temel sınıf.
    Bu sınıf, yaygın HTTP metodlarını (GET, POST, PUT, DELETE) merkezileştirir, 
    böylece her istemcide aynı kodları tekrar yazmak zorunda kalmayız (DRY prensibi).
    
    EN: Base client for API service clients.
    This class centralizes common HTTP methods so service-specific clients 
    do not repeat raw requests logic (DRY principle).
    """

    def __init__(self, base_url, timeout=DEFAULT_TIMEOUT):
        # Temel URL'in sonundaki / işaretini temizleyerek kaydediyoruz.
        # Storing the base URL after stripping any trailing slashes.
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _build_url(self, endpoint):
        """
        TR: Temel URL ve uç nokta yolundan tam bir URL oluşturur.
        EN: Build a full URL from the base URL and endpoint path.
        """
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def get(self, endpoint, params=None, headers=None):
        """
        TR: Bir GET isteği gönderir (Veri okumak için kullanılır).
        EN: Send a GET request (Used for reading data).
        """
        return requests.get(
            self._build_url(endpoint),
            params=params,
            headers=headers,
            timeout=self.timeout,
        )

    def post(self, endpoint, json=None, headers=None):
        """
        TR: Bir POST isteği gönderir (Yeni veri oluşturmak için kullanılır).
        EN: Send a POST request (Used for creating new data).
        """
        return requests.post(
            self._build_url(endpoint),
            json=json,
            headers=headers,
            timeout=self.timeout,
        )

    def put(self, endpoint, json=None, headers=None):
        """
        TR: Bir PUT isteği gönderir (Var olan veriyi tamamen güncellemek için kullanılır).
        EN: Send a PUT request (Used for fully updating an existing resource).
        """
        return requests.put(
            self._build_url(endpoint),
            json=json,
            headers=headers,
            timeout=self.timeout,
        )

    def delete(self, endpoint, headers=None):
        """
        TR: Bir DELETE isteği gönderir (Veriyi silmek için kullanılır).
        EN: Send a DELETE request (Used for deleting a resource).
        """
        return requests.delete(
            self._build_url(endpoint),
            headers=headers,
            timeout=self.timeout,
        )