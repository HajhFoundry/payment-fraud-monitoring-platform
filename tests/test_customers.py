import requests
import time

BASE_URL = "http://127.0.0.1:8000"


def test_create_customer():

    unique_email = f"pytest_{int(time.time())}@test.com"

    payload = {
        "first_name": "Pytest",
        "last_name": "Customer",
        "email": unique_email,
        "country": "Canada"
    }

    response = requests.post(
        f"{BASE_URL}/customers/",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["first_name"] == "Pytest"
    assert data["country"] == "Canada"
    assert "customer_id" in data