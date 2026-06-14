import requests
import time

BASE_URL = "http://127.0.0.1:8000"


def test_create_and_update_fraud_case():

    unique_email = f"case_pytest_{int(time.time())}@test.com"

    # Create Customer
    customer_payload = {
        "first_name": "Case",
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

    # Create Account
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

    # Create Fraud Transaction
    transaction_payload = {
        "account_id": account_id,
        "merchant_name": "Crypto Exchange",
        "merchant_category": "Crypto",
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

    # Get latest fraud alert
    alerts_response = requests.get(
        f"{BASE_URL}/fraud-alerts/"
    )

    assert alerts_response.status_code == 200

    alerts = alerts_response.json()

    latest_alert = alerts[-1]
    alert_id = latest_alert["alert_id"]

    # Create Fraud Case
    case_payload = {
        "alert_id": alert_id,
        "assigned_to": "Fraud Analyst 1",
        "case_status": "OPEN",
        "notes": "Pytest fraud case"
    }

    case_response = requests.post(
        f"{BASE_URL}/fraud-cases/",
        json=case_payload
    )

    assert case_response.status_code == 200

    case_data = case_response.json()

    case_id = case_data["case_id"]

    assert case_data["case_status"] == "OPEN"

    # Update Fraud Case
    update_payload = {
        "assigned_to": "Fraud Analyst 1",
        "case_status": "INVESTIGATING",
        "notes": "Updated by pytest"
    }

    update_response = requests.patch(
        f"{BASE_URL}/fraud-cases/{case_id}",
        json=update_payload
    )
    assert update_response.status_code == 200

    updated_case = update_response.json()

    assert updated_case["case_status"] == "INVESTIGATING"