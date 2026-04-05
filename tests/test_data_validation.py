import requests

def test_get_users_data():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    print(data)
    assert isinstance(data, list)
    assert len(data) > 0

def test_first_user():
    response=requests.get("https://jsonplaceholder.typicode.com/users")
    data=response.json()
    assert data[0]["id"]==1