-- Analytical Transformations

-- 1. Customer Metrics
WITH customer_metrics AS (
    SELECT 
        c.customer_id,
        COUNT(DISTINCT o.order_id) as total_orders,
        SUM(oi.line_total) as total_spent,
        AVG(oi.line_total) as average_order_value,
        SUM(oi.quantity) as total_items_purchased,
        COUNT(DISTINCT oi.product_id) as unique_products_purchased,
        MIN(o.order_date) as first_order_date,
        MAX(o.order_date) as last_order_date
    FROM clean_customers c
    LEFT JOIN clean_orders o ON c.customer_id = o.customer_id
    LEFT JOIN clean_order_items oi ON o.order_id = oi.order_id
    WHERE o.order_status = 'Completed'
    GROUP BY c.customer_id
)
SELECT * FROM customer_metrics;

-- 2. Product Metrics
SELECT 
    p.product_id,
    p.name,
    p.category,
    p.subcategory,
    SUM(oi.quantity) as total_units_sold,
    SUM(oi.line_total) as total_revenue,
    COUNT(DISTINCT oi.order_id) as number_of_orders,
    AVG(oi.unit_price * (1 - oi.discount_pct/100)) as avg_selling_price
FROM clean_products p
INNER JOIN clean_order_items oi ON p.product_id = oi.product_id
INNER JOIN clean_orders o ON oi.order_id = o.order_id
WHERE o.order_status = 'Completed'
GROUP BY p.product_id, p.name, p.category, p.subcategory;

-- 3. Category Metrics
SELECT 
    p.category,
    SUM(oi.quantity) as total_units_sold,
    SUM(oi.line_total) as total_revenue,
    AVG(oi.line_total) as avg_order_value,
    COUNT(DISTINCT oi.order_id) as number_of_orders
FROM clean_products p
INNER JOIN clean_order_items oi ON p.product_id = oi.product_id
INNER JOIN clean_orders o ON oi.order_id = o.order_id
WHERE o.order_status = 'Completed'
GROUP BY p.category
ORDER BY total_revenue DESC;

-- 4. Time Metrics
WITH daily_metrics AS (
    SELECT 
        DATE_TRUNC('day', order_date) as day,
        COUNT(DISTINCT order_id) as orders,
        SUM(oi.line_total) as revenue,
        COUNT(DISTINCT customer_id) as active_customers
    FROM clean_orders o
    INNER JOIN clean_order_items oi ON o.order_id = oi.order_id
    WHERE o.order_status = 'Completed'
    GROUP BY DATE_TRUNC('day', order_date)
)
SELECT 
    day,
    orders,
    revenue,
    AVG(revenue) OVER (ORDER BY day ROWS BETWEEN 7 PRECEDING AND CURRENT ROW) as revenue_7_day_avg,
    active_customers
FROM daily_metrics
ORDER BY day;