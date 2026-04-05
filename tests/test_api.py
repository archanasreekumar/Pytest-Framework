

def test_get_users(api_client_fixture):
    response = api_client_fixture("/users")
    assert response.status_code == 200

