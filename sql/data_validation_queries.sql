-- DATA VALIDATION QUERIES
-- Payment Fraud Monitoring Platform

-- DV-001: Customers without accounts
SELECT
    c.customer_id,
    c.first_name,
    c.last_name
FROM customers c
LEFT JOIN accounts a
    ON c.customer_id = a.customer_id
WHERE a.account_id IS NULL;

-- DV-002: Accounts without transactions
SELECT
    a.account_id,
    a.customer_id,
    a.account_type
FROM accounts a
LEFT JOIN transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_id IS NULL;

-- DV-003: Transactions without accounts
SELECT
    t.transaction_id,
    t.account_id
FROM transactions t
LEFT JOIN accounts a
    ON t.account_id = a.account_id
WHERE a.account_id IS NULL;

-- DV-004: Fraud alerts without matching transaction
-- Expected for login/security fraud alerts only
SELECT *
FROM fraud_alerts
WHERE transaction_id IS NULL;

-- DV-005: Negative transaction amounts
SELECT *
FROM transactions
WHERE amount < 0;

-- DV-006: Missing customer email
SELECT *
FROM customers
WHERE email IS NULL OR email = '';

-- DV-007: Duplicate customer emails
SELECT
    email,
    COUNT(*) AS duplicate_count
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;