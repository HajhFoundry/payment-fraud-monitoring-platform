from app.risk.risk_calculator import RiskCalculator

from app.risk.risk_models import RiskAnalysisResult

from app.risk.risk_constants import (
    LOW,
    MEDIUM,
    HIGH,
    CRITICAL,
    APPROVE,
    APPROVE_WITH_MONITORING,
    MANUAL_REVIEW,
    DECLINE
)


class RiskAnalysisManager:

    def __init__(self):

        self.calculator = RiskCalculator()


    def analyze(self, transaction):

        result = RiskAnalysisResult()

        categories = {

            "TRANSACTION":
                self.calculator.transaction_risk(transaction),

            "CUSTOMER":
                self.calculator.customer_risk(transaction),

            "ACCOUNT":
                self.calculator.account_risk(transaction),

            "DEVICE":
                self.calculator.device_risk(transaction),

            "NETWORK":
                self.calculator.network_risk(transaction),

            "MERCHANT":
                self.calculator.merchant_risk(transaction),

            "BEHAVIOR":
                self.calculator.behavior_risk(transaction),

            "AUTHENTICATION":
                self.calculator.authentication_risk(transaction)

        }

        total_score = 0

        for category, (score, factors) in categories.items():

            result.category_scores[category] = score

            result.triggered_factors.extend(factors)

            total_score += score

        result.risk_score = min(total_score, 100)

        if result.risk_score < 25:

            result.risk_level = LOW

            result.recommendation = APPROVE

        elif result.risk_score < 50:

            result.risk_level = MEDIUM

            result.recommendation = APPROVE_WITH_MONITORING

        elif result.risk_score < 75:

            result.risk_level = HIGH

            result.recommendation = MANUAL_REVIEW

        else:

            result.risk_level = CRITICAL

            result.recommendation = DECLINE

        return result