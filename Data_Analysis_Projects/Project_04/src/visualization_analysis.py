# ================================= Project 04 - Professional Edition ======================================== #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set professional style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

class VisualAnalytics:
    def __init__(self, data_path='../data/ecommerce_customers.csv'):
        """
        Initialize the VisualAnalytics class with data path
        
        Parameters:
        data_path: str - Path to the CSV file (default: '../data/ecommerce_customers.csv')
        """
        self.data_path = data_path
        self.df = None
        self.seperator = '-'*100
        
        # Set professional plotting style
        sns.set_theme(style="whitegrid")
        plt.rcParams['figure.figsize'] = (12, 7)
        plt.rcParams['font.size'] = 11
        plt.rcParams['axes.titlesize'] = 14
        plt.rcParams['axes.labelsize'] = 12
        plt.rcParams['xtick.labelsize'] = 10
        plt.rcParams['ytick.labelsize'] = 10
        
        # Professional color palette
        self.colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#6A994E',
                       '#BC4B51', '#5D576B', '#F4B942', '#3D5A80', '#EE6C4D']
        
    def load_data(self):
        """Load the dataset from CSV file"""
        try:
            self.df = pd.read_csv(self.data_path)
            print("✅ Data loaded successfully.")
            print(f"📊 Shape: {self.df.shape}")
            print(self.seperator)
            return self.df
        except FileNotFoundError:
            print("❌ Error: Data file not found!")
            print("Please ensure the data file exists at:", self.data_path)
            print("Creating sample data for demonstration...")
            self.create_sample_data()
            return self.df

    def create_sample_data(self):
        """Create sample data if file doesn't exist"""
        print("📝 Generating sample data...")
        np.random.seed(42)
        n = 1000
        
        # Generate sample data
        dates = pd.date_range("2024-01-01", "2024-12-31", freq="D")
        self.df = pd.DataFrame({
            'order_id': [f'ORD{i:06d}' for i in range(1, n+1)],
            'order_date': np.random.choice(dates, n),
            'customer_id': np.random.randint(1000, 2000, n),
            'age': np.random.randint(18, 75, n),
            'gender': np.random.choice(['Male', 'Female'], n),
            'city': np.random.choice(['Karachi', 'Lahore', 'Islamabad', 'Faisalabad'], n),
            'region': np.random.choice(['North', 'South', 'East', 'West'], n),
            'category': np.random.choice(['Electronics', 'Clothing', 'Accessories'], n),
            'product': np.random.choice(['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Shoes'], n),
            'unit_price': np.random.uniform(50, 500, n),
            'quantity': np.random.randint(1, 5, n),
            'discount': np.random.choice([0, 0.05, 0.10, 0.15, 0.20], n),
            'payment_method': np.random.choice(['Credit Card', 'Debit Card', 'Cash'], n),
            'customer_type': np.random.choice(['New', 'Returning', 'VIP'], n),
            'rating': np.random.uniform(3, 5, n),
            'revenue': np.random.uniform(50, 1000, n)
        })
        print("✅ Sample data created successfully!")
        print(f"📊 Shape: {self.df.shape}")
        print(self.seperator)

    def data_exploration(self):
        """Comprehensive data exploration and summary statistics"""
        print("\n" + "="*100)
        print("📊 DATA EXPLORATION & ANALYSIS")
        print("="*100)
        
        print("\n📋 FIRST 5 ROWS:")
        print(self.df.head())
        
        print(f"\n📐 DATASET SHAPE: {self.df.shape}")
        
        print("\n📂 COLUMN INFORMATION:")
        print(f"Columns: {list(self.df.columns)}")
        
        print("\n📊 DATA TYPES:")
        print(self.df.dtypes)
        
        print("\n📈 SUMMARY STATISTICS:")
        print(self.df.describe())
        
        print("\n🔍 MISSING VALUES:")
        missing = self.df.isnull().sum()
        missing_percent = (missing / len(self.df)) * 100
        missing_df = pd.DataFrame({'Missing Count': missing, 'Percentage': missing_percent})
        print(missing_df[missing_df['Missing Count'] > 0])
        
        print("\n🔄 UNIQUE VALUES:")
        print(self.df.nunique())
        
        print("\n" + self.seperator)

    def data_preparation(self):
        """Data preparation and feature engineering"""
        print("\n🛠️ DATA PREPARATION & FEATURE ENGINEERING")
        print("="*100)
        
        # Convert date column
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])
        
        # Extract time-based features
        self.df['year'] = self.df['order_date'].dt.year
        self.df['month'] = self.df['order_date'].dt.month
        self.df['month_name'] = self.df['order_date'].dt.month_name()
        self.df['day_of_week'] = self.df['order_date'].dt.dayofweek
        self.df['day_name'] = self.df['order_date'].dt.day_name()
        self.df['quarter'] = self.df['order_date'].dt.quarter
        
        # Calculate additional metrics
        self.df['discount_amount'] = self.df['unit_price'] * self.df['quantity'] * self.df['discount']
        self.df['revenue_per_item'] = self.df['revenue'] / self.df['quantity']
        
        # Customer segmentation
        customer_avg = self.df.groupby('customer_id')['revenue'].mean()
        self.df['customer_segment'] = self.df['customer_id'].map(
            lambda x: 'High Value' if customer_avg.get(x, 0) > 500 
            else 'Medium Value' if customer_avg.get(x, 0) > 200 
            else 'Low Value'
        )
        
        print("✅ Feature engineering completed!")
        print(f"📊 Total columns: {len(self.df.columns)}")
        print(f"📋 First 5 rows with new features:")
        print(self.df.head())
        print(self.seperator)

    def visualize_time_series(self):
        """Professional Time Series Analysis Visualizations"""
        print("\n📈 TIME SERIES ANALYSIS")
        print("="*100)
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # 1. Monthly Revenue Trend
        monthly_revenue = self.df.groupby('month')['revenue'].sum()
        ax1 = axes[0, 0]
        ax1.plot(monthly_revenue.index, monthly_revenue.values, 
                marker='o', linewidth=2.5, markersize=8, 
                color=self.colors[0], label='Monthly Revenue')
        ax1.set_title('Monthly Revenue Trend', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Month')
        ax1.set_ylabel('Total Revenue ($)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Revenue by Day of Week
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_revenue = self.df.groupby('day_name')['revenue'].sum().reindex(day_order)
        ax2 = axes[0, 1]
        colors = [self.colors[5] if day in ['Saturday', 'Sunday'] else self.colors[0] for day in day_revenue.index]
        ax2.bar(day_revenue.index, day_revenue.values, color=colors, edgecolor='black', linewidth=0.5)
        ax2.set_title('Revenue by Day of Week', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Day')
        ax2.set_ylabel('Revenue ($)')
        ax2.tick_params(axis='x', rotation=45)
        ax2.grid(True, alpha=0.3, axis='y')
        
        # 3. Average Order Value by Month
        monthly_aov = self.df.groupby('month')['revenue'].mean()
        ax3 = axes[1, 0]
        ax3.bar(monthly_aov.index, monthly_aov.values, color=self.colors[1], edgecolor='black', linewidth=0.5)
        ax3.set_title('Average Order Value by Month', fontsize=14, fontweight='bold')
        ax3.set_xlabel('Month')
        ax3.set_ylabel('Average Revenue ($)')
        ax3.grid(True, alpha=0.3, axis='y')
        
        # 4. Order Volume by Day
        day_orders = self.df.groupby('day_name')['order_id'].count().reindex(day_order)
        ax4 = axes[1, 1]
        ax4.barh(day_orders.index, day_orders.values, color=self.colors[2], edgecolor='black', linewidth=0.5)
        ax4.set_title('Order Volume by Day', fontsize=14, fontweight='bold')
        ax4.set_xlabel('Number of Orders')
        ax4.set_ylabel('Day')
        ax4.grid(True, alpha=0.3, axis='x')
        
        plt.suptitle('Time Series & Temporal Analysis', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()

    def visualize_products(self):
        """Professional Product & Category Analysis"""
        print("\n🏷️ PRODUCT & CATEGORY ANALYSIS")
        print("="*100)
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # 1. Top Products by Revenue
        top_products = self.df.groupby('product')['revenue'].sum().sort_values(ascending=True).tail(8)
        ax1 = axes[0, 0]
        ax1.barh(top_products.index, top_products.values, color=self.colors[:len(top_products)])
        ax1.set_title('Top Products by Revenue', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Revenue ($)')
        ax1.set_ylabel('Product')
        ax1.grid(True, alpha=0.3, axis='x')
        
        # 2. Category Performance
        category_perf = self.df.groupby('category')['revenue'].agg(['sum', 'mean'])
        ax2 = axes[0, 1]
        x = np.arange(len(category_perf))
        width = 0.35
        ax2.bar(x - width/2, category_perf['sum'], width, label='Total Revenue', color=self.colors[0])
        ax2.bar(x + width/2, category_perf['mean'], width, label='Avg Revenue', color=self.colors[1])
        ax2.set_title('Category Performance', fontsize=14, fontweight='bold')
        ax2.set_xticks(x)
        ax2.set_xticklabels(category_perf.index)
        ax2.set_ylabel('Revenue ($)')
        ax2.legend()
        ax2.grid(True, alpha=0.3, axis='y')
        
        # 3. Category Distribution
        category_counts = self.df['category'].value_counts()
        ax3 = axes[1, 0]
        ax3.pie(category_counts.values, labels=category_counts.index, 
                autopct='%1.1f%%', colors=self.colors[:3], startangle=90)
        ax3.set_title('Category Distribution', fontsize=14, fontweight='bold')
        
        # 4. Discount Impact
        discount_impact = self.df.groupby('discount')['revenue'].sum()
        ax4 = axes[1, 1]
        ax4.bar(discount_impact.index.astype(str), discount_impact.values, 
                color=self.colors[3], edgecolor='black', linewidth=0.5)
        ax4.set_title('Discount Impact on Revenue', fontsize=14, fontweight='bold')
        ax4.set_xlabel('Discount Rate')
        ax4.set_ylabel('Total Revenue ($)')
        ax4.grid(True, alpha=0.3, axis='y')
        
        plt.suptitle('Product & Category Analysis', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()

    def visualize_customers(self):
        """Professional Customer & Demographic Analysis"""
        print("\n👥 CUSTOMER & DEMOGRAPHIC ANALYSIS")
        print("="*100)
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # 1. Age Distribution
        ax1 = axes[0, 0]
        ax1.hist(self.df['age'].dropna(), bins=20, color=self.colors[0], alpha=0.7, edgecolor='black')
        ax1.axvline(self.df['age'].mean(), color='red', linestyle='--', label=f'Mean: {self.df["age"].mean():.1f}')
        ax1.set_title('Age Distribution of Customers', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Age')
        ax1.set_ylabel('Count')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Gender Distribution
        gender_counts = self.df['gender'].value_counts()
        ax2 = axes[0, 1]
        ax2.pie(gender_counts.values, labels=gender_counts.index, 
                autopct='%1.1f%%', colors=self.colors[:2], startangle=90)
        ax2.set_title('Gender Distribution', fontsize=14, fontweight='bold')
        
        # 3. Customer Type Analysis
        customer_type = self.df.groupby('customer_type')['revenue'].agg(['sum', 'mean'])
        ax3 = axes[1, 0]
        x = np.arange(len(customer_type))
        width = 0.35
        ax3.bar(x - width/2, customer_type['sum'], width, label='Total Revenue', color=self.colors[0])
        ax3.bar(x + width/2, customer_type['mean'], width, label='Avg Revenue', color=self.colors[1])
        ax3.set_title('Customer Type Performance', fontsize=14, fontweight='bold')
        ax3.set_xticks(x)
        ax3.set_xticklabels(customer_type.index)
        ax3.set_ylabel('Revenue ($)')
        ax3.legend()
        ax3.grid(True, alpha=0.3, axis='y')
        
        # 4. Age vs Revenue Relationship
        age_revenue = self.df.groupby('age')['revenue'].mean()
        ax4 = axes[1, 1]
        ax4.scatter(age_revenue.index, age_revenue.values, 
                   s=80, alpha=0.7, color=self.colors[2])
        ax4.plot(age_revenue.index, age_revenue.rolling(window=5, center=True).mean(), 
                color='red', linewidth=2, label='Trend')
        ax4.set_title('Age vs Revenue Relationship', fontsize=14, fontweight='bold')
        ax4.set_xlabel('Age')
        ax4.set_ylabel('Average Revenue ($)')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.suptitle('Customer & Demographic Analysis', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()

    def visualize_statistics(self):
        """Professional Statistical Analysis Visualizations"""
        print("\n📊 STATISTICAL ANALYSIS")
        print("="*100)
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # 1. Revenue Distribution
        ax1 = axes[0, 0]
        sns.histplot(data=self.df, x='revenue', kde=True, color=self.colors[0], ax=ax1, bins=30)
        ax1.axvline(self.df['revenue'].mean(), color='red', linestyle='--', 
                   label=f"Mean: ${self.df['revenue'].mean():.2f}")
        ax1.set_title('Revenue Distribution', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Revenue ($)')
        ax1.set_ylabel('Frequency')
        ax1.legend()
        
        # 2. Correlation Heatmap
        ax2 = axes[0, 1]
        numerical_cols = ['age', 'unit_price', 'quantity', 'discount', 'rating', 'revenue']
        corr_matrix = self.df[numerical_cols].corr()
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
        sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', 
                   cmap='coolwarm', center=0, square=True, 
                   linewidths=1, cbar_kws={"shrink": 0.8}, ax=ax2)
        ax2.set_title('Correlation Matrix', fontsize=14, fontweight='bold')
        
        # 3. Boxplot by Category
        ax3 = axes[1, 0]
        sns.boxplot(data=self.df, x='category', y='revenue', 
                    palette=self.colors[:3], ax=ax3)
        ax3.set_title('Revenue Distribution by Category', fontsize=14, fontweight='bold')
        ax3.set_xlabel('Category')
        ax3.set_ylabel('Revenue ($)')
        
        # 4. Violin Plot - Revenue by Category and Gender
        ax4 = axes[1, 1]
        sns.violinplot(data=self.df, x='category', y='revenue', 
                      hue='gender', split=True, palette=[self.colors[0], self.colors[1]], ax=ax4)
        ax4.set_title('Revenue Distribution by Category & Gender', fontsize=14, fontweight='bold')
        ax4.set_xlabel('Category')
        ax4.set_ylabel('Revenue ($)')
        ax4.legend(title='Gender')
        
        plt.suptitle('Statistical Analysis & Distributions', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()

    def visualize_advanced(self):
        """Professional Advanced Visualizations"""
        print("\n🎨 ADVANCED VISUALIZATIONS")
        print("="*100)
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # 1. Scatter Plot - Price vs Quantity
        ax1 = axes[0, 0]
        scatter = ax1.scatter(self.df['unit_price'], self.df['quantity'], 
                            c=self.df['revenue'], cmap='viridis', 
                            alpha=0.6, s=50)
        ax1.set_title('Price vs Quantity Relationship', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Unit Price ($)')
        ax1.set_ylabel('Quantity')
        plt.colorbar(scatter, ax=ax1, label='Revenue ($)')
        ax1.grid(True, alpha=0.3)
        
        # 2. Heatmap - Product by Region Performance
        ax2 = axes[0, 1]
        if len(self.df['product'].unique()) <= 15:  # Check if not too many products
            pivot_table = self.df.pivot_table(
                values='revenue',
                index='product',
                columns='region',
                aggfunc='sum',
                fill_value=0
            )
            sns.heatmap(pivot_table, annot=True, fmt='.0f', 
                       cmap='YlOrRd', cbar_kws={'label': 'Revenue ($)'}, ax=ax2)
            ax2.set_title('Product Performance by Region', fontsize=14, fontweight='bold')
        
        # 3. KDE Plot - Revenue by Customer Type
        ax3 = axes[1, 0]
        for i, customer_type in enumerate(self.df['customer_type'].unique()):
            subset = self.df[self.df['customer_type'] == customer_type]
            sns.kdeplot(data=subset, x='revenue', label=customer_type, 
                       fill=True, alpha=0.3, ax=ax3, color=self.colors[i])
        ax3.set_title('Revenue Distribution by Customer Type', fontsize=14, fontweight='bold')
        ax3.set_xlabel('Revenue ($)')
        ax3.set_ylabel('Density')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # 4. Payment Method Analysis
        ax4 = axes[1, 1]
        payment_revenue = self.df.groupby('payment_method')['revenue'].sum().sort_values(ascending=True)
        ax4.barh(payment_revenue.index, payment_revenue.values, 
                color=self.colors[:len(payment_revenue)], edgecolor='black', linewidth=0.5)
        ax4.set_title('Payment Method Analysis', fontsize=14, fontweight='bold')
        ax4.set_xlabel('Revenue ($)')
        ax4.set_ylabel('Payment Method')
        ax4.grid(True, alpha=0.3, axis='x')
        
        plt.suptitle('Advanced Multi-Dimensional Analysis', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()

    def create_dashboard(self):
        """Create Executive Dashboard with Key Metrics"""
        print("\n📋 EXECUTIVE DASHBOARD")
        print("="*100)
        
        # Calculate key metrics
        total_revenue = self.df['revenue'].sum()
        avg_order_value = self.df['revenue'].mean()
        total_orders = len(self.df)
        unique_customers = self.df['customer_id'].nunique()
        avg_rating = self.df['rating'].mean()
        
        fig, axes = plt.subplots(2, 3, figsize=(16, 8))
        
        # Create KPI cards
        metrics = [
            (f'${total_revenue:,.0f}', 'Total Revenue', f'Avg: ${avg_order_value:,.2f}'),
            (f'{total_orders:,}', 'Total Orders', f'Customers: {unique_customers:,}'),
            (f'{avg_rating:.1f}⭐', 'Average Rating', 'Customer Satisfaction')
        ]
        
        for i, (value, title, subtitle) in enumerate(metrics):
            ax = axes[0, i]
            ax.text(0.5, 0.6, value, fontsize=28, ha='center', fontweight='bold', color='#2C3E50')
            ax.text(0.5, 0.35, title, fontsize=14, ha='center', color='#7F8C8D')
            ax.text(0.5, 0.15, subtitle, fontsize=11, ha='center', color='#95A5A6')
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
            ax.set_title(f'Key Metric {i+1}', fontsize=12, fontweight='bold', pad=10)
        
        # Additional insights
        # Best Product
        if len(self.df) > 0:
            top_product = self.df.groupby('product')['revenue'].sum().idxmax()
            top_revenue = self.df.groupby('product')['revenue'].sum().max()
            ax = axes[1, 0]
            ax.text(0.5, 0.6, top_product[:15], fontsize=18, ha='center', fontweight='bold', color='#2C3E50')
            ax.text(0.5, 0.3, f'Revenue: ${top_revenue:,.0f}', fontsize=13, ha='center', color='#7F8C8D')
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
            ax.set_title('🏆 Best Product', fontsize=12, fontweight='bold')
        
        # Best Region
            top_region = self.df.groupby('region')['revenue'].sum().idxmax()
            region_revenue = self.df.groupby('region')['revenue'].sum().max()
            ax = axes[1, 1]
            ax.text(0.5, 0.6, top_region, fontsize=18, ha='center', fontweight='bold', color='#2C3E50')
            ax.text(0.5, 0.3, f'Revenue: ${region_revenue:,.0f}', fontsize=13, ha='center', color='#7F8C8D')
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
            ax.set_title('📍 Best Region', fontsize=12, fontweight='bold')
        
        # Best Customer Segment
            top_segment = self.df.groupby('customer_segment')['revenue'].sum().idxmax()
            segment_revenue = self.df.groupby('customer_segment')['revenue'].sum().max()
            ax = axes[1, 2]
            ax.text(0.5, 0.6, top_segment, fontsize=18, ha='center', fontweight='bold', color='#2C3E50')
            ax.text(0.5, 0.3, f'Revenue: ${segment_revenue:,.0f}', fontsize=13, ha='center', color='#7F8C8D')
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
            ax.set_title('🎯 Best Customer Segment', fontsize=12, fontweight='bold')
        
        plt.suptitle('Executive Dashboard - Key Performance Indicators', fontsize=18, fontweight='bold')
        plt.tight_layout()
        plt.show()

    def generate_insights(self):
        """Generate actionable insights from the analysis"""
        print("\n💡 KEY INSIGHTS & RECOMMENDATIONS")
        print("="*100)
        
        # Calculate insights
        if len(self.df) > 0:
            # Product insights
            top_product = self.df.groupby('product')['revenue'].sum().idxmax()
            top_product_revenue = self.df.groupby('product')['revenue'].sum().max()
            
            # Category insights
            category_perf = self.df.groupby('category')['revenue'].sum()
            best_category = category_perf.idxmax()
            
            # Customer insights
            avg_revenue_per_customer = self.df.groupby('customer_id')['revenue'].sum().mean()
            top_customer_type = self.df.groupby('customer_type')['revenue'].sum().idxmax()
            
            # Temporal insights
            if 'month_name' in self.df.columns:
                peak_month = self.df.groupby('month_name')['revenue'].sum().idxmax()
            else:
                peak_month = "N/A"
            
            if 'day_name' in self.df.columns:
                peak_day = self.df.groupby('day_name')['revenue'].sum().idxmax()
            else:
                peak_day = "N/A"
            
            # Correlation insights
            discount_corr = self.df['discount'].corr(self.df['revenue']) if 'discount' in self.df.columns else 0
            
            print("\n📈 TOP PERFORMERS:")
            print(f"  • Best Product: {top_product} (${top_product_revenue:,.2f})")
            print(f"  • Best Category: {best_category} (${category_perf[best_category]:,.2f})")
            
            print("\n👥 CUSTOMER INSIGHTS:")
            print(f"  • Average Revenue per Customer: ${avg_revenue_per_customer:,.2f}")
            print(f"  • Best Customer Type: {top_customer_type}")
            
            print("\n🕐 TEMPORAL INSIGHTS:")
            print(f"  • Peak Month: {peak_month}")
            print(f"  • Peak Day: {peak_day}")
            
            print("\n📊 CORRELATION INSIGHTS:")
            print(f"  • Discount vs Revenue Correlation: {discount_corr:.3f}")
            print(f"  • Rating vs Revenue Correlation: {self.df['rating'].corr(self.df['revenue']):.3f}")
            
            print("\n💡 RECOMMENDATIONS:")
            print("  • ✅ Focus on promoting top-performing products and categories")
            print("  • ✅ Develop targeted marketing strategies for different customer segments")
            print("  • ✅ Optimize pricing strategies based on discount impact analysis")
            print("  • ✅ Improve customer experience in peak periods to maximize revenue")
            print("  • ✅ Consider regional expansion in high-performing areas")
        
        print("\n" + self.seperator)

    def run_analysis(self):
        """Execute complete analysis pipeline"""
        print("\n" + "="*100)
        print("🚀 RETAIL ANALYTICS SYSTEM - PROFESSIONAL EDITION")
        print("="*100)
        
        # Step 1: Load data
        print("\n📥 Step 1: Loading Data")
        self.load_data()
        
        # Step 2: Data Exploration
        print("\n📊 Step 2: Data Exploration")
        self.data_exploration()
        
        # Step 3: Data Preparation
        print("\n🛠️ Step 3: Data Preparation")
        self.data_preparation()
        
        # Step 4: Visualizations
        print("\n🎨 Step 4: Generating Visualizations")
        self.visualize_time_series()
        self.visualize_products()
        self.visualize_customers()
        self.visualize_statistics()
        self.visualize_advanced()
        
        # Step 5: Dashboard
        print("\n📋 Step 5: Executive Dashboard")
        self.create_dashboard()
        
        # Step 6: Insights
        print("\n💡 Step 6: Generating Insights")
        self.generate_insights()
        
        print("\n" + "="*100)
        print("✅ ANALYSIS COMPLETED SUCCESSFULLY!")
        print("="*100)

if __name__ == "__main__":
    print("🚀 Starting Retail Analytics System...")
    print("📊 Generating comprehensive visualizations...")
    print("💡 Analyzing customer and product data...")
    print()
    
    # Try different possible file paths
    import os
    possible_paths = [
        'ecommerce_customers.csv',
        '../data/ecommerce_customers.csv',
        '../../data/ecommerce_customers.csv',
        './data/ecommerce_customers.csv'
    ]
    
    visualization = None
    for path in possible_paths:
        if os.path.exists(path):
            print(f"✅ Found data file at: {path}")
            visualization = VisualAnalytics(path)
            break
    
    if visualization is None:
        print("⚠️ Data file not found. Using sample data...")
        visualization = VisualAnalytics('sample_data.csv')
    
    visualization.run_analysis()