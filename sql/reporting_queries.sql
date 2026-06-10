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