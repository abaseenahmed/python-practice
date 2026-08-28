-- Create database (run this separately)
-- CREATE DATABASE ecommerce_ml;

-- Connect to the database
-- \c ecommerce_ml;

-- Create raw tables
DROP TABLE IF EXISTS raw_customers CASCADE;
CREATE TABLE raw_customers (
    customer_id INTEGER,
    name TEXT,
    email TEXT,
    age INTEGER,
    country TEXT,
    customer_segment TEXT,
    registration_date TIMESTAMP
);

DROP TABLE IF EXISTS raw_products CASCADE;
CREATE TABLE raw_products (
    product_id INTEGER,
    name TEXT,
    category TEXT,
    subcategory TEXT,
    unit_price NUMERIC(10,2),
    stock_quantity INTEGER
);

DROP TABLE IF EXISTS raw_orders CASCADE;
CREATE TABLE raw_orders (
    order_id INTEGER,
    customer_id INTEGER,
    order_date TIMESTAMP,
    order_status TEXT,
    payment_method TEXT
);

DROP TABLE IF EXISTS raw_order_items CASCADE;
CREATE TABLE raw_order_items (
    order_item_id INTEGER,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    unit_price NUMERIC(10,2),
    discount_pct NUMERIC(5,2),
    line_total NUMERIC(10,2)
);

DROP TABLE IF EXISTS raw_payments CASCADE;
CREATE TABLE raw_payments (
    payment_id INTEGER,
    order_id INTEGER,
    payment_date TIMESTAMP,
    payment_method TEXT,
    payment_amount NUMERIC(10,2),
    payment_status TEXT
);

-- Create clean tables with constraints
DROP TABLE IF EXISTS clean_customers CASCADE;
CREATE TABLE clean_customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER CHECK (age >= 18 AND age <= 100),
    country TEXT NOT NULL,
    customer_segment TEXT NOT NULL,
    registration_date TIMESTAMP
);

DROP TABLE IF EXISTS clean_products CASCADE;
CREATE TABLE clean_products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    subcategory TEXT NOT NULL,
    unit_price NUMERIC(10,2) CHECK (unit_price > 0),
    stock_quantity INTEGER CHECK (stock_quantity >= 0)
);

DROP TABLE IF EXISTS clean_orders CASCADE;
CREATE TABLE clean_orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES clean_customers(customer_id),
    order_date TIMESTAMP NOT NULL,
    order_status TEXT CHECK (order_status IN ('Completed', 'Pending', 'Cancelled', 'Returned')),
    payment_method TEXT
);

DROP TABLE IF EXISTS clean_order_items CASCADE;
CREATE TABLE clean_order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER REFERENCES clean_orders(order_id),
    product_id INTEGER REFERENCES clean_products(product_id),
    quantity INTEGER CHECK (quantity > 0),
    unit_price NUMERIC(10,2) CHECK (unit_price > 0),
    discount_pct NUMERIC(5,2) CHECK (discount_pct >= 0 AND discount_pct <= 100),
    line_total NUMERIC(10,2) CHECK (line_total >= 0)
);

DROP TABLE IF EXISTS clean_payments CASCADE;
CREATE TABLE clean_payments (
    payment_id INTEGER PRIMARY KEY,
    order_id INTEGER REFERENCES clean_orders(order_id),
    payment_date TIMESTAMP NOT NULL,
    payment_method TEXT,
    payment_amount NUMERIC(10,2) CHECK (payment_amount > 0),
    payment_status TEXT CHECK (payment_status IN ('Completed', 'Pending', 'Failed'))
);

-- Create ML feature table
DROP TABLE IF EXISTS customer_ml_features CASCADE;
CREATE TABLE customer_ml_features (
    customer_id INTEGER PRIMARY KEY,
    age INTEGER,
    country TEXT,
    customer_segment TEXT,
    total_orders INTEGER,
    total_spent NUMERIC(10,2),
    average_order_value NUMERIC(10,2),
    total_items_purchased INTEGER,
    unique_products_purchased INTEGER,
    first_order_date DATE,
    last_order_date DATE,
    days_since_last_order INTEGER,
    orders_last_30_days INTEGER,
    orders_last_90_days INTEGER,
    spending_last_30_days NUMERIC(10,2),
    spending_last_90_days NUMERIC(10,2),
    high_value_customer INTEGER
);