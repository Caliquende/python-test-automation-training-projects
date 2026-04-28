"""
Base API client for reusable HTTP request logic.
"""

import requests

from api.config.settings import DEFAULT_TIMEOUT


class BaseClient:
    """
    Base client for API service clients.

    This class centralizes common HTTP methods so test files and
    service-specific clients do not repeat raw requests logic.
    """

    def __init__(self, base_url, timeout=DEFAULT_TIMEOUT):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _build_url(self, endpoint):
        """
        Build a full URL from the base URL and endpoint path.
        """
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def get(self, endpoint, params=None, headers=None):
        """
        Send a GET request.
        """
        return requests.get(
            self._build_url(endpoint),
            params=params,
            headers=headers,
            timeout=self.timeout,
        )

    def post(self, endpoint, json=None, headers=None):
        """
        Send a POST request.
        """
        return requests.post(
            self._build_url(endpoint),
            json=json,
            headers=headers,
            timeout=self.timeout,
        )

    def put(self, endpoint, json=None, headers=None):
        """
        Send a PUT request.
        """
        return requests.put(
            self._build_url(endpoint),
            json=json,
            headers=headers,
            timeout=self.timeout,
        )

    def delete(self, endpoint, headers=None):
        """
        Send a DELETE request.
        """
        return requests.delete(
            self._build_url(endpoint),
            headers=headers,
            timeout=self.timeout,
        )