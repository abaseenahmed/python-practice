-- ================= Module 08: Advanced SQL for Time-Series & Analytical Queries =========== --
CREATE TABLE IF NOT EXISTS saas_customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100),
    country VARCHAR(50),
    signup_date DATE,
    customer_type VARCHAR(30)
);
INSERT INTO saas_customers
    (customer_id, customer_name, country, signup_date, customer_type)
VALUES
    (101, 'Ali Ahmed', 'Pakistan', '2025-01-15', 'Individual'),
    (102, 'Sara Khan', 'Pakistan', '2025-02-10', 'Business'),
    (103, 'John Smith', 'USA', '2025-03-05', 'Business'),
    (104, 'Emma Wilson', 'UK', '2025-03-20', 'Individual'),
    (105, 'Hamza Malik', 'Pakistan', '2025-04-12', 'Business'),
    (106, 'David Brown', 'USA', '2025-05-18', 'Individual'),
    (107, 'Ayesha Khan', 'Pakistan', '2025-06-22', 'Business'),
    (108, 'Daniel Taylor', 'Canada', '2025-07-09', 'Individual'),
    (109, 'Michael Lee', 'USA', '2025-08-14', 'Business'),
    (110, 'Fatima Noor', 'Pakistan', '2025-09-03', 'Individual');

CREATE TABLE IF NOT EXISTS subscriptions (
    subscription_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    subscription_date DATE,
    plan VARCHAR(30),
    amount NUMERIC(10,2),
    status VARCHAR(20),
    FOREIGN KEY (customer_id)
        REFERENCES saas_customers(customer_id)
);
-- ============================================================
-- Additional realistic subscription data
-- ============================================================

INSERT INTO subscriptions
    (subscription_id, customer_id, subscription_date, plan, amount, status)
VALUES

    (1061, 102, '2026-01-10', 'Premium', 80.00, 'Paid'),
    (1062, 103, '2026-01-12', 'Premium', 80.00, 'Paid'),
    (1063, 104, '2026-01-15', 'Basic', 20.00, 'Paid'),
    (1064, 105, '2026-01-17', 'Enterprise', 150.00, 'Paid'),
    (1065, 106, '2026-01-19', 'Basic', 20.00, 'Paid'),

    (1066, 107, '2026-02-05', 'Premium', 80.00, 'Paid'),
    (1067, 108, '2026-02-07', 'Basic', 20.00, 'Paid'),
    (1068, 109, '2026-02-15', 'Enterprise', 150.00, 'Paid'),
    (1069, 110, '2026-02-21', 'Basic', 20.00, 'Pending'),
    (1070, 101, '2026-02-25', 'Basic', 20.00, 'Paid'),

    (1071, 102, '2026-03-03', 'Premium', 80.00, 'Paid'),
    (1072, 104, '2026-03-13', 'Basic', 20.00, 'Paid'),
    (1073, 105, '2026-03-15', 'Enterprise', 150.00, 'Paid'),
    (1074, 107, '2026-03-20', 'Premium', 80.00, 'Paid'),
    (1075, 109, '2026-03-27', 'Enterprise', 150.00, 'Cancelled'),

    (1076, 101, '2026-04-07', 'Basic', 20.00, 'Paid'),
    (1077, 103, '2026-04-17', 'Premium', 80.00, 'Paid'),
    (1078, 106, '2026-04-18', 'Basic', 20.00, 'Paid'),
    (1079, 108, '2026-04-21', 'Basic', 20.00, 'Pending'),
    (1080, 110, '2026-04-26', 'Premium', 80.00, 'Paid');

SELECT *
FROM saas_customers;

SELECT *
FROM subscriptions;

-- Task 01: Monthly Revenue
SELECT 
    DATE_TRUNC('month', subscription_date) AS month,
    SUM(amount) AS monthly_revenue
FROM subscriptions
GROUP BY DATE_TRUNC('month', subscription_date)
ORDER BY month;