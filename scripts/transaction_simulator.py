import random
import time
import requests

API_URL = "http://127.0.0.1:8000/transactions/"

NORMAL_MERCHANTS = [
    ("Walmart", "Retail"),
    ("Tim Hortons", "Food"),
    ("Shell", "Fuel"),
    ("Amazon", "Ecommerce"),
    ("Shoppers Drug Mart", "Pharmacy"),
]

HIGH_RISK_MERCHANTS = [
    ("Crypto Exchange", "CRYPTO"),
    ("Online Casino", "GAMBLING"),
    ("Money Transfer App", "MONEY_TRANSFER"),
]

COUNTRIES = ["Canada", "USA", "Mexico", "Brazil", "UK"]


def send_transaction(payload):
    response = requests.post(API_URL, json=payload)

    print("Status:", response.status_code)
    print("Response:", response.json())
    print("-" * 60)


def generate_normal_transaction():
    merchant_name, merchant_category = random.choice(NORMAL_MERCHANTS)

    return {
        "account_id": 1,
        "merchant_name": merchant_name,
        "merchant_category": merchant_category,
        "amount": round(random.uniform(5, 300), 2),
        "currency": "CAD",
        "country": "Canada",
        "status": "APPROVED",
    }


def generate_high_amount_transaction():
    merchant_name, merchant_category = random.choice(NORMAL_MERCHANTS)

    return {
        "account_id": 1,
        "merchant_name": merchant_name,
        "merchant_category": merchant_category,
        "amount": round(random.uniform(5500, 9000), 2),
        "currency": "CAD",
        "country": "Canada",
        "status": "APPROVED",
    }


def generate_foreign_high_risk_transaction():
    merchant_name, merchant_category = random.choice(HIGH_RISK_MERCHANTS)

    return {
        "account_id": 1,
        "merchant_name": merchant_name,
        "merchant_category": merchant_category,
        "amount": round(random.uniform(1200, 8000), 2),
        "currency": "CAD",
        "country": random.choice(["USA", "Mexico", "Brazil", "UK"]),
        "status": random.choice(["APPROVED", "DECLINED"]),
    }


def run_velocity_scenario():
    print("Running velocity scenario...")

    for _ in range(5):
        payload = {
            "account_id": 1,
            "merchant_name": "Tim Hortons",
            "merchant_category": "Food",
            "amount": 15.00,
            "currency": "CAD",
            "country": "Canada",
            "status": "APPROVED",
        }
        send_transaction(payload)
        time.sleep(1)


def run_simulation():
    print("Starting transaction simulation...")

    for _ in range(5):
        send_transaction(generate_normal_transaction())
        time.sleep(1)

    for _ in range(3):
        send_transaction(generate_high_amount_transaction())
        time.sleep(1)

    for _ in range(3):
        send_transaction(generate_foreign_high_risk_transaction())
        time.sleep(1)

    run_velocity_scenario()

    print("Simulation complete.")


if __name__ == "__main__":
    run_simulation()