# src/generate_data.py
import numpy as np
import pandas as pd
import os

def generate_retail_data():
    """Generate messy retail transaction data with intentional data quality issues."""
    
    np.random.seed(42)
    
    n = 15000
    
    transaction_id = np.arange(100001, 100001 + n)
    customer_id = np.random.randint(1001, 4001, n)
    
    products = [
        "Laptop", "Smartphone", "Tablet", "Headphones", "Keyboard",
        "Mouse", "Monitor", "Smartwatch", "Camera", "Printer"
    ]
    
    product = np.random.choice(products, n)
    
    categories = {
        "Laptop": "Electronics", "Smartphone": "Electronics",
        "Tablet": "Electronics", "Headphones": "Accessories",
        "Keyboard": "Accessories", "Mouse": "Accessories",
        "Monitor": "Electronics", "Smartwatch": "Wearables",
        "Camera": "Electronics", "Printer": "Office"
    }
    
    category = [categories[p] for p in product]
    
    regions = ["North", "South", "East", "West"]
    region = np.random.choice(regions, n)
    
    payment_methods = ["Cash", "Card", "Online", "Bank Transfer"]
    payment_method = np.random.choice(payment_methods, n)
    
    quantity = np.random.randint(1, 8, n)
    
    unit_price_map = {
        "Laptop": 1200, "Smartphone": 800, "Tablet": 500,
        "Headphones": 120, "Keyboard": 70, "Mouse": 40,
        "Monitor": 300, "Smartwatch": 250, "Camera": 900,
        "Printer": 220
    }
    
    base_price = np.array([unit_price_map[p] for p in product])
    unit_price = base_price * np.random.uniform(0.85, 1.15, n)
    
    discount = np.random.uniform(0, 0.30, n)
    revenue = quantity * unit_price * (1 - discount)
    
    dates = pd.date_range("2024-01-01", "2025-12-31", periods=n)
    
    customer_age = np.random.randint(18, 70, n)
    customer_gender = np.random.choice(["Male", "Female"], n)
    customer_type = np.random.choice(
        ["New", "Returning", "VIP"],
        n,
        p=[0.45, 0.45, 0.10]
    )
    
    rating = np.random.uniform(1, 5, n)
    shipping_cost = np.random.uniform(5, 50, n)
    
    df = pd.DataFrame({
        "transaction_id": transaction_id,
        "customer_id": customer_id,
        "order_date": dates,
        "product": product,
        "category": category,
        "region": region,
        "payment_method": payment_method,
        "quantity": quantity,
        "unit_price": unit_price,
        "discount": discount,
        "revenue": revenue,
        "customer_age": customer_age,
        "customer_gender": customer_gender,
        "customer_type": customer_type,
        "rating": rating,
        "shipping_cost": shipping_cost
    })
    
    # 1. Missing values
    for column in ["region", "payment_method", "customer_age", "rating", "shipping_cost"]:
        indices = np.random.choice(df.index, 120, replace=False)
        df.loc[indices, column] = np.nan
    
    # 2. Duplicate transactions
    duplicates = df.sample(100, random_state=42)
    df = pd.concat([df, duplicates], ignore_index=True)
    
    # 3. Inconsistent category names
    indices = np.random.choice(df.index, 100, replace=False)
    df.loc[indices, "region"] = "north"
    indices = np.random.choice(df.index, 100, replace=False)
    df.loc[indices, "region"] = " SOUTH "
    
    # 4. Invalid values
    indices = np.random.choice(df.index, 50, replace=False)
    df.loc[indices, "quantity"] = -1
    indices = np.random.choice(df.index, 50, replace=False)
    df.loc[indices, "discount"] = 1.5
    
    # 5. Extreme values
    indices = np.random.choice(df.index, 20, replace=False)
    df.loc[indices, "unit_price"] *= 20
    
    # 6. Invalid customer ages
    indices = np.random.choice(df.index, 30, replace=False)
    df.loc[indices, "customer_age"] = 150
    
    # 7. Invalid ratings
    indices = np.random.choice(df.index, 20, replace=False)
    df.loc[indices, "rating"] = 8
    
    # Create data directory if it doesn't exist
    os.makedirs("../data", exist_ok=True)
    
    # Save
    df.to_csv("../data/raw_retail_transactions.csv", index=False)
    
    print("Messy retail dataset generated.")
    print("Shape:", df.shape)
    return df

if __name__ == "__main__":
    generate_retail_data()