import pandas as pd
import numpy as np
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')

# ==============================
# 1. GENERATE SYNTHETIC DATASET
# ==============================

np.random.seed(42)
n_samples = 5000

# Generate features
age = np.random.randint(18, 70, n_samples)
income = np.random.normal(50000, 20000, n_samples)
income = np.maximum(income, 15000)  # Minimum income
credit_score = np.random.normal(700, 50, n_samples)
credit_score = np.clip(credit_score, 300, 850)
loan_amount = np.random.normal(15000, 5000, n_samples)
loan_amount = np.maximum(loan_amount, 1000)
employment_years = np.random.exponential(5, n_samples)
employment_years = np.minimum(employment_years, 40)
debt_to_income = np.random.uniform(0.1, 0.6, n_samples)
num_dependents = np.random.poisson(1, n_samples)
num_dependents = np.minimum(num_dependents, 5)

# Categorical features
education = np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n_samples, 
                            p=[0.3, 0.4, 0.2, 0.1])
home_ownership = np.random.choice(['Rent', 'Own', 'Mortgage'], n_samples, p=[0.3, 0.4, 0.3])
marital_status = np.random.choice(['Single', 'Married', 'Divorced'], n_samples, p=[0.3, 0.6, 0.1])

# Create target variable (loan default) based on logical relationships
default_prob = 1 / (1 + np.exp(-(
    -3 + 
    0.02 * (age - 30) + 
    -0.000005 * (income - 50000) + 
    -0.005 * (credit_score - 700) + 
    0.0001 * loan_amount + 
    -0.05 * employment_years + 
    1.5 * debt_to_income + 
    0.1 * num_dependents +
    0.2 * (education == 'High School') +
    -0.1 * (education == 'PhD') +
    0.3 * (home_ownership == 'Rent') +
    -0.2 * (home_ownership == 'Own') +
    0.1 * (marital_status == 'Single')
)))

target = np.random.binomial(1, default_prob)

# Create DataFrame
df = pd.DataFrame({
    'age': age,
    'income': income,
    'credit_score': credit_score,
    'loan_amount': loan_amount,
    'employment_years': employment_years,
    'debt_to_income': debt_to_income,
    'num_dependents': num_dependents,
    'education': education,
    'home_ownership': home_ownership,
    'marital_status': marital_status,
    'default': target
})

# Add some missing values
missing_indices = np.random.choice(n_samples, int(n_samples * 0.05), replace=False)
df.loc[missing_indices, 'income'] = np.nan
missing_indices = np.random.choice(n_samples, int(n_samples * 0.03), replace=False)
df.loc[missing_indices, 'credit_score'] = np.nan

print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nDataset info:")
print(df.info())

# ==============================
# 2. SAVE TO SQLITE DATABASE
# ==============================

# Create a single connection that we'll reuse
conn = sqlite3.connect('loan_data.db')
df.to_sql('loan_data', conn, if_exists='replace', index=False)
print("\n✅ Data saved to SQLite database")

# ==============================
# 3. COMPLETE SQL EDA CODE
# ==============================

sql_eda_queries = """
-- ==========================================
-- COMPLETE SQL EDA FOR LOAN DEFAULT ANALYSIS
-- ==========================================

-- 1. BASIC DATA OVERVIEW
-- ----------------------
-- Total records and missing values per column
SELECT 
    COUNT(*) as total_records,
    SUM(CASE WHEN income IS NULL THEN 1 ELSE 0 END) as missing_income,
    SUM(CASE WHEN credit_score IS NULL THEN 1 ELSE 0 END) as missing_credit_score,
    SUM(CASE WHEN age IS NULL THEN 1 ELSE 0 END) as missing_age,
    SUM(CASE WHEN loan_amount IS NULL THEN 1 ELSE 0 END) as missing_loan_amount,
    SUM(CASE WHEN employment_years IS NULL THEN 1 ELSE 0 END) as missing_employment,
    SUM(CASE WHEN debt_to_income IS NULL THEN 1 ELSE 0 END) as missing_dti,
    SUM(CASE WHEN num_dependents IS NULL THEN 1 ELSE 0 END) as missing_dependents
FROM loan_data;

-- 2. DESCRIPTIVE STATISTICS
-- ------------------------
-- Numeric columns statistics
SELECT 
    'Age' as feature,
    ROUND(AVG(age), 2) as mean,
    ROUND(MIN(age), 2) as min_val,
    ROUND(MAX(age), 2) as max_val,
    ROUND(STDEV(age), 2) as std_dev
FROM loan_data
UNION ALL
SELECT 
    'Income',
    ROUND(AVG(income), 2),
    ROUND(MIN(income), 2),
    ROUND(MAX(income), 2),
    ROUND(STDEV(income), 2)
FROM loan_data
UNION ALL
SELECT 
    'Credit_Score',
    ROUND(AVG(credit_score), 2),
    ROUND(MIN(credit_score), 2),
    ROUND(MAX(credit_score), 2),
    ROUND(STDEV(credit_score), 2)
FROM loan_data;

-- 3. TARGET VARIABLE DISTRIBUTION
-- ------------------------------
SELECT 
    default,
    COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM loan_data), 2) as percentage
FROM loan_data
GROUP BY default;

-- 4. CORRELATION WITH TARGET
-- -------------------------
-- Average values by default status
SELECT 
    default,
    ROUND(AVG(age), 2) as avg_age,
    ROUND(AVG(income), 2) as avg_income,
    ROUND(AVG(credit_score), 2) as avg_credit_score,
    ROUND(AVG(loan_amount), 2) as avg_loan_amount,
    ROUND(AVG(employment_years), 2) as avg_employment_years,
    ROUND(AVG(debt_to_income), 2) as avg_debt_to_income,
    ROUND(AVG(num_dependents), 2) as avg_dependents,
    COUNT(*) as count
FROM loan_data
GROUP BY default;

-- 5. CATEGORICAL ANALYSIS
-- ----------------------
-- Default rate by education
SELECT 
    education,
    COUNT(*) as total,
    SUM(default) as defaults,
    ROUND(SUM(default) * 100.0 / COUNT(*), 2) as default_rate
FROM loan_data
GROUP BY education
ORDER BY default_rate DESC;

-- Default rate by home ownership
SELECT 
    home_ownership,
    COUNT(*) as total,
    SUM(default) as defaults,
    ROUND(SUM(default) * 100.0 / COUNT(*), 2) as default_rate
FROM loan_data
GROUP BY home_ownership
ORDER BY default_rate DESC;

-- Default rate by marital status
SELECT 
    marital_status,
    COUNT(*) as total,
    SUM(default) as defaults,
    ROUND(SUM(default) * 100.0 / COUNT(*), 2) as default_rate
FROM loan_data
GROUP BY marital_status
ORDER BY default_rate DESC;

-- 6. AGE BUCKET ANALYSIS
-- ---------------------
SELECT 
    CASE 
        WHEN age < 25 THEN '18-24'
        WHEN age BETWEEN 25 AND 34 THEN '25-34'
        WHEN age BETWEEN 35 AND 44 THEN '35-44'
        WHEN age BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55+'
    END as age_group,
    COUNT(*) as total,
    SUM(default) as defaults,
    ROUND(SUM(default) * 100.0 / COUNT(*), 2) as default_rate,
    ROUND(AVG(income), 2) as avg_income
FROM loan_data
GROUP BY age_group
ORDER BY age_group;

-- 7. CREDIT SCORE SEGMENTS
-- -----------------------
SELECT 
    CASE 
        WHEN credit_score < 580 THEN 'Poor (300-579)'
        WHEN credit_score BETWEEN 580 AND 669 THEN 'Fair (580-669)'
        WHEN credit_score BETWEEN 670 AND 739 THEN 'Good (670-739)'
        WHEN credit_score BETWEEN 740 AND 799 THEN 'Very Good (740-799)'
        ELSE 'Excellent (800-850)'
    END as credit_segment,
    COUNT(*) as total,
    SUM(default) as defaults,
    ROUND(SUM(default) * 100.0 / COUNT(*), 2) as default_rate
FROM loan_data
WHERE credit_score IS NOT NULL
GROUP BY credit_segment
ORDER BY credit_segment;

-- 8. DEBT-TO-INCOME RATIO ANALYSIS
-- --------------------------------
SELECT 
    CASE 
        WHEN debt_to_income < 0.25 THEN 'Low (<25%)'
        WHEN debt_to_income BETWEEN 0.25 AND 0.36 THEN 'Moderate (25-36%)'
        WHEN debt_to_income BETWEEN 0.36 AND 0.43 THEN 'High (36-43%)'
        ELSE 'Very High (>43%)'
    END as dti_category,
    COUNT(*) as total,
    SUM(default) as defaults,
    ROUND(SUM(default) * 100.0 / COUNT(*), 2) as default_rate,
    ROUND(AVG(loan_amount), 2) as avg_loan
FROM loan_data
GROUP BY dti_category
ORDER BY debt_to_income;

-- 9. MULTI-DIMENSIONAL ANALYSIS
-- ----------------------------
-- Default rate by education and home ownership
SELECT 
    education,
    home_ownership,
    COUNT(*) as total,
    SUM(default) as defaults,
    ROUND(SUM(default) * 100.0 / COUNT(*), 2) as default_rate
FROM loan_data
GROUP BY education, home_ownership
ORDER BY education, default_rate DESC;

-- 10. OUTLIER DETECTION (using IQR method)
-- ----------------------------------------
WITH stats AS (
    SELECT 
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY income) as q1_income,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY income) as q3_income,
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY loan_amount) as q1_loan,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY loan_amount) as q3_loan
    FROM loan_data
)
SELECT 
    'Income' as feature,
    COUNT(*) as outliers
FROM loan_data, stats
WHERE income < q1_income - 1.5 * (q3_income - q1_income)
   OR income > q3_income + 1.5 * (q3_income - q1_income)
UNION ALL
SELECT 
    'Loan_Amount',
    COUNT(*)
FROM loan_data, stats
WHERE loan_amount < q1_loan - 1.5 * (q3_loan - q1_loan)
   OR loan_amount > q3_loan + 1.5 * (q3_loan - q1_loan);

-- 11. TREND ANALYSIS
-- -----------------
-- Default rate by employment years category
SELECT 
    CASE 
        WHEN employment_years < 2 THEN '< 2 years'
        WHEN employment_years BETWEEN 2 AND 5 THEN '2-5 years'
        WHEN employment_years BETWEEN 5 AND 10 THEN '5-10 years'
        ELSE '10+ years'
    END as exp_category,
    COUNT(*) as total,
    SUM(default) as defaults,
    ROUND(SUM(default) * 100.0 / COUNT(*), 2) as default_rate
FROM loan_data
GROUP BY exp_category
ORDER BY employment_years;

-- 12. KEY INSIGHTS SUMMARY
-- -----------------------
SELECT 
    'Total Default Rate' as insight,
    ROUND(SUM(default) * 100.0 / COUNT(*), 2) as value
FROM loan_data
UNION ALL
SELECT 
    'Avg Income for Defaulters',
    ROUND(AVG(income), 2)
FROM loan_data
WHERE default = 1
UNION ALL
SELECT 
    'Avg Income for Non-Defaulters',
    ROUND(AVG(income), 2)
FROM loan_data
WHERE default = 0
UNION ALL
SELECT 
    'Avg Credit Score for Defaulters',
    ROUND(AVG(credit_score), 2)
FROM loan_data
WHERE default = 1
UNION ALL
SELECT 
    'Avg Credit Score for Non-Defaulters',
    ROUND(AVG(credit_score), 2)
FROM loan_data
WHERE default = 0;
"""

# Execute SQL queries using the existing connection
def execute_sql_eda(conn):
    queries = sql_eda_queries.split(';')
    
    for query in queries:
        if query.strip():
            try:
                print("\n" + "="*80)
                print("SQL QUERY RESULT:")
                print("-"*80)
                result = pd.read_sql_query(query, conn)
                print(result)
                print("="*80)
            except Exception as e:
                print(f"Error executing query: {e}")

print("\n" + "="*80)
print("RUNNING SQL EDA QUERIES")
print("="*80)
execute_sql_eda(conn)

# ==============================
# 4. PYTHON EDA AND FEATURE ENGINEERING
# ==============================

print("\n" + "="*80)
print("PYTHON EDA AND FEATURE ENGINEERING")
print("="*80)

# Load data from SQL (using existing connection)
df = pd.read_sql_query("SELECT * FROM loan_data", conn)

# 4.1 Missing Value Analysis
print("\n4.1 MISSING VALUE ANALYSIS")
print("-"*40)
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing Values': missing_values,
    'Percentage': missing_percentage
})
print(missing_df[missing_df['Missing Values'] > 0])

# 4.2 Data Imputation
print("\n4.2 DATA IMPUTATION")
print("-"*40)
# Impute numeric columns with median
numeric_cols = ['income', 'credit_score']
for col in numeric_cols:
    median_val = df[col].median()
    df[col].fillna(median_val, inplace=True)
    print(f"Imputed {col} with median: {median_val:.2f}")

# 4.3 Feature Engineering
print("\n4.3 FEATURE ENGINEERING")
print("-"*40)

# Create new features
df['income_per_dependent'] = df['income'] / (df['num_dependents'] + 1)
df['loan_to_income_ratio'] = df['loan_amount'] / df['income']
df['credit_utilization'] = df['loan_amount'] / (df['income'] * 0.4)  # Proxy for utilization
df['age_group'] = pd.cut(df['age'], 
                         bins=[18, 25, 35, 45, 55, 70], 
                         labels=['18-24', '25-34', '35-44', '45-54', '55+'])
df['credit_score_bucket'] = pd.cut(df['credit_score'],
                                   bins=[300, 580, 670, 740, 800, 850],
                                   labels=['Poor', 'Fair', 'Good', 'Very Good', 'Excellent'])
df['dti_category'] = pd.cut(df['debt_to_income'],
                            bins=[0, 0.25, 0.36, 0.43, 1],
                            labels=['Low', 'Moderate', 'High', 'Very High'])

# Interaction features
df['age_credit_interaction'] = df['age'] * df['credit_score'] / 1000
df['income_debt_interaction'] = df['income'] * (1 - df['debt_to_income'])

print(f"✅ New features created: {len(df.columns) - 11}")  # 11 original columns

# 4.4 Encoding Categorical Variables
print("\n4.4 ENCODING CATEGORICAL VARIABLES")
print("-"*40)
categorical_cols = ['education', 'home_ownership', 'marital_status', 
                   'age_group', 'credit_score_bucket', 'dti_category']

# Label Encoding for ordinal
le_dict = {}
for col in ['age_group', 'credit_score_bucket', 'dti_category']:
    le = LabelEncoder()
    df[col + '_encoded'] = le.fit_transform(df[col].astype(str))
    le_dict[col] = le
    print(f"✅ Encoded {col}")

# One-Hot Encoding for nominal
df_encoded = pd.get_dummies(df, columns=['education', 'home_ownership', 'marital_status'], 
                           prefix=['edu', 'home', 'marital'])
print(f"✅ After encoding, dataset has {df_encoded.shape[1]} features")

# 4.5 Feature Selection
print("\n4.5 FEATURE SELECTION")
print("-"*40)

# Prepare features for selection
feature_cols = ['age', 'income', 'credit_score', 'loan_amount', 'employment_years',
                'debt_to_income', 'num_dependents', 'income_per_dependent',
                'loan_to_income_ratio', 'credit_utilization', 'age_credit_interaction',
                'income_debt_interaction', 'age_group_encoded', 'credit_score_bucket_encoded',
                'dti_category_encoded']

# Add encoded categorical columns
encoded_cols = [col for col in df_encoded.columns if col.startswith(('edu_', 'home_', 'marital_'))]
feature_cols.extend(encoded_cols)

X = df_encoded[feature_cols]
y = df_encoded['default']

# Remove any remaining NaN values
X = X.fillna(0)

# Feature selection using SelectKBest
selector = SelectKBest(f_classif, k=15)
selector.fit(X, y)

# Get feature scores
feature_scores = pd.DataFrame({
    'Feature': X.columns,
    'Score': selector.scores_
}).sort_values('Score', ascending=False)

print("Top 15 features by ANOVA F-score:")
print(feature_scores.head(15))

# 4.6 Feature Importance using Random Forest
print("\n4.6 FEATURE IMPORTANCE (RANDOM FOREST)")
print("-"*40)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, y)

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf.feature_importances_
}).sort_values('Importance', ascending=False)

print("Top 15 features by Random Forest importance:")
print(feature_importance.head(15))

# 4.7 Correlation Analysis
print("\n4.7 CORRELATION ANALYSIS")
print("-"*40)
# Select only numeric columns for correlation
numeric_df = df_encoded.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr()

# Correlation with target
target_corr = correlation_matrix['default'].sort_values(ascending=False)
print("Top 10 features correlated with target:")
print(target_corr.head(11))  # Including default itself

# 4.8 Data Visualization
print("\n4.8 GENERATING VISUALIZATIONS")
print("-"*40)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Distribution of target
df['default'].value_counts().plot(kind='bar', ax=axes[0, 0])
axes[0, 0].set_title('Target Distribution')
axes[0, 0].set_xlabel('Default')
axes[0, 0].set_ylabel('Count')

# Age distribution by default
df[df['default']==0]['age'].hist(bins=30, alpha=0.5, label='Non-default', ax=axes[0, 1])
df[df['default']==1]['age'].hist(bins=30, alpha=0.5, label='Default', ax=axes[0, 1])
axes[0, 1].set_title('Age Distribution by Default Status')
axes[0, 1].legend()

# Income distribution by default
df[df['default']==0]['income'].hist(bins=50, alpha=0.5, label='Non-default', ax=axes[0, 2])
df[df['default']==1]['income'].hist(bins=50, alpha=0.5, label='Default', ax=axes[0, 2])
axes[0, 2].set_title('Income Distribution by Default Status')
axes[0, 2].legend()

# Credit score distribution by default
df[df['default']==0]['credit_score'].hist(bins=30, alpha=0.5, label='Non-default', ax=axes[1, 0])
df[df['default']==1]['credit_score'].hist(bins=30, alpha=0.5, label='Default', ax=axes[1, 0])
axes[1, 0].set_title('Credit Score Distribution by Default Status')
axes[1, 0].legend()

# Default rate by education
df.groupby('education')['default'].mean().plot(kind='bar', ax=axes[1, 1])
axes[1, 1].set_title('Default Rate by Education')
axes[1, 1].set_ylabel('Default Rate')

# Default rate by home ownership
df.groupby('home_ownership')['default'].mean().plot(kind='bar', ax=axes[1, 2])
axes[1, 2].set_title('Default Rate by Home Ownership')
axes[1, 2].set_ylabel('Default Rate')

plt.tight_layout()
plt.savefig('eda_visualizations.png', dpi=300, bbox_inches='tight')
print("✅ Visualizations saved as 'eda_visualizations.png'")

# 4.9 Feature Scaling
print("\n4.9 FEATURE SCALING")
print("-"*40)
# Select features for scaling
features_to_scale = ['age', 'income', 'credit_score', 'loan_amount', 'employment_years',
                     'debt_to_income', 'num_dependents', 'income_per_dependent',
                     'loan_to_income_ratio', 'credit_utilization', 'age_credit_interaction',
                     'income_debt_interaction']

scaler = StandardScaler()
df_encoded[features_to_scale] = scaler.fit_transform(df_encoded[features_to_scale])

print(f"✅ Scaled {len(features_to_scale)} numeric features")
print("Sample of scaled data:")
print(df_encoded[features_to_scale].head())

# 4.10 Train-Test Split
print("\n4.10 TRAIN-TEST SPLIT")
print("-"*40)
X_final = df_encoded.drop(['default'], axis=1)
y_final = df_encoded['default']

X_train, X_test, y_train, y_test = train_test_split(X_final, y_final, 
                                                    test_size=0.2, 
                                                    random_state=42,
                                                    stratify=y_final)

print(f"Training set size: {len(X_train)}")
print(f"Test set size: {len(X_test)}")
print(f"Training set default rate: {y_train.mean():.2%}")
print(f"Test set default rate: {y_test.mean():.2%}")

# 4.11 Data Quality Report
print("\n4.11 DATA QUALITY REPORT")
print("-"*40)
print(f"Total samples: {len(df)}")
print(f"Total features: {len(df_encoded.columns) - 1} (excluding target)")
print(f"Missing values after imputation: {df_encoded.isnull().sum().sum()}")
print(f"Feature types:")
print(df_encoded.dtypes.value_counts())

# ==============================
# 5. SAVE CLEANED AND PROCESSED DATA
# ==============================

print("\n" + "="*80)
print("SAVING CLEANED AND PROCESSED DATA")
print("="*80)

# Save the cleaned dataset as CSV (ready for ML)
cleaned_filename = 'cleaned_loan_data_ready_for_ml.csv'
df_encoded.to_csv(cleaned_filename, index=False)
print(f"✅ Cleaned dataset saved as: {cleaned_filename}")

# Also save to SQLite (using the same connection)
df_encoded.to_sql('cleaned_loan_data', conn, if_exists='replace', index=False)
print(f"✅ Cleaned dataset saved to SQLite table: 'cleaned_loan_data'")

# Save feature importance results
feature_importance.to_csv('feature_importance.csv', index=False)
feature_scores.to_csv('feature_scores.csv', index=False)

print("\n📁 Files Generated:")
print(f"  1. {cleaned_filename} - Cleaned dataset ready for ML models")
print("  2. cleaned_loan_data (SQLite table) - Same dataset in database")
print("  3. feature_importance.csv - Random Forest feature importance")
print("  4. feature_scores.csv - ANOVA F-score feature selection")
print("  5. eda_visualizations.png - Visualizations")

# ==============================
# 6. CLOSE DATABASE CONNECTION
# ==============================

conn.close()
print("\n✅ Database connection closed")

print("\n" + "="*80)
print("🎉 EDA AND FEATURE ENGINEERING COMPLETED SUCCESSFULLY!")
print("="*80)
print(f"\n📊 The cleaned dataset '{cleaned_filename}' is ready for ML model training!")
print("   It contains:")
print(f"   - {df_encoded.shape[0]} rows (samples)")
print(f"   - {df_encoded.shape[1]} columns (features)")
print("   - All missing values handled")
print("   - Features engineered and scaled")
print("   - Categorical variables encoded")
print("="*80)