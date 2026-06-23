TC-050 Lambda Trigger From S3
TC-051 Lambda Reads JSON
TC-052 Lambda Detects Chargeback
TC-053 Lambda High Severity Event
TC-054 Lambda CloudWatch Logs
TC-055 Lambda Error Handling

# AWS Lambda Manual Test Cases

## Purpose

Validate serverless fraud processing, S3 event triggers, CloudWatch logging, and fraud classification.

---

## TC-LAMBDA-001 - Verify S3 Triggers Lambda

**Objective:** Verify AWS Lambda executes automatically when a payment event report is uploaded to S3.

**Preconditions:**
- Lambda function deployed.
- S3 trigger configured.

**Steps:**
1. Send chargeback webhook.
2. Verify JSON uploaded to S3.
3. Open CloudWatch Logs.
4. Review latest Lambda execution.

**Expected Result:**
- Lambda executes automatically.
- Log contains:
  Payment fraud Lambda triggered

**Status:** Pass

---

## TC-LAMBDA-002 - Verify Lambda Reads S3 Object

**Objective:** Verify Lambda can read uploaded payment event JSON.

**Steps:**
1. Trigger chargeback webhook.
2. Open CloudWatch Logs.
3. Review payload output.

**Expected Result:**
- Lambda successfully reads JSON file.
- Payment event payload is displayed in logs.

**Status:** Pass

---

## TC-LAMBDA-003 - Verify Chargeback Detection

**Objective:** Verify Lambda identifies chargeback events as fraud.

**Test Data:**

```json
{
  "event_type": "CHARGEBACK"
}
```

**Steps:**
1. Trigger chargeback webhook.
2. Review CloudWatch logs.

**Expected Result:**
- Lambda detects fraud.
- Log contains:
  HIGH RISK: Chargeback event detected

**Status:** Pass

---

## TC-LAMBDA-004 - Verify Lambda Writes To DynamoDB

**Objective:** Verify Lambda stores processed fraud events.

**Steps:**
1. Trigger chargeback webhook.
2. Open DynamoDB.
3. Review table contents.

**Expected Result:**
- New event record created.
- Severity = HIGH.
- Fraud detected = True.

**Status:** Pass

---

## TC-LAMBDA-005 - Verify CloudWatch Logging

**Objective:** Verify Lambda execution logs are stored.

**Steps:**
1. Trigger Lambda.
2. Open CloudWatch.
3. Review latest log stream.

**Expected Result:**
- Lambda execution appears in CloudWatch.
- No runtime errors.

**Status:** Pass

---

## TC-LAMBDA-006 - Verify Lambda Permission Handling

**Objective:** Verify IAM permissions are required for S3 and DynamoDB access.

**Steps:**
1. Review Lambda execution role.
2. Review attached IAM policies.

**Expected Result:**
- S3 GetObject permission exists.
- DynamoDB PutItem permission exists.

**Status:** Pass
