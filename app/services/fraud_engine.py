from datetime import timedelta

from app.database.models import Transaction
from app.risk.risk_analysis_manager import RiskAnalysisManager


HIGH_RISK_MERCHANT_CATEGORIES = ["CRYPTO", "GAMBLING", "MONEY_TRANSFER"]


def evaluate_transaction(transaction, account=None, customer=None, db=None):
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

    if db:
        window_start = transaction.transaction_time - timedelta(seconds=60)

        recent_count = db.query(Transaction).filter(
            Transaction.account_id == transaction.account_id,
            Transaction.transaction_time >= window_start,
            Transaction.transaction_time <= transaction.transaction_time
        ).count()

        if recent_count > 3:
            alerts.append({
                "rule_name": "HIGH_TRANSACTION_VELOCITY",
                "severity": "HIGH"
            })

    risk_manager = RiskAnalysisManager()
    risk_result = risk_manager.analyze(transaction)

    if risk_result.risk_level in ["HIGH", "CRITICAL"]:
        alerts.append({
            "rule_name": f"RISK_SCORE_{risk_result.risk_level}",
            "severity": "HIGH" if risk_result.risk_level == "HIGH" else "CRITICAL"
        })

    return alerts