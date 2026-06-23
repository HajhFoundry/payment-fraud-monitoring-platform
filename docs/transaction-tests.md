TC-001 Health Check
TC-002 Create Customer - Positive
TC-003 Create Customer - Duplicate Email
TC-004 Create Account - Positive
TC-005 Create Account - Invalid Customer
TC-006 Create Transaction - Normal
TC-007 Create Transaction - High Amount Fraud
TC-008 Create Transaction - Country Mismatch
TC-009 Create Transaction - High Risk Merchant
TC-010 View Fraud Alerts
TC-011 Create Fraud Case
TC-012 Update Fraud Case
TC-013 Login Event - OTP Failure
TC-014 Login Event - Impossible Travel
TC-015 Dashboard Loads

# Manual Test Cases - Payment Fraud Monitoring Platform

## TC-001 - Health Check

**Objective:** Verify backend service is running.

**Endpoint:** GET /

**Steps:**
1. Start FastAPI using `uvicorn app.main:app --reload`
2. Open Swagger or Postman
3. Send GET request to `/`

**Expected Result:**
- Status code is 200
- Response shows application status as running

---

## TC-002 - Create Customer - Positive

**Objective:** Verify a new customer can be created.

**Endpoint:** POST /customers/

**Test Data:**
```json
{
  "first_name": "John",
  "last_name": "Smith",
  "email": "john.smith@test.com",
  "country": "Canada"
}