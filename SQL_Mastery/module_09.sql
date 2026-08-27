-- ============================== Module 09: Advanced JOINs & Multi-Table Analysis ============================ --
CREATE TABLE IF NOT EXISTS ecommerce_customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100),
    country VARCHAR(50),
    customer_segment VARCHAR(30),
    signup_date DATE
);
INSERT INTO ecommerce_customers
(customer_id, customer_name, country, customer_segment, signup_date)
VALUES
(201, 'Ali Ahmed', 'Pakistan', 'Regular', '2025-01-15'),
(202, 'Sara Khan', 'Pakistan', 'Premium', '2025-02-10'),
(203, 'John Smith', 'USA', 'Regular', '2025-03-05'),
(204, 'Emma Wilson', 'UK', 'VIP', '2025-03-20'),
(205, 'Hamza Malik', 'Pakistan', 'Regular', '2025-04-12'),
(206, 'David Brown', 'USA', 'Premium', '2025-05-18'),
(207, 'Ayesha Khan', 'Pakistan', 'VIP', '2025-06-22'),
(208, 'Daniel Taylor', 'Canada', 'Regular', '2025-07-09');

CREATE TABLE IF NOT EXISTS ecommerce_orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    product_category VARCHAR(50),
    order_amount NUMERIC(10,2),
    order_status VARCHAR(20),
    FOREIGN KEY (customer_id)
        REFERENCES ecommerce_customers(customer_id)
);
INSERT INTO ecommerce_orders
(order_id, customer_id, order_date, product_category, order_amount, order_status)
VALUES
(5001, 201, '2026-01-05', 'Electronics', 850.00, 'Completed'),
(5002, 202, '2026-01-08', 'Clothing', 320.00, 'Completed'),
(5003, 203, '2026-01-12', 'Electronics', 1200.00, 'Completed'),
(5004, 201, '2026-01-20', 'Books', 150.00, 'Pending'),
(5005, 204, '2026-01-26', 'Electronics', 2500.00, 'Completed'),

(5006, 205, '2026-02-03', 'Clothing', 450.00, 'Completed'),
(5007, 202, '2026-02-07', 'Electronics', 1800.00, 'Completed'),
(5008, 206, '2026-02-11', 'Books', 220.00, 'Cancelled'),
(5009, 207, '2026-02-18', 'Electronics', 3200.00, 'Completed'),
(5010, 203, '2026-02-22', 'Clothing', 600.00, 'Completed'),

(5011, 201, '2026-03-02', 'Electronics', 950.00, 'Completed'),
(5012, 205, '2026-03-06', 'Books', 180.00, 'Completed'),
(5013, 206, '2026-03-10', 'Electronics', 2100.00, 'Completed'),
(5014, 207, '2026-03-15', 'Clothing', 750.00, 'Completed'),
(5015, 202, '2026-03-21', 'Books', 300.00, 'Pending'),

(5016, 204, '2026-04-01', 'Electronics', 2800.00, 'Completed'),
(5017, 206, '2026-04-05', 'Clothing', 900.00, 'Completed'),
(5018, 208, '2026-04-10', 'Books', 250.00, 'Completed'),
(5019, 201, '2026-04-14', 'Clothing', 550.00, 'Pending'),
(5020, 207, '2026-04-20', 'Electronics', 3500.00, 'Completed');

-- INNER JOIN: INNER JOIN returns only records where a match exists in both tables.
SELECT
    c.customer_name,
    o.order_id,
    o.order_amount
FROM ecommerce_customers c
INNER JOIN ecommerce_orders o
    ON c.customer_id = o.customer_id;

-- LEFT JOIN: 
SELECT
    c.customer_name,
    o.order_id,
    o.order_amount
FROM ecommerce_customers c
LEFT JOIN ecommerce_orders o
    ON c.customer_id = o.customer_id;

-- JOIN + Aggregation
SELECT
    c.customer_id,
    c.customer_name,
    SUM(o.order_amount) AS total_spent
FROM ecommerce_customers c
INNER JOIN ecommerce_orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.customer_name;

-- LEFT JOIN + COALESCE Is Powerful
SELECT
    c.customer_id,
    c.customer_name,
    COALESCE(SUM(o.order_amount), 0) AS total_spent
FROM ecommerce_customers c
LEFT JOIN ecommerce_orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.customer_name;

-- JOIN + WHERE
SELECT
    c.customer_name,
    o.order_id,
    o.order_amount
FROM ecommerce_customers c
JOIN ecommerce_orders o
    ON c.customer_id = o.customer_id
WHERE o.order_status = 'Completed';

-- JOIN + CASE
SELECT
    c.customer_name,
    COALESCE(SUM(o.order_amount), 0) AS total_spent,

    CASE
        WHEN COALESCE(SUM(o.order_amount), 0) >= 5000
            THEN 'High Value'

        WHEN COALESCE(SUM(o.order_amount), 0) >= 2000
            THEN 'Medium Value'

        ELSE 'Low Value'
    END AS customer_value
FROM ecommerce_customers c
LEFT JOIN ecommerce_orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.customer_name;

    -- Task 01: Customer Order Information
    SELECT 
        c.customer_name,
        o.order_id,
        o.order_date,
        o.order_amount
    FROM ecommerce_customers c 
    INNER JOIN ecommerce_orders o 
    ON c.customer_id = o.customer_id;

    -- Task 02: Customer Spending
    SELECT 
        c.customer_name,
        COALESCE(SUM(o.order_amount), 0) AS total_spent
    FROM ecommerce_customers c 
    LEFT JOIN ecommerce_orders o 
    ON c.customer_id = o.customer_id 
    GROUP BY c.customer_id
    ORDER BY COALESCE(SUM(o.order_amount), 0) DESC;

    -- Task 03: Number of Orders
    SELECT 
        c.customer_name,
        COALESCE(COUNT(o.order_id), 0) AS order_count
    FROM ecommerce_customers c 
    LEFT JOIN ecommerce_orders o 
    ON c.customer_id = o.customer_id 
    GROUP BY c.customer_id
    ORDER BY COALESCE(COUNT(o.order_id), 0) DESC;

    -- Task 04: Completed Spending
    SELECT 
        c.customer_name,
        COALESCE(SUM(o.order_amount), 0) AS completed_spending
    FROM ecommerce_customers c 
    LEFT JOIN ecommerce_orders o 
    ON c.customer_id = o.customer_id 
    WHERE o.order_status = 'Completed'
    GROUP BY c.customer_id
    ORDER BY COALESCE(SUM(o.order_amount), 0) DESC;

    -- Task 05: Customer Value Classification
    SELECT 
        c.customer_name,
        COALESCE(SUM(o.order_amount), 0) AS total_spent,
        CASE 
            WHEN COALESCE(SUM(o.order_amount), 0) >= 5000 THEN 'High Value'
            WHEN COALESCE(SUM(o.order_amount), 0) >= 2000 THEN 'Medium Value'
            ELSE 'Low Value'
        END AS customer_value
    FROM ecommerce_customers c 
    LEFT JOIN ecommerce_orders o 
    ON c.customer_id = o.customer_id
    GROUP BY c.customer_id
    ORDER BY COALESCE(SUM(o.order_amount), 0) DESC;

    -- Task 06: Most Active Customers
    SELECT 
        c.customer_name,
        COALESCE(COUNT(o.order_id), 0) AS order_count
    From ecommerce_customers c 
    LEFT JOIN ecommerce_orders o 
    ON c.customer_id = o.customer_id
    GROUP BY c.customer_id
    HAVING COALESCE(COUNT(o.order_id), 0) >= 3 ;

    -- Task 07: Mini Challenge
    SELECT
        c.customer_id,
        c.customer_name,
        COALESCE(COUNT(o.order_id), 0) AS total_orders,
        COALESCE(SUM(o.order_amount), 0) AS total_spent
    FROM ecommerce_customers c 
    INNER JOIN ecommerce_orders o 
    ON c.customer_id = o.customer_id
    GROUP BY c.customer_id
    HAVING COALESCE(COUNT(o.order_id), 0) >= 2 
    AND COALESCE(SUM(o.order_amount), 0) >= 3000
    ORDER BY COALESCE(SUM(o.order_amount), 0);

    