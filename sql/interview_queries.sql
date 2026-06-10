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