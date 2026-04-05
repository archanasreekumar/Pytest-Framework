import requests
from config.config import BASE_URL

def get(endpoint):
    return requests.get(f"{BASE_URL}{endpoint}")