-- Feature Engineering for ML

-- 1. Calculate customer features
WITH customer_features AS (
    SELECT 
        c.customer_id,
        c.age,
        c.country,
        c.customer_segment,
        COALESCE(COUNT(DISTINCT o.order_id), 0) as total_orders,
        COALESCE(SUM(oi.line_total), 0) as total_spent,
        CASE 
            WHEN COUNT(DISTINCT o.order_id) > 0 
            THEN SUM(oi.line_total) / COUNT(DISTINCT o.order_id)
            ELSE 0
        END as average_order_value,
        COALESCE(SUM(oi.quantity), 0) as total_items_purchased,
        COALESCE(COUNT(DISTINCT oi.product_id), 0) as unique_products_purchased,
        MIN(o.order_date) as first_order_date,
        MAX(o.order_date) as last_order_date,
        -- Recency features
        EXTRACT(DAY FROM (NOW() - MAX(o.order_date))) as days_since_last_order,
        -- Recent order counts
        COUNT(DISTINCT CASE 
            WHEN o.order_date >= NOW() - INTERVAL '30 days' 
            THEN o.order_id 
        END) as orders_last_30_days,
        COUNT(DISTINCT CASE 
            WHEN o.order_date >= NOW() - INTERVAL '90 days' 
            THEN o.order_id 
        END) as orders_last_90_days,
        -- Recent spending
        COALESCE(SUM(CASE 
            WHEN o.order_date >= NOW() - INTERVAL '30 days' 
            THEN oi.line_total 
        END), 0) as spending_last_30_days,
        COALESCE(SUM(CASE 
            WHEN o.order_date >= NOW() - INTERVAL '90 days' 
            THEN oi.line_total 
        END), 0) as spending_last_90_days
    FROM clean_customers c
    LEFT JOIN clean_orders o ON c.customer_id = o.customer_id AND o.order_status = 'Completed'
    LEFT JOIN clean_order_items oi ON o.order_id = oi.order_id
    GROUP BY c.customer_id, c.age, c.country, c.customer_segment
)

-- 2. Create final ML feature table
INSERT INTO customer_ml_features
SELECT 
    customer_id,
    age,
    country,
    customer_segment,
    total_orders,
    total_spent,
    average_order_value,
    total_items_purchased,
    unique_products_purchased,
    first_order_date::DATE as first_order_date,
    last_order_date::DATE as last_order_date,
    CASE 
        WHEN days_since_last_order IS NULL THEN 999
        ELSE days_since_last_order::INTEGER
    END as days_since_last_order,
    orders_last_30_days::INTEGER,
    orders_last_90_days::INTEGER,
    spending_last_30_days,
    spending_last_90_days,
    -- Target variable: High value customer (top 20% by total spending)
    CASE 
        WHEN total_spent >= (
            SELECT PERCENTILE_CONT(0.8) WITHIN GROUP (ORDER BY total_spent)
            FROM customer_features
            WHERE total_spent > 0
        ) THEN 1
        ELSE 0
    END as high_value_customer
FROM customer_features;