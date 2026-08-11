# src/retail_analysis.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from datetime import datetime
import os
import warnings
warnings.filterwarnings('ignore')

# Set matplotlib style
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

class RetailAnalytics:
    def __init__(self, data_path="../data/raw_retail_transactions.csv"):
        """Initialize the Retail Analytics system with raw data."""
        self.data_path = data_path
        self.df = None
        self.cleaned_df = None
        self.customer_df = None
        self.initial_shape = None
        self.setup_directories()
        
    def setup_directories(self):
        """Create necessary directories."""
        os.makedirs("../data", exist_ok=True)
        os.makedirs("../visualizations", exist_ok=True)
        
    def load_data(self):
        """Load the raw retail transactions data."""
        self.df = pd.read_csv(self.data_path)
        self.initial_shape = self.df.shape
        print("Data loaded successfully.")
        print(f"Shape: {self.df.shape}")
        return self.df
    
    def data_quality_audit(self):
        """Perform comprehensive data quality audit."""
        print("\n" + "="*50)
        print("DATA QUALITY AUDIT")
        print("="*50)
        
        # Basic information
        print("\n1. BASIC INFORMATION")
        print("-" * 40)
        print(f"Number of rows: {len(self.df)}")
        print(f"Number of columns: {len(self.df.columns)}")
        print(f"Column names: {list(self.df.columns)}")
        print(f"Data types:")
        print(self.df.dtypes)
        
        # Missing values
        print("\n2. MISSING VALUES")
        print("-" * 40)
        missing = self.df.isnull().sum()
        missing_percent = (missing / len(self.df)) * 100
        missing_df = pd.DataFrame({
            'Missing Count': missing,
            'Missing Percentage': missing_percent
        })
        missing_df = missing_df[missing_df['Missing Count'] > 0]
        if len(missing_df) > 0:
            print(missing_df)
        else:
            print("No missing values found.")
        
        # Unique values
        print("\n3. UNIQUE VALUES")
        print("-" * 40)
        print(f"Unique customers: {self.df['customer_id'].nunique()}")
        print(f"Unique products: {self.df['product'].nunique()}")
        print(f"Unique categories: {self.df['category'].nunique()}")
        print(f"Unique regions: {self.df['region'].nunique()}")
        
        # Duplicates
        print("\n4. DUPLICATE ANALYSIS")
        print("-" * 40)
        duplicate_rows = self.df.duplicated().sum()
        duplicate_percent = (duplicate_rows / len(self.df)) * 100
        print(f"Duplicate rows: {duplicate_rows}")
        print(f"Duplicate percentage: {duplicate_percent:.2f}%")
        
        # Check transaction_id duplicates
        transaction_dupes = self.df['transaction_id'].duplicated().sum()
        print(f"Duplicate transaction_ids: {transaction_dupes}")
        
        # Numerical columns analysis
        print("\n5. NUMERICAL COLUMN STATISTICS")
        print("-" * 40)
        numerical_cols = ['quantity', 'unit_price', 'discount', 'revenue', 
                         'customer_age', 'rating', 'shipping_cost']
        
        for col in numerical_cols:
            if col in self.df.columns:
                print(f"\n{col.upper()}:")
                print(f"  min: {self.df[col].min():.2f}")
                print(f"  max: {self.df[col].max():.2f}")
                print(f"  mean: {self.df[col].mean():.2f}")
                print(f"  median: {self.df[col].median():.2f}")
                print(f"  std: {self.df[col].std():.2f}")
        
        # Invalid values
        print("\n6. INVALID VALUES")
        print("-" * 40)
        invalid_checks = {
            'quantity <= 0': self.df['quantity'] <= 0,
            'discount < 0': self.df['discount'] < 0,
            'discount > 1': self.df['discount'] > 1,
            'customer_age < 18': self.df['customer_age'] < 18,
            'customer_age > 100': self.df['customer_age'] > 100,
            'rating < 1': self.df['rating'] < 1,
            'rating > 5': self.df['rating'] > 5,
            'unit_price <= 0': self.df['unit_price'] <= 0,
            'revenue <= 0': self.df['revenue'] <= 0
        }
        
        for check, condition in invalid_checks.items():
            count = condition.sum()
            if count > 0:
                print(f"{check}: {count} records")
        
        return missing_df
    
    def clean_data(self):
        """Clean the dataset with documented reasoning."""
        print("\n" + "="*50)
        print("DATA CLEANING PROCESS")
        print("="*50)
        
        df = self.df.copy()
        
        # 1. Remove true duplicate rows
        print("\n1. Removing duplicate rows...")
        before_dupes = df.duplicated().sum()
        df = df.drop_duplicates()
        after_dupes = df.duplicated().sum()
        print(f"  Removed {before_dupes} duplicate rows")
        print(f"  Remaining duplicates: {after_dupes}")
        
        # 2. Standardize region names
        print("\n2. Standardizing region names...")
        df['region'] = df['region'].str.strip().str.title()
        df['region'] = df['region'].replace({
            'South': 'South',
            'North': 'North', 
            'East': 'East',
            'West': 'West'
        })
        print(f"  Unique regions: {df['region'].unique()}")
        
        # 3. Handle invalid values
        print("\n3. Handling invalid values...")
        
        # Quantity: set negative values to NaN
        invalid_qty = df['quantity'] <= 0
        df.loc[invalid_qty, 'quantity'] = np.nan
        print(f"  Set {invalid_qty.sum()} invalid quantity values to NaN")
        
        # Discount: clip to [0, 1] range
        invalid_discount = (df['discount'] < 0) | (df['discount'] > 1)
        df.loc[df['discount'] < 0, 'discount'] = 0
        df.loc[df['discount'] > 1, 'discount'] = 1
        print(f"  Clipped {invalid_discount.sum()} discount values to [0,1] range")
        
        # Customer age: set invalid ages to NaN
        invalid_age = (df['customer_age'] < 18) | (df['customer_age'] > 100)
        df.loc[invalid_age, 'customer_age'] = np.nan
        print(f"  Set {invalid_age.sum()} invalid age values to NaN")
        
        # Rating: clip to [1, 5] range
        invalid_rating = (df['rating'] < 1) | (df['rating'] > 5)
        df['rating'] = df['rating'].clip(1, 5)
        print(f"  Clipped {invalid_rating.sum()} rating values to [1,5] range")
        
        # Unit price: remove extreme outliers (20x normal)
        price_issues = df['unit_price'] > df['unit_price'].quantile(0.99)
        df.loc[price_issues, 'unit_price'] = np.nan
        print(f"  Set {price_issues.sum()} extreme unit price values to NaN")
        
        # 4. Handle missing values
        print("\n4. Handling missing values...")
        
        # Categorical: use mode
        for col in ['region', 'payment_method']:
            if df[col].isnull().any():
                mode_val = df[col].mode()[0]
                df[col] = df[col].fillna(mode_val)
                print(f"  Filled {col} missing values with mode: {mode_val}")
        
        # Numerical: use median
        for col in ['customer_age', 'rating', 'shipping_cost']:
            if df[col].isnull().any():
                median_val = df[col].median()
                df[col] = df[col].fillna(median_val)
                print(f"  Filled {col} missing values with median: {median_val:.2f}")
        
        # 5. Recalculate revenue
        print("\n5. Recalculating revenue...")
        df['calculated_revenue'] = df['quantity'] * df['unit_price'] * (1 - df['discount'])
        
        # Compare original vs calculated
        df['revenue_difference'] = df['revenue'] - df['calculated_revenue']
        mismatches = np.abs(df['revenue_difference']) > 0.01
        
        print(f"  Revenue mismatches: {mismatches.sum()}")
        print(f"  Max difference: {df['revenue_difference'].max():.2f}")
        print(f"  Mean difference: {df['revenue_difference'].mean():.2f}")
        
        # Use calculated revenue where original is NaN or mismatch is significant
        df['revenue'] = np.where(
            (mismatches) | (df['revenue'].isnull()),
            df['calculated_revenue'],
            df['revenue']
        )
        
        # Clean up
        df = df.drop(['calculated_revenue', 'revenue_difference'], axis=1)
        
        self.cleaned_df = df
        
        print("\n" + "="*50)
        print("DATA CLEANING COMPLETE")
        print("="*50)
        print(f"Initial rows: {len(self.df)}")
        print(f"Final rows: {len(df)}")
        print(f"Rows removed: {len(self.df) - len(df)}")
        
        return df
    
    def feature_engineering(self):
        """Create new features from existing data."""
        print("\n" + "="*50)
        print("FEATURE ENGINEERING")
        print("="*50)
        
        df = self.cleaned_df.copy()
        
        # Date features
        df['order_date'] = pd.to_datetime(df['order_date'])
        df['year'] = df['order_date'].dt.year
        df['month'] = df['order_date'].dt.month
        df['month_name'] = df['order_date'].dt.month_name()
        df['day_of_week'] = df['order_date'].dt.day_name()
        df['quarter'] = df['order_date'].dt.quarter
        df['year_week'] = df['order_date'].dt.isocalendar().week
        
        # Financial features
        df['gross_revenue'] = df['quantity'] * df['unit_price']
        df['discount_amount'] = df['gross_revenue'] * df['discount']
        
        # Profit-like metric (assuming 40% cost of goods sold)
        # This is a simplified assumption for analytical purposes
        df['estimated_profit'] = df['revenue'] * 0.4
        
        print("Created features:")
        new_features = ['year', 'month', 'month_name', 'day_of_week', 
                       'quarter', 'gross_revenue', 'discount_amount', 
                       'estimated_profit']
        for feature in new_features:
            print(f"  - {feature}")
        
        self.cleaned_df = df
        return df
    
    def sales_analysis(self):
        """Perform comprehensive sales analysis."""
        print("\n" + "="*50)
        print("SALES ANALYSIS")
        print("="*50)
        
        df = self.cleaned_df
        
        # Overall metrics
        print("\n1. OVERALL METRICS")
        print("-" * 40)
        total_revenue = df['revenue'].sum()
        avg_transaction = df['revenue'].mean()
        median_transaction = df['revenue'].median()
        total_units = df['quantity'].sum()
        avg_quantity = df['quantity'].mean()
        
        print(f"Total Revenue: ${total_revenue:,.2f}")
        print(f"Average Transaction Revenue: ${avg_transaction:,.2f}")
        print(f"Median Transaction Revenue: ${median_transaction:,.2f}")
        print(f"Total Units Sold: {total_units:,.0f}")
        print(f"Average Quantity per Transaction: {avg_quantity:.2f}")
        
        # Product analysis
        print("\n2. PRODUCT ANALYSIS")
        print("-" * 40)
        product_metrics = df.groupby('product').agg({
            'quantity': 'sum',
            'revenue': 'sum',
            'unit_price': 'mean',
            'discount': 'mean',
            'rating': 'mean',
            'transaction_id': 'count'
        }).reset_index()
        product_metrics.columns = ['product', 'total_quantity', 'total_revenue', 
                                  'avg_price', 'avg_discount', 'avg_rating', 'transaction_count']
        
        best_selling = product_metrics.loc[product_metrics['total_quantity'].idxmax()]
        highest_revenue = product_metrics.loc[product_metrics['total_revenue'].idxmax()]
        lowest_revenue = product_metrics.loc[product_metrics['total_revenue'].idxmin()]
        
        print(f"Best-selling product: {best_selling['product']} ({best_selling['total_quantity']:,.0f} units)")
        print(f"Highest revenue product: {highest_revenue['product']} (${highest_revenue['total_revenue']:,.2f})")
        print(f"Lowest revenue product: {lowest_revenue['product']} (${lowest_revenue['total_revenue']:,.2f})")
        
        # Category analysis
        print("\n3. CATEGORY ANALYSIS")
        print("-" * 40)
        category_metrics = df.groupby('category').agg({
            'revenue': 'sum',
            'quantity': 'sum',
            'transaction_id': 'count'
        }).reset_index()
        category_metrics['avg_transaction'] = category_metrics['revenue'] / category_metrics['transaction_id']
        
        for _, row in category_metrics.iterrows():
            print(f"{row['category']}:")
            print(f"  Revenue: ${row['revenue']:,.2f}")
            print(f"  Quantity: {row['quantity']:,.0f}")
            print(f"  Avg Transaction: ${row['avg_transaction']:,.2f}")
        
        # Region analysis
        print("\n4. REGION ANALYSIS")
        print("-" * 40)
        region_metrics = df.groupby('region').agg({
            'revenue': 'sum',
            'quantity': 'sum',
            'transaction_id': 'count'
        }).reset_index()
        region_metrics['avg_transaction'] = region_metrics['revenue'] / region_metrics['transaction_id']
        
        for _, row in region_metrics.iterrows():
            print(f"{row['region']}:")
            print(f"  Revenue: ${row['revenue']:,.2f}")
            print(f"  Quantity: {row['quantity']:,.0f}")
            print(f"  Avg Transaction: ${row['avg_transaction']:,.2f}")
        
        return {
            'product_metrics': product_metrics,
            'category_metrics': category_metrics,
            'region_metrics': region_metrics,
            'overall': {
                'total_revenue': total_revenue,
                'avg_transaction': avg_transaction,
                'median_transaction': median_transaction,
                'total_units': total_units,
                'avg_quantity': avg_quantity
            }
        }
    
    def monthly_analysis(self):
        """Analyze monthly sales trends."""
        print("\n" + "="*50)
        print("MONTHLY SALES ANALYSIS")
        print("="*50)
        
        df = self.cleaned_df
        
        monthly = df.groupby(['year', 'month']).agg({
            'revenue': 'sum',
            'quantity': 'sum',
            'transaction_id': 'count'
        }).reset_index()
        
        # Highest/Lowest months
        highest_revenue = monthly.loc[monthly['revenue'].idxmax()]
        lowest_revenue = monthly.loc[monthly['revenue'].idxmin()]
        highest_volume = monthly.loc[monthly['quantity'].idxmax()]
        lowest_volume = monthly.loc[monthly['quantity'].idxmin()]
        
        highest_year = int(highest_revenue['year'])
        highest_month = int(highest_revenue['month'])
        lowest_year = int(lowest_revenue['year'])
        lowest_month = int(lowest_revenue['month'])
        highest_volume_year = int(highest_volume['year'])
        highest_volume_month = int(highest_volume['month'])
        lowest_volume_year = int(lowest_volume['year'])
        lowest_volume_month = int(lowest_volume['month'])
        
        print(f"Highest revenue month: {highest_year}-{highest_month:02d} (${highest_revenue['revenue']:,.2f})")
        print(f"Lowest revenue month: {lowest_year}-{lowest_month:02d} (${lowest_revenue['revenue']:,.2f})")
        print(f"Highest volume month: {highest_volume_year}-{highest_volume_month:02d} ({highest_volume['quantity']:,.0f} units)")
        print(f"Lowest volume month: {lowest_volume_year}-{lowest_volume_month:02d} ({lowest_volume['quantity']:,.0f} units)")
        
        # Year-over-year growth
        revenue_2024 = monthly[monthly['year'] == 2024]['revenue'].sum()
        revenue_2025 = monthly[monthly['year'] == 2025]['revenue'].sum()
        
        if revenue_2024 > 0:
            yoy_growth = ((revenue_2025 - revenue_2024) / revenue_2024) * 100
            print(f"\nYear-over-Year Revenue Growth:")
            print(f"  2024 Revenue: ${revenue_2024:,.2f}")
            print(f"  2025 Revenue: ${revenue_2025:,.2f}")
            print(f"  Growth: {yoy_growth:.2f}%")
        
        return monthly
    
    def customer_analysis(self):
        """Perform customer-level analytics and segmentation."""
        print("\n" + "="*50)
        print("CUSTOMER ANALYTICS")
        print("="*50)
        
        df = self.cleaned_df
        
        # Customer-level metrics
        customer_metrics = df.groupby('customer_id').agg({
            'transaction_id': 'count',
            'quantity': 'sum',
            'revenue': 'sum',
            'discount': 'mean',
            'rating': 'mean'
        }).reset_index()
        customer_metrics.columns = ['customer_id', 'total_orders', 'total_quantity', 
                                   'total_revenue', 'avg_discount', 'avg_rating']
        customer_metrics['avg_order_value'] = customer_metrics['total_revenue'] / customer_metrics['total_orders']
        
        self.customer_df = customer_metrics
        
        # Top customers
        top_revenue = customer_metrics.nlargest(10, 'total_revenue')
        top_orders = customer_metrics.nlargest(10, 'total_orders')
        top_quantity = customer_metrics.nlargest(10, 'total_quantity')
        
        print("\n1. TOP 10 CUSTOMERS BY REVENUE")
        print("-" * 40)
        for _, row in top_revenue.iterrows():
            print(f"Customer {row['customer_id']}: ${row['total_revenue']:,.2f} ({row['total_orders']} orders)")
        
        print("\n2. TOP 10 CUSTOMERS BY ORDER COUNT")
        print("-" * 40)
        for _, row in top_orders.iterrows():
            print(f"Customer {row['customer_id']}: {row['total_orders']} orders (${row['total_revenue']:,.2f})")
        
        print("\n3. TOP 10 CUSTOMERS BY QUANTITY PURCHASED")
        print("-" * 40)
        for _, row in top_quantity.iterrows():
            print(f"Customer {row['customer_id']}: {row['total_quantity']:,.0f} units (${row['total_revenue']:,.2f})")
        
        # Customer segmentation
        print("\n4. CUSTOMER SEGMENTATION")
        print("-" * 40)
        
        # Inspect distribution
        q1 = customer_metrics['total_revenue'].quantile(0.25)
        median = customer_metrics['total_revenue'].quantile(0.50)
        q3 = customer_metrics['total_revenue'].quantile(0.75)
        
        print(f"Revenue Distribution:")
        print(f"  Q1: ${q1:,.2f}")
        print(f"  Median: ${median:,.2f}")
        print(f"  Q3: ${q3:,.2f}")
        
        # Define segments based on actual distribution
        def segment_customer(revenue):
            if revenue > q3 * 2:
                return 'VIP'
            elif revenue > q3:
                return 'High Value'
            elif revenue > median:
                return 'Regular'
            else:
                return 'Low Value'
        
        customer_metrics['segment'] = customer_metrics['total_revenue'].apply(segment_customer)
        
        segment_metrics = customer_metrics.groupby('segment').agg({
            'customer_id': 'count',
            'total_revenue': 'mean',
            'avg_order_value': 'mean',
            'total_quantity': 'mean',
            'avg_discount': 'mean',
            'total_orders': 'mean'
        }).reset_index()
        
        print("\nSegment Metrics:")
        for _, row in segment_metrics.iterrows():
            print(f"\n{row['segment']}:")
            print(f"  Customers: {row['customer_id']}")
            print(f"  Avg Revenue: ${row['total_revenue']:,.2f}")
            print(f"  Avg Order Value: ${row['avg_order_value']:,.2f}")
            print(f"  Avg Quantity: {row['total_quantity']:.1f}")
            print(f"  Avg Orders: {row['total_orders']:.1f}")
        
        # Customer retention analysis
        print("\n5. CUSTOMER RETENTION ANALYSIS")
        print("-" * 40)
        
        # Merge customer_type back from original data
        customer_types = df.groupby('customer_id')['customer_type'].first().reset_index()
        customer_metrics = customer_metrics.merge(customer_types, on='customer_id', how='left')
        
        type_metrics = customer_metrics.groupby('customer_type').agg({
            'total_revenue': 'mean',
            'avg_order_value': 'mean',
            'total_quantity': 'mean',
            'avg_discount': 'mean',
            'total_orders': 'mean'
        }).reset_index()
        
        print("Customer Type Metrics:")
        for _, row in type_metrics.iterrows():
            print(f"\n{row['customer_type']}:")
            print(f"  Avg Revenue: ${row['total_revenue']:,.2f}")
            print(f"  Avg Order Value: ${row['avg_order_value']:,.2f}")
            print(f"  Avg Quantity: {row['total_quantity']:.1f}")
            print(f"  Avg Orders: {row['total_orders']:.1f}")
        
        self.customer_df = customer_metrics
        return customer_metrics
    
    def discount_analysis(self):
        """Analyze discount effectiveness."""
        print("\n" + "="*50)
        print("DISCOUNT ANALYSIS")
        print("="*50)
        
        df = self.cleaned_df
        
        # Create discount groups
        df['discount_group'] = pd.cut(df['discount'], 
                                      bins=[0, 0.05, 0.10, 0.20, 0.30, 1.0],
                                      labels=['0-5%', '5-10%', '10-20%', '20-30%', '30%+'])
        
        discount_metrics = df.groupby('discount_group').agg({
            'revenue': 'mean',
            'quantity': 'mean',
            'transaction_id': 'count'
        }).reset_index()
        discount_metrics.columns = ['discount_group', 'avg_revenue', 'avg_quantity', 'transaction_count']
        
        print("Discount Group Analysis:")
        print("-" * 40)
        for _, row in discount_metrics.iterrows():
            print(f"{row['discount_group']}:")
            print(f"  Avg Revenue: ${row['avg_revenue']:,.2f}")
            print(f"  Avg Quantity: {row['avg_quantity']:.2f}")
            print(f"  Transactions: {row['transaction_count']}")
        
        # Correlation analysis
        correlation = df[['discount', 'revenue', 'quantity']].corr()
        print("\nCorrelation Analysis:")
        print(f"  Discount vs Revenue: {correlation.loc['discount', 'revenue']:.3f}")
        print(f"  Discount vs Quantity: {correlation.loc['discount', 'quantity']:.3f}")
        
        return discount_metrics
    
    def product_performance(self):
        """Product performance ranking with custom scoring."""
        print("\n" + "="*50)
        print("PRODUCT PERFORMANCE RANKING")
        print("="*50)
        
        df = self.cleaned_df
        
        # Product metrics
        product_metrics = df.groupby('product').agg({
            'revenue': 'sum',
            'quantity': 'sum',
            'unit_price': 'mean',
            'discount': 'mean',
            'rating': 'mean',
            'transaction_id': 'count'
        }).reset_index()
        product_metrics.columns = ['product', 'total_revenue', 'total_quantity', 
                                  'avg_price', 'avg_discount', 'avg_rating', 'transaction_count']
        
        # Normalize metrics for scoring
        product_metrics['revenue_score'] = product_metrics['total_revenue'] / product_metrics['total_revenue'].max()
        product_metrics['quantity_score'] = product_metrics['total_quantity'] / product_metrics['total_quantity'].max()
        product_metrics['rating_score'] = product_metrics['avg_rating'] / 5  # Max rating is 5
        
        # Weighted score
        weights = {'revenue': 0.5, 'quantity': 0.3, 'rating': 0.2}
        product_metrics['performance_score'] = (
            weights['revenue'] * product_metrics['revenue_score'] +
            weights['quantity'] * product_metrics['quantity_score'] +
            weights['rating'] * product_metrics['rating_score']
        )
        
        # Sort by score
        product_metrics = product_metrics.sort_values('performance_score', ascending=False)
        
        print("Product Performance Ranking:")
        print("-" * 80)
        print(f"{'Product':<15} {'Revenue':>12} {'Units':>10} {'Rating':>8} {'Score':>8}")
        print("-" * 80)
        for _, row in product_metrics.head(10).iterrows():
            print(f"{row['product']:<15} ${row['total_revenue']:>10,.0f} {row['total_quantity']:>10,.0f} {row['avg_rating']:>8.2f} {row['performance_score']:>8.3f}")
        
        return product_metrics
    
    def outlier_detection(self):
        """Detect outliers using IQR method."""
        print("\n" + "="*50)
        print("OUTLIER DETECTION (IQR Method)")
        print("="*50)
        
        df = self.cleaned_df
        
        columns = ['revenue', 'unit_price', 'quantity', 'discount', 'customer_age']
        
        outlier_results = {}
        
        for col in columns:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            
            outliers = (df[col] < lower_bound) | (df[col] > upper_bound)
            outlier_count = outliers.sum()
            outlier_percent = (outlier_count / len(df)) * 100
            
            print(f"\n{col.upper()}:")
            print(f"  Q1: {q1:.2f}")
            print(f"  Q3: {q3:.2f}")
            print(f"  IQR: {iqr:.2f}")
            print(f"  Lower Bound: {lower_bound:.2f}")
            print(f"  Upper Bound: {upper_bound:.2f}")
            print(f"  Outliers: {outlier_count} ({outlier_percent:.2f}%)")
            
            outlier_results[col] = {
                'q1': q1,
                'q3': q3,
                'iqr': iqr,
                'lower_bound': lower_bound,
                'upper_bound': upper_bound,
                'outlier_count': outlier_count,
                'outlier_percent': outlier_percent
            }
        
        # Largest revenue transactions
        print("\nLargest Revenue Transactions (Potential High-Value Sales):")
        print("-" * 40)
        top_revenue = df.nlargest(10, 'revenue')[['transaction_id', 'product', 'revenue', 'quantity', 'unit_price']]
        print(top_revenue)
        
        return outlier_results
    
    def numpy_analysis(self):
        """Perform NumPy-based statistical analysis."""
        print("\n" + "="*50)
        print("NUMPY STATISTICAL ANALYSIS")
        print("="*50)
        
        revenue = self.cleaned_df['revenue'].values
        
        mean = np.mean(revenue)
        median = np.median(revenue)
        std = np.std(revenue)
        variance = np.var(revenue)
        percentiles = np.percentile(revenue, [25, 50, 75, 90, 95, 99])
        
        print("Revenue Statistics:")
        print(f"  Mean: ${mean:,.2f}")
        print(f"  Median: ${median:,.2f}")
        print(f"  Standard Deviation: ${std:,.2f}")
        print(f"  Variance: ${variance:,.2f}")
        print(f"  Percentiles:")
        print(f"    25th: ${percentiles[0]:,.2f}")
        print(f"    50th: ${percentiles[1]:,.2f}")
        print(f"    75th: ${percentiles[2]:,.2f}")
        print(f"    90th: ${percentiles[3]:,.2f}")
        print(f"    95th: ${percentiles[4]:,.2f}")
        print(f"    99th: ${percentiles[5]:,.2f}")
        
        # 95th percentile - separates top 5%
        print(f"\n95th Percentile Revenue: ${percentiles[4]:,.2f}")
        print(f"This means {sum(revenue > percentiles[4])} transactions (5%) exceed this value.")
        
        return {
            'mean': mean,
            'median': median,
            'std': std,
            'variance': variance,
            'percentiles': percentiles
        }
    
    def create_visualizations(self):
        """Create comprehensive visualizations."""
        print("\n" + "="*50)
        print("CREATING VISUALIZATIONS")
        print("="*50)
        
        df = self.cleaned_df
        
        # Create dashboard
        fig = plt.figure(figsize=(20, 16))
        fig.suptitle('Retail Sales Performance Dashboard', fontsize=24, fontweight='bold', y=0.98)
        
        gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3)
        
        # 1. Monthly Revenue
        ax1 = fig.add_subplot(gs[0, 0])
        monthly = df.groupby(['year', 'month'])['revenue'].sum().reset_index()
        monthly['date'] = pd.to_datetime(monthly['year'].astype(str) + '-' + monthly['month'].astype(str))
        monthly = monthly.sort_values('date')
        ax1.plot(monthly['date'], monthly['revenue'], marker='o', linewidth=2, color='#2E86AB')
        ax1.set_title('Monthly Revenue', fontweight='bold')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Revenue ($)')
        ax1.tick_params(axis='x', rotation=45)
        
        # 2. Revenue by Product
        ax2 = fig.add_subplot(gs[0, 1])
        product_revenue = df.groupby('product')['revenue'].sum().sort_values(ascending=True)
        colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(product_revenue)))
        ax2.barh(product_revenue.index, product_revenue.values, color=colors)
        ax2.set_title('Revenue by Product', fontweight='bold')
        ax2.set_xlabel('Revenue ($)')
        
        # 3. Revenue by Region
        ax3 = fig.add_subplot(gs[0, 2])
        region_revenue = df.groupby('region')['revenue'].sum()
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
        ax3.pie(region_revenue.values, labels=region_revenue.index, autopct='%1.1f%%', 
                colors=colors, startangle=90)
        ax3.set_title('Revenue by Region', fontweight='bold')
        
        # 4. Revenue Distribution
        ax4 = fig.add_subplot(gs[1, 0])
        ax4.hist(df['revenue'], bins=50, color='#2E86AB', alpha=0.7, edgecolor='black')
        ax4.axvline(df['revenue'].mean(), color='red', linestyle='--', label=f'Mean: ${df["revenue"].mean():,.0f}')
        ax4.axvline(df['revenue'].median(), color='green', linestyle='--', label=f'Median: ${df["revenue"].median():,.0f}')
        ax4.set_title('Revenue Distribution', fontweight='bold')
        ax4.set_xlabel('Revenue ($)')
        ax4.set_ylabel('Frequency')
        ax4.legend()
        
        # 5. Revenue vs Quantity
        ax5 = fig.add_subplot(gs[1, 1])
        sample = df.sample(min(1000, len(df)))
        ax5.scatter(sample['quantity'], sample['revenue'], alpha=0.5, color='#2E86AB')
        ax5.set_title('Revenue vs Quantity', fontweight='bold')
        ax5.set_xlabel('Quantity')
        ax5.set_ylabel('Revenue ($)')
        
        # 6. Discount vs Revenue
        ax6 = fig.add_subplot(gs[1, 2])
        sample = df.sample(min(1000, len(df)))
        ax6.scatter(sample['discount'], sample['revenue'], alpha=0.5, color='#FF6B6B')
        ax6.set_title('Discount vs Revenue', fontweight='bold')
        ax6.set_xlabel('Discount Rate')
        ax6.set_ylabel('Revenue ($)')
        
        # 7. Customer Revenue Distribution
        ax7 = fig.add_subplot(gs[2, 0])
        customer_revenue = df.groupby('customer_id')['revenue'].sum()
        ax7.hist(customer_revenue, bins=50, color='#4ECDC4', alpha=0.7, edgecolor='black')
        ax7.axvline(customer_revenue.mean(), color='red', linestyle='--', 
                   label=f'Mean: ${customer_revenue.mean():,.0f}')
        ax7.set_title('Customer Revenue Distribution', fontweight='bold')
        ax7.set_xlabel('Total Revenue ($)')
        ax7.set_ylabel('Number of Customers')
        ax7.legend()
        
        # 8. Top 10 Customers
        ax8 = fig.add_subplot(gs[2, 1])
        top_customers = customer_revenue.nlargest(10)
        colors = plt.cm.Greens(np.linspace(0.4, 0.9, len(top_customers)))
        ax8.barh([f'Customer {c}' for c in top_customers.index], top_customers.values, color=colors)
        ax8.set_title('Top 10 Customers by Revenue', fontweight='bold')
        ax8.set_xlabel('Revenue ($)')
        
        # 9. Correlation Matrix
        ax9 = fig.add_subplot(gs[2, 2])
        numerical_cols = ['quantity', 'unit_price', 'discount', 'revenue', 
                         'customer_age', 'rating', 'shipping_cost']
        corr_matrix = df[numerical_cols].corr()
        im = ax9.imshow(corr_matrix, cmap='RdBu', vmin=-1, vmax=1)
        ax9.set_xticks(range(len(numerical_cols)))
        ax9.set_yticks(range(len(numerical_cols)))
        ax9.set_xticklabels(numerical_cols, rotation=45, ha='right')
        ax9.set_yticklabels(numerical_cols)
        ax9.set_title('Correlation Matrix', fontweight='bold')
        
        # Add colorbar
        plt.colorbar(im, ax=ax9, shrink=0.8)
        
        plt.tight_layout()
        plt.savefig('../visualizations/retail_sales_dashboard.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        print("Dashboard saved to visualizations/retail_sales_dashboard.png")
        
        # Individual plots
        self.create_individual_plots()
        
    def create_individual_plots(self):
        """Create individual visualization plots."""
        df = self.cleaned_df
        
        # 1. Monthly Revenue Line Chart
        plt.figure(figsize=(12, 6))
        monthly = df.groupby(['year', 'month'])['revenue'].sum().reset_index()
        monthly['date'] = pd.to_datetime(monthly['year'].astype(str) + '-' + monthly['month'].astype(str))
        monthly = monthly.sort_values('date')
        plt.plot(monthly['date'], monthly['revenue'], marker='o', linewidth=2, color='#2E86AB')
        plt.title('Monthly Revenue Trend', fontsize=16, fontweight='bold')
        plt.xlabel('Date')
        plt.ylabel('Revenue ($)')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('../visualizations/monthly_revenue.png', dpi=300)
        plt.close()
        
        # 2. Revenue by Product Bar Chart
        plt.figure(figsize=(12, 6))
        product_revenue = df.groupby('product')['revenue'].sum().sort_values()
        colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(product_revenue)))
        plt.barh(product_revenue.index, product_revenue.values, color=colors)
        plt.title('Revenue by Product', fontsize=16, fontweight='bold')
        plt.xlabel('Revenue ($)')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('../visualizations/revenue_by_product.png', dpi=300)
        plt.close()
        
        # 3. Revenue by Category
        plt.figure(figsize=(12, 6))
        category_revenue = df.groupby('category')['revenue'].sum()
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
        plt.bar(category_revenue.index, category_revenue.values, color=colors)
        plt.title('Revenue by Category', fontsize=16, fontweight='bold')
        plt.xlabel('Category')
        plt.ylabel('Revenue ($)')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('../visualizations/revenue_by_category.png', dpi=300)
        plt.close()
        
        # 4. Revenue Distribution Histogram
        plt.figure(figsize=(12, 6))
        plt.hist(df['revenue'], bins=50, color='#2E86AB', alpha=0.7, edgecolor='black')
        plt.axvline(df['revenue'].mean(), color='red', linestyle='--', 
                   label=f'Mean: ${df["revenue"].mean():,.0f}')
        plt.axvline(df['revenue'].median(), color='green', linestyle='--', 
                   label=f'Median: ${df["revenue"].median():,.0f}')
        plt.title('Revenue Distribution', fontsize=16, fontweight='bold')
        plt.xlabel('Revenue ($)')
        plt.ylabel('Frequency')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('../visualizations/revenue_distribution.png', dpi=300)
        plt.close()
        
        print("Individual plots saved to visualizations/")
    
    def quality_summary(self):
        """Generate data quality summary before and after cleaning."""
        print("\n" + "="*50)
        print("DATA QUALITY SUMMARY")
        print("="*50)
        
        original = self.df
        cleaned = self.cleaned_df
        
        # Before cleaning
        print("\nBEFORE CLEANING")
        print("-" * 40)
        print(f"Rows: {len(original)}")
        print(f"Missing Values: {original.isnull().sum().sum()}")
        print(f"Duplicates: {original.duplicated().sum()}")
        
        invalid_before = 0
        invalid_before += (original['quantity'] <= 0).sum()
        invalid_before += ((original['discount'] < 0) | (original['discount'] > 1)).sum()
        invalid_before += ((original['customer_age'] < 18) | (original['customer_age'] > 100)).sum()
        invalid_before += ((original['rating'] < 1) | (original['rating'] > 5)).sum()
        invalid_before += (original['unit_price'] <= 0).sum()
        print(f"Invalid Values: {invalid_before}")
        
        # After cleaning
        print("\nAFTER CLEANING")
        print("-" * 40)
        print(f"Rows: {len(cleaned)}")
        print(f"Missing Values: {cleaned.isnull().sum().sum()}")
        print(f"Duplicates: {cleaned.duplicated().sum()}")
        
        invalid_after = 0
        invalid_after += (cleaned['quantity'] <= 0).sum()
        invalid_after += ((cleaned['discount'] < 0) | (cleaned['discount'] > 1)).sum()
        invalid_after += ((cleaned['customer_age'] < 18) | (cleaned['customer_age'] > 100)).sum()
        invalid_after += ((cleaned['rating'] < 1) | (cleaned['rating'] > 5)).sum()
        invalid_after += (cleaned['unit_price'] <= 0).sum()
        print(f"Invalid Values: {invalid_after}")
        
        # Improvement
        print("\nIMPROVEMENT")
        print("-" * 40)
        improvement = len(original) - len(cleaned)
        print(f"Rows removed: {improvement}")
        missing_reduction = original.isnull().sum().sum() - cleaned.isnull().sum().sum()
        print(f"Missing values fixed: {missing_reduction}")
        invalid_reduction = invalid_before - invalid_after
        print(f"Invalid values fixed: {invalid_reduction}")
    
    def generate_report(self):
        """Generate the final business report."""
        print("\n" + "="*50)
        print("RETAIL BUSINESS ANALYSIS REPORT")
        print("="*50)
        
        df = self.cleaned_df
        
        # Overall metrics
        total_transactions = len(df)
        total_customers = df['customer_id'].nunique()
        total_revenue = df['revenue'].sum()
        avg_order_value = df['revenue'].mean()
        total_units = df['quantity'].sum()
        
        print(f"\nTotal Transactions: {total_transactions:,}")
        print(f"Total Customers: {total_customers:,}")
        print(f"Total Revenue: ${total_revenue:,.2f}")
        print(f"Average Order Value: ${avg_order_value:,.2f}")
        print(f"Total Units Sold: {total_units:,.0f}")
        
        # Product metrics
        product_revenue = df.groupby('product')['revenue'].sum()
        product_quantity = df.groupby('product')['quantity'].sum()
        
        best_selling = product_quantity.idxmax()
        highest_revenue = product_revenue.idxmax()
        
        print(f"\nBest Selling Product: {best_selling}")
        print(f"Highest Revenue Product: {highest_revenue}")
        
        # Category metrics
        category_revenue = df.groupby('category')['revenue'].sum()
        best_category = category_revenue.idxmax()
        
        print(f"Best Performing Category: {best_category}")
        
        # Region metrics
        region_revenue = df.groupby('region')['revenue'].sum()
        best_region = region_revenue.idxmax()
        
        print(f"Best Performing Region: {best_region}")
        
        # Monthly metrics
        monthly = df.groupby(['year', 'month'])['revenue'].sum()
        highest_month = monthly.idxmax()
        lowest_month = monthly.idxmin()
        
        print(f"\nHighest Revenue Month: {highest_month[0]}-{highest_month[1]:02d}")
        print(f"Lowest Revenue Month: {lowest_month[0]}-{lowest_month[1]:02d}")
        
        # Customer metrics
        customer_revenue = df.groupby('customer_id')['revenue'].sum()
        top_customer = customer_revenue.idxmax()
        
        print(f"\nTop Customer: {top_customer}")
        
        # 95th percentile
        revenue_95th = np.percentile(df['revenue'], 95)
        print(f"\n95th Percentile Revenue: ${revenue_95th:,.2f}")
        
        # High-value customers
        high_value_count = len(customer_revenue[customer_revenue > df['revenue'].mean()])
        print(f"High-Value Customers (above average): {high_value_count}")
        
        # KEY FINDINGS
        print("\n" + "="*50)
        print("KEY FINDINGS")
        print("="*50)
        
        findings = []
        
        # Revenue concentration
        top_20_percent_revenue = customer_revenue.nlargest(int(len(customer_revenue) * 0.2)).sum()
        revenue_concentration = (top_20_percent_revenue / total_revenue) * 100
        findings.append(f"Top 20% of customers generate {revenue_concentration:.1f}% of total revenue")
        
        # Product performance
        top_product_revenue_pct = (product_revenue.max() / total_revenue) * 100
        findings.append(f"{highest_revenue} is the top product, contributing {top_product_revenue_pct:.1f}% of revenue")
        
        # Region performance
        best_region_pct = (region_revenue.max() / total_revenue) * 100
        findings.append(f"{best_region} region performs best, contributing {best_region_pct:.1f}% of revenue")
        
        # Discount impact
        discount_corr = df['discount'].corr(df['revenue'])
        if discount_corr > 0:
            findings.append(f"Discounts show a positive correlation (r={discount_corr:.2f}) with revenue")
        else:
            findings.append(f"Discounts show a negative correlation (r={discount_corr:.2f}) with revenue")
        
        # Monthly trend
        monthly_trend = df.groupby('month')['revenue'].mean()
        peak_month = monthly_trend.idxmax()
        findings.append(f"Month {peak_month} shows the highest average sales")
        
        for i, finding in enumerate(findings, 1):
            print(f"{i}. {finding}")
        
        # RECOMMENDATIONS
        print("\n" + "="*50)
        print("RECOMMENDATIONS")
        print("="*50)
        
        recommendations = []
        
        # Customer targeting
        recommendations.append(
            "Focus marketing efforts on high-value customers (top 20%) who generate "
            "the majority of revenue through personalized loyalty programs"
        )
        
        # Product focus
        recommendations.append(
            f"Leverage {highest_revenue} as the flagship product, and consider "
            "bundling it with complementary products to increase average order value"
        )
        
        # Regional strategy
        recommendations.append(
            f"Expand successful strategies from the {best_region} region to other "
            "regions, particularly focusing on the top-selling products there"
        )
        
        # Discount optimization
        if discount_corr > 0:
            recommendations.append(
                "Strategic discounts (10-20%) show positive impact on revenue. "
                "Consider targeted promotions for high-value products during peak seasons"
            )
        else:
            recommendations.append(
                "Current discount strategy may not be effective. Consider reducing "
                "discounts or targeting them more precisely to high-margin products"
            )
        
        # Monthly strategy
        recommendations.append(
            f"Intensify marketing and promotional activities in month {peak_month} "
            "to capitalize on peak sales periods"
        )
        
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")
    
    def save_cleaned_data(self):
        """Save cleaned datasets."""
        self.cleaned_df.to_csv('../data/cleaned_retail_transactions.csv', index=False)
        if self.customer_df is not None:
            self.customer_df.to_csv('../data/customer_summary.csv', index=False)
        
        print("\nCleaned data saved to:")
        print("  - data/cleaned_retail_transactions.csv")
        print("  - data/customer_summary.csv")
    
    def run_analysis(self):
        """Execute the complete analysis pipeline."""
        print("\n" + "="*60)
        print("RETAIL ANALYTICS SYSTEM")
        print("="*60)
        
        # Step 1: Load data
        print("\nStep 1: Loading Data")
        self.load_data()
        
        # Step 2: Data quality audit
        print("\nStep 2: Data Quality Audit")
        self.data_quality_audit()
        
        # Step 3: Clean data
        print("\nStep 3: Data Cleaning")
        self.clean_data()
        
        # Step 4: Feature engineering
        print("\nStep 4: Feature Engineering")
        self.feature_engineering()
        
        # Step 5: Sales analysis
        print("\nStep 5: Sales Analysis")
        self.sales_analysis()
        
        # Step 6: Monthly analysis
        print("\nStep 6: Monthly Analysis")
        self.monthly_analysis()
        
        # Step 7: Customer analysis
        print("\nStep 7: Customer Analysis")
        self.customer_analysis()
        
        # Step 8: Discount analysis
        print("\nStep 8: Discount Analysis")
        self.discount_analysis()
        
        # Step 9: Product performance
        print("\nStep 9: Product Performance")
        self.product_performance()
        
        # Step 10: Outlier detection
        print("\nStep 10: Outlier Detection")
        self.outlier_detection()
        
        # Step 11: NumPy analysis
        print("\nStep 11: NumPy Analysis")
        self.numpy_analysis()
        
        # Step 12: Visualizations
        print("\nStep 12: Creating Visualizations")
        self.create_visualizations()
        
        # Step 13: Quality summary
        print("\nStep 13: Quality Summary")
        self.quality_summary()
        
        # Step 14: Save data
        print("\nStep 14: Saving Data")
        self.save_cleaned_data()
        
        # Step 15: Generate report
        print("\nStep 15: Generating Report")
        self.generate_report()
        
        print("\n" + "="*60)
        print("ANALYSIS COMPLETE!")
        print("="*60)


# Main execution
if __name__ == "__main__":
    # Generate the data first
    print("Generating retail data...")
    import generate_data
    generate_data.generate_retail_data()
    
    # Run analysis
    analytics = RetailAnalytics()
    analytics.run_analysis()