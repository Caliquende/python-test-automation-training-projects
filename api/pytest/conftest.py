import json
import re
from pathlib import Path

import pytest

from api.pytest.clients.jsonplaceholder_client import JsonPlaceholderClient
from api.pytest.clients.dummyjson_client import DummyJsonClient


API_HTTP_LOGS_DIR = Path("reports") / "api" / "http-exchanges"


def _safe_artifact_name(nodeid):
    """
    TR: Pytest nodeid değerini dosya adı olarak güvenli hale getirir.
    EN: Convert a Pytest nodeid into a safe artifact file name.
    """
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", nodeid).strip("_")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    TR: API testi başarısız olduğunda request/response geçmişini JSON olarak yazar.
    EN: Write request/response history as JSON when an API test fails.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    exchanges = []

    for fixture_value in item.funcargs.values():
        request_history = getattr(fixture_value, "request_history", None)

        if request_history:
            exchanges.extend(request_history)

    if not exchanges:
        return

    API_HTTP_LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_path = API_HTTP_LOGS_DIR / f"{_safe_artifact_name(item.nodeid)}.json"
    log_path.write_text(
        json.dumps(exchanges, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


@pytest.fixture
def jsonplaceholder_client():
    """
    TR: Testler için JSONPlaceholder API istemcisi sağlar.
    Bu fixture 'api' klasörü altındaki tüm testlerde kullanılabilir.
    
    EN: Provides a JSONPlaceholder API client for tests.
    This fixture is available to all tests under the 'api' directory.
    """
    return JsonPlaceholderClient()

@pytest.fixture
def dummyjson_client():
    """
    TR: Testler için DummyJSON API istemcisi sağlar.
    EN: Provide a DummyJSON API client for tests.
    """
    return DummyJsonClient()
