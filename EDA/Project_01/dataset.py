import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

def generate_customer_dataset(n_samples=1000):
    """
    Generate a synthetic customer dataset for EDA practice
    """
    
    # Customer IDs
    customer_ids = range(1, n_samples + 1)
    
    # Age distribution (skewed right)
    ages = np.random.normal(45, 15, n_samples).astype(int)
    ages = np.clip(ages, 18, 80)
    
    # Gender
    genders = np.random.choice(['Male', 'Female'], n_samples, p=[0.48, 0.52])
    
    # Income (log-normal distribution)
    income = np.random.lognormal(mean=10.5, sigma=0.6, size=n_samples)
    income = np.round(income * 1000, 2)
    income = np.clip(income, 20000, 200000)
    
    # Education level
    education = np.random.choice(
        ['High School', 'Bachelor', 'Master', 'PhD'], 
        n_samples, 
        p=[0.25, 0.45, 0.20, 0.10]
    )
    
    # Employment status
    employment = np.random.choice(
        ['Employed', 'Self-Employed', 'Unemployed', 'Retired'], 
        n_samples, 
        p=[0.55, 0.15, 0.15, 0.15]
    )
    
    # Marital status
    marital = np.random.choice(
        ['Single', 'Married', 'Divorced', 'Widowed'], 
        n_samples, 
        p=[0.30, 0.50, 0.15, 0.05]
    )
    
    # Number of dependents
    dependents = np.random.poisson(1, n_samples)
    dependents = np.clip(dependents, 0, 5)
    
    # Annual spending (correlated with income)
    spending_base = income * np.random.uniform(0.15, 0.45, n_samples)
    spending = np.round(spending_base + np.random.normal(0, 1000, n_samples), 2)
    spending = np.clip(spending, 500, 80000)
    
    # Number of purchases
    purchases = np.random.poisson(lam=15, size=n_samples)
    purchases = np.clip(purchases, 1, 50)
    
    # Average purchase value
    avg_purchase = spending / purchases
    avg_purchase = np.round(avg_purchase, 2)
    
    # Customer satisfaction score (1-5)
    satisfaction = np.random.normal(3.5, 0.8, n_samples)
    satisfaction = np.clip(satisfaction, 1, 5)
    satisfaction = np.round(satisfaction, 1)
    
    # Churn risk (correlated with satisfaction)
    churn_prob = 0.8 - (satisfaction - 1) * 0.15
    churn_prob = np.clip(churn_prob, 0.05, 0.95)
    churn = np.random.binomial(1, churn_prob, n_samples)
    
    # Account age (in months)
    account_age = np.random.exponential(scale=24, size=n_samples)
    account_age = np.clip(account_age, 1, 120).astype(int)
    
    # Product categories purchased
    categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']
    product_categories = np.random.choice(categories, n_samples, p=[0.3, 0.25, 0.15, 0.2, 0.1])
    
    # Premium customer status
    premium = (spending > 20000) & (purchases > 20)
    premium = premium.astype(int)
    
    # Engagement score
    engagement = np.random.normal(50, 15, n_samples)
    engagement = np.clip(engagement, 0, 100).astype(int)
    
    # Create DataFrame
    df = pd.DataFrame({
        'customer_id': customer_ids,
        'age': ages,
        'gender': genders,
        'income': income,
        'education': education,
        'employment_status': employment,
        'marital_status': marital,
        'dependents': dependents,
        'annual_spending': spending,
        'purchase_count': purchases,
        'avg_purchase_value': avg_purchase,
        'satisfaction_score': satisfaction,
        'churn_risk': churn,
        'account_age_months': account_age,
        'preferred_category': product_categories,
        'is_premium': premium,
        'engagement_score': engagement
    })
    
    return df

def add_time_based_features(df):
    """Add time-based features to the dataset"""
    
    # Signup dates (within last 5 years)
    today = datetime.now()
    days_range = np.random.randint(1, 1825, size=len(df))
    
    # Convert numpy int to Python int for timedelta
    signup_dates = [today - timedelta(days=int(x)) for x in days_range]
    df['signup_date'] = signup_dates
    
    # Last purchase date (within last 6 months)
    last_purchase_days = np.random.exponential(scale=30, size=len(df))
    last_purchase_days = np.clip(last_purchase_days, 0, 180).astype(int)
    
    # Convert numpy int to Python int for timedelta
    last_purchase = [today - timedelta(days=int(x)) for x in last_purchase_days]
    df['last_purchase_date'] = last_purchase
    
    # Season of signup
    df['signup_season'] = df['signup_date'].apply(
        lambda x: 'Winter' if x.month in [12, 1, 2] 
        else 'Spring' if x.month in [3, 4, 5] 
        else 'Summer' if x.month in [6, 7, 8] 
        else 'Fall'
    )
    
    # Days since last purchase
    df['days_since_last_purchase'] = (today - df['last_purchase_date']).dt.days
    
    return df

def add_missing_values(df, missing_rate=0.05):
    """Add some missing values to the dataset"""
    
    df_with_missing = df.copy()
    
    # Add missing values to selected columns
    columns_to_corrupt = ['income', 'satisfaction_score', 'engagement_score', 'age']
    
    for col in columns_to_corrupt:
        mask = np.random.random(len(df_with_missing)) < missing_rate
        df_with_missing.loc[mask, col] = np.nan
    
    return df_with_missing

def add_outliers(df):
    """Add some outliers to the dataset"""
    
    df_with_outliers = df.copy()
    
    # Add extreme income outliers
    outlier_indices = np.random.choice(len(df_with_outliers), size=10, replace=False)
    df_with_outliers.loc[outlier_indices, 'income'] = np.random.uniform(300000, 500000, 10)
    
    # Add extreme age outliers
    outlier_indices = np.random.choice(len(df_with_outliers), size=5, replace=False)
    df_with_outliers.loc[outlier_indices, 'age'] = np.random.randint(90, 100, 5)
    
    return df_with_outliers

def generate_dataset():
    """Main function to generate the complete dataset"""
    
    print("Generating customer dataset...")
    df = generate_customer_dataset(1000)
    df = add_time_based_features(df)
    df = add_missing_values(df, missing_rate=0.03)
    df = add_outliers(df)
    
    # Save to CSV
    df.to_csv('customer_dataset.csv', index=False)
    
    print(f"Dataset generated with {len(df)} rows and {len(df.columns)} columns")
    print("\nDataset info:")
    print(df.info())
    print("\nFirst few rows:")
    print(df.head())
    print(f"\nDataset saved as 'customer_dataset.csv'")
    
    return df

if __name__ == "__main__":
    df = generate_dataset()