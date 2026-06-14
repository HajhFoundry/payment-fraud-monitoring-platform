import requests
import time

BASE_URL = "http://127.0.0.1:8000"


def test_high_amount_transaction_generates_alert():

    unique_email = f"txn_pytest_{int(time.time())}@test.com"

    customer_payload = {
        "first_name": "Transaction",
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
        "balance": 10000,
        "status": "ACTIVE"
    }

    account_response = requests.post(
        f"{BASE_URL}/accounts/",
        json=account_payload
    )

    assert account_response.status_code == 200

    account_id = account_response.json()["account_id"]

    transaction_payload = {
        "account_id": account_id,
        "merchant_name": "Best Buy",
        "merchant_category": "Electronics",
        "amount": 7000,
        "currency": "CAD",
        "country": "USA",
        "status": "APPROVED"
    }

    transaction_response = requests.post(
        f"{BASE_URL}/transactions/",
        json=transaction_payload
    )

    assert transaction_response.status_code == 200

    transaction_data = transaction_response.json()

    assert transaction_data["amount"] == 7000
    assert transaction_data["fraud_alert_count"] > 0