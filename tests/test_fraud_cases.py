import time


def test_create_and_update_fraud_case(client):

    unique_email = f"case_pytest_{int(time.time())}@test.com"

    # Create Customer
    customer_payload = {
        "first_name": "Case",
        "last_name": "Tester",
        "email": unique_email,
        "country": "Canada"
    }

    customer_response = client.post(
        "/customers/",
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

    account_response = client.post(
        "/accounts/",
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

    transaction_response = client.post(
        "/transactions/",
        json=transaction_payload
    )

    assert transaction_response.status_code == 200

    # Get latest fraud alert
    alerts_response = client.get(
        "/fraud-alerts/"
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

    case_response = client.post(
        "/fraud-cases/",
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

    update_response = client.patch(
        f"/fraud-cases/{case_id}",
        json=update_payload
    )

    assert update_response.status_code == 200

    updated_case = update_response.json()

    assert updated_case["case_status"] == "INVESTIGATING"