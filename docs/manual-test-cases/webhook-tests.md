TC-036 AUTHORIZED Event
TC-037 CAPTURED Event
TC-038 REFUNDED Event
TC-039 CHARGEBACK Event
TC-040 Invalid Event Type
TC-041 Missing Transaction ID
TC-042 Duplicate Webhook
TC-043 Webhook Processing Time

# Webhook Manual Test Cases

## Purpose

Validate payment provider webhook processing, payment event creation, fraud alert generation, and AWS S3 report upload.

---

## TC-WEBHOOK-001 - Process Chargeback Webhook

**Objective:** Verify chargeback webhook is processed successfully.

**Endpoint:** POST /payments/webhook

**Test Data:**
```json
{
  "transaction_id": 53,
  "event_type": "CHARGEBACK",
  "amount": 7000,
  "provider": "SIMULATED_STRIPE"
}

```

Steps:

Start FastAPI.
Open Swagger or Postman.
Send POST request to /payments/webhook.
Review API response.

Expected Result:

Status code is 200.
Payment event is created.
Fraud alert is created.
Fraud rule is WEBHOOK_CHARGEBACK.
S3 upload status is uploaded = true.

Status: Pass

TC-WEBHOOK-002 - Process Capture Webhook

Objective: Verify capture webhook is processed as a non-fraud payment event.

Endpoint: POST /payments/webhook

Test Data:

{
  "transaction_id": 53,
  "event_type": "CAPTURE",
  "amount": 7000,
  "provider": "SIMULATED_STRIPE"
}

Steps:

Send POST request to /payments/webhook.
Review response.
Confirm no high-risk fraud alert is generated.

Expected Result:

Payment event is created.
Event type is CAPTURE.
No chargeback fraud rule is created.

Status: Not Executed

TC-WEBHOOK-003 - Invalid Transaction ID

Objective: Verify webhook fails when transaction does not exist.

Test Data:

{
  "transaction_id": 999999,
  "event_type": "CHARGEBACK",
  "amount": 7000,
  "provider": "SIMULATED_STRIPE"
}

Expected Result:

API returns error.
No payment event is created.
No S3 report is uploaded.

Status: Not Executed
