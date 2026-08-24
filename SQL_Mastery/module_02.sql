-- ==================== Module 02: Filtering, Conditions & Data Selection ===================== --
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

SELECT *
FROM customers;

-- Task 1
SELECT first_name, age, country
FROM customers
WHERE age > 25;

-- Task 2
SELECT first_name, age
FROM customers
WHERE age BETWEEN 24 AND 30;

-- Task 3
SELECT first_name, country
FROM customers
WHERE country IN ('Pakistan', 'USA', 'Canada');

-- Task 4
SELECT first_name, country
FROM customers
WHERE country NOT IN ('Pakistan');

-- Task 5
SELECT first_name, country, age
FROM customers
WHERE country = 'Pakistan'
AND age >= 25;

-- Task 6
SELECT *
FROM customers
WHERE (country = 'Pakistan'AND age >= 25)
OR (country = 'USA' AND age >= 30);

-- Task 7
SELECT first_name, email
FROM customers
WHERE email is NULL;

-- Task 8
SELECT first_name, country, age
FROM customers
WHERE first_name LIKE 'A%';

-- Task 9
SELECT first_name, country, age
FROM customers
-- WHERE first_name ILIKE ('ALI', 'Ali', 'ali');
WHERE first_name ILIKE 'ali';

-- Task 10
SELECT customer_id, first_name, country, age, email 
FROM customers
WHERE (country = 'Pakistan' OR country = 'USA')
AND (age BETWEEN 24 AND 30)
AND email IS NOT NULL;

-- Task 11
SELECT customer_id, first_name, country, age, email 
FROM customers
WHERE ((country = 'Pakistan' OR country = 'USA') AND (age >= 35))
OR ((country = 'Canada') AND (age >= 35));

