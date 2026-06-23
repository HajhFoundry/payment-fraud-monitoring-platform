TC-056 DynamoDB Insert Event
TC-057 DynamoDB High Severity Event
TC-058 DynamoDB Attribute Validation
TC-059 DynamoDB Duplicate Event Prevention
TC-060 DynamoDB Query Validation


# AWS DynamoDB Manual Test Cases

## Purpose

Validate storage, retrieval, integrity, and fraud event persistence within DynamoDB.

---

## TC-DDB-001 - Verify Fraud Event Stored

**Objective:** Verify Lambda stores fraud events in DynamoDB.

**Steps:**
1. Trigger chargeback webhook.
2. Open DynamoDB table.
3. Open Explore Table Items.

**Expected Result:**
- New event appears.
- Event ID populated.
- Transaction ID populated.

**Status:** Pass

---

## TC-DDB-002 - Verify Fraud Detection Fields

**Objective:** Verify fraud decision fields are stored correctly.

**Steps:**
1. Open latest DynamoDB record.
2. Review attributes.

**Expected Result:**
- fraud_detected = True
- severity = HIGH
- event_type = CHARGEBACK

**Status:** Pass

---

## TC-DDB-003 - Verify Provider Information

**Objective:** Verify payment provider details are stored.

**Steps:**
1. Open DynamoDB record.
2. Review provider field.

**Expected Result:**
- provider = SIMULATED_STRIPE

**Status:** Pass

---

## TC-DDB-004 - Verify S3 Metadata Stored

**Objective:** Verify S3 source information is captured.

**Steps:**
1. Open latest record.
2. Review bucket and object key.

**Expected Result:**
- s3_bucket populated
- s3_key populated

**Status:** Pass

---

## TC-DDB-005 - Verify Event Timestamp

**Objective:** Verify processing timestamp exists.

**Steps:**
1. Open latest record.
2. Review processed_at field.

**Expected Result:**
- Timestamp exists.
- Value is not null.

**Status:** Pass

---

## TC-DDB-006 - Verify Multiple Fraud Events

**Objective:** Verify multiple events are stored independently.

**Steps:**
1. Trigger chargeback webhook multiple times.
2. Open DynamoDB table.

**Expected Result:**
- Multiple records exist.
- Unique event_id generated for each record.

**Status:** Pass
