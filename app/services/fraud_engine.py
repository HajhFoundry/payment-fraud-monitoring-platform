HIGH_RISK_MERCHANT_CATEGORIES = ["CRYPTO", "GAMBLING", "MONEY_TRANSFER"]


def evaluate_transaction(transaction, account=None, customer=None):
    alerts = []

    if float(transaction.amount) > 5000:
        alerts.append({
            "rule_name": "HIGH_AMOUNT_TRANSACTION",
            "severity": "HIGH"
        })

    if customer and transaction.country != customer.country:
        alerts.append({
            "rule_name": "COUNTRY_MISMATCH",
            "severity": "MEDIUM"
        })

    if transaction.merchant_category.upper() in HIGH_RISK_MERCHANT_CATEGORIES:
        alerts.append({
            "rule_name": "HIGH_RISK_MERCHANT",
            "severity": "MEDIUM"
        })

    return alerts