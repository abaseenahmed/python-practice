-- ========================== Module 04: Data Transformation & Conditional Logic ==============--
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

-- Table 1: customers
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    country VARCHAR(50),
    customer_segment VARCHAR(30),
    signup_date DATE,
    age INTEGER
);

INSERT INTO customers
    (customer_id, first_name, last_name, email, country, customer_segment, signup_date, age)
VALUES
    (101, 'Ali', 'Ahmed', 'ali@example.com', 'Pakistan', 'Regular', '2025-01-15', 22),
    (102, 'Sara', 'Khan', 'sara@example.com', 'Pakistan', 'Premium', '2025-02-10', 28),
    (103, 'John', 'Smith', 'john@example.com', 'USA', 'Premium', '2025-02-18', 34),
    (104, 'Emma', 'Wilson', 'emma@example.com', 'UK', 'Regular', '2025-03-05', 29),
    (105, 'Hamza', 'Ali', NULL, 'Pakistan', 'Regular', '2025-03-22', 24),
    (106, 'David', 'Brown', 'david@example.com', 'USA', 'VIP', '2025-04-01', NULL),
    (107, 'Ayesha', 'Malik', 'ayesha@example.com', 'Pakistan', 'Premium', '2025-04-12', 31),
    (108, 'Daniel', 'Taylor', 'daniel@example.com', 'Canada', 'Regular', '2025-05-03', 36),
    (109, 'Fatima', 'Khan', 'fatima@example.com', 'Pakistan', NULL, '2025-05-18', 27),
    (110, 'Michael', 'Clark', 'michael@example.com', 'USA', 'Regular', '2025-06-02', 41);

-- Table 2: orders
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    order_status VARCHAR(30),
    shipping_country VARCHAR(50),
    discount_percent NUMERIC(5,2),
    shipping_cost NUMERIC(10,2),
    total_amount NUMERIC(10,2),

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

INSERT INTO orders
    (order_id, customer_id, order_date, order_status, shipping_country,
     discount_percent, shipping_cost, total_amount)
VALUES
    (5001, 101, '2026-01-05', 'Completed', 'Pakistan', 10.00, 5.00, 120.00),
    (5002, 102, '2026-01-08', 'Completed', 'Pakistan', 15.00, 0.00, 450.00),
    (5003, 103, '2026-01-12', 'Completed', 'USA', 5.00, 12.00, 850.00),
    (5004, 104, '2026-01-15', 'Cancelled', 'UK', 0.00, 15.00, 300.00),
    (5005, 105, '2026-01-20', 'Completed', 'Pakistan', NULL, 7.00, 75.00),
    (5006, 106, '2026-02-02', 'Completed', 'USA', 20.00, 0.00, 1200.00),
    (5007, 107, '2026-02-05', 'Pending', 'Pakistan', 10.00, 5.00, 600.00),
    (5008, 108, '2026-02-10', 'Completed', 'Canada', 5.00, 20.00, 950.00),
    (5009, 109, '2026-02-15', 'Completed', 'Pakistan', NULL, 6.00, 180.00),
    (5010, 110, '2026-02-18', 'Completed', 'USA', 25.00, 0.00, 1500.00),
    (5011, 101, '2026-03-01', 'Completed', 'Pakistan', 0.00, 5.00, 250.00),
    (5012, 102, '2026-03-04', 'Returned', 'Pakistan', 10.00, 0.00, 400.00);

-- Table 3: order_items
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_name VARCHAR(100),
    category VARCHAR(50),
    quantity INTEGER,
    unit_price NUMERIC(10,2),

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);

INSERT INTO order_items
    (order_item_id, order_id, product_name, category, quantity, unit_price)
VALUES
    (1, 5001, 'Wireless Mouse', 'Electronics', 2, 25.00),
    (2, 5001, 'Keyboard', 'Electronics', 1, 45.00),
    (3, 5002, 'Monitor', 'Electronics', 1, 300.00),
    (4, 5002, 'USB Cable', 'Accessories', 3, 10.00),
    (5, 5003, 'Laptop', 'Computers', 1, 800.00),
    (6, 5004, 'Office Chair', 'Furniture', 1, 300.00),
    (7, 5005, 'Keyboard', 'Electronics', 1, 45.00),
    (8, 5006, 'Laptop', 'Computers', 1, 1100.00),
    (9, 5007, 'Desk Lamp', 'Furniture', 2, 75.00),
    (10, 5008, 'Smartphone', 'Mobile', 1, 900.00),
    (11, 5009, 'Headphones', 'Accessories', 2, 70.00),
    (12, 5010, 'Laptop', 'Computers', 1, 1400.00),
    (13, 5011, 'Webcam', 'Electronics', 2, 80.00),
    (14, 5012, 'Mechanical Keyboard', 'Electronics', 1, 400.00);

-- Inspecting the Dataset
SELECT * FROM customers;
SELECT * FROM orders;
SELECT * FROM order_items;

-- CASE Simple Method 
SELECT
    first_name,
    age,
    CASE
        WHEN age < 25 THEN 'Young'
        WHEN age < 35 THEN 'Adult'
        ELSE 'Senior'
    END AS age_group
FROM customers;

-- CASE with Business Logic
SELECT
    order_id,
    total_amount,
    CASE
        WHEN total_amount >= 1000 THEN 'High Value'
        WHEN total_amount >= 500 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS order_value_category
FROM orders;

-- CASE for Multiple Conditions
SELECT
    order_id,
    total_amount,
    discount_percent,
    CASE
        WHEN total_amount >= 1000
             AND discount_percent >= 20
            THEN 'High Value - Heavy Discount'

        WHEN total_amount >= 1000
            THEN 'High Value'

        WHEN total_amount >= 500
            THEN 'Medium Value'

        ELSE 'Low Value'
    END AS order_category
FROM orders;

-- COALESCE
SELECT
    order_id,
    discount_percent,
    COALESCE(discount_percent, 0) AS effective_discount
FROM orders;

-- COALESCE with Text
SELECT
    first_name,
    COALESCE(customer_segment, 'Unknown') AS segment
FROM customers;

-- NULLIF: If these two values are equal, return NULL.
-- Type Conversion
SELECT
    order_id,
    total_amount,
    total_amount::INTEGER AS rounded_amount
FROM orders;

-- String Functions
SELECT
    first_name,
    UPPER(first_name) AS uppercase_name,
    LOWER(first_name) AS lowercase_name
FROM customers;

SELECT
    CONCAT(first_name, ' ', last_name) AS full_name
FROM customers;

-- Date Functions
SELECT
    order_id,
    order_date,
    EXTRACT(YEAR FROM order_date) AS order_year,
    EXTRACT(MONTH FROM order_date) AS order_month
FROM orders;

SELECT
    customer_id,
    signup_date,
    AGE(DATE '2026-08-24', signup_date) AS customer_age
FROM customers;

-- Numeric Transformations
SELECT
    order_id,
    total_amount,
    shipping_cost,
    total_amount + shipping_cost AS gross_cost
FROM orders;

SELECT
    order_id,
    total_amount,
    discount_percent,
    total_amount * discount_percent / 100 AS discount_amount
FROM orders;

