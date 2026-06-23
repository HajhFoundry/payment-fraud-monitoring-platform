TC-068 Complete Payment Flow
TC-069 Complete Fraud Flow
TC-070 Chargeback Lifecycle
TC-071 S3 → Lambda → DynamoDB Validation
TC-072 Dashboard Reflects Cloud Event
TC-073 End-To-End Audit Trail Validation

# End-to-End Manual Test Cases

## Purpose

Validate the complete payment fraud monitoring workflow across FastAPI, PostgreSQL, AWS S3, AWS Lambda, DynamoDB, CloudWatch, and Streamlit Dashboard.

---

## TC-E2E-001 - Complete Chargeback Fraud Flow

**Objective:** Verify that a chargeback webhook is processed end-to-end across the platform.

**Preconditions:**
- FastAPI is running
- PostgreSQL is running
- AWS S3 bucket exists
- Lambda trigger is configured
- DynamoDB table exists
- Streamlit dashboard is running

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

Open Swagger or Postman.
Send POST /payments/webhook.
Verify API response returns s3_upload.uploaded = true.
Open PostgreSQL and verify record exists in payment_events.
Verify fraud alert exists in fraud_alerts.
Open AWS S3 bucket.
Verify JSON report exists under reports/payment_events/.
Open CloudWatch logs.
Verify Lambda executed successfully.
Open DynamoDB table.
Verify fraud event was inserted.
Open Streamlit dashboard.
Verify Cloud Fraud Events section shows the new event.

Expected Result:

Webhook returns 200 OK.
Payment event is stored in PostgreSQL.
Fraud alert is created.
JSON report is uploaded to AWS S3.
Lambda is triggered by S3.
Lambda writes fraud decision to DynamoDB.
Dashboard displays the cloud fraud event.

Status: Pass

TC-E2E-002 - Verify Cloud Fraud Dashboard Updates

Objective: Verify dashboard reflects fraud events stored in DynamoDB.

Steps:

Trigger a chargeback webhook.
Open Streamlit dashboard.
Go to Cloud Fraud Events section.
Verify KPI values update.
Verify severity chart displays HIGH event.
Verify provider chart displays SIMULATED_STRIPE.

Expected Result:

Cloud Fraud Events count increases.
High Severity Events count increases.
Chargeback Events count increases.
Cloud Fraud Amount updates correctly.

Status: Pass