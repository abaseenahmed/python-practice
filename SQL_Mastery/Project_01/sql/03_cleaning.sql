-- Data Cleaning

-- 1. Clean customers
INSERT INTO clean_customers
SELECT DISTINCT ON (customer_id)
    customer_id,
    name,
    email,
    COALESCE(
        age,
        (SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY age) 
         FROM raw_customers WHERE age IS NOT NULL)
    ) as age,
    INITCAP(TRIM(country)) as country,
    INITCAP(TRIM(customer_segment)) as customer_segment,
    registration_date
FROM raw_customers
WHERE age >= 18 AND age <= 100
ORDER BY customer_id, registration_date DESC;

-- 2. Clean products
INSERT INTO clean_products
SELECT 
    product_id,
    name,
    category,
    subcategory,
    COALESCE(
        CASE 
            WHEN unit_price <= 0 THEN NULL 
            ELSE unit_price 
        END,
        (SELECT AVG(unit_price) FROM raw_products WHERE unit_price > 0)
    ) as unit_price,
    CASE 
        WHEN stock_quantity < 0 THEN 0
        ELSE stock_quantity
    END as stock_quantity
FROM raw_products
WHERE unit_price IS NOT NULL OR unit_price > 0;

-- 3. Clean orders
INSERT INTO clean_orders
SELECT 
    o.order_id,
    o.customer_id,
    o.order_date,
    o.order_status,
    o.payment_method
FROM raw_orders o
INNER JOIN clean_customers c ON o.customer_id = c.customer_id
WHERE o.order_status IN ('Completed', 'Pending', 'Cancelled', 'Returned');

-- 4. Clean order items
INSERT INTO clean_order_items
SELECT 
    oi.order_item_id,
    oi.order_id,
    oi.product_id,
    CASE 
        WHEN oi.quantity <= 0 THEN 1
        ELSE oi.quantity
    END as quantity,
    COALESCE(
        CASE 
            WHEN oi.unit_price <= 0 THEN NULL 
            ELSE oi.unit_price 
        END,
        (SELECT AVG(unit_price) FROM raw_order_items WHERE unit_price > 0)
    ) as unit_price,
    CASE 
        WHEN oi.discount_pct < 0 THEN 0
        WHEN oi.discount_pct > 100 THEN 100
        ELSE oi.discount_pct
    END as discount_pct,
    -- Recalculate line_total
    (CASE 
        WHEN oi.quantity <= 0 THEN 1
        ELSE oi.quantity
    END * 
    COALESCE(
        CASE 
            WHEN oi.unit_price <= 0 THEN NULL 
            ELSE oi.unit_price 
        END,
        (SELECT AVG(unit_price) FROM raw_order_items WHERE unit_price > 0)
    ) * 
    (1 - CASE 
        WHEN oi.discount_pct < 0 THEN 0
        WHEN oi.discount_pct > 100 THEN 100
        ELSE oi.discount_pct
    END / 100.0)) as line_total
FROM raw_order_items oi
INNER JOIN clean_orders o ON oi.order_id = o.order_id
INNER JOIN clean_products p ON oi.product_id = p.product_id;

-- 5. Clean payments
INSERT INTO clean_payments
SELECT DISTINCT ON (payment_id)
    payment_id,
    order_id,
    payment_date,
    payment_method,
    CASE 
        WHEN payment_amount <= 0 THEN 100
        ELSE payment_amount
    END as payment_amount,
    payment_status
FROM raw_payments
WHERE payment_status IN ('Completed', 'Pending', 'Failed')
ORDER BY payment_id, payment_date DESC;