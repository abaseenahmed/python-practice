import pandas as pd
import numpy as np
from pathlib import Path

# Reproducibility
rng = np.random.default_rng(42)

# -----------------------------
# Configuration
# -----------------------------
N_CUSTOMERS = 5000
N_PRODUCTS = 500
N_ORDERS = 30000
OUTPUT_DIR = Path("/mnt/data/project_01_ecommerce_ml_dataset")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Customers
# -----------------------------
customer_ids = np.arange(1, N_CUSTOMERS + 1)

countries = np.array(["Pakistan", "India", "UAE", "Saudi Arabia", "UK", "USA", "Canada", "Germany"])
country_probs = np.array([0.34, 0.16, 0.12, 0.10, 0.07, 0.10, 0.06, 0.05])

segments = np.array(["Budget", "Standard", "Premium", "VIP"])
segment_probs = np.array([0.30, 0.42, 0.22, 0.06])

signup_start = pd.Timestamp("2023-01-01")
signup_end = pd.Timestamp("2025-12-31")
signup_days = (signup_end - signup_start).days

signup_dates = signup_start + pd.to_timedelta(
    rng.integers(0, signup_days + 1, N_CUSTOMERS), unit="D"
)

customers = pd.DataFrame({
    "customer_id": customer_ids,
    "customer_name": [f"Customer_{i:05d}" for i in customer_ids],
    "age": rng.integers(18, 66, N_CUSTOMERS),
    "gender": rng.choice(["Male", "Female", "Other"], N_CUSTOMERS, p=[0.49, 0.49, 0.02]),
    "country": rng.choice(countries, N_CUSTOMERS, p=country_probs),
    "customer_segment": rng.choice(segments, N_CUSTOMERS, p=segment_probs),
    "signup_date": signup_dates
})

# -----------------------------
# Products
# -----------------------------
product_ids = np.arange(1, N_PRODUCTS + 1)

categories = {
    "Electronics": ["Smartphone", "Laptop", "Headphones", "Monitor", "Tablet"],
    "Home": ["Chair", "Desk", "Lamp", "Cookware", "Vacuum Cleaner"],
    "Fashion": ["Shirt", "Shoes", "Jacket", "Jeans", "Bag"],
    "Books": ["Fiction", "Technology", "Business", "Science", "History"],
    "Sports": ["Football", "Cricket", "Fitness", "Running", "Camping"],
}

category_names = list(categories.keys())
category_probs = [0.24, 0.22, 0.21, 0.17, 0.16]

product_category = rng.choice(category_names, N_PRODUCTS, p=category_probs)
product_subcategory = [
    rng.choice(categories[cat]) for cat in product_category
]

base_prices = {
    "Electronics": (80, 1800),
    "Home": (20, 700),
    "Fashion": (15, 300),
    "Books": (5, 80),
    "Sports": (10, 500),
}

prices = np.array([
    rng.uniform(*base_prices[cat]) for cat in product_category
])

products = pd.DataFrame({
    "product_id": product_ids,
    "product_name": [
        f"{subcat} Product {i:03d}"
        for i, subcat in zip(product_ids, product_subcategory)
    ],
    "category": product_category,
    "subcategory": product_subcategory,
    "unit_price": np.round(prices, 2)
})

# -----------------------------
# Orders
# -----------------------------
order_ids = np.arange(1, N_ORDERS + 1)

# Give some customers higher purchasing probability
customer_weights = rng.lognormal(mean=0, sigma=0.8, size=N_CUSTOMERS)
customer_weights /= customer_weights.sum()

order_customer_ids = rng.choice(
    customer_ids,
    size=N_ORDERS,
    p=customer_weights
)

order_start = pd.Timestamp("2024-01-01")
order_end = pd.Timestamp("2025-12-31")
order_days = (order_end - order_start).days

order_dates = order_start + pd.to_timedelta(
    rng.integers(0, order_days + 1, N_ORDERS), unit="D"
)

order_status = rng.choice(
    ["Completed", "Cancelled", "Returned", "Pending"],
    N_ORDERS,
    p=[0.78, 0.07, 0.10, 0.05]
)

payment_methods = rng.choice(
    ["Credit Card", "Debit Card", "Bank Transfer", "Cash on Delivery", "Digital Wallet"],
    N_ORDERS,
    p=[0.24, 0.20, 0.13, 0.23, 0.20]
)

orders = pd.DataFrame({
    "order_id": order_ids,
    "customer_id": order_customer_ids,
    "order_date": order_dates,
    "order_status": order_status,
    "payment_method": payment_methods
})

# -----------------------------
# Order Items
# 1-4 items per order
# -----------------------------
item_counts = rng.choice([1, 2, 3, 4], N_ORDERS, p=[0.50, 0.30, 0.15, 0.05])
order_item_rows = []

order_item_id = 1
for order_id, count in zip(order_ids, item_counts):
    selected_products = rng.choice(product_ids, count, replace=False)

    for product_id in selected_products:
        quantity = int(rng.choice([1, 2, 3, 4], p=[0.65, 0.23, 0.09, 0.03]))
        unit_price = float(products.loc[
            products["product_id"].eq(product_id), "unit_price"
        ].iloc[0])

        # Small realistic discount
        discount_pct = float(rng.choice(
            [0, 5, 10, 15, 20],
            p=[0.42, 0.22, 0.20, 0.11, 0.05]
        ))

        order_item_rows.append([
            order_item_id,
            order_id,
            product_id,
            quantity,
            round(unit_price, 2),
            discount_pct
        ])
        order_item_id += 1

order_items = pd.DataFrame(
    order_item_rows,
    columns=[
        "order_item_id",
        "order_id",
        "product_id",
        "quantity",
        "unit_price",
        "discount_pct"
    ]
)

order_items["line_total"] = np.round(
    order_items["quantity"]
    * order_items["unit_price"]
    * (1 - order_items["discount_pct"] / 100),
    2
)

# -----------------------------
# Payments
# One payment per order
# -----------------------------
order_totals = (
    order_items.groupby("order_id", as_index=False)["line_total"]
    .sum()
    .rename(columns={"line_total": "order_amount"})
)

orders = orders.merge(order_totals, on="order_id", how="left")
orders["order_amount"] = orders["order_amount"].round(2)

payment_ids = np.arange(1, N_ORDERS + 1)

payment_status = []
for status in orders["order_status"]:
    if status == "Completed":
        payment_status.append(rng.choice(["Paid", "Failed"], p=[0.97, 0.03]))
    elif status == "Cancelled":
        payment_status.append("Refunded")
    elif status == "Returned":
        payment_status.append("Refunded")
    else:
        payment_status.append(rng.choice(["Pending", "Paid"], p=[0.7, 0.3]))

payments = pd.DataFrame({
    "payment_id": payment_ids,
    "order_id": orders["order_id"],
    "payment_date": orders["order_date"] + pd.to_timedelta(
        rng.integers(0, 3, N_ORDERS), unit="D"
    ),
    "payment_method": orders["payment_method"],
    "payment_amount": orders["order_amount"],
    "payment_status": payment_status
})

# -----------------------------
# Inject realistic data-quality issues
# These are intentional and are part of the project.
# -----------------------------

# Missing ages
missing_age_idx = rng.choice(customers.index, size=120, replace=False)
customers.loc[missing_age_idx, "age"] = np.nan

# Inconsistent country formatting
country_issue_idx = rng.choice(customers.index, size=100, replace=False)
customers.loc[country_issue_idx[:35], "country"] = " pakistan "
customers.loc[country_issue_idx[35:65], "country"] = "PAKISTAN"
customers.loc[country_issue_idx[65:], "country"] = "India "

# Missing customer segments
missing_segment_idx = rng.choice(customers.index, size=80, replace=False)
customers.loc[missing_segment_idx, "customer_segment"] = np.nan

# Missing product prices in a few product records
missing_price_idx = rng.choice(products.index, size=12, replace=False)
products.loc[missing_price_idx, "unit_price"] = np.nan

# A few invalid/negative order item quantities
bad_quantity_idx = rng.choice(order_items.index, size=35, replace=False)
order_items.loc[bad_quantity_idx[:20], "quantity"] = 0
order_items.loc[bad_quantity_idx[20:], "quantity"] = -1

# A few excessive discounts
bad_discount_idx = rng.choice(order_items.index, size=20, replace=False)
order_items.loc[bad_discount_idx, "discount_pct"] = 150

# Duplicate-looking customer rows for data-quality auditing
duplicate_customers = customers.sample(15, random_state=42).copy()
duplicate_customers["customer_id"] = duplicate_customers["customer_id"]
customers_raw = pd.concat([customers, duplicate_customers], ignore_index=True)

# A few duplicate payment rows
duplicate_payments = payments.sample(10, random_state=42).copy()
payments_raw = pd.concat([payments, duplicate_payments], ignore_index=True)

# Recalculate order amount from the intentionally corrupted items
orders["order_amount"] = (
    order_items.assign(
        corrupted_line_total=
        order_items["quantity"]
        * order_items["unit_price"].fillna(0)
        * (1 - order_items["discount_pct"] / 100)
    )
    .groupby("order_id")["corrupted_line_total"]
    .sum()
    .reindex(orders["order_id"])
    .fillna(0)
    .round(2)
)

payments_raw = payments_raw.drop(columns=["payment_amount"]).merge(
    orders[["order_id", "order_amount"]],
    on="order_id",
    how="left"
).rename(columns={"order_amount": "payment_amount"})

# -----------------------------
# Save CSVs
# -----------------------------
files = {
    "customers.csv": customers_raw,
    "products.csv": products,
    "orders.csv": orders,
    "order_items.csv": order_items,
    "payments.csv": payments_raw
}

for filename, df in files.items():
    df.to_csv(OUTPUT_DIR / filename, index=False)

# README describing the dataset
readme = f"""# Project 01 E-Commerce ML Dataset

Synthetic but realistic e-commerce dataset generated for SQL + AI/ML data pipeline practice.

## Files

- customers.csv: {len(customers_raw):,} rows
- products.csv: {len(products):,} rows
- orders.csv: {len(orders):,} rows
- order_items.csv: {len(order_items):,} rows
- payments.csv: {len(payments_raw):,} rows

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
"""

(OUTPUT_DIR / "README.txt").write_text(readme, encoding="utf-8")

# Create a zip for convenient transfer
import zipfile
zip_path = Path("/mnt/data/project_01_ecommerce_ml_dataset.zip")
with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
    for path in OUTPUT_DIR.iterdir():
        z.write(path, arcname=f"project_01_ecommerce_ml_dataset/{path.name}")

print(f"Created dataset folder: {OUTPUT_DIR}")
print(f"Created ZIP: {zip_path}")
print("\nFiles:")
