from utils.logger import get_logger

logger = get_logger()

def test_get_users(api_client_fixture):
    logger.info("Calling API")
    response = api_client_fixture("/users")
    assert response.status_code == 200

