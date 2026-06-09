# Payment Fraud Detection Platform Architecture

## System Flow

Customer
    |
    v
Account
    |
    v
Transaction API (FastAPI)
    |
    v
Fraud Rules Engine
    |
    +-----> Fraud Alerts
    |
    +-----> Audit Logs
    |
    v
PostgreSQL Database
    |
    v
Reporting Layer
    |
    v
Streamlit Dashboard

---

## Components

### FastAPI

Provides REST APIs for transaction processing and fraud monitoring.

### PostgreSQL

Stores customers, accounts, transactions, fraud alerts, and audit logs.

### Fraud Rules Engine

Evaluates transactions against configured fraud detection rules.

### Reporting Layer

Provides SQL-based analytics and operational reporting.

### Streamlit Dashboard

Displays transaction metrics, fraud trends, and monitoring KPIs.

### Postman

Used for API validation and regression testing.

### Pytest

Used for automated backend testing.

### GitHub Actions

Provides CI/CD automation.

### AWS

Future deployment:
- API Gateway
- Lambda
- S3
- DynamoDB