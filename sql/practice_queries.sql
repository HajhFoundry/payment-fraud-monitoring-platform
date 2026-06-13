-- =====================================================
-- SQL Practice Pack V1
-- Payment Fraud Monitoring Platform
-- =====================================================

-- 1. View all customers
SELECT *
FROM customers;

-- 2. View all accounts
SELECT *
FROM accounts;

-- 3. View all transactions
SELECT *
FROM transactions;

-- 4. View all fraud alerts
SELECT *
FROM fraud_alerts;

-- 5. View all fraud cases
SELECT *
FROM fraud_cases;

-- 6. View all login events
SELECT *
FROM login_events;

-- 7. Find high amount transactions
SELECT *
FROM transactions
WHERE amount > 5000;

-- 8. Find foreign transactions
SELECT *
FROM transactions
WHERE country <> 'Canada';

-- 9. Find declined transactions
SELECT *
FROM transactions
WHERE status = 'DECLINED';

-- 10. Count transactions by status
SELECT
    status,
    COUNT(*) AS total_transactions
FROM transactions
GROUP BY status;

-- 11. Count fraud alerts by severity
SELECT
    severity,
    COUNT(*) AS total_alerts
FROM fraud_alerts
GROUP BY severity;

-- 12. Count fraud alerts by rule
SELECT
    rule_name,
    COUNT(*) AS total_alerts
FROM fraud_alerts
GROUP BY rule_name
ORDER BY total_alerts DESC;

-- 13. Show open fraud cases
SELECT *
FROM fraud_cases
WHERE case_status = 'OPEN';

-- 14. Show login failures
SELECT *
FROM login_events
WHERE login_status = 'FAILED';

-- 15. Show OTP failures
SELECT *
FROM login_events
WHERE otp_status = 'FAILED';