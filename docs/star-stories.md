# STAR Stories – Payment Fraud Monitoring Platform

## STAR 1 – Building the Fraud Rules Engine

### Situation

The platform initially supported transaction processing but did not have any fraud detection capability.

### Task

Design and implement a fraud detection mechanism that could identify suspicious transactions and generate fraud alerts.

### Action

* Analyzed common fraud scenarios used by financial institutions.
* Implemented fraud rules for:

  * High transaction amount
  * Country mismatch
  * High-risk merchants
  * Transaction velocity
  * Large foreign transactions
* Designed the fraud_alerts table to store rule violations.
* Connected fraud evaluation directly to transaction processing APIs.

### Result

The platform automatically generated fraud alerts during transaction processing and supported multiple alerts per transaction, creating a realistic fraud monitoring workflow.

---

## STAR 2 – Designing the Database Model

### Situation

The project required managing customers, accounts, transactions, fraud alerts, and fraud investigations.

### Task

Create a relational database model that maintained integrity and supported reporting.

### Action

* Designed PostgreSQL schema.
* Created:

  * customers
  * accounts
  * transactions
  * fraud_alerts
  * fraud_cases
  * login_events
  * audit_logs
* Implemented foreign key relationships.
* Used SQLAlchemy ORM for database access.

### Result

Created a scalable data model that supported transaction processing, fraud detection, reporting, and investigations.

---

## STAR 3 – Implementing Fraud Case Management

### Situation

Fraud alerts alone were insufficient because analysts need workflows to investigate suspicious activity.

### Task

Build a fraud case management process.

### Action

* Designed fraud_cases table.
* Implemented APIs for:

  * Create Case
  * Update Case
  * View Cases
* Created workflow states:

  * OPEN
  * INVESTIGATING
  * CLOSED

### Result

The platform simulated real fraud operations workflows used by banks and payment processors.

---

## STAR 4 – Introducing Login Security Monitoring

### Situation

Fraud is not limited to transactions. Account takeover and login abuse are also major risks.

### Task

Extend the platform to support login security monitoring.

### Action

Implemented detection rules for:

* MULTIPLE_OTP_FAILURES
* IMPOSSIBLE_TRAVEL_LOGIN
* MULTIPLE_FAILED_LOGINS
* OTP_SUCCESS_ON_RISKY_LOGIN

Created login_events APIs and integrated alert generation.

### Result

Expanded fraud monitoring beyond transactions and demonstrated broader security awareness.

---

## STAR 5 – Building Dashboard Analytics

### Situation

Raw database records were difficult for analysts and managers to interpret.

### Task

Provide a dashboard that summarizes fraud activity.

### Action

Built a Streamlit dashboard displaying:

* Total transactions
* Total fraud alerts
* Fraud alert rate
* Fraud cases by status
* Fraud alerts by severity
* Fraud alerts by rule
* Top customers by fraud alerts
* Recent activity

### Result

Created a single monitoring interface that improved visibility into fraud activity.

---

## STAR 6 – Implementing Automated Testing

### Situation

Manual testing became repetitive as the project grew.

### Task

Introduce automated regression testing.

### Action

Created Pytest suite:

* test_health.py
* test_customers.py
* test_accounts.py
* test_transactions.py
* test_fraud_cases.py

Automated customer creation, account creation, transaction processing, fraud detection, and case management validation.

### Result

Reduced manual validation effort and created repeatable regression testing.

---

## STAR 7 – Solving API Integration Issues

### Situation

While building automated tests, some API requests failed unexpectedly.

### Task

Identify and resolve API integration problems.

### Action

Investigated response codes and API definitions.

Discovered that the fraud case update endpoint used PATCH rather than PUT.

Updated test automation to align with API contracts.

### Result

Successfully completed automated testing and improved understanding of REST API design.

---

## STAR 8 – Creating Reporting and SQL Analytics

### Situation

Fraud analysts require reporting beyond operational APIs.

### Task

Develop SQL reporting capabilities.

### Action

Created reporting queries covering:

* Fraud alerts by rule
* Fraud alerts by severity
* Top customers
* Transaction volume
* Fraud trends
* Data validation

Practiced advanced SQL concepts including:

* JOIN
* GROUP BY
* HAVING
* CASE
* CTE
* Window Functions

### Result

Built a reporting layer demonstrating both technical and business analytics capabilities.

---

## STAR 9 – Introducing CI/CD

### Situation

The project lacked automated validation during code changes.

### Task

Introduce CI/CD practices.

### Action

Configured GitHub Actions workflow.

Implemented:

* Repository checkout
* Python environment setup
* Dependency installation
* Workflow execution

Prepared the foundation for future automated test execution.

### Result

Introduced DevOps concepts and continuous integration practices.

---

## STAR 10 – End-to-End System Design

### Situation

The objective was to create more than a simple CRUD application.

### Task

Design a realistic business system demonstrating multiple engineering disciplines.

### Action

Combined:

* FastAPI
* PostgreSQL
* SQLAlchemy
* Fraud Detection
* Case Management
* Reporting
* Dashboards
* Postman
* Pytest
* GitHub Actions

into a single platform.

### Result

Delivered an end-to-end fraud monitoring solution demonstrating backend development, database design, testing, analytics, reporting, and operational workflows.
