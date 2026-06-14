-- REPORT-001
-- Fraud Alerts By Severity

SELECT
    severity,
    COUNT(*) AS total_alerts
FROM fraud_alerts
GROUP BY severity;


-- REPORT-002
-- Fraud Alerts By Rule

SELECT
    rule_name,
    COUNT(*) AS total_occurrences
FROM fraud_alerts
GROUP BY rule_name
ORDER BY total_occurrences DESC;


-- REPORT-003
-- Most Suspicious Transactions

SELECT
    transaction_id,
    COUNT(*) AS alert_count
FROM fraud_alerts
GROUP BY transaction_id
ORDER BY alert_count DESC;


-- REPORT-004
-- Fraud Alerts By Status

SELECT
    alert_status,
    COUNT(*) AS total_alerts
FROM fraud_alerts
GROUP BY alert_status;


-- REPORT-005
-- Total Transaction Volume

SELECT
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount
FROM transactions;

-- REPORT-006
-- Fraud Alerts By Country

SELECT
    t.country,
    COUNT(f.alert_id) AS total_alerts
FROM transactions t
JOIN fraud_alerts f
    ON t.transaction_id = f.transaction_id
GROUP BY t.country
ORDER BY total_alerts DESC;


-- REPORT-007
-- Fraud Alerts By Merchant Category

SELECT
    t.merchant_category,
    COUNT(f.alert_id) AS total_alerts
FROM transactions t
JOIN fraud_alerts f
    ON t.transaction_id = f.transaction_id
GROUP BY t.merchant_category
ORDER BY total_alerts DESC;


-- REPORT-008
-- Open Fraud Cases By Status

SELECT
    case_status,
    COUNT(*) AS total_cases
FROM fraud_cases
GROUP BY case_status
ORDER BY total_cases DESC;


-- REPORT-009
-- Login Fraud Alerts

SELECT
    rule_name,
    COUNT(*) AS total_alerts
FROM fraud_alerts
WHERE transaction_id IS NULL
GROUP BY rule_name
ORDER BY total_alerts DESC;


-- REPORT-010
-- Transaction Fraud Alerts

SELECT
    rule_name,
    COUNT(*) AS total_alerts
FROM fraud_alerts
WHERE transaction_id IS NOT NULL
GROUP BY rule_name
ORDER BY total_alerts DESC;