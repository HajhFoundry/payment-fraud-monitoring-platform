# Manual Test Cases – Payment Fraud Detection Platform

## Module Interaction Flow

Customer → Account → Transaction API → Fraud Rules Engine → Fraud Alert Table → Reporting Dashboard → Audit Log

---

## TC-001: Verify Health Check API

**Module:** FastAPI Backend  
**Endpoint:** GET /  
**Purpose:** Verify application is running.

**Steps:**
1. Start FastAPI server.
2. Open http://127.0.0.1:8000
3. Verify response.

**Expected Result:**
Application returns status as running.

---

## TC-002: Create Normal Transaction

**Module:** Transaction API  
**Endpoint:** POST /transactions  
**Purpose:** Verify normal transaction is accepted without fraud alert.

**Test Data:**
Amount: 120.50  
Country: Canada  
Merchant: Walmart  
Category: Retail

**Expected Result:**
Transaction is saved with status APPROVED. No fraud alert is generated.

---

## TC-003: High Amount Fraud Rule

**Module:** Fraud Rules Engine  
**Rule:** Amount greater than 5000

**Test Data:**
Amount: 7500.00  
Merchant: BestBuy  
Country: Canada

**Expected Result:**
Transaction is saved and fraud alert is generated with severity HIGH.

---

## TC-004: High-Risk Merchant Rule

**Module:** Fraud Rules Engine  
**Rule:** High-risk merchant category

**Test Data:**
Merchant Category: Crypto  
Amount: 900.00

**Expected Result:**
Fraud alert is generated with severity MEDIUM.

---

## TC-005: Transaction Reporting

**Module:** SQL Reporting / Dashboard  
**Purpose:** Verify transactions appear in reporting layer.

**Steps:**
1. Create multiple transactions.
2. Open dashboard.
3. Check transaction count and fraud count.

**Expected Result:**
Dashboard shows total transactions, fraud alerts, and fraud rate correctly.