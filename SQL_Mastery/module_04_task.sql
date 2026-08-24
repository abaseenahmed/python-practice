-- ======================= Module 04: Data Transformation & Conditional Logic ==============

-- Task 01: Categorize customers by age group
SELECT 
    customer_id,
    first_name,
    age,
    CASE 
        WHEN age < 25 THEN 'Young'
        WHEN age < 35 THEN 'Middle Aged'
        ELSE 'Senior'
    END AS age_group
FROM customers;

-- Task 02: Check data quality status for customer records
SELECT
    customer_id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    email,
    customer_segment,
    CASE 
        WHEN (email IS NULL) AND (customer_segment IS NULL) THEN 'Critical'
        WHEN (email IS NULL) OR (customer_segment IS NULL) THEN 'Incomplete'
        ELSE 'Complete'
    END AS data_quality_status
FROM customers;

-- Task 03: Categorize orders by total amount
SELECT
    order_id,
    total_amount,
    COALESCE(discount_percent, 0) AS discount_percent,
    CASE
        WHEN total_amount >= 1000 THEN 'High Value'
        WHEN total_amount >= 500 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS order_value_category
FROM orders;

-- Task 04: Calculate discount amounts and categorize discount levels
SELECT 
    order_id,
    total_amount,
    COALESCE(discount_percent, 0) AS effective_discount,
    (total_amount * COALESCE(discount_percent, 0)) / 100 AS discount_amount,
    CASE 
        WHEN (total_amount * COALESCE(discount_percent, 0)) / 100 >= 20 THEN 'High Discount'
        WHEN (total_amount * COALESCE(discount_percent, 0)) / 100 >= 10 THEN 'Moderate Discount'
        ELSE 'Low Discount'
    END AS discount_risk
FROM orders;

-- Task 05: Convert order status to boolean flag
SELECT 
    order_id,
    order_status,
    CASE
        WHEN order_status = 'Completed' THEN 1
        ELSE 0
    END AS is_successful
FROM orders;

-- Task 06: Calculate customer tenure in days (FIXED)
SELECT 
    customer_id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    signup_date,
    EXTRACT(DAY FROM signup_date) AS signup_day,
    EXTRACT(DAY FROM CURRENT_DATE) AS current_day,
    EXTRACT(DAY FROM CURRENT_DATE) - EXTRACT(DAY FROM signup_date) AS tenure_days
FROM customers;

-- Alternative: Better tenure calculation using date difference
SELECT 
    customer_id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    signup_date,
    CURRENT_DATE - signup_date AS tenure_days,
    EXTRACT(YEAR FROM AGE(CURRENT_DATE, signup_date)) AS tenure_years,
    EXTRACT(MONTH FROM AGE(CURRENT_DATE, signup_date)) AS tenure_months
FROM customers;

-- Task 07: Calculate revenue by product category (FIXED)
SELECT 
    product_name,
    category,
    quantity_sold,
    quantity_sold * unit_price AS revenue
FROM order_items
GROUP BY category, product_name, quantity_sold, unit_price
ORDER BY revenue DESC;

-- Better version with category aggregates
SELECT 
    category,
    COUNT(*) AS total_products,
    SUM(quantity_sold) AS total_quantity_sold,
    SUM(quantity_sold * unit_price) AS total_revenue,
    AVG(unit_price) AS avg_price,
    ROUND(AVG(quantity_sold * unit_price), 2) AS avg_revenue_per_product
FROM order_items
GROUP BY category
ORDER BY total_revenue DESC;

-- Task 08: Calculate recognized revenue based on order status
SELECT 
    order_id,
    order_status,
    total_amount,
    CASE
        WHEN order_status = 'Completed' THEN total_amount
        WHEN order_status = 'Cancelled' THEN 0
        WHEN order_status = 'Pending' THEN 0
        WHEN order_status = 'Returned' THEN 0
        ELSE 0
    END AS recognized_revenue
FROM orders;

-- Task 09: Determine customer risk level based on segment and age (FIXED)
SELECT
    customer_id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    customer_segment,
    age,
    CASE 
        WHEN customer_segment = 'VIP' THEN 'Low Risk'
        WHEN customer_segment = 'Premium' AND age >= 30 THEN 'Low Risk'
        WHEN customer_segment = 'Premium' AND age < 30 THEN 'Medium Risk'
        WHEN customer_segment = 'Regular' AND age >= 35 THEN 'Medium Risk'
        WHEN customer_segment = 'Regular' AND age < 35 THEN 'High Risk'
        WHEN customer_segment IS NULL OR age IS NULL THEN 'Unknown'
        ELSE 'Undefined'
    END AS customer_risk
FROM customers;

-- ======================= ADDITIONAL DATA ANALYSIS QUERIES ===============================

-- Task 10: Customer lifetime value analysis
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    c.customer_segment,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_spent,
    AVG(o.total_amount) AS avg_order_value,
    MIN(o.order_date) AS first_order_date,
    MAX(o.order_date) AS last_order_date,
    CASE 
        WHEN COUNT(o.order_id) >= 10 AND SUM(o.total_amount) > 5000 THEN 'Platinum'
        WHEN COUNT(o.order_id) >= 5 AND SUM(o.total_amount) > 2000 THEN 'Gold'
        WHEN COUNT(o.order_id) >= 3 AND SUM(o.total_amount) > 1000 THEN 'Silver'
        ELSE 'Bronze'
    END AS loyalty_tier
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name, c.customer_segment
ORDER BY total_spent DESC;

-- Task 11: Monthly sales trend analysis
SELECT 
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month,
    COUNT(*) AS total_orders,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS avg_order_value,
    COUNT(CASE WHEN order_status = 'Completed' THEN 1 END) AS completed_orders,
    ROUND(COUNT(CASE WHEN order_status = 'Completed' THEN 1 END) * 100.0 / COUNT(*), 2) AS completion_rate
FROM orders
GROUP BY EXTRACT(YEAR FROM order_date), EXTRACT(MONTH FROM order_date)
ORDER BY year DESC, month DESC;

-- Task 12: Product performance analysis
SELECT 
    oi.product_id,
    oi.product_name,
    oi.category,
    COUNT(DISTINCT oi.order_id) AS order_count,
    SUM(oi.quantity_sold) AS total_quantity,
    SUM(oi.quantity_sold * oi.unit_price) AS total_revenue,
    ROUND(AVG(oi.unit_price), 2) AS avg_price,
    ROUND(SUM(oi.quantity_sold * oi.unit_price) / SUM(oi.quantity_sold), 2) AS avg_revenue_per_unit,
    RANK() OVER (ORDER BY SUM(oi.quantity_sold * oi.unit_price) DESC) AS revenue_rank
FROM order_items oi
GROUP BY oi.product_id, oi.product_name, oi.category
ORDER BY total_revenue DESC;

-- Task 13: Customer segmentation by purchase behavior
SELECT 
    c.customer_segment,
    COUNT(DISTINCT c.customer_id) AS customer_count,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_revenue,
    ROUND(AVG(o.total_amount), 2) AS avg_order_value,
    ROUND(SUM(o.total_amount) / COUNT(DISTINCT c.customer_id), 2) AS revenue_per_customer,
    ROUND(COUNT(o.order_id) * 1.0 / COUNT(DISTINCT c.customer_id), 2) AS orders_per_customer
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_segment
ORDER BY total_revenue DESC;

-- Task 14: Order status distribution and performance
SELECT 
    order_status,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS avg_order_value,
    MIN(order_date) AS first_order_date,
    MAX(order_date) AS last_order_date,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM orders
GROUP BY order_status
ORDER BY order_count DESC;

-- Task 15: Discount effectiveness analysis
SELECT 
    CASE 
        WHEN discount_percent = 0 THEN 'No Discount'
        WHEN discount_percent < 10 THEN 'Low Discount'
        WHEN discount_percent < 20 THEN 'Medium Discount'
        ELSE 'High Discount'
    END AS discount_category,
    COUNT(*) AS order_count,
    AVG(total_amount) AS avg_revenue,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount * discount_percent / 100) AS avg_discount_amount,
    ROUND(AVG(total_amount * discount_percent / 100) / AVG(total_amount) * 100, 2) AS discount_revenue_ratio
FROM orders
GROUP BY discount_category
ORDER BY discount_category;

-- Task 16: Customer churn risk analysis
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    c.customer_segment,
    COUNT(o.order_id) AS order_count,
    MAX(o.order_date) AS last_order_date,
    CURRENT_DATE - MAX(o.order_date) AS days_since_last_order,
    CASE 
        WHEN CURRENT_DATE - MAX(o.order_date) > 180 THEN 'High Churn Risk'
        WHEN CURRENT_DATE - MAX(o.order_date) > 90 THEN 'Medium Churn Risk'
        WHEN CURRENT_DATE - MAX(o.order_date) > 30 THEN 'Low Churn Risk'
        ELSE 'Active'
    END AS churn_risk_category
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name, c.customer_segment
HAVING MAX(o.order_date) IS NOT NULL
ORDER BY days_since_last_order DESC;

-- Task 17: Revenue by product category with growth indicators
WITH category_revenue AS (
    SELECT 
        category,
        EXTRACT(YEAR FROM o.order_date) AS year,
        EXTRACT(MONTH FROM o.order_date) AS month,
        SUM(oi.quantity_sold * oi.unit_price) AS monthly_revenue
    FROM order_items oi
    JOIN orders o ON oi.order_id = o.order_id
    GROUP BY category, year, month
)
SELECT 
    category,
    year,
    month,
    monthly_revenue,
    LAG(monthly_revenue, 1) OVER (PARTITION BY category ORDER BY year, month) AS previous_month_revenue,
    ROUND(((monthly_revenue - LAG(monthly_revenue, 1) OVER (PARTITION BY category ORDER BY year, month)) / 
        LAG(monthly_revenue, 1) OVER (PARTITION BY category ORDER BY year, month)) * 100, 2) AS month_over_month_growth
FROM category_revenue
ORDER BY category, year DESC, month DESC;

-- Task 18: Customer value tier transition tracking
SELECT 
    customer_id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    age,
    customer_segment,
    CASE 
        WHEN total_spent > 10000 THEN 'Tier 1: Elite'
        WHEN total_spent > 5000 THEN 'Tier 2: Premium'
        WHEN total_spent > 1000 THEN 'Tier 3: Standard'
        ELSE 'Tier 4: Basic'
    END AS revenue_tier,
    CASE 
        WHEN order_count > 20 THEN 'High Frequency'
        WHEN order_count > 10 THEN 'Medium Frequency'
        ELSE 'Low Frequency'
    END AS frequency_category,
    CASE 
        WHEN total_spent > 10000 AND order_count > 20 THEN 'Star Customer'
        WHEN total_spent > 5000 OR order_count > 15 THEN 'High Potential'
        ELSE 'Regular Customer'
    END AS customer_profile
FROM (
    SELECT 
        c.customer_id,
        c.first_name,
        c.last_name,
        c.age,
        c.customer_segment,
        COUNT(o.order_id) AS order_count,
        COALESCE(SUM(o.total_amount), 0) AS total_spent
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.first_name, c.last_name, c.age, c.customer_segment
) AS customer_metrics
ORDER BY total_spent DESC;