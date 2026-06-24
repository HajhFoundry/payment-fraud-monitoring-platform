import time


def test_create_customer(client):
    unique_email = f"pytest_{int(time.time())}@test.com"

    payload = {
        "first_name": "Pytest",
        "last_name": "Customer",
        "email": unique_email,
        "country": "Canada"
    }

    response = client.post(
        "/customers/",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["first_name"] == "Pytest"
    assert data["country"] == "Canada"
    assert "customer_id" in data