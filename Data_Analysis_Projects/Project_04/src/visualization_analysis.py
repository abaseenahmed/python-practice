# ================================= Project 04 ======================================== #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

class VisualAnalytics:
    def __init__(self, data_path='../data/ecommerce_customers.csv'):
        self.data_path = data_path
        self.df = None
        self.cleaned_df = None
        self.customer_df = None
        self.initial_shape = None
        self.seperator = '-'*100
        sns.set_theme(style="whitegrid")

    def load_data(self):
        self.df = pd.read_csv(self.data_path)
        self.initial_shape = self.df.shape
        print("Data loaded successfully.")
        print(f"Shape: {self.df.shape}")
        print(self.seperator)
        return self.df

    def data_exploration(self):
        print("\n" + "="*100)
        print("DATA EXPLORATION")
        print("="*100)
        print(self.df.head())
        print(f'The shape of the dataset is {self.df.shape}')
        print(f'The columns of the dataset are: {self.df.columns}')
        print(f'The data types of each column is:\n{self.df.dtypes}')
        print(self.df.info())
        print(self.df.describe())
        print(f'The number of null values in each column are: \n{self.df.isnull().sum()}')
        print(f'Number of unique rows: \n{self.df.nunique()}')
        print(self.seperator)

    def data_preparation(self):
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])
        self.df['year'] = self.df['order_date'].dt.year
        self.df['month'] = self.df['order_date'].dt.month
        self.df['month_name'] = self.df['order_date'].dt.month_name()
        self.df['day_of_week'] = self.df['order_date'].dt.day_of_week
        self.df['calculated_revenue'] = self.df['unit_price'] * self.df['quantity'] * (1 - self.df['discount'])
        self.df['revenue_comparison'] = ( self.df['revenue'] - self.df['calculated_revenue'] ).abs()
        self.df.sort_values(by='revenue_comparison', ignore_index=True)
        print(self.df.head(10))

    def visuals(self):
        # Visual_01 Monthly Revenue Trend
        monthly_revenue = self.df.groupby('month')['revenue'].sum()
        print(monthly_revenue)
        fig, ax = plt.subplots(figsize=(10, 6), dpi=120)
        ax.plot(
            self.df['month_name'].unique(),
            monthly_revenue,
            marker = 'o',
            label = 'Montly Revenue',
        )
        ax.set_title('Monthly Revenue by Company')
        ax.set_xlabel('Months Name')
        ax.set_ylabel('Revenue')
        ax.legend()
        ax.grid(axis='x') 
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        plt.tight_layout()
        plt.show()

        # Visual_02 Revenue by Product
        fig, ax = plt.subplots(figsize=(10, 6), dpi = 120)
        rev_col = self.df.groupby('product')['revenue'].sum().sort_values()
        print(rev_col)
        ax.bar(
            self.df['product'].unique(),
            rev_col,
            color = 'lightgreen'
        )
        ax.set_title('Revenue by Product')
        ax.set_xlabel('Product Name')
        ax.set_ylabel('Revenue')
        ax.grid(axis='x')
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        plt.tight_layout()
        plt.show()

        # Visual_03 Revenue by Region
        fig, ax = plt.subplots(figsize=(10, 6), dpi = 120)
        reg_col = self.df.groupby('region')['revenue'].sum().sort_values()
        print(reg_col)
        ax.barh(
            self.df['region'].unique(),
            reg_col,
            color = 'skyblue'
        )
        ax.set_title('Revenue by Region')
        ax.set_xlabel('Revenue')
        ax.set_ylabel('Regions')
        ax.grid(axis='y')
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        plt.tight_layout()
        plt.show()

        # Visual_04 Revenue Histogram
        fig, ax = plt.subplots(figsize=(10, 6), dpi = 120)
        ax.hist(
            self.df['revenue'],
            color = 'purple',
            bins=5
        )
        ax.set_title('Revenue Histogram Chart')
        ax.set_xlabel('Revenue')
        ax.grid(axis='x')
        plt.axvline() 
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        plt.tight_layout()
        plt.show()                

    def seaborn_visuals(self):
        # Category Revenue Comparison
        sns.barplot(data = self.df, x = 'category', y = 'revenue', hue='gender')
        plt.title('Category Revenue Comparison')
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        plt.show()

        # Revenue by Gender
        sns.boxplot(data = self.df, x = 'gender', y = 'revenue')
        plt.title('Revenue by Gender Comparison')
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        plt.show()

        # Revenue by Age
        sns.histplot(data = self.df, x='age', bins=20, kde=True, color='brown')
        plt.title('Revenue by Age Comparison')
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        plt.show()

        # Age vs Revenue Scatter Plot
        sns.scatterplot(data = self.df, x = 'age', y = 'revenue', hue = 'gender', size = 'quantity')
        plt.title('Age VS Revenue Scatter Plot')
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        plt.show()

        # Discount vs Revenue Scatter Plot
        sns.scatterplot(data = self.df, x = 'discount', y = 'revenue', hue = 'category', color = 'ligtred')
        plt.title('Discount VS Revenue Scatter Plot')
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        plt.show()

        # Correlation Heatmapt
        numerical_columns = ['age', 'unit_price', 'quantity', 'discount', 'rating', 'revenue']
        correlation = self.df[numerical_columns].corr()
        sns.heatmap(correlation, annot=True, cmap = 'coolwarm')
        plt.title('Numerical Columns Correlation Matrix')
        plt.show()

        # Revenue by Category and Gender
        sns.barplot(data = self.df, x = 'category', y = 'revenue', hue='gender')
        plt.title('Category Revenue Comparison')
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        plt.show()

        # Customer Type Analysis
        sns.countplot(data = self.df, x = 'customer_type')
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        plt.show()

        # Distribution accross rating
        sns.histplot(data = self.df, x = 'category', y = 'rating')
        plt.show()

        #
        pivot = self.df.pivot_table(
            values='revenue',
            index='product',
            columns='region',
            aggfunc='sum'
        )
        sns.heatmap(
            pivot,
            annot=True,
            fmt='.0f',
            cmap='YlGnBu'
        )
        plt.show()

    def advance_visuals(self):
        numerical_columns = ['age', 'unit_price', 'quantity', 'discount', 'rating', 'revenue']
        sns.pairplot(
             data = self.df[numerical_columns],
             diag_kind='hist'
        )
        plt.show()

        sns.violinplot(data = self.df, x = 'category', y = 'revenue')
        plt.show()

        sns.kdeplot(
            data=self.df,
            x='revenue',
            hue='customer_type',
            fill=True
        )

    def both_visuals(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(
            data=df,
            x='category',
            y='revenue',
            ax=ax
        )
        ax.set_title('Revenue Distribution by Category')
        ax.set_xlabel('Product Category')
        ax.set_ylabel('Revenue')
        plt.tight_layout()
        plt.show()

    # def final_dashboard(self):
      

    def run_analysis(self):
        print("\n" + "="*60)
        print("RETAIL ANALYTICS SYSTEM")
        print("="*100)
                
        # Step 1: Load data
        print("\nStep 1: Loading Data")
        self.load_data()

        # Step 2: Data Exploration
        print("\nStep 2: Data Exploration")
        self.data_exploration()

        # Step 3: Data Preparation
        print("\nStep 3: Data Preparation")
        self.data_preparation()

        # Step 4: Data Visuals
        print("\nStep 4: Data Visuals")
        # self.visuals()

        # Step 5: Data Visuals by Seaborn
        print("\nStep 5: Data Visuals By Seaborn")
        # self.seaborn_visuals()

        # Step 6: Advance Data Visuals by Seaborn
        print("\nStep 6: Advance Data Visuals By Seaborn")
        self.advance_visuals()

        print("\n" + "="*100)
        print("VISUAL ANALYSIS COMPLETED")
        print("="*60)

if __name__ =="__main__":
    print("Generating retail data...")
    visualization = VisualAnalytics()
    visualization.run_analysis()

