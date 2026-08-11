# 🛒 Retail Sales and Customer Analytics System

A comprehensive retail sales analytics project built with **Python, NumPy, Pandas, and Matplotlib**.

The project simulates a real-world retail analytics workflow starting from raw transaction data and progressing through **data quality auditing, data cleaning, feature engineering, exploratory analysis, customer analytics, product performance analysis, outlier detection, statistical analysis, visualization, and business recommendations**.

This project was developed as **Project 03** in my practical journey toward becoming an **AI/ML Engineer**, with a strong focus on developing practical data analysis and data preprocessing skills.

---

## 📌 Project Overview

Real-world datasets are rarely clean.

They may contain:

- Missing values
- Duplicate records
- Invalid numerical values
- Incorrect discounts
- Invalid customer ages
- Invalid ratings
- Extreme values
- Inconsistent categorical values
- Incorrect revenue calculations

This project demonstrates how to build a complete analytical pipeline that handles these problems before performing business analysis.

The system takes raw retail transaction data and performs the following workflow:

```text
Raw Retail Data
       ↓
Data Loading
       ↓
Data Quality Audit
       ↓
Data Cleaning
       ↓
Feature Engineering
       ↓
Sales Analysis
       ↓
Monthly Analysis
       ↓
Customer Analytics
       ↓
Discount Analysis
       ↓
Product Performance
       ↓
Outlier Detection
       ↓
NumPy Statistical Analysis
       ↓
Data Visualization
       ↓
Business Report
       ↓
Cleaned Dataset
Project Objectives

The main objectives of this project are:

Load and inspect raw retail transaction data.
Perform a comprehensive data quality audit.
Detect missing values and duplicate records.
Detect invalid values in numerical columns.
Clean and standardize the dataset.
Handle missing values using appropriate techniques.
Recalculate and validate revenue.
Perform feature engineering using Pandas.
Analyze product performance.
Analyze category and regional performance.
Analyze monthly sales trends.
Perform customer-level analytics.
Segment customers based on revenue.
Analyze discount effectiveness.
Rank products using a custom performance score.
Detect statistical outliers using the IQR method.
Perform statistical analysis using NumPy.
Create professional business visualizations.
Generate a final business analysis report.
Export cleaned datasets for further analysis or machine learning.

## Technologies Used
Technology	Purpose
Python	Core programming language
NumPy	Numerical and statistical analysis
Pandas	Data manipulation, cleaning, grouping and feature engineering
Matplotlib	Data visualization
Matplotlib GridSpec	Dashboard layout
OS	Directory and file management
Warnings	Warning management

## 📂 Project Structure
Project_03/
│
├── data/
│   ├── raw_retail_transactions.csv
│   ├── cleaned_retail_transactions.csv
│   └── customer_summary.csv
│
├── src/
│   ├── retail_analysis.py
│   └── generate_data.py
│
├── visualizations/
│   ├── retail_sales_dashboard.png
│   ├── monthly_revenue.png
│   ├── revenue_by_product.png
│   ├── revenue_by_category.png
│   └── revenue_distribution.png
│
├── README.md
└── requirements.txt
📊 Dataset

The project works with retail transaction-level data.

The dataset contains information related to:

Transaction ID
Customer ID
Product
Category
Region
Quantity
Unit Price
Discount
Revenue
Customer Age
Rating
Shipping Cost
Payment Method
Customer Type
Order Date

The project also generates the retail dataset before running the analysis pipeline.

🔍 Data Quality Audit

The first stage of the system performs a detailed data quality audit.

It checks:

Basic Dataset Information
Number of rows
Number of columns
Column names
Data types
Missing Values

The system calculates:

df.isnull().sum()

and determines the percentage of missing values for each column.

Duplicate Records

The project checks both:

df.duplicated()

and duplicate transaction IDs.

Unique Values

The following are analyzed:

Customers
Products
Categories
Regions
Numerical Statistics

The system calculates:

Minimum
Maximum
Mean
Median
Standard deviation

for important numerical columns.

Invalid Values

The system checks for:

Quantity <= 0
Discount < 0
Discount > 1
Customer age < 18
Customer age > 100
Rating < 1
Rating > 5
Unit price <= 0
Revenue <= 0
🧹 Data Cleaning

The project contains a dedicated data-cleaning pipeline.

Duplicate Removal

True duplicate rows are removed using:

df.drop_duplicates()
Region Standardization

Region names are standardized using:

df['region'].str.strip().str.title()

This prevents problems caused by inconsistent capitalization or whitespace.

Invalid Quantity

Invalid quantities are converted to missing values:

df.loc[invalid_qty, 'quantity'] = np.nan
Discount Cleaning

Discount values are constrained to the valid range:

0 ≤ discount ≤ 1

Values below 0 are changed to 0.

Values above 1 are changed to 1.

Customer Age Cleaning

Customer ages outside the accepted range of:

18 - 100

are converted to missing values.

Rating Cleaning

Ratings are restricted to:

1 - 5

using:

df['rating'].clip(1, 5)
Missing Value Handling

Categorical missing values are filled using the mode.

Numerical missing values are filled using the median.

This approach helps reduce the effect of extreme values compared with blindly using the mean.

💰 Revenue Validation

One of the important parts of this project is validating the revenue column.

Revenue is recalculated using:

quantity × unit_price × (1 - discount)

The project then compares the calculated revenue with the original revenue.

A revenue mismatch is identified when the difference exceeds:

0.01

If a significant mismatch is detected, the calculated revenue replaces the original value.

This introduces an important real-world data engineering concept:

Never blindly trust a dataset just because a column already exists.

⚙️ Feature Engineering

Several new features are created from the raw data.

Date Features
year
month
month_name
day_of_week
quarter
year_week
Financial Features
gross_revenue
discount_amount
estimated_profit

Gross revenue is calculated as:

quantity * unit_price

Discount amount is calculated as:

gross_revenue * discount

An estimated profit metric is also created using a simplified 40% assumption.

Note: This is an analytical assumption, not actual accounting profit.

📈 Sales Analysis

The project calculates overall sales metrics including:

Total revenue
Average transaction revenue
Median transaction revenue
Total units sold
Average quantity per transaction
Product Analysis

Products are analyzed using:

Total quantity sold
Total revenue
Average price
Average discount
Average rating
Transaction count

The system identifies:

Best-selling product
Highest-revenue product
Lowest-revenue product
🗂️ Category Analysis

Each category is analyzed according to:

Total revenue
Total quantity
Transaction count
Average transaction value

This helps identify which categories contribute most to overall business performance.

🌍 Regional Analysis

The project analyzes sales across different regions.

For each region, it calculates:

Revenue
Quantity sold
Transaction count
Average transaction value

The highest-performing region is also identified.

📅 Monthly Sales Analysis

The system analyzes sales over time.

It identifies:

Highest revenue month
Lowest revenue month
Highest sales-volume month
Lowest sales-volume month

The project also calculates Year-over-Year revenue growth.

Example:

2024 Revenue
2025 Revenue
Growth Percentage

This introduces a basic business time-series analysis workflow.

👥 Customer Analytics

Customer-level analysis is one of the major components of the project.

For each customer, the system calculates:

Total orders
Total quantity purchased
Total revenue
Average discount
Average rating
Average order value
🏆 Top Customers

The project identifies the top 10 customers based on:

Revenue

Customers generating the highest total revenue.

Order Count

Customers making the highest number of purchases.

Quantity

Customers purchasing the highest number of units.

🎯 Customer Segmentation

Customers are segmented based on their total revenue.

The project calculates:

Q1
Median
Q3

and uses these values to create customer segments.

The resulting segments are:

VIP
High Value
Regular
Low Value

The segmentation logic is based on the actual distribution of customer revenue rather than arbitrary fixed thresholds.

🔄 Customer Type Analysis

The project also analyzes existing customer types and calculates metrics such as:

Average revenue
Average order value
Average quantity
Average discount
Average number of orders

This provides another perspective on customer behavior.

🏷️ Discount Analysis

The project groups customers' transactions into discount ranges:

0-5%
5-10%
10-20%
20-30%
30%+

For each group, it calculates:

Average revenue
Average quantity
Number of transactions

The project also calculates correlations between:

Discount ↔ Revenue
Discount ↔ Quantity

This provides a basic way to investigate whether higher discounts are associated with different purchasing behavior.

🏅 Product Performance Ranking

Products receive a custom performance score based on three metrics:

Revenue     → 50%
Quantity    → 30%
Rating      → 20%

The metrics are normalized before calculating the final score.

The formula is:

Performance Score =
    0.5 × Revenue Score
  + 0.3 × Quantity Score
  + 0.2 × Rating Score

Products are then ranked according to their performance score.

This demonstrates how multiple business metrics can be combined into a single analytical ranking.

🚨 Outlier Detection

The project uses the Interquartile Range (IQR) method to detect outliers.

Outliers are analyzed for:

Revenue
Unit Price
Quantity
Discount
Customer Age

The IQR is calculated as:

IQR = Q3 - Q1

Lower and upper boundaries are calculated as:

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR

The project also displays the largest revenue transactions for further investigation.

🔢 NumPy Statistical Analysis

NumPy is used directly for statistical calculations.

The project calculates:

Mean
Median
Standard deviation
Variance
Percentiles

Revenue percentiles calculated include:

25th percentile
50th percentile
75th percentile
90th percentile
95th percentile
99th percentile

The 95th percentile is also used to identify the approximate top 5% of high-revenue transactions.

📊 Data Visualization

The project creates a complete retail analytics dashboard using Matplotlib.

The dashboard contains:

1. Monthly Revenue

A line chart showing revenue trends over time.

2. Revenue by Product

A horizontal bar chart showing product-level revenue.

3. Revenue by Region

A pie chart showing regional revenue distribution.

4. Revenue Distribution

A histogram showing the distribution of transaction revenue.

The mean and median are also displayed.

5. Revenue vs Quantity

A scatter plot examining the relationship between units sold and revenue.

6. Discount vs Revenue

A scatter plot examining the relationship between discount rate and revenue.

7. Customer Revenue Distribution

A histogram showing the distribution of customer-level revenue.

8. Top 10 Customers

A horizontal bar chart showing the highest-revenue customers.

9. Correlation Matrix

A heatmap showing correlations between numerical variables.

🖼️ Generated Visualizations

The project automatically generates:

visualizations/
│
├── retail_sales_dashboard.png
├── monthly_revenue.png
├── revenue_by_product.png
├── revenue_by_category.png
└── revenue_distribution.png

The main dashboard combines multiple visualizations into a single analytical view.

📋 Data Quality Summary

The project compares the dataset before and after cleaning.

It reports:

Before Cleaning
Number of rows
Missing values
Duplicate rows
Invalid values
After Cleaning
Number of rows
Missing values
Duplicate rows
Invalid values
Improvement

The system calculates:

Rows removed
Missing values fixed
Invalid values fixed

This makes the data-cleaning process measurable rather than simply saying:

"I cleaned the data."

📑 Business Report

The final report summarizes important business metrics.

It includes:

Total transactions
Total customers
Total revenue
Average order value
Total units sold
Best-selling product
Highest-revenue product
Best-performing category
Best-performing region
Highest-revenue month
Lowest-revenue month
Top customer
95th percentile revenue
Number of high-value customers
💡 Key Business Findings

The system automatically generates business findings such as:

Revenue concentration among top customers
Top-performing products
Regional revenue contribution
Relationship between discounts and revenue
Peak sales months
🚀 Business Recommendations

Based on the analysis, the system generates recommendations related to:

Customer Strategy

Focus marketing efforts on high-value customers through personalized loyalty programs.

Product Strategy

Use high-performing products as flagship products and consider product bundling.

Regional Strategy

Study successful regions and apply their strategies to weaker regions.

Discount Strategy

Evaluate whether discounts are positively or negatively associated with revenue.

Seasonal Strategy

Increase marketing activity during high-performing sales periods.

▶️ How to Run the Project
1. Clone the Repository
git clone <your-repository-url>

Move into the project directory:

cd Project_03
2. Install Dependencies

Install the required Python libraries:

pip install -r requirements.txt

Required libraries include:

numpy
pandas
matplotlib
3. Run the Analysis

Navigate to the source directory:

cd src

Run:

python retail_analysis.py

The program will:

Generate the retail dataset.
Load the data.
Audit data quality.
Clean the dataset.
Engineer features.
Perform sales analysis.
Perform monthly analysis.
Analyze customers.
Analyze discounts.
Rank products.
Detect outliers.
Perform NumPy statistical analysis.
Generate visualizations.
Produce a quality summary.
Save cleaned datasets.
Generate the final business report.
📦 Output Files

After successful execution, the project generates cleaned datasets:

data/cleaned_retail_transactions.csv
data/customer_summary.csv

and visualizations:

visualizations/retail_sales_dashboard.png
visualizations/monthly_revenue.png
visualizations/revenue_by_product.png
visualizations/revenue_by_category.png
visualizations/revenue_distribution.png
🧠 Skills Practiced

This project provided hands-on practice with:

NumPy
Arrays
Statistical calculations
Mean
Median
Variance
Standard deviation
Percentiles
Numerical operations
Boolean filtering
Pandas
DataFrame operations
Data loading
Data cleaning
Missing values
Duplicate detection
GroupBy
Aggregation
Sorting
Filtering
DateTime operations
Feature engineering
Quantiles
Correlation
Data transformation
Categorical data
Exporting CSV files
Matplotlib
Line plots
Bar charts
Horizontal bar charts
Histograms
Scatter plots
Pie charts
Heatmaps
Multiple axes
GridSpec
Dashboards
Figure customization
Saving high-resolution figures
🤖 Relevance to AI & ML Engineering

Although this project does not train a machine learning model, the skills developed here are fundamental to machine learning.

A typical ML workflow looks roughly like:

Raw Data
   ↓
Data Understanding
   ↓
Data Quality Analysis
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Evaluation
   ↓
Deployment

This project covers a significant portion of the data preparation and exploratory analysis stages.

These skills will later be directly useful when working with:

Scikit-learn
Machine Learning
Deep Learning
NLP
Computer Vision
Time Series
Recommendation Systems
Predictive Analytics
🔮 Future Improvements

Possible future versions of this project could include:

Interactive dashboards
Plotly visualizations
Streamlit web application
SQL database integration
Machine learning-based sales forecasting
Customer churn prediction
Customer lifetime value prediction
Recommendation system
Product demand forecasting
Automated anomaly detection
Automated report generation
Scikit-learn integration
Model deployment using FastAPI
📚 Project Learning Outcome

The main goal of this project was not simply to produce charts.

The goal was to understand how raw business data can be transformed into useful information through a structured analytical pipeline.

The project strengthened practical understanding of:

Data
 ↓
Cleaning
 ↓
Transformation
 ↓
Analysis
 ↓
Visualization
 ↓
Insights
 ↓
Business Decisions

This workflow forms an important foundation for future Data Science and Machine Learning projects.

👨‍💻 Author

Abaseen Ahmed

Software Engineer / Aspiring AI & ML Engineer

Interested in:

Artificial Intelligence
Machine Learning
Data Science
Python
Software Engineering
AI Engineering
⭐ Project Status

Completed ✅

Project 03 of my practical AI/ML Engineering learning journey.

NumPy        ✅
Pandas       ✅
Matplotlib   ✅
Data Analysis ✅
Data Cleaning ✅
Feature Engineering ✅
Exploratory Analysis ✅
Visualization ✅