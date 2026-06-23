# Interview Demo Script

## Demo Duration

5-10 Minutes

---

## Business Problem

Financial institutions process thousands of payment transactions daily.

Fraud analysts need visibility into:

* High-value transactions
* Chargebacks
* Fraud alerts
* Payment events
* Cloud-based event processing

The goal was to build a Payment Fraud Monitoring Platform capable of detecting fraud events and processing them through an event-driven AWS architecture.

---

## Architecture Overview

FastAPI

↓

PostgreSQL

↓

Fraud Rules Engine

↓

AWS S3

↓

AWS Lambda

↓

DynamoDB

↓

Streamlit Dashboard

---

## Demo Step 1 - Show Architecture

Open architecture diagram.

Explain:

* API Layer
* Database Layer
* Fraud Layer
* Cloud Layer
* Reporting Layer

---

## Demo Step 2 - Create Fraud Event

Open Swagger or Postman.

Execute:

POST /payments/webhook

Use:

```json
{
  "transaction_id": 53,
  "event_type": "CHARGEBACK",
  "amount": 7000,
  "provider": "SIMULATED_STRIPE"
}
```

Explain:

* Webhook ingestion
* Fraud event processing

---

## Demo Step 3 - Show API Response

Show:

* payment_event_id
* fraud_alert_id
* report_path
* s3_upload

Explain:

* Fraud rule execution
* Event archival

---

## Demo Step 4 - Show AWS S3

Open:

reports/payment_events/

Show uploaded JSON report.

Explain:

* Event archive
* Audit trail

---

## Demo Step 5 - Show AWS Lambda

Open CloudWatch.

Show:

Payment fraud Lambda triggered

Explain:

* Serverless processing
* Event-driven architecture

---

## Demo Step 6 - Show DynamoDB

Open table:

payment_fraud_lambda_events

Show:

* event_type
* severity
* fraud_detected

Explain:

* Fraud decision storage

---

## Demo Step 7 - Show Dashboard

Open Streamlit Dashboard.

Show:

* Fraud KPIs
* Cloud Fraud Events
* Severity Chart
* Provider Chart

Explain:

* Fraud monitoring
* Operational reporting

---

## Demo Conclusion

This solution demonstrates:

* FastAPI
* PostgreSQL
* Fraud Detection
* REST APIs
* AWS S3
* AWS Lambda
* AWS DynamoDB
* CloudWatch
* Dashboard Reporting
* End-to-End Integration
