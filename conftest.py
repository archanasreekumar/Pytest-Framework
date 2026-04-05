import pytest
from utils.api_client import get

@pytest.fixture
def api_client_fixture():
    return get
