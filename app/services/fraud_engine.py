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

    if transaction.status.upper() == "DECLINED":
        alerts.append({
            "rule_name": "DECLINED_TRANSACTION",
            "severity": "LOW"
        })

    if customer and transaction.country != customer.country and float(transaction.amount) > 1000:
        alerts.append({
            "rule_name": "LARGE_FOREIGN_TRANSACTION",
            "severity": "HIGH"
        })

    if (
        transaction.merchant_category.upper() in HIGH_RISK_MERCHANT_CATEGORIES
        and float(transaction.amount) > 1000
    ):
        alerts.append({
            "rule_name": "HIGH_RISK_HIGH_AMOUNT_MERCHANT",
            "severity": "HIGH"
        })

    return alerts