# 🚀 Payment Fraud Intelligence Platform

Enterprise-grade payment fraud detection, transaction monitoring, investigation, and analytics platform built with **FastAPI**, **PostgreSQL**, **Docker**, **AWS**, **Streamlit**, **Selenium**, and **Machine Learning**.

This project simulates how modern financial institutions detect suspicious transactions, investigate fraud cases, monitor payment events, and evaluate fraud detection performance using both business rules and machine learning.

---

# Business Problem

Financial institutions process millions of payment transactions every day.

A production fraud platform must be able to:

* Detect suspicious transactions in real time
* Generate fraud alerts
* Calculate transaction risk
* Support fraud investigators
* Process payment gateway events
* Maintain audit history
* Produce operational dashboards
* Evaluate fraud detection performance
* Compare rule-based detection with machine learning

This project demonstrates how these capabilities can be implemented using modern enterprise technologies.

---

# Project Vision

The goal of this project is **not** to build a simple CRUD application.

Instead, it demonstrates the architecture of an enterprise fraud intelligence platform similar to those used by:

* Banks
* Payment Processors
* FinTech Companies
* Digital Banking Platforms
* Fraud Investigation Teams

---

# Enterprise Architecture

```text
                        Client Applications
                               │
                               ▼
                      FastAPI REST APIs
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
  Rule Engine           Risk Analysis         Machine Learning
                               │
                               ▼
                      Fraud Decision Engine
                               │
                               ▼
                    PostgreSQL Transaction DB
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
    Dashboard              AWS Services         Batch Import
```

---

# Enterprise Features

## Fraud Detection

* Rule-based fraud detection
* Risk scoring engine
* Fraud alert generation
* Fraud case management
* Chargeback simulation
* Login anomaly detection

## Data Engineering

* Kaggle transaction import
* Batch processing
* Import job tracking
* Historical fraud evaluation

## Machine Learning

* Random Forest baseline model
* Rule Engine vs ML comparison
* Accuracy, Precision, Recall, and F1 evaluation
* Feature engineering using transaction data

> **Note:** The ML implementation is an experimental baseline trained using the PaySim synthetic fraud dataset. It demonstrates the integration of machine learning into a fraud platform and is not intended as a production-ready fraud model.

## Cloud Integration

* AWS S3
* AWS Lambda
* DynamoDB
* CloudWatch

## DevOps

* Docker
* Docker Compose
* GitHub Actions
* CI/CD Pipeline

## Testing

* Pytest
* Selenium UI Automation
* Postman API Testing
* Manual Test Cases

---

# Technology Stack

| Layer            | Technology                             |
| ---------------- | -------------------------------------- |
| Backend          | FastAPI                                |
| Language         | Python                                 |
| Database         | PostgreSQL                             |
| ORM              | SQLAlchemy                             |
| Dashboard        | Streamlit + Plotly                     |
| Machine Learning | Scikit-learn                           |
| Cloud            | AWS (S3, Lambda, DynamoDB, CloudWatch) |
| Testing          | Pytest, Selenium, Postman              |
| DevOps           | Docker, GitHub Actions                 |

---

# Project Structure

```text
payment-fraud-monitoring-platform/
│
├── app/
│   ├── api/
│   ├── analytics/
│   ├── database/
│   ├── importers/
│   ├── ml/
│   ├── risk/
│   ├── services/
│   └── main.py
│
├── dashboard/
│
├── tests/
│
├── scripts/
│
├── docs/
│   ├── screenshots/
│   ├── qa/
│   ├── interview/
│   └── architecture.md
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/HajhFoundry/payment-fraud-monitoring-platform.git
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```
---

# Running the Platform

## Option 1 – Local Development

Start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

Start the Streamlit dashboard:

```bash
streamlit run dashboard/app.py
```

Open:

* Swagger API Documentation: `http://127.0.0.1:8000/docs`
* Streamlit Dashboard: `http://localhost:8501`

---

## Option 2 – Docker Deployment

Build and start the platform:

```bash
docker compose up --build
```

Stop the platform:

```bash
docker compose down
```

Docker deployment includes:

* FastAPI API
* PostgreSQL Database
* Database Health Checks
* Persistent Database Volume

---

# Interview Demo Launcher

To simplify demonstrations during interviews, the repository includes helper scripts.

| Script                      | Purpose                                         |
| --------------------------- | ----------------------------------------------- |
| interview_demo_launcher.bat | Starts FastAPI, Streamlit, and opens Swagger UI |
| start_local_api.bat         | Starts the FastAPI application                  |
| start_dashboard.bat         | Starts the Streamlit dashboard                  |
| start_docker_app.bat        | Starts Docker containers                        |
| stop_docker_app.bat         | Stops Docker containers                         |
| run_selenium_demo.bat       | Executes Selenium UI tests                      |
| run_kaggle_demo.bat         | Executes the Kaggle batch import                |
| run_tests.bat               | Executes the Pytest API test suite              |

---

# API Modules

The platform exposes REST APIs for multiple business domains.

| Module         | Description                        |
| -------------- | ---------------------------------- |
| Customers      | Customer onboarding and management |
| Accounts       | Customer account management        |
| Transactions   | Transaction processing             |
| Fraud Alerts   | Fraud alert generation             |
| Fraud Cases    | Fraud investigation workflow       |
| Login Events   | Authentication monitoring          |
| Payment Events | Payment gateway simulation         |
| Import Jobs    | Batch import tracking              |

---

# Risk Analysis Engine

The platform combines traditional business rules with an enterprise risk analysis framework.

Current risk evaluation includes:

* High Amount Transactions
* Country Mismatch
* High Risk Merchant Categories
* Transaction Velocity
* Large Foreign Transactions
* Merchant Risk Evaluation

The Risk Analysis Manager aggregates individual category scores and produces:

* Risk Score
* Risk Level
* Recommended Action

---

# Kaggle Batch Import

The platform supports importing historical transaction datasets for fraud analysis.

Current implementation includes:

* CSV validation
* Batch import processing
* Import job tracking
* Fraud row statistics
* Import history

Imported datasets can later be used for:

* Fraud analytics
* Machine learning experiments
* Historical reporting

---

# Machine Learning Baseline

An experimental Random Forest model has been added to compare machine learning against the existing rule-based fraud engine.

The implementation demonstrates:

* Feature engineering
* Model training
* Fraud prediction
* Performance evaluation

Current evaluation compares:

* Accuracy
* Precision
* Recall
* F1 Score

> **Note**
>
> The machine learning implementation is a baseline trained using the PaySim synthetic fraud dataset.
>
> The objective is to demonstrate ML integration into an enterprise fraud platform rather than provide a production-ready fraud model.

---

# Dashboard

The Streamlit dashboard provides operational visibility into the platform.

Current dashboard includes:

* Transaction Metrics
* Fraud Alert Metrics
* Fraud Cases
* Login Events
* Payment Events
* Import Jobs
* AWS Cloud Events
* Charts and Analytics

---

# Testing

The project includes multiple testing approaches.

### API Testing

* Swagger UI
* Postman
* Pytest

### UI Testing

* Selenium

### Continuous Integration

GitHub Actions automatically:

* Installs dependencies
* Creates database tables
* Starts the FastAPI application
* Executes automated tests

---

# Application Screenshots

Add screenshots for the following sections.

* Enterprise Architecture
* Swagger API Documentation
* Streamlit Dashboard
* Fraud Alerts
* Fraud Cases
* Docker Deployment
* GitHub Actions
* Selenium Automation
* Kaggle Batch Import
* AWS Dashboard (optional)

---

# Enterprise Concepts Demonstrated

This project demonstrates software engineering practices commonly used across banking, fintech, and payment processing organizations.

### Backend Engineering

* REST API Development
* Layered Application Architecture
* Service-Oriented Design
* Business Rule Engine
* Risk Analysis Framework

### Database Engineering

* PostgreSQL Relational Database
* SQLAlchemy ORM
* Entity Relationships
* Transaction Management
* Batch Data Processing

### Cloud Engineering

* AWS S3
* AWS Lambda
* DynamoDB
* CloudWatch
* Cloud Event Processing

### DevOps

* Docker
* Docker Compose
* GitHub Actions
* Continuous Integration
* Environment Configuration

### Quality Engineering

* Pytest Automation
* Selenium UI Automation
* API Validation
* Manual Test Cases
* Regression Testing

### Machine Learning

* Feature Engineering
* Random Forest Baseline
* Model Evaluation
* Rule Engine vs ML Comparison

---

# Skills Demonstrated

This project demonstrates practical experience with:

* Enterprise REST API Development
* Payment Processing Workflows
* Fraud Detection
* Risk Analysis
* PostgreSQL Database Design
* Cloud Integration
* Dashboard Development
* Docker Containerization
* CI/CD Pipelines
* Automated Testing
* Machine Learning Integration
* Enterprise Architecture

---

# Interview Talking Points

This project can be discussed from multiple perspectives during technical interviews.

### Software Engineering

* API Design
* Database Modeling
* Layered Architecture
* Error Handling
* Batch Processing

### Business Systems Analysis

* Fraud Investigation Workflow
* Risk Assessment
* Payment Processing Lifecycle
* Business Rules
* Reporting Requirements

### Quality Assurance

* API Testing
* Selenium Automation
* Regression Testing
* Test Planning

### Cloud & DevOps

* Docker Deployment
* AWS Services
* CI/CD Automation

### Data & Machine Learning

* Transaction Data Processing
* Fraud Analytics
* Feature Engineering
* Machine Learning Baseline

---

# Project Roadmap

## Completed

* REST APIs
* PostgreSQL Integration
* Rule-Based Fraud Detection
* Fraud Alerts
* Fraud Case Management
* Login Event Monitoring
* Payment Event Processing
* AWS Integration
* Streamlit Dashboard
* Docker Deployment
* GitHub Actions CI/CD
* Selenium UI Automation
* Kaggle Batch Import
* Risk Analysis Framework
* Machine Learning Baseline
* Interview Demo Launcher

## Future Enhancements

* Hybrid Rule + ML Decision Engine
* Explainable AI (XAI)
* Real-Time Event Streaming
* Kafka Integration
* Multi-Tenant SaaS Deployment
* Feature Store
* REST SDK

---

# Release History

| Version | Description                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------ |
| v1.0    | Enterprise Payment Fraud Monitoring Platform                                                     |
| v1.1    | Docker Deployment, Utility Scripts, DevOps Improvements                                          |
| v1.2    | AWS Integration, Selenium Automation, Dashboard Enhancements                                     |
| v1.3    | Kaggle Batch Import, Risk Analysis Framework, Machine Learning Baseline, Interview Demo Launcher |

---

# About Future Minds

This repository is part of the **Future Minds Engineering Portfolio**.

Future Minds focuses on designing enterprise software platforms across:

* FinTech
* Automotive
* Artificial Intelligence
* Cloud Engineering
* Enterprise Integration

Each repository emphasizes practical engineering, enterprise architecture, testing, documentation, and real-world design rather than tutorial-style implementations.

---

# License

This repository is intended for portfolio, educational, and demonstration purposes.

If you are interested in enterprise software development, fraud monitoring platforms, cloud integration, API development, or technical consulting, please connect through the Future Minds network or LinkedIn.

---

**Author**

**Harpreet Singh**

Independent Technology Consultant

Enterprise Software • FinTech • Automotive • Cloud • AI
