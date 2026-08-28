# Project 01 E-Commerce ML Dataset

Synthetic but realistic e-commerce dataset generated for SQL + AI/ML data pipeline practice.

## Files

- customers.csv: 5,015 rows
- products.csv: 500 rows
- orders.csv: 30,000 rows
- order_items.csv: 52,537 rows
- payments.csv: 30,010 rows

## Intended relationships

customers.customer_id -> orders.customer_id
orders.order_id -> order_items.order_id
products.product_id -> order_items.product_id
orders.order_id -> payments.order_id

## Important

The dataset intentionally contains data-quality problems:
- missing customer ages
- missing customer segments
- inconsistent country capitalization/whitespace
- duplicate customer records
- missing product prices
- invalid order-item quantities
- invalid discount percentages
- duplicate payment records

Do NOT clean these problems in Python first. The purpose of Project 01 is to practice auditing and cleaning the raw data using PostgreSQL/SQL.

## Recommended ML target

Start with customer purchase behavior and later create a target such as:
- high_value_customer
- repeat_customer
- purchase_next_30_days

For time-based targets, define a prediction date and prevent future-data leakage.

Generated with random seed 42 for reproducibility.
