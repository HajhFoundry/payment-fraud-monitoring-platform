import requests
import time

BASE_URL = "http://127.0.0.1:8000"


def test_create_account():

    unique_email = f"account_pytest_{int(time.time())}@test.com"

    customer_payload = {
        "first_name": "Account",
        "last_name": "Tester",
        "email": unique_email,
        "country": "Canada"
    }

    customer_response = requests.post(
        f"{BASE_URL}/customers/",
        json=customer_payload
    )

    assert customer_response.status_code == 200

    customer_id = customer_response.json()["customer_id"]

    account_payload = {
        "customer_id": customer_id,
        "account_type": "CHECKING",
        "balance": 5000,
        "status": "ACTIVE"
    }

    account_response = requests.post(
        f"{BASE_URL}/accounts/",
        json=account_payload
    )

    assert account_response.status_code == 200

    account_data = account_response.json()

    assert account_data["customer_id"] == customer_id
    assert account_data["account_type"] == "CHECKING"
    assert account_data["status"] == "ACTIVE"