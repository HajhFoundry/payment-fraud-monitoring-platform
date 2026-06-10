-- DQ-001: Duplicate customer emails
SELECT
    email,
    COUNT(*) AS duplicate_count
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;

-- DQ-002: Accounts without valid customers
SELECT
    a.*
FROM accounts a
LEFT JOIN customers c
    ON a.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- DQ-003: Transactions without valid accounts
SELECT
    t.*
FROM transactions t
LEFT JOIN accounts a
    ON t.account_id = a.account_id
WHERE a.account_id IS NULL;

-- DQ-004: Fraud alerts without valid transactions
SELECT
    f.*
FROM fraud_alerts f
LEFT JOIN transactions t
    ON f.transaction_id = t.transaction_id
WHERE t.transaction_id IS NULL;

-- DQ-005: Invalid transaction amounts
SELECT *
FROM transactions
WHERE amount <= 0;

-- DQ-006: Missing merchant information
SELECT *
FROM transactions
WHERE merchant_name IS NULL
   OR merchant_category IS NULL;

-- DQ-007: Invalid transaction status
SELECT *
FROM transactions
WHERE status NOT IN ('APPROVED', 'DECLINED');

-- DQ-008: Invalid fraud alert severity
SELECT *
FROM fraud_alerts
WHERE severity NOT IN ('HIGH', 'MEDIUM', 'LOW');