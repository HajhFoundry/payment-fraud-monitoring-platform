import json


def lambda_handler(event, context=None):
    """
    Simulated AWS Lambda fraud processor.

    In real AWS, this function would be triggered when a new payment
    event report is uploaded to S3.
    """

    print("Lambda fraud processor started")

    event_type = event.get("event_type")
    transaction_id = event.get("transaction_id")
    amount = event.get("amount")
    provider = event.get("provider")

    fraud_detected = False
    fraud_rule = None
    severity = None

    if event_type == "CHARGEBACK":
        fraud_detected = True
        fraud_rule = "LAMBDA_CHARGEBACK_REVIEW"
        severity = "HIGH"

    result = {
        "transaction_id": transaction_id,
        "event_type": event_type,
        "amount": amount,
        "provider": provider,
        "fraud_detected": fraud_detected,
        "fraud_rule": fraud_rule,
        "severity": severity
    }

    print(json.dumps(result, indent=4))

    return result


if __name__ == "__main__":
    sample_event = {
        "transaction_id": 53,
        "event_type": "CHARGEBACK",
        "amount": 7000,
        "provider": "SIMULATED_STRIPE"
    }

    lambda_handler(sample_event)