"""
TR: Yeniden kullanılabilir HTTP istek mantığı için temel API istemcisi.
EN: Base API client for reusable HTTP request logic.
"""

from copy import deepcopy

import requests

from api.pytest.config.settings import DEFAULT_TIMEOUT


SENSITIVE_KEYS = {
    "access_token",
    "authorization",
    "accesstoken",
    "cookie",
    "password",
    "refresh_token",
    "refreshtoken",
    "set-cookie",
    "token",
}


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
        self.request_history = []

    def _build_url(self, endpoint):
        """
        TR: Temel URL ve uç nokta yolundan tam bir URL oluşturur.
        EN: Build a full URL from the base URL and endpoint path.
        """
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def _redact_sensitive_values(self, value):
        """
        TR: Log dosyalarına hassas değerlerin yazılmasını engeller.
        EN: Prevent sensitive values from being written to log files.
        """
        if isinstance(value, dict):
            return {
                key: "***REDACTED***"
                if str(key).lower() in SENSITIVE_KEYS
                else self._redact_sensitive_values(item)
                for key, item in value.items()
            }

        if isinstance(value, list):
            return [self._redact_sensitive_values(item) for item in value]

        return value

    def _record_exchange(self, method, url, request_kwargs, response):
        """
        TR: Başarısız API testlerinde yazdırılmak üzere request/response bilgisini saklar.
        EN: Store request/response data for failed API test diagnostics.
        """
        request_data = deepcopy(request_kwargs)
        request_data = self._redact_sensitive_values(request_data)
        response_headers = self._redact_sensitive_values(dict(response.headers))

        try:
            response_body = response.json()
        except ValueError:
            response_body = response.text

        response_body = self._redact_sensitive_values(response_body)

        self.request_history.append(
            {
                "request": {
                    "method": method,
                    "url": url,
                    "params": request_data.get("params"),
                    "headers": request_data.get("headers"),
                    "json": request_data.get("json"),
                    "timeout": request_data.get("timeout"),
                },
                "response": {
                    "status_code": response.status_code,
                    "headers": response_headers,
                    "body": response_body,
                },
            }
        )

    def _send(self, method, endpoint, **request_kwargs):
        """
        TR: Ortak HTTP gönderim noktası; tüm istekleri loglanabilir hale getirir.
        EN: Shared HTTP sender that makes every request loggable.
        """
        url = self._build_url(endpoint)
        request_kwargs["timeout"] = self.timeout

        response = requests.request(method, url, **request_kwargs)
        self._record_exchange(method, url, request_kwargs, response)

        return response

    def get(self, endpoint, params=None, headers=None):
        """
        TR: Bir GET isteği gönderir (Veri okumak için kullanılır).
        EN: Send a GET request (Used for reading data).
        """
        return self._send(
            "GET",
            endpoint,
            params=params,
            headers=headers,
        )

    def post(self, endpoint, json=None, headers=None):
        """
        TR: Bir POST isteği gönderir (Yeni veri oluşturmak için kullanılır).
        EN: Send a POST request (Used for creating new data).
        """
        return self._send(
            "POST",
            endpoint,
            json=json,
            headers=headers,
        )

    def put(self, endpoint, json=None, headers=None):
        """
        TR: Bir PUT isteği gönderir (Var olan veriyi tamamen güncellemek için kullanılır).
        EN: Send a PUT request (Used for fully updating an existing resource).
        """
        return self._send(
            "PUT",
            endpoint,
            json=json,
            headers=headers,
        )

    def delete(self, endpoint, headers=None):
        """
        TR: Bir DELETE isteği gönderir (Veriyi silmek için kullanılır).
        EN: Send a DELETE request (Used for deleting a resource).
        """
        return self._send(
            "DELETE",
            endpoint,
            headers=headers,
        )
