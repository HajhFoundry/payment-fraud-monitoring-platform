# Requirements Traceability Matrix - Payment Fraud Monitoring Platform

| Req ID | Requirement | Module | Test Case ID | Status |
|---|---|---|---|---|
| REQ-001 | System shall provide customer creation API | Customer API | TC-001, TC-002 | Pass |
| REQ-002 | System shall provide account creation API | Account API | TC-011, TC-012 | Pass |
| REQ-003 | System shall process transactions | Transaction API | TC-019, TC-020 | Pass |
| REQ-004 | System shall detect high amount fraud | Fraud Engine | TC-028 | Pass |
| REQ-005 | System shall detect country mismatch fraud | Fraud Engine | TC-029 | Pass |
| REQ-006 | System shall detect high risk merchant fraud | Fraud Engine | TC-030 | Pass |
| REQ-007 | System shall create fraud alerts | Fraud Alerts | TC-033 | Pass |
| REQ-008 | System shall support fraud case management | Fraud Cases | TC-011, TC-012 | Pass |
| REQ-009 | System shall process payment webhooks | Webhook | TC-WEBHOOK-001 | Pass |
| REQ-010 | System shall archive payment event reports to AWS S3 | AWS S3 | TC-S3-001 | Pass |
| REQ-011 | System shall trigger AWS Lambda from S3 upload | AWS Lambda | TC-LAMBDA-001 | Pass |
| REQ-012 | System shall store cloud fraud decisions in DynamoDB | DynamoDB | TC-DDB-001 | Pass |
| REQ-013 | System shall log Lambda execution in CloudWatch | CloudWatch | TC-LAMBDA-005 | Pass |
| REQ-014 | System shall display fraud KPIs in dashboard | Dashboard | TC-DASH-004 | Pass |
| REQ-015 | System shall display cloud fraud events in dashboard | Dashboard | TC-DASH-003 | Pass |
| REQ-016 | System shall support end-to-end chargeback fraud workflow | End-to-End | TC-E2E-001 | Pass |