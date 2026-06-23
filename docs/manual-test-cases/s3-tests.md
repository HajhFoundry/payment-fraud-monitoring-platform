TC-044 Payment Event Upload To S3
TC-045 S3 File Naming Convention
TC-046 S3 JSON Validation
TC-047 Multiple Upload Validation
TC-048 S3 Bucket Accessibility
TC-049 S3 Error Handling

# AWS S3 Manual Test Cases

## Purpose

Validate that payment event reports are generated locally and uploaded to AWS S3 for cloud archival.

---

## TC-S3-001 - Upload Payment Event Report to S3

**Objective:** Verify webhook processing uploads a JSON report to AWS S3.

**Preconditions:**
- FastAPI is running.
- AWS credentials are configured locally.
- S3 bucket `hajhfoundry-payment-events-2026` exists.
- `.env` has correct bucket name.

**Test Data:**
```json
{
  "transaction_id": 53,
  "event_type": "CHARGEBACK",
  "amount": 7000,
  "provider": "SIMULATED_STRIPE"
}
```

**Steps:**
1. Send `POST /payments/webhook`.
2. Verify response contains `s3_upload.uploaded = true`.
3. Open AWS Console.
4. Go to S3 bucket `hajhfoundry-payment-events-2026`.
5. Open `reports/payment_events/`.
6. Verify new JSON file exists.

**Expected Result:**
- JSON report is created locally.
- JSON report is uploaded to S3.
- API response shows uploaded as true.

**Status:** Pass

---

## TC-S3-002 - Verify S3 Object Naming Convention

**Objective:** Verify uploaded payment event files follow expected naming convention.

**Steps:**
1. Trigger webhook.
2. Open S3 path `reports/payment_events/`.
3. Review uploaded file name.

**Expected Result:**
- File path starts with `reports/payment_events/`.
- File name starts with `payment_event_`.
- File extension is `.json`.

**Status:** Pass

---

## TC-S3-003 - Verify S3 JSON Content

**Objective:** Verify uploaded S3 JSON contains payment and fraud details.

**Steps:**
1. Open latest uploaded JSON file in S3.
2. Review content.

**Expected Result:**
JSON contains:
- transaction_id
- event_type
- payment_status
- amount
- provider
- fraud_alert_id
- fraud_rule
- created_at

**Status:** Pass

---

## TC-S3-004 - Verify S3 Upload Failure Handling

**Objective:** Verify application handles missing or invalid S3 configuration safely.

**Preconditions:**
- Temporarily remove or modify `AWS_S3_BUCKET_NAME` in `.env`.

**Steps:**
1. Restart FastAPI.
2. Send webhook request.
3. Review API response.

**Expected Result:**
- Webhook still processes.
- Payment event is created.
- Fraud alert is created.
- API does not crash.
- Response shows S3 upload failure reason.

**Status:** Pass

---

## TC-S3-005 - Verify S3 Bucket Security

**Objective:** Verify S3 bucket is not publicly accessible.

**Steps:**
1. Open AWS S3 bucket permissions.
2. Review Block Public Access settings.
3. Review bucket encryption settings.

**Expected Result:**
- Block Public Access is enabled.
- Objects are private.
- Server-side encryption is enabled.

**Status:** Pass

