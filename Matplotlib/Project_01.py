import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import sys
import io

# Set UTF-8 encoding for console output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Set style for better visualizations
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# ============================================
# 1. CREATE SAMPLE DATASET
# ============================================
def create_sample_data():
    """Create a sample dataset for analysis"""
    np.random.seed(42)
    
    # Generate dates
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(365)]
    
    # Generate data
    n = len(dates)
    
    # Sales data with trend and seasonality
    trend = np.linspace(100, 300, n)
    seasonal = 50 * np.sin(2 * np.pi * np.arange(n) / 30)  # Monthly seasonality
    noise = np.random.normal(0, 20, n)
    sales = trend + seasonal + noise
    sales = np.maximum(sales, 0)  # No negative sales
    
    # Other metrics
    customers = np.random.poisson(50, n) + np.random.randint(0, 30, n)
    marketing_spend = np.random.uniform(500, 2000, n)
    
    # Product categories
    categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Toys']
    category = np.random.choice(categories, n, p=[0.3, 0.25, 0.2, 0.15, 0.1])
    
    # Create DataFrame
    df = pd.DataFrame({
        'date': dates,
        'sales': sales,
        'customers': customers,
        'marketing_spend': marketing_spend,
        'category': category
    })
    
    # Add derived columns
    df['month'] = df['date'].dt.month
    df['quarter'] = df['date'].dt.quarter
    df['day_of_week'] = df['date'].dt.day_name()
    df['is_weekend'] = df['day_of_week'].isin(['Saturday', 'Sunday'])
    
    return df

# ============================================
# 2. DATA EXPLORATION AND CLEANING
# ============================================
def explore_data(df):
    """Perform initial data exploration"""
    print("=" * 60)
    print("DATA EXPLORATION")
    print("=" * 60)
    
    # Basic info
    print("\n[INFO] Dataset Info:")
    print(df.info())
    
    print("\n[INFO] Summary Statistics:")
    print(df.describe())
    
    print("\n[INFO] Missing Values:")
    print(df.isnull().sum())
    
    print("\n[INFO] Data Types:")
    print(df.dtypes)
    
    return df

# ============================================
# 3. DATA CLEANING
# ============================================
def clean_data(df):
    """Clean the dataset"""
    print("\n" + "=" * 60)
    print("DATA CLEANING")
    print("=" * 60)
    
    # Check for duplicates
    duplicates = df.duplicated().sum()
    print(f"Duplicate rows: {duplicates}")
    
    # Handle missing values (if any)
    if df.isnull().sum().sum() > 0:
        print("Filling missing values...")
        # Fill numeric columns with median
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            df[col].fillna(df[col].median(), inplace=True)
        
        # Fill categorical with mode
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            df[col].fillna(df[col].mode()[0], inplace=True)
    
    print("[OK] Data cleaning complete!")
    return df

# ============================================
# 4. DATA ANALYSIS
# ============================================
def analyze_data(df):
    """Perform detailed data analysis"""
    print("\n" + "=" * 60)
    print("DATA ANALYSIS")
    print("=" * 60)
    
    # 4.1 Sales Analysis by Category
    print("\n[ANALYSIS] Sales by Category:")
    category_stats = df.groupby('category').agg({
        'sales': ['mean', 'sum', 'std', 'count']
    }).round(2)
    print(category_stats)
    
    # 4.2 Time-based Analysis
    print("\n[ANALYSIS] Monthly Sales Analysis:")
    monthly_sales = df.groupby('month')['sales'].agg(['mean', 'sum']).round(2)
    print(monthly_sales)
    
    # 4.3 Correlation Analysis
    print("\n[ANALYSIS] Correlation Matrix:")
    numeric_cols = ['sales', 'customers', 'marketing_spend']
    correlation = df[numeric_cols].corr()
    print(correlation.round(3))
    
    # 4.4 Weekend vs Weekday Analysis
    print("\n[ANALYSIS] Weekend vs Weekday Sales:")
    weekend_stats = df.groupby('is_weekend')['sales'].agg(['mean', 'median', 'std']).round(2)
    print(weekend_stats)
    
    return category_stats, monthly_sales, correlation

# ============================================
# 5. VISUALIZATIONS
# ============================================
def create_visualizations(df):
    """Create various visualizations"""
    print("\n" + "=" * 60)
    print("CREATING VISUALIZATIONS")
    print("=" * 60)
    
    # Create figure with subplots
    fig = plt.figure(figsize=(16, 12))
    
    # 1. Time Series Plot
    ax1 = plt.subplot(3, 2, 1)
    ax1.plot(df['date'], df['sales'], linewidth=1, alpha=0.7, color='blue')
    ax1.set_title('Sales Trend Over Time', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Sales')
    ax1.grid(True, alpha=0.3)
    
    # 2. Sales by Category (Boxplot)
    ax2 = plt.subplot(3, 2, 2)
    df.boxplot(column='sales', by='category', ax=ax2)
    ax2.set_title('Sales Distribution by Category', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Category')
    ax2.set_ylabel('Sales')
    ax2.grid(True, alpha=0.3)
    
    # 3. Histogram of Sales
    ax3 = plt.subplot(3, 2, 3)
    ax3.hist(df['sales'], bins=30, edgecolor='black', alpha=0.7, color='green')
    ax3.axvline(df['sales'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["sales"].mean():.2f}')
    ax3.axvline(df['sales'].median(), color='orange', linestyle='--', linewidth=2, label=f'Median: {df["sales"].median():.2f}')
    ax3.set_title('Sales Distribution', fontsize=12, fontweight='bold')
    ax3.set_xlabel('Sales')
    ax3.set_ylabel('Frequency')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # 4. Correlation Heatmap
    ax4 = plt.subplot(3, 2, 4)
    numeric_cols = ['sales', 'customers', 'marketing_spend']
    corr_matrix = df[numeric_cols].corr()
    im = ax4.imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1)
    ax4.set_xticks(range(len(numeric_cols)))
    ax4.set_yticks(range(len(numeric_cols)))
    ax4.set_xticklabels(numeric_cols)
    ax4.set_yticklabels(numeric_cols)
    ax4.set_title('Correlation Matrix', fontsize=12, fontweight='bold')
    
    # Add correlation values to heatmap
    for i in range(len(numeric_cols)):
        for j in range(len(numeric_cols)):
            text = ax4.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                           ha="center", va="center", color="black", fontweight='bold')
    
    plt.colorbar(im, ax=ax4)
    
    # 5. Monthly Sales Bar Chart
    ax5 = plt.subplot(3, 2, 5)
    monthly_sales = df.groupby('month')['sales'].mean()
    ax5.bar(monthly_sales.index, monthly_sales.values, color='skyblue', edgecolor='black')
    ax5.set_title('Average Monthly Sales', fontsize=12, fontweight='bold')
    ax5.set_xlabel('Month')
    ax5.set_ylabel('Average Sales')
    ax5.grid(True, alpha=0.3, axis='y')
    
    # 6. Scatter Plot: Marketing Spend vs Sales
    ax6 = plt.subplot(3, 2, 6)
    scatter = ax6.scatter(df['marketing_spend'], df['sales'], 
                         c=df['customers'], cmap='viridis', alpha=0.6, s=50)
    ax6.set_title('Marketing Spend vs Sales (Color: Customers)', fontsize=12, fontweight='bold')
    ax6.set_xlabel('Marketing Spend')
    ax6.set_ylabel('Sales')
    plt.colorbar(scatter, ax=ax6, label='Number of Customers')
    ax6.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('data_analysis_visualizations.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("[OK] Visualizations saved as 'data_analysis_visualizations.png'")

# ============================================
# 6. ADVANCED ANALYSIS
# ============================================
def advanced_analysis(df):
    """Perform advanced analysis"""
    print("\n" + "=" * 60)
    print("ADVANCED ANALYSIS")
    print("=" * 60)
    
    # 6.1 Rolling Statistics (Moving Average)
    df['sales_ma_7'] = df['sales'].rolling(window=7).mean()
    df['sales_ma_30'] = df['sales'].rolling(window=30).mean()
    
    # 6.2 Growth Rate
    df['sales_growth'] = df['sales'].pct_change() * 100
    
    # 6.3 Cumulative Sales
    df['cumulative_sales'] = df['sales'].cumsum()
    
    # 6.4 Customer Efficiency (Sales per Customer)
    df['sales_per_customer'] = df['sales'] / df['customers']
    
    # 6.5 ROI Analysis
    df['marketing_roi'] = (df['sales'] / df['marketing_spend']) * 100
    
    # 6.6 Category Performance (using pivot table)
    pivot_table = pd.pivot_table(df, 
                                 values='sales', 
                                 index='month', 
                                 columns='category', 
                                 aggfunc='mean')
    
    print("\n[ANALYSIS] Category Performance by Month (Average Sales):")
    print(pivot_table.round(2))
    
    # 6.7 Statistical Tests
    from scipy import stats
    
    # Test if weekend sales differ from weekday sales
    weekend_sales = df[df['is_weekend']]['sales']
    weekday_sales = df[~df['is_weekend']]['sales']
    t_stat, p_value = stats.ttest_ind(weekend_sales, weekday_sales)
    
    print(f"\n[ANALYSIS] Weekend vs Weekday Sales T-Test:")
    print(f"T-statistic: {t_stat:.4f}")
    print(f"P-value: {p_value:.4f}")
    print(f"Significant difference: {'Yes' if p_value < 0.05 else 'No'}")
    
    return df, pivot_table

# ============================================
# 7. GENERATE REPORT
# ============================================
def generate_report(df, pivot_table):
    """Generate summary report"""
    print("\n" + "=" * 60)
    print("SUMMARY REPORT")
    print("=" * 60)
    
    report = f"""
    DATA ANALYSIS SUMMARY REPORT
    ================================
    
    Dataset Overview:
    - Total Records: {len(df)}
    - Date Range: {df['date'].min()} to {df['date'].max()}
    - Total Sales: ${df['sales'].sum():,.2f}
    - Average Sales: ${df['sales'].mean():,.2f}
    - Median Sales: ${df['sales'].median():,.2f}
    - Max Sales: ${df['sales'].max():,.2f}
    - Min Sales: ${df['sales'].min():,.2f}
    
    Customer Metrics:
    - Total Customers: {df['customers'].sum():,}
    - Average Customers per Day: {df['customers'].mean():.2f}
    - Sales per Customer (Avg): ${df['sales_per_customer'].mean():.2f}
    
    Marketing Metrics:
    - Total Marketing Spend: ${df['marketing_spend'].sum():,.2f}
    - Average Marketing ROI: {df['marketing_roi'].mean():.2f}%
    
    Category Performance:
    {df.groupby('category')['sales'].agg(['mean', 'sum']).round(2)}
    
    Best Performing Months:
    {df.groupby('month')['sales'].mean().sort_values(ascending=False).head(3)}
    
    Worst Performing Months:
    {df.groupby('month')['sales'].mean().sort_values(ascending=True).head(3)}
    """
    
    print(report)
    
    # Save report to file with UTF-8 encoding
    try:
        with open('analysis_report.txt', 'w', encoding='utf-8') as f:
            f.write(report)
        print("[OK] Report saved as 'analysis_report.txt'")
    except Exception as e:
        # Fallback to ASCII-only report if UTF-8 fails
        print(f"Warning: Could not save with UTF-8 encoding. Trying ASCII...")
        try:
            with open('analysis_report.txt', 'w', encoding='ascii', errors='ignore') as f:
                f.write(report)
            print("[OK] Report saved as 'analysis_report.txt' (ASCII only)")
        except:
            print("[ERROR] Could not save report file")

# ============================================
# MAIN EXECUTION
# ============================================
def main():
    """Main function to run the complete analysis"""
    print("Starting Data Analysis Program...")
    print("=" * 60)
    
    # Step 1: Create data
    print("\n[INFO] Creating sample dataset...")
    df = create_sample_data()
    print(f"[OK] Dataset created with {len(df)} records")
    
    # Step 2: Explore data
    df = explore_data(df)
    
    # Step 3: Clean data
    df = clean_data(df)
    
    # Step 4: Analyze data
    category_stats, monthly_sales, correlation = analyze_data(df)
    
    # Step 5: Advanced analysis
    df, pivot_table = advanced_analysis(df)
    
    # Step 6: Create visualizations
    create_visualizations(df)
    
    # Step 7: Generate report
    generate_report(df, pivot_table)
    
    print("\n" + "=" * 60)
    print("[OK] Analysis Complete!")
    print("Files generated:")
    print("   - data_analysis_visualizations.png")
    print("   - analysis_report.txt")
    print("=" * 60)

# ============================================
# RUN THE PROGRAM
# ============================================
if __name__ == "__main__":
    main()