import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)
n = 5000

# Customer and order information
order_ids = [f"ORD{100001 + i}" for i in range(n)]
customer_ids = np.random.choice(np.arange(1001, 1801), size=n)

dates = pd.date_range("2024-01-01", "2025-12-31", freq="D")
order_dates = np.random.choice(dates, size=n)

ages = np.clip(np.random.normal(34, 11, n).round(), 18, 75).astype(int)
genders = np.random.choice(["Male", "Female"], n, p=[0.52, 0.48])

cities = np.random.choice(
    ["Karachi", "Lahore", "Islamabad", "Faisalabad",
     "Peshawar", "Quetta", "Multan", "Rawalpindi"],
    n
)

city_to_region = {
    "Karachi": "South", "Lahore": "East",
    "Islamabad": "North", "Faisalabad": "East",
    "Peshawar": "West", "Quetta": "West",
    "Multan": "South", "Rawalpindi": "North"
}
regions = pd.Series(cities).map(city_to_region).to_numpy()

# Product information
products = [
    "Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch",
    "Keyboard", "Mouse", "Monitor", "T-Shirt", "Jeans",
    "Shoes", "Jacket", "Backpack", "Sunglasses", "Wallet"
]

product_category = {
    "Laptop": "Electronics", "Smartphone": "Electronics",
    "Tablet": "Electronics", "Headphones": "Electronics",
    "Smartwatch": "Electronics", "Keyboard": "Electronics",
    "Mouse": "Electronics", "Monitor": "Electronics",
    "T-Shirt": "Clothing", "Jeans": "Clothing",
    "Shoes": "Clothing", "Jacket": "Clothing",
    "Backpack": "Accessories", "Sunglasses": "Accessories",
    "Wallet": "Accessories"
}

product_price = {
    "Laptop": 1200, "Smartphone": 750, "Tablet": 500,
    "Headphones": 120, "Smartwatch": 220, "Keyboard": 70,
    "Mouse": 35, "Monitor": 300, "T-Shirt": 30, "Jeans": 65,
    "Shoes": 90, "Jacket": 110, "Backpack": 55,
    "Sunglasses": 80, "Wallet": 45
}

product_probs = np.array([
    0.07, 0.10, 0.07, 0.09, 0.06, 0.05, 0.08, 0.06,
    0.08, 0.07, 0.09, 0.04, 0.06, 0.05, 0.03
])
product_probs /= product_probs.sum()

selected_products = np.random.choice(products, n, p=product_probs)
categories = np.array([product_category[p] for p in selected_products])
base_prices = np.array([product_price[p] for p in selected_products])

unit_prices = np.round(
    base_prices * np.random.normal(1, 0.06, n), 2
)
unit_prices = np.maximum(unit_prices, 5)

quantities = np.random.choice(
    range(1, 9), n,
    p=[0.32, 0.25, 0.17, 0.11, 0.06, 0.04, 0.03, 0.02]
)

discounts = np.random.choice(
    [0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30],
    n,
    p=[0.30, 0.16, 0.20, 0.14, 0.10, 0.06, 0.04]
)

payment_methods = np.random.choice(
    ["Credit Card", "Debit Card", "Cash", "Bank Transfer", "Digital Wallet"],
    n,
    p=[0.28, 0.22, 0.10, 0.15, 0.25]
)

customer_types = np.random.choice(
    ["New", "Returning", "VIP"],
    n,
    p=[0.45, 0.43, 0.12]
)

ratings = np.clip(
    np.round(
        np.random.normal(3.8, 0.75, n)
        + np.where(customer_types == "VIP", 0.25,
                   np.where(customer_types == "Returning", 0.10, 0)),
        1
    ),
    1, 5
)

revenue = np.round(
    unit_prices * quantities * (1 - discounts), 2
)

df = pd.DataFrame({
    "order_id": order_ids,
    "order_date": order_dates,
    "customer_id": customer_ids,
    "age": ages,
    "gender": genders,
    "city": cities,
    "region": regions,
    "category": categories,
    "product": selected_products,
    "unit_price": unit_prices,
    "quantity": quantities,
    "discount": discounts,
    "payment_method": payment_methods,
    "customer_type": customer_types,
    "rating": ratings,
    "revenue": revenue
}).sort_values("order_date").reset_index(drop=True)

# Small amount of missing data for cleaning practice
rng = np.random.default_rng(42)

for col, fraction in {"age": 0.01, "rating": 0.008, "payment_method": 0.006}.items():
    idx = rng.choice(df.index, size=int(n * fraction), replace=False)
    df.loc[idx, col] = np.nan

output_dir = Path("/mnt/data/Project_04/data")
output_dir.mkdir(parents=True, exist_ok=True)

output_path = "ecommerce_customers.csv"
df.to_csv(output_path, index=False)

print(f"Dataset generated successfully: {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"File: {output_path}")
print("\nColumns:")
print(list(df.columns))
print("\nMissing values:")
print(df.isnull().sum())
