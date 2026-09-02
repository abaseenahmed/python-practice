import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(123)
random.seed(123)

def generate_employee_dataset(n_samples=2000):
    """
    Generate a synthetic employee dataset for attrition and performance analysis
    """
    
    # Employee IDs
    employee_ids = range(1001, 1001 + n_samples)
    
    # Age distribution
    ages = np.random.normal(35, 10, n_samples).astype(int)
    ages = np.clip(ages, 22, 65)
    
    # Gender
    genders = np.random.choice(['Male', 'Female', 'Non-Binary'], n_samples, p=[0.47, 0.48, 0.05])
    
    # Department
    departments = np.random.choice(
        ['Sales', 'Marketing', 'Engineering', 'HR', 'Finance', 'Operations', 'IT'], 
        n_samples,
        p=[0.15, 0.12, 0.25, 0.08, 0.12, 0.18, 0.10]
    )
    
    # Job role within department
    job_roles = np.random.choice(
        ['Manager', 'Senior', 'Junior', 'Intern', 'Lead', 'Executive'],
        n_samples,
        p=[0.15, 0.25, 0.30, 0.05, 0.15, 0.10]
    )
    
    # Years at company
    years_at_company = np.random.exponential(scale=5, size=n_samples)
    years_at_company = np.clip(years_at_company, 0.5, 25).round(1)
    
    # Years in current role
    years_in_role = np.random.exponential(scale=3, size=n_samples)
    years_in_role = np.clip(years_in_role, 0.1, 15).round(1)
    years_in_role = np.minimum(years_in_role, years_at_company)
    
    # Monthly salary (correlated with age and years)
    salary_base = 3000 + ages * 50 + years_at_company * 200
    salary = np.random.normal(salary_base, 500, n_samples)
    salary = np.clip(salary, 2500, 15000).round(2)
    
    # Performance rating (1-5)
    performance = np.random.normal(3.5, 0.7, n_samples)
    performance = np.clip(performance, 1, 5).round(1)
    
    # Work-life balance rating (1-4)
    work_life_balance = np.random.choice([1, 2, 3, 4], n_samples, p=[0.10, 0.25, 0.40, 0.25])
    
    # Job satisfaction (1-5)
    job_satisfaction = np.random.normal(3.3, 0.8, n_samples)
    job_satisfaction = np.clip(job_satisfaction, 1, 5).round(1)
    
    # Environment satisfaction (1-5)
    env_satisfaction = np.random.normal(3.5, 0.7, n_samples)
    env_satisfaction = np.clip(env_satisfaction, 1, 5).round(1)
    
    # Relationship satisfaction (1-5)
    relationship_satisfaction = np.random.normal(3.7, 0.6, n_samples)
    relationship_satisfaction = np.clip(relationship_satisfaction, 1, 5).round(1)
    
    # Overtime (binary)
    overtime = np.random.binomial(1, 0.35, n_samples)
    
    # Number of companies worked before
    companies_worked = np.random.poisson(2, n_samples)
    companies_worked = np.clip(companies_worked, 0, 8)
    
    # Distance from home (km)
    distance_from_home = np.random.exponential(scale=15, size=n_samples)
    distance_from_home = np.clip(distance_from_home, 1, 80).round(1)
    
    # Training hours
    training_hours = np.random.normal(60, 20, n_samples)
    training_hours = np.clip(training_hours, 10, 120).astype(int)
    
    # Promotion status (binary)
    promotion = np.random.binomial(1, 0.15, n_samples)
    
    # Attrition status (correlated with satisfaction, overtime, salary)
    attrition_prob = 0.05 + (1 - job_satisfaction/5) * 0.3 + overtime * 0.15 + (salary/15000) * 0.1
    attrition_prob = np.clip(attrition_prob, 0.05, 0.85)
    attrition = np.random.binomial(1, attrition_prob, n_samples)
    
    # Remote work status
    remote_work = np.random.choice(['Remote', 'Hybrid', 'Onsite'], n_samples, p=[0.20, 0.35, 0.45])
    
    # Education level
    education = np.random.choice(
        ['High School', 'Bachelor', 'Master', 'PhD'],
        n_samples,
        p=[0.15, 0.45, 0.30, 0.10]
    )
    
    # Marital status
    marital_status = np.random.choice(
        ['Single', 'Married', 'Divorced'],
        n_samples,
        p=[0.35, 0.55, 0.10]
    )
    
    # Create DataFrame
    df = pd.DataFrame({
        'employee_id': employee_ids,
        'age': ages,
        'gender': genders,
        'department': departments,
        'job_role': job_roles,
        'years_at_company': years_at_company,
        'years_in_current_role': years_in_role,
        'monthly_salary': salary,
        'performance_rating': performance,
        'work_life_balance': work_life_balance,
        'job_satisfaction': job_satisfaction,
        'environment_satisfaction': env_satisfaction,
        'relationship_satisfaction': relationship_satisfaction,
        'overtime': overtime,
        'companies_worked_before': companies_worked,
        'distance_from_home': distance_from_home,
        'training_hours': training_hours,
        'promotion': promotion,
        'attrition': attrition,
        'remote_work': remote_work,
        'education': education,
        'marital_status': marital_status
    })
    
    return df

def add_time_based_features(df):
    """Add time-based features to the dataset"""
    
    # Hire dates (within last 10 years)
    today = datetime.now()
    days_range = np.random.randint(30, 3650, size=len(df))
    hire_dates = [today - timedelta(days=int(x)) for x in days_range]
    df['hire_date'] = hire_dates
    
    # Last promotion date
    promotion_days = np.random.exponential(scale=500, size=len(df))
    promotion_days = np.clip(promotion_days, 0, 2000).astype(int)
    last_promotion = [today - timedelta(days=int(x)) for x in promotion_days]
    df['last_promotion_date'] = last_promotion
    
    # Quarter of hire
    df['hire_quarter'] = df['hire_date'].apply(
        lambda x: 'Q1' if x.month in [1, 2, 3]
        else 'Q2' if x.month in [4, 5, 6]
        else 'Q3' if x.month in [7, 8, 9]
        else 'Q4'
    )
    
    # Days since last promotion
    df['days_since_promotion'] = (today - df['last_promotion_date']).dt.days
    
    # Tenure category
    df['tenure_category'] = pd.cut(df['years_at_company'], 
                                   bins=[0, 1, 3, 5, 10, 25],
                                   labels=['<1 year', '1-3 years', '3-5 years', '5-10 years', '>10 years'])
    
    return df

def add_correlations_and_outliers(df):
    """Add correlations between features and outliers"""
    
    # Create correlation: Performance increases with training hours
    df['performance_rating'] = df['performance_rating'] + (df['training_hours'] - 60) * 0.005
    df['performance_rating'] = np.clip(df['performance_rating'], 1, 5).round(1)
    
    # Create correlation: Salary increases with performance
    df['monthly_salary'] = df['monthly_salary'] + (df['performance_rating'] - 3) * 200
    df['monthly_salary'] = np.clip(df['monthly_salary'], 2500, 16000).round(2)
    
    # Add outliers
    outlier_indices = np.random.choice(len(df), size=15, replace=False)
    df.loc[outlier_indices, 'monthly_salary'] = np.random.uniform(18000, 25000, 15)
    
    outlier_indices = np.random.choice(len(df), size=10, replace=False)
    df.loc[outlier_indices, 'age'] = np.random.randint(18, 22, 10)
    
    outlier_indices = np.random.choice(len(df), size=8, replace=False)
    df.loc[outlier_indices, 'performance_rating'] = np.random.uniform(0.5, 1.5, 8)
    
    outlier_indices = np.random.choice(len(df), size=12, replace=False)
    df.loc[outlier_indices, 'training_hours'] = np.random.randint(150, 200, 12)
    
    return df

def add_missing_values(df, missing_rate=0.04):
    """Add missing values to the dataset"""
    
    df_with_missing = df.copy()
    
    columns_to_corrupt = ['monthly_salary', 'performance_rating', 'job_satisfaction', 
                         'work_life_balance', 'education', 'marital_status']
    
    for col in columns_to_corrupt:
        mask = np.random.random(len(df_with_missing)) < missing_rate
        df_with_missing.loc[mask, col] = np.nan
    
    return df_with_missing

def generate_dataset():
    """Main function to generate the complete dataset"""
    
    print("Generating employee attrition dataset...")
    df = generate_employee_dataset(2000)
    df = add_time_based_features(df)
    df = add_correlations_and_outliers(df)
    df = add_missing_values(df, missing_rate=0.04)
    
    # Save to CSV
    df.to_csv('employee_attrition_dataset.csv', index=False)
    
    print(f"Dataset generated with {len(df)} rows and {len(df.columns)} columns")
    print("\nDataset info:")
    print(df.info())
    print("\nFirst few rows:")
    print(df.head())
    print("\nAttrition distribution:")
    print(df['attrition'].value_counts(normalize=True) * 100)
    print(f"\nDataset saved as 'employee_attrition_dataset.csv'")
    
    return df

if __name__ == "__main__":
    df = generate_dataset()