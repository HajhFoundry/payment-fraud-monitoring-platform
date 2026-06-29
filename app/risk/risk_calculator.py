from app.risk.risk_models import RiskFactor


class RiskCalculator:

    def transaction_risk(self, transaction):

        score = 0

        factors = []

        if transaction.amount >= 5000:

            score += 25

            factors.append(
                RiskFactor(
                    category="TRANSACTION",
                    name="High Amount Transaction",
                    score=25
                )
            )

        return score, factors


    def merchant_risk(self, transaction):

        score = 0

        factors = []

        high_risk_merchants = [
            "Electronics",
            "Crypto",
            "Gift Cards"
        ]

        if transaction.merchant_category.upper() in [m.upper() for m in high_risk_merchants]:

            score += 20

            factors.append(
                RiskFactor(
                    category="MERCHANT",
                    name="High Risk Merchant",
                    score=20
                )
            )

        return score, factors


    def customer_risk(self, transaction):

        return 0, []


    def account_risk(self, transaction):

        return 0, []


    def device_risk(self, transaction):

        return 0, []


    def network_risk(self, transaction):

        return 0, []


    def behavior_risk(self, transaction):

        return 0, []


    def authentication_risk(self, transaction):

        return 0, []