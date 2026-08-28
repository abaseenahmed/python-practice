-- Data Quality Audit

-- 1. Row Counts
SELECT 'raw_customers' as table_name, COUNT(*) as row_count FROM raw_customers
UNION ALL
SELECT 'raw_products', COUNT(*) FROM raw_products
UNION ALL
SELECT 'raw_orders', COUNT(*) FROM raw_orders
UNION ALL
SELECT 'raw_order_items', COUNT(*) FROM raw_order_items
UNION ALL
SELECT 'raw_payments', COUNT(*) FROM raw_payments;

-- 2. NULL Values Analysis
-- Customers table NULLs
SELECT 
    'customers' as table_name,
    COUNT(*) - COUNT(customer_id) as null_customer_id,
    COUNT(*) - COUNT(name) as null_name,
    COUNT(*) - COUNT(email) as null_email,
    COUNT(*) - COUNT(age) as null_age,
    COUNT(*) - COUNT(country) as null_country,
    COUNT(*) - COUNT(customer_segment) as null_segment,
    COUNT(*) - COUNT(registration_date) as null_registration
FROM raw_customers;

-- Products table NULLs
SELECT 
    'products' as table_name,
    COUNT(*) - COUNT(product_id) as null_product_id,
    COUNT(*) - COUNT(name) as null_name,
    COUNT(*) - COUNT(category) as null_category,
    COUNT(*) - COUNT(subcategory) as null_subcategory,
    COUNT(*) - COUNT(unit_price) as null_unit_price,
    COUNT(*) - COUNT(stock_quantity) as null_stock
FROM raw_products;

-- 3. Duplicate Analysis
-- Duplicate customers
SELECT customer_id, COUNT(*) as duplicates
FROM raw_customers
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- Duplicate payments
SELECT payment_id, COUNT(*) as duplicates
FROM raw_payments
GROUP BY payment_id
HAVING COUNT(*) > 1;

-- 4. Invalid Values Analysis
-- Age issues
SELECT 'customers' as table_name, 'age < 18' as issue, COUNT(*) as count
FROM raw_customers 
WHERE age < 18
UNION ALL
SELECT 'customers', 'age > 100', COUNT(*)
FROM raw_customers 
WHERE age > 100;

-- Quantity issues
SELECT 'order_items' as table_name, 'quantity <= 0' as issue, COUNT(*) as count
FROM raw_order_items 
WHERE quantity <= 0;

-- Discount issues
SELECT 'order_items' as table_name, 'discount_pct < 0' as issue, COUNT(*) as count
FROM raw_order_items 
WHERE discount_pct < 0
UNION ALL
SELECT 'order_items', 'discount_pct > 100', COUNT(*)
FROM raw_order_items 
WHERE discount_pct > 100;

-- 5. Referential Integrity
-- Orders with missing customers
SELECT COUNT(*) as missing_customers
FROM raw_orders o
LEFT JOIN raw_customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- Order items with missing orders
SELECT COUNT(*) as missing_orders
FROM raw_order_items oi
LEFT JOIN raw_orders o ON oi.order_id = o.order_id
WHERE o.order_id IS NULL;

-- Order items with missing products
SELECT COUNT(*) as missing_products
FROM raw_order_items oi
LEFT JOIN raw_products p ON oi.product_id = p.product_id
WHERE p.product_id IS NULL;