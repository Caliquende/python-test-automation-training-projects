from types import SimpleNamespace

import pytest
import requests

from api.pytest.clients.base_client import BaseClient


def test_exchange_redacts_sensitive_json_headers_and_url(monkeypatch):
    response = SimpleNamespace(
        status_code=200,
        headers={"Set-Cookie": "cookie-value", "Content-Type": "application/json"},
        json=lambda: {"nested": [{"accessToken": "token-value", "ok": 7}]},
    )
    monkeypatch.setattr(requests, "request", lambda *args, **kwargs: response)
    client = BaseClient("https://example.test")

    assert client.post(
        "users?password=url-secret",
        json={"password": "body-secret"},
        headers={"Authorization": "header-secret"},
    ) is response
    exchange = client.request_history[0]
    assert exchange["request"]["url"] == "https://example.test/users"
    assert exchange["request"]["json"]["password"] == "***REDACTED***"
    assert exchange["request"]["headers"]["Authorization"] == "***REDACTED***"
    assert exchange["response"]["headers"]["Set-Cookie"] == "***REDACTED***"
    assert exchange["response"]["body"]["nested"][0] == {
        "accessToken": "***REDACTED***", "ok": 7
    }


def test_non_json_response_body_is_not_logged(monkeypatch):
    def invalid_json():
        raise ValueError("not JSON")

    response = SimpleNamespace(status_code=500, headers={}, json=invalid_json)
    monkeypatch.setattr(requests, "request", lambda *args, **kwargs: response)
    client = BaseClient("https://example.test")
    client.get("users")
    assert client.request_history[0]["response"]["body"] == "[non-JSON response omitted]"


def test_connection_error_is_recorded_without_exception_text(monkeypatch):
    def fail(*args, **kwargs):
        raise requests.ConnectionError("private value")

    monkeypatch.setattr(requests, "request", fail)
    client = BaseClient("https://user:secret@example.test")
    with pytest.raises(requests.ConnectionError):
        client.get("users?token=secret")
    exchange = client.request_history[0]
    assert exchange["request"]["url"] == "https://example.test/users"
    assert exchange["response"] is None
    assert exchange["error_type"] == "ConnectionError"
    assert "private value" not in str(exchange)
