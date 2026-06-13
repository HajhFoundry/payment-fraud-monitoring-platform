-- All customers
SELECT * FROM customers;

-- All accounts
SELECT * FROM accounts;

-- All transactions
SELECT * FROM transactions;

-- All fraud alerts
SELECT * FROM fraud_alerts;

-- Customer and account information
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    a.account_type,
    a.balance
FROM customers c
JOIN accounts a
    ON c.customer_id = a.customer_id;

-- Transactions with customer names
SELECT
    c.first_name,
    c.last_name,
    t.transaction_id,
    t.amount,
    t.country,
    t.status
FROM customers c
JOIN accounts a
    ON c.customer_id = a.customer_id
JOIN transactions t
    ON a.account_id = t.account_id;


-- Fraud alerts by customer
SELECT
    c.first_name,
    c.last_name,
    f.rule_name,
    f.severity
FROM customers c
JOIN accounts a
    ON c.customer_id = a.customer_id
JOIN transactions t
    ON a.account_id = t.account_id
JOIN fraud_alerts f
    ON t.transaction_id = f.transaction_id;


-- Count fraud alerts by customer
SELECT
    c.first_name,
    c.last_name,
    COUNT(f.alert_id) AS total_alerts
FROM customers c
JOIN accounts a
    ON c.customer_id = a.customer_id
JOIN transactions t
    ON a.account_id = t.account_id
JOIN fraud_alerts f
    ON t.transaction_id = f.transaction_id
GROUP BY c.first_name, c.last_name
ORDER BY total_alerts DESC;

-- Customers with more than 5 fraud alerts
SELECT
    c.first_name,
    c.last_name,
    COUNT(f.alert_id) AS total_alerts
FROM customers c
JOIN accounts a
    ON c.customer_id = a.customer_id
JOIN transactions t
    ON a.account_id = t.account_id
JOIN fraud_alerts f
    ON t.transaction_id = f.transaction_id
GROUP BY c.first_name, c.last_name
HAVING COUNT(f.alert_id) > 5
ORDER BY total_alerts DESC;

-- Top 5 highest value transactions
SELECT
    transaction_id,
    amount,
    merchant_name,
    country
FROM transactions
ORDER BY amount DESC
LIMIT 5;

-- Total transaction amount by customer
SELECT
    c.first_name,
    c.last_name,
    SUM(t.amount) AS total_amount
FROM customers c
JOIN accounts a
    ON c.customer_id = a.customer_id
JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY c.first_name, c.last_name
ORDER BY total_amount DESC;

-- Total number of transactions
SELECT COUNT(*) AS total_transactions
FROM transactions;

-- Average transaction amount
SELECT AVG(amount) AS average_amount
FROM transactions;

-- Highest transaction amount
SELECT MAX(amount) AS highest_amount
FROM transactions;

-- Lowest transaction amount
SELECT MIN(amount) AS lowest_amount
FROM transactions;

-- Total money processed
SELECT SUM(amount) AS total_processed
FROM transactions;

-- Categorize transaction risk by amount
SELECT
    transaction_id,
    amount,
    CASE
        WHEN amount >= 5000 THEN 'HIGH RISK'
        WHEN amount >= 1000 THEN 'MEDIUM RISK'
        ELSE 'LOW RISK'
    END AS risk_category
FROM transactions
ORDER BY amount DESC;

-- Rank transactions by amount
SELECT
    transaction_id,
    amount,
    RANK() OVER (
        ORDER BY amount DESC
    ) AS transaction_rank
FROM transactions;

-- Compare ROW_NUMBER, RANK, and DENSE_RANK
SELECT
    transaction_id,
    amount,
    ROW_NUMBER() OVER (
        ORDER BY amount DESC
    ) AS row_number_rank,
    RANK() OVER (
        ORDER BY amount DESC
    ) AS rank_value,
    DENSE_RANK() OVER (
        ORDER BY amount DESC
    ) AS dense_rank_value
FROM transactions
ORDER BY amount DESC;

-- CTE: Fraud alerts by customer
WITH customer_alerts AS (
    SELECT
        c.first_name,
        c.last_name,
        COUNT(f.alert_id) AS total_alerts
    FROM customers c
    JOIN accounts a
        ON c.customer_id = a.customer_id
    JOIN transactions t
        ON a.account_id = t.account_id
    JOIN fraud_alerts f
        ON t.transaction_id = f.transaction_id
    GROUP BY c.first_name, c.last_name
)

SELECT *
FROM customer_alerts
ORDER BY total_alerts DESC;

-- Rank customers by fraud alerts
WITH customer_alerts AS (
    SELECT
        c.customer_id,
        c.first_name,
        c.last_name,
        COUNT(f.alert_id) AS total_alerts
    FROM customers c
    JOIN accounts a
        ON c.customer_id = a.customer_id
    JOIN transactions t
        ON a.account_id = t.account_id
    JOIN fraud_alerts f
        ON t.transaction_id = f.transaction_id
    GROUP BY
        c.customer_id,
        c.first_name,
        c.last_name
)

SELECT
    customer_id,
    first_name,
    last_name,
    total_alerts,
    RANK() OVER (
        ORDER BY total_alerts DESC
    ) AS fraud_rank
FROM customer_alerts
ORDER BY fraud_rank;