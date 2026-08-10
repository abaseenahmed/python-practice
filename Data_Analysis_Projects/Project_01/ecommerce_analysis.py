import numpy as np
import pandas as pd

np.random.seed(42)

n = 5000

products = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Tablet",
    "Smartwatch"
]

categories = {
    "Laptop": "Electronics",
    "Smartphone": "Electronics",
    "Headphones": "Accessories",
    "Keyboard": "Accessories",
    "Mouse": "Accessories",
    "Monitor": "Electronics",
    "Tablet": "Electronics",
    "Smartwatch": "Wearables"
}

regions = [
    "Punjab",
    "Sindh",
    "Balochistan",
    "KPK",
    "Islamabad"
]

customers = [
    "Customer_" + str(i)
    for i in range(1, 1001)
]

dates = pd.date_range(
    start="2024-01-01",
    end="2025-12-31",
    periods=n
)

product = np.random.choice(products, n)

quantity = np.random.randint(1, 6, n)

price_map = {
    "Laptop": 150000,
    "Smartphone": 90000,
    "Headphones": 8000,
    "Keyboard": 5000,
    "Mouse": 3000,
    "Monitor": 45000,
    "Tablet": 60000,
    "Smartwatch": 25000
}

price = np.array([
    price_map[p]
    for p in product
])

discount = np.random.uniform(0, 0.25, n)

df = pd.DataFrame({
    "order_date": dates,
    "customer": np.random.choice(customers, n),
    "product": product,
    "category": [categories[p] for p in product],
    "region": np.random.choice(regions, n),
    "quantity": quantity,
    "unit_price": price,
    "discount": discount
})

df["revenue"] = (
    df["quantity"]
    * df["unit_price"]
    * (1 - df["discount"])
)

df.to_csv(
    "ecommerce_sales.csv",
    index=False
)

print("Dataset created successfully.")
print(df.head())