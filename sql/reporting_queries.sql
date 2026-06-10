-- Most suspicious transactions
SELECT
    transaction_id,
    COUNT(*) AS alert_count
FROM fraud_alerts
GROUP BY transaction_id
ORDER BY alert_count DESC;

-- Fraud alerts by severity
SELECT
    severity,
    COUNT(*) AS total_alerts
FROM fraud_alerts
GROUP BY severity;