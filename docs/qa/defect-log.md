# Defect Log

| Defect ID | Description | Severity | Status | Resolution |
|------------|------------|------------|------------|------------|
| DEF-001 | Lambda could not read S3 object due to IAM permission issue | High | Closed | Added S3 GetObject permission |
| DEF-002 | AWS credentials not configured for S3 upload | Medium | Closed | Configured AWS CLI credentials |
| DEF-003 | S3 bucket name missing from .env | Medium | Closed | Updated environment configuration |
| DEF-004 | Lambda unable to write to DynamoDB | High | Closed | Added DynamoDB PutItem permission |
| DEF-005 | Dashboard initially showed no cloud events | Low | Closed | Verified Lambda deployment and DynamoDB integration |
