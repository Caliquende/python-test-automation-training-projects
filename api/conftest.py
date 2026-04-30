import pytest

from api.clients.jsonplaceholder_client import JsonPlaceholderClient
from api.clients.dummyjson_client import DummyJsonClient

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
