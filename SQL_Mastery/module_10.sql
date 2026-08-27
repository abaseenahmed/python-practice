-- ================================== Module 10: SQL for AI/ML Data Pipeline ==================================== --
DROP TABLE IF EXISTS raw_customers;

CREATE TABLE raw_customers (
    customer_id INTEGER,
    customer_name VARCHAR(100),
    email VARCHAR(150),
    country VARCHAR(50),
    age INTEGER,
    signup_date DATE,
    total_spent NUMERIC(10,2),
    total_orders INTEGER,
    last_order_date DATE,
    customer_status VARCHAR(30)
);

INSERT INTO raw_customers
(customer_id, customer_name, email, country, age, signup_date,
 total_spent, total_orders, last_order_date, customer_status)
VALUES
(1001, 'Ali Ahmed', 'ali@example.com', 'Pakistan', 24, '2025-01-15', 2450.50, 12, '2026-07-15', 'Active'),
(1002, 'Sara Khan', 'sara@example.com', 'Pakistan', 31, '2025-02-20', 5200.00, 25, '2026-08-01', 'Active'),
(1003, 'John Smith', 'john@example.com', 'USA', 42, '2024-11-10', 1800.75, 8, '2026-05-12', 'Inactive'),
(1004, 'Emma Wilson', NULL, 'UK', 29, '2025-03-05', 950.00, 5, '2026-06-20', 'Active'),
(1005, 'Hamza Malik', 'hamza@example.com', 'Pakistan', NULL, '2025-04-18', 3200.00, 15, '2026-07-25', 'Active'),
(1006, 'David Brown', 'david@example.com', 'USA', 37, '2025-05-22', 0.00, 0, NULL, 'New'),
(1007, 'Ayesha Malik', 'ayesha@example.com', 'Pakistan', 27, '2025-06-10', 4100.25, 18, '2026-07-30', 'Active'),
(1008, 'Daniel Taylor', 'daniel@example.com', 'Canada', 34, '2025-07-14', 2750.00, 11, '2026-06-15', 'Inactive'),
(1009, 'Michael Lee', 'michael@example.com', 'USA', 52, '2024-08-19', 8900.00, 32, '2026-08-05', 'Active'),
(1010, 'Fatima Noor', 'fatima@example.com', 'Pakistan', 22, '2025-09-01', 1250.00, 6, '2026-04-10', 'Inactive'),
(1011, 'Ali Ahmed', 'ali@example.com', 'Pakistan', 24, '2025-01-15', 2450.50, 12, '2026-07-15', 'Active'),
(1012, 'James Wilson', 'james@example.com', 'USA', 150, '2025-02-11', 3400.00, 14, '2026-07-12', 'Active'),
(1013, 'Sofia Garcia', 'sofia@example.com', 'Spain', -5, '2025-03-19', 1200.00, 7, '2026-06-01', 'Active'),
(1014, 'Omar Khan', 'omar@example.com', 'Pakistan', 30, '2025-04-25', NULL, 9, '2026-07-01', 'Active'),
(1015, 'Noah Brown', 'noah@example.com', 'USA', 39, '2025-05-30', 6200.00, -3, '2026-07-20', 'Active'),
(1016, 'Mia Johnson', 'mia@example.com', 'USA', 28, '2025-06-15', 2100.00, 10, '2026-07-18', 'ACTIVE'),
(1017, 'Lucas Martin', 'lucas@example.com', 'France', 33, '2025-07-20', 1750.00, 7, '2026-06-28', 'active'),
(1018, 'Olivia Davis', 'olivia@example.com', 'UK', 26, '2025-08-05', 3100.00, 13, '2026-07-29', 'Active');

-- First technique: Inspecting the dataset
SELECT *
FROM raw_customers;

-- Checking duplicate rows, ids
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT customer_id) AS unique_customers,
    COUNT(*) - COUNT(DISTINCT customer_id) AS duplicate_id_count
FROM raw_customers;

-- Detecting missing values
SELECT
    COUNT(*) AS total_rows,
    COUNT(*) FILTER (WHERE email IS NULL) AS missing_emails,
    COUNT(*) FILTER (WHERE age IS NULL) AS missing_ages,
    COUNT(*) FILTER (WHERE total_spent IS NULL) AS missing_spending,
    COUNT(*) FILTER (WHERE last_order_date IS NULL) AS missing_last_orders
FROM raw_customers;

-- Detecting Invalid Age of customers
SELECT
    customer_id,
    customer_name,
    age
FROM raw_customers
WHERE age < 18
   OR age > 100;

-- Detecting Invalid ORDERS of customers
SELECT
    customer_id,
    customer_name,
    total_orders
FROM raw_customers
WHERE total_orders < 0;

-- Detecting Invalid TOTAL_SPENT of customers
SELECT
    customer_id,
    customer_name,
    total_spent
FROM raw_customers
WHERE total_spent < 0;

-- Detect inconsistent categories
SELECT DISTINCT customer_status
FROM raw_customers
ORDER BY customer_status;

SELECT
    customer_id,
    customer_name,
    LOWER(customer_status) AS normalized_status
FROM raw_customers;

-- Feature: NULLIF(num, 0). When num becomes 0 the it is automatically set to NULL.
SELECT
    customer_id,
    customer_name,
    total_spent,
    total_orders,
    total_spent / NULLIF(total_orders, 0) AS average_order_value
FROM raw_customers;

-- IMPORTANT CONCEPTS TO MEMORIZE 
COUNT(*)
COUNT(DISTINCT ...)
FILTER (WHERE ...)