-- ==================== Module 01: SQL Foundations and Query Thinking ===================== --
CREATE TABLE IF NOT EXISTS customers(
    customer_id varchar(50),
    first_name varchar(50),
    last_name varchar(50),
    email varchar(100),
    country varchar(50),
    age integer,
    signup_date date
);

INSERT INTO customers
    (customer_id, first_name, last_name, email, country, age, signup_date)
VALUES
    (1, 'Ali', 'Ahmed', 'ali@example.com', 'Pakistan', 22, '2026-01-15'),
    (2, 'Sara', 'Khan', 'sara@example.com', 'Pakistan', 25, '2026-01-20'),
    (3, 'John', 'Smith', 'john@example.com', 'USA', 31, '2026-02-10'),
    (4, 'Emma', 'Wilson', 'emma@example.com', 'UK', 28, '2026-02-15'),
    (5, 'Hamza', 'Ali', NULL, 'Pakistan', 24, '2026-03-01'),
    (6, 'David', 'Brown', 'david@example.com', 'USA', NULL, '2026-03-05'),
    (7, 'Ayesha', 'Malik', 'ayesha@example.com', 'Pakistan', 29, '2026-03-12'),
    (8, 'Daniel', 'Taylor', 'daniel@example.com', 'Canada', 35, '2026-03-20');

-- SELECT QUERY
SELECT *
FROM customers;

SELECT first_name, country
FROM customers;

SELECT
    first_name,
    last_name,
    age
FROM customers;

-- Calculated Columns
SELECT
    first_name,
    age,
    2026 - age AS estimated_birth_year
FROM customers;

-- Distinct Column
SELECT DISTINCT country
FROM customers;

SELECT DISTINCT country, age
FROM customers;

-- Select Query
SELECT *
FROM customers
WHERE age IS NULL;

SELECT *
FROM customers
WHERE age IS NOT NULL;

-- Coalesce
SELECT
    first_name,
    COALESCE(age, 0) AS age
FROM customers;

-- SQL Execution Order
SELECT country, COUNT(*) AS customer_count
FROM customers
WHERE age >= 25
GROUP BY country
HAVING COUNT(*) > 1
ORDER BY customer_count DESC;
-- From -> Where -> Group By -> Having -> Select -> Order By

