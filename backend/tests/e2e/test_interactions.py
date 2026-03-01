"""End-to-end tests for the GET /interactions endpoint."""
import os
import requests

BASE_URL = os.getenv("API_BASE_URL", "http://localhost:42001")
API_TOKEN = os.getenv("API_TOKEN", "")

def test_get_interactions_returns_200():
    url = f"{BASE_URL}/interactions/"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200

def test_get_interactions_response_is_a_list():
    url = f"{BASE_URL}/interactions/"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    assert isinstance(data, list)