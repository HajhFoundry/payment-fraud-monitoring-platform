import hashlib


HIGH_RISK_TYPES = ["TRANSFER", "CASH_OUT"]


def stable_hash(value: str) -> int:
    return int(hashlib.md5(value.encode()).hexdigest(), 16)


def enrich_transaction_features(row: dict) -> dict:
    amount = float(row["amount"])
    transaction_type = str(row["type"])
    old_balance = float(row["oldbalanceOrg"])
    new_balance = float(row["newbalanceOrig"])
    destination_balance = float(row["oldbalanceDest"])
    origin_account = str(row["nameOrig"])
    destination_account = str(row["nameDest"])

    hash_value = stable_hash(origin_account + destination_account)

    is_new_device = hash_value % 5 == 0
    is_vpn = hash_value % 7 == 0
    is_foreign_ip = hash_value % 11 == 0
    failed_login_count_1h = hash_value % 6
    merchant_risk_score = hash_value % 100
    beneficiary_age_days = hash_value % 365

    balance_drained = old_balance > 0 and new_balance == 0
    amount_to_balance_ratio = amount / old_balance if old_balance > 0 else 0

    return {
        "amount": amount,
        "transaction_type": transaction_type,
        "old_balance": old_balance,
        "new_balance": new_balance,
        "destination_balance": destination_balance,
        "balance_drained": balance_drained,
        "amount_to_balance_ratio": amount_to_balance_ratio,
        "is_high_risk_type": transaction_type in HIGH_RISK_TYPES,
        "is_new_device": is_new_device,
        "is_vpn": is_vpn,
        "is_foreign_ip": is_foreign_ip,
        "failed_login_count_1h": failed_login_count_1h,
        "merchant_risk_score": merchant_risk_score,
        "beneficiary_age_days": beneficiary_age_days,
    }