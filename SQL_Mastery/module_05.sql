-- ============================ Module 05: Joins & Relational Data Analysis ======================= --

-- Customers Table
CREATE TABLE m05_customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    country VARCHAR(50),
    age INT,
    customer_segment VARCHAR(20),
    signup_date DATE
);

INSERT INTO m05_customers
(customer_id, first_name, last_name, email, country, age, customer_segment, signup_date)
VALUES
(1, 'Ali', 'Ahmed', 'ali@example.com', 'Pakistan', 24, 'Regular', '2025-01-15'),
(2, 'Sara', 'Khan', 'sara@example.com', 'Pakistan', 31, 'Premium', '2025-02-10'),
(3, 'John', 'Smith', 'john@example.com', 'USA', 38, 'VIP', '2024-11-20'),
(4, 'Emma', 'Wilson', 'emma@example.com', 'UK', 27, 'Regular', '2025-03-05'),
(5, 'Hamza', 'Ali', 'hamza@example.com', 'Pakistan', 29, 'Premium', '2025-04-12'),
(6, 'David', 'Brown', 'david@example.com', 'USA', 42, 'VIP', '2024-08-18'),
(7, 'Ayesha', 'Malik', 'ayesha@example.com', 'Pakistan', 35, 'Premium', '2025-05-22'),
(8, 'Daniel', 'Taylor', 'daniel@example.com', 'Canada', 33, 'Regular', '2025-06-01'),
(9, 'Fatima', 'Khan', 'fatima@example.com', 'Pakistan', 26, 'Regular', '2025-06-15'),
(10, 'Michael', 'Johnson', 'michael@example.com', 'USA', 45, 'VIP', '2024-12-01'),
(11, 'Zain', 'Shah', 'zain@example.com', 'Pakistan', 22, 'Regular', '2025-07-10'),
(12, 'Sophia', 'Martin', 'sophia@example.com', 'France', 30, 'Premium', '2025-07-20');


-- Products Table
CREATE TABLE m05_products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price NUMERIC(10,2),
    stock_quantity INT
);

INSERT INTO m05_products
(product_id, product_name, category, unit_price, stock_quantity)
VALUES
(101, 'Laptop Pro 15', 'Electronics', 1200.00, 25),
(102, 'Wireless Mouse', 'Accessories', 35.00, 150),
(103, 'Mechanical Keyboard', 'Accessories', 85.00, 90),
(104, '4K Monitor', 'Electronics', 450.00, 40),
(105, 'USB-C Hub', 'Accessories', 55.00, 120),
(106, 'Noise Cancelling Headphones', 'Audio', 180.00, 70),
(107, 'Smartphone X', 'Mobile', 950.00, 35),
(108, 'Tablet Air', 'Mobile', 600.00, 50),
(109, 'Webcam HD', 'Accessories', 75.00, 80),
(110, 'External SSD 1TB', 'Storage', 110.00, 65);


-- Orders Table
CREATE TABLE m05_orders (
    order_id INT PRIMARY KEY,
    customer_id INT REFERENCES m05_customers(customer_id),
    order_date DATE,
    order_status VARCHAR(20),
    shipping_country VARCHAR(50),
    discount_percent NUMERIC(5,2)
);

INSERT INTO m05_orders
(order_id, customer_id, order_date, order_status, shipping_country, discount_percent)
VALUES
(1001, 1, '2026-01-05', 'Completed', 'Pakistan', 5),
(1002, 2, '2026-01-08', 'Completed', 'Pakistan', 10),
(1003, 3, '2026-01-12', 'Completed', 'USA', 15),
(1004, 1, '2026-01-20', 'Completed', 'Pakistan', 0),
(1005, 4, '2026-02-02', 'Cancelled', 'UK', 5),
(1006, 5, '2026-02-10', 'Completed', 'Pakistan', 10),
(1007, 6, '2026-02-15', 'Completed', 'USA', 20),
(1008, 7, '2026-02-20', 'Pending', 'Pakistan', 0),
(1009, 2, '2026-03-01', 'Completed', 'Pakistan', 5),
(1010, 8, '2026-03-05', 'Completed', 'Canada', 10),
(1011, 3, '2026-03-12', 'Returned', 'USA', 15),
(1012, 9, '2026-03-18', 'Completed', 'Pakistan', 0),
(1013, 10, '2026-03-22', 'Completed', 'USA', 10),
(1014, 5, '2026-04-01', 'Completed', 'Pakistan', 5),
(1015, 1, '2026-04-08', 'Pending', 'Pakistan', 0),
(1016, 7, '2026-04-12', 'Completed', 'Pakistan', 15),
(1017, 6, '2026-04-20', 'Completed', 'USA', 10),
(1018, 10, '2026-05-01', 'Completed', 'USA', 20);

-- Order Items Table
CREATE TABLE m05_order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT REFERENCES m05_orders(order_id),
    product_id INT REFERENCES m05_products(product_id),
    quantity INT,
    unit_price NUMERIC(10,2)
);

INSERT INTO m05_order_items
(order_item_id, order_id, product_id, quantity, unit_price)
VALUES
(1, 1001, 101, 1, 1200),
(2, 1001, 102, 2, 35),

(3, 1002, 107, 1, 950),
(4, 1002, 105, 1, 55),

(5, 1003, 101, 1, 1200),
(6, 1003, 106, 1, 180),

(7, 1004, 103, 2, 85),

(8, 1005, 104, 1, 450),

(9, 1006, 108, 1, 600),
(10, 1006, 102, 1, 35),

(11, 1007, 101, 2, 1200),

(12, 1008, 109, 1, 75),

(13, 1009, 107, 1, 950),
(14, 1009, 106, 1, 180),

(15, 1010, 110, 2, 110),

(16, 1011, 104, 1, 450),
(17, 1011, 103, 1, 85),

(18, 1012, 102, 3, 35),
(19, 1012, 109, 1, 75),

(20, 1013, 107, 1, 950),

(21, 1014, 105, 2, 55),
(22, 1014, 102, 2, 35),

(23, 1015, 106, 1, 180),

(24, 1016, 108, 1, 600),
(25, 1016, 105, 1, 55),

(26, 1017, 101, 1, 1200),
(27, 1017, 109, 2, 75),

(28, 1018, 107, 1, 950),
(29, 1018, 106, 1, 180);

-- Payments Table
CREATE TABLE m05_payments (
    payment_id INT PRIMARY KEY,
    order_id INT REFERENCES m05_orders(order_id),
    payment_date DATE,
    payment_method VARCHAR(30),
    payment_status VARCHAR(20),
    amount NUMERIC(10,2)
);

INSERT INTO m05_payments
(payment_id, order_id, payment_date, payment_method, payment_status, amount)
VALUES
(1, 1001, '2026-01-05', 'Credit Card', 'Paid', 1270),
(2, 1002, '2026-01-08', 'PayPal', 'Paid', 1005),
(3, 1003, '2026-01-12', 'Credit Card', 'Paid', 1173),
(4, 1004, '2026-01-20', 'Bank Transfer', 'Paid', 170),
(5, 1005, '2026-02-02', 'Credit Card', 'Refunded', 450),
(6, 1006, '2026-02-10', 'PayPal', 'Paid', 635),
(7, 1007, '2026-02-15', 'Credit Card', 'Paid', 2400),
(8, 1008, '2026-02-20', 'Credit Card', 'Pending', 75),
(9, 1009, '2026-03-01', 'PayPal', 'Paid', 1130),
(10, 1010, '2026-03-05', 'Credit Card', 'Paid', 220),
(11, 1011, '2026-03-12', 'Credit Card', 'Refunded', 535),
(12, 1012, '2026-03-18', 'Cash', 'Paid', 180),
(13, 1013, '2026-03-22', 'Credit Card', 'Paid', 950),
(14, 1014, '2026-04-01', 'PayPal', 'Paid', 180),
(15, 1015, '2026-04-08', 'Credit Card', 'Pending', 180),
(16, 1016, '2026-04-12', 'Bank Transfer', 'Paid', 655),
(17, 1017, '2026-04-20', 'Credit Card', 'Paid', 1350),
(18, 1018, '2026-05-01', 'PayPal', 'Paid', 1130);

-- Veryfying Tables. 
SELECT * FROM m05_customers;
SELECT * FROM m05_products;
SELECT * FROM m05_orders;
SELECT * FROM m05_order_items;
SELECT * FROM m05_payments;

SELECT * FROM m05_customers;
SELECT * FROM m05_products;
SELECT * FROM m05_orders;
SELECT * FROM m05_order_items;
SELECT * FROM m05_payments;

-- Simple SQL Join || Inner Join
SELECT
    c.customer_id,
    c.first_name,
    o.order_id,
    o.order_date
FROM m05_customers c
JOIN m05_orders o
    ON c.customer_id = o.customer_id;

-- Left Join
SELECT
    c.customer_id,
    c.first_name,
    o.order_id,
    o.order_date
FROM m05_customers c
LEFT JOIN m05_orders o
    ON c.customer_id = o.customer_id;

-- Right Join
SELECT
    c.customer_id,
    c.first_name,
    o.order_id,
    o.order_date
FROM m05_customers c
RIGHT JOIN m05_orders o
    ON c.customer_id = o.customer_id;

-- full Outer Join
SELECT
    c.customer_id,
    c.first_name,
    o.order_id,
    o.order_date
FROM m05_customers c
FULL OUTER JOIN m05_orders o
    ON c.customer_id = o.customer_id;

-- Task 01: Basic INNER JOIN
SELECT
    c.customer_id,
    concat(c.first_name, ' ' , c.last_name) AS full_name,
    o.order_id,
    o.order_date,
    o.order_status
FROM m05_customers c
INNER JOIN m05_orders o
    ON c.customer_id = o.customer_id;

-- Task 02: Customer Order Count
SELECT
    c.customer_id,
    concat(c.first_name, ' ' , c.last_name) AS full_name,
    count(c.customer_id = o.customer_id) AS total_orders
FROM m05_customers c
INNER JOIN m05_orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY total_orders DESC;

-- Task 03: Customers With No Orders
SELECT
    c.customer_id,
    concat(c.first_name, ' ' , c.last_name) AS full_name,
    c.country,
    c.customer_segment,
    o.order_id,
    o.order_date,
    o.order_status
FROM m05_customers c 
LEFT JOIN m05_orders o 
ON c.customer_id = o.customer_id;

-- Task 04: Customer Revenue
SELECT
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    c.country,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COALESCE(SUM(p.amount), 0) AS total_spent
FROM m05_customers c 
LEFT JOIN m05_orders o ON c.customer_id = o.customer_id
LEFT JOIN m05_payments p ON o.order_id = p.order_id 
GROUP BY 
    c.customer_id, 
    c.first_name, 
    c.last_name, 
    c.country;                    

-- Task 05: Product Sales Performance m05_products
SELECT
    pr.product_id,
    pr.product_name,
    pr.category,
    oi.quantity, 
    COALESCE(SUM(oi.unit_price * oi.quantity), 0) AS total_revenue
FROM m05_products pr
INNER JOIN m05_order_items oi
ON pr.product_id = oi.product_id
GROUP BY pr.product_id, oi.quantity 
ORDER BY total_revenue DESC;  

-- Task 06: Customer + Product Behavior
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    p.product_name,
    p.category,
    oi.quantity,
    o.order_date
FROM m05_customers c
JOIN m05_orders o ON c.customer_id = o.customer_id
JOIN m05_order_items oi ON o.order_id = oi.order_id
JOIN m05_products p ON oi.product_id = p.product_id
ORDER BY c.customer_id, o.order_date;

-- Task 07: 
SELECT 
    c.country,
    COUNT(DISTINCT c.customer_id) AS total_customers,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COALESCE(SUM(oi.quantity * oi.unit_price * (1 - o.discount_percent/100)), 0) AS total_revenue
FROM m05_customers c
LEFT JOIN m05_orders o ON c.customer_id = o.customer_id
LEFT JOIN m05_order_items oi ON o.order_id = oi.order_id
GROUP BY c.country
ORDER BY total_revenue DESC;

-- Task 08:
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    c.customer_segment,
    COUNT(o.order_id) AS total_orders,
    COALESCE(SUM(oi.quantity * oi.unit_price * (1 - o.discount_percent/100)), 0) AS total_spent
FROM m05_customers c
LEFT JOIN m05_orders o ON c.customer_id = o.customer_id
LEFT JOIN m05_order_items oi ON o.order_id = oi.order_id
GROUP BY c.customer_id, c.first_name, c.last_name, c.customer_segment
HAVING COALESCE(SUM(oi.quantity * oi.unit_price * (1 - o.discount_percent/100)), 0) > 2000
ORDER BY total_spent DESC;

-- Task 09: 
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    COUNT(o.order_id) AS completed_orders,
    COALESCE(SUM(oi.quantity * oi.unit_price * (1 - o.discount_percent/100)), 0) AS completed_revenue
FROM m05_customers c
LEFT JOIN m05_orders o ON c.customer_id = o.customer_id AND o.order_status = 'Completed'
LEFT JOIN m05_order_items oi ON o.order_id = oi.order_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY completed_revenue DESC;

-- Task 10: Customer Payment Behavior
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(DISTINCT p.order_id) AS paid_orders,
    COALESCE(SUM(p.amount), 0) AS total_paid
FROM m05_customers c
LEFT JOIN m05_orders o ON c.customer_id = o.customer_id
LEFT JOIN m05_payments p ON o.order_id = p.order_id AND p.payment_status = 'Paid'
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_paid DESC;

-- Challenge 11: Customer Purchasing Profile
WITH customer_orders AS (
    SELECT 
        c.customer_id,
        c.first_name,
        c.last_name,
        c.country,
        c.customer_segment,
        o.order_id,
        o.order_date,
        o.order_status,
        COALESCE(SUM(oi.quantity * oi.unit_price * (1 - o.discount_percent/100)), 0) AS order_value
    FROM m05_customers c
    LEFT JOIN m05_orders o ON c.customer_id = o.customer_id
    LEFT JOIN m05_order_items oi ON o.order_id = oi.order_id
    GROUP BY c.customer_id, c.first_name, c.last_name, c.country, c.customer_segment, 
             o.order_id, o.order_date, o.order_status
)
SELECT 
    customer_id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    country,
    customer_segment,
    COUNT(order_id) AS total_orders,
    COUNT(CASE WHEN order_status = 'Completed' THEN 1 END) AS completed_orders,
    COALESCE(SUM(order_value), 0) AS total_spent,
    COALESCE(AVG(CASE WHEN order_value > 0 THEN order_value END), 0) AS avg_order_value,
    MAX(order_date) AS last_order_date
FROM customer_orders
GROUP BY customer_id, first_name, last_name, country, customer_segment
ORDER BY total_spent DESC;

-- Challenge 12: Product Category Performance
SELECT 
    p.category,
    COUNT(DISTINCT p.product_id) AS unique_products,
    COALESCE(SUM(oi.quantity), 0) AS total_quantity_sold,
    COALESCE(SUM(oi.quantity * oi.unit_price * (1 - o.discount_percent/100)), 0) AS total_revenue,
    COUNT(DISTINCT c.customer_id) AS unique_customers
FROM m05_products p
LEFT JOIN m05_order_items oi ON p.product_id = oi.product_id
LEFT JOIN m05_orders o ON oi.order_id = o.order_id
LEFT JOIN m05_customers c ON o.customer_id = c.customer_id
GROUP BY p.category
ORDER BY total_revenue DESC;

-- Senior-Level Challenge 13: Customer Risk Dataset
WITH customer_metrics AS (
    SELECT 
        c.customer_id,
        c.first_name,
        c.last_name,
        c.customer_segment,
        COUNT(o.order_id) AS total_orders,
        COUNT(CASE WHEN o.order_status = 'Completed' THEN 1 END) AS completed_orders,
        COALESCE(SUM(oi.quantity * oi.unit_price * (1 - o.discount_percent/100)), 0) AS total_spent,
        COALESCE(AVG(CASE WHEN oi.quantity * oi.unit_price * (1 - o.discount_percent/100) > 0 
                     THEN oi.quantity * oi.unit_price * (1 - o.discount_percent/100) END), 0) AS avg_order_value,
        MAX(o.order_date) AS last_order_date
    FROM m05_customers c
    LEFT JOIN m05_orders o ON c.customer_id = o.customer_id
    LEFT JOIN m05_order_items oi ON o.order_id = oi.order_id
    GROUP BY c.customer_id, c.first_name, c.last_name, c.customer_segment
)
SELECT 
    customer_id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    customer_segment,
    total_orders,
    completed_orders,
    total_spent,
    avg_order_value,
    last_order_date,
    COALESCE(DATEDIFF(CURRENT_DATE, last_order_date), 999) AS days_since_last_order,
    CASE 
        WHEN total_spent >= 3000 THEN 'High Value'
        WHEN total_spent >= 1000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS customer_value,
    CASE 
        WHEN total_orders = 0 THEN 'Never Purchased'
        WHEN DATEDIFF(CURRENT_DATE, last_order_date) > 90 THEN 'Inactive'
        WHEN DATEDIFF(CURRENT_DATE, last_order_date) > 30 THEN 'At Risk'
        ELSE 'Active'
    END AS activity_status
FROM customer_metrics
ORDER BY total_spent DESC;


