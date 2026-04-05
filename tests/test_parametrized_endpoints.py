import pytest

@pytest.mark.parametrize("endpoint",["/users","/posts","/comments"])
def test_api_endpoints(api_client_fixture, endpoint):
    response = api_client_fixture(endpoint)
    assert response.status_code == 200
