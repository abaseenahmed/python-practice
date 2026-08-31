import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import skew, kurtosis
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

class CustomerEDA:
    def __init__(self, data_path='customer_dataset.csv'):
        """Initialize EDA with dataset"""
        self.df = pd.read_csv(data_path)
        self.df_original = self.df.copy()
        print("="*80)
        print("CUSTOMER DATASET EXPLORATORY DATA ANALYSIS")
        print("="*80)
        
    def dataset_overview(self):
        """Basic information about the dataset"""
        print("\n1. DATASET OVERVIEW")
        print("-"*50)
        print(f"Number of rows: {self.df.shape[0]}")
        print(f"Number of columns: {self.df.shape[1]}")
        print(f"Memory usage: {self.df.memory_usage().sum() / 1024**2:.2f} MB")
        
        print("\nColumn Names and Data Types:")
        print(self.df.dtypes)
        
        print("\nDataset Info:")
        print(self.df.info())
        
        print("\nFirst 5 Rows:")
        print(self.df.head())
        
        print("\nLast 5 Rows:")
        print(self.df.tail())
        
    def missing_values_analysis(self):
        """Analyze missing values in the dataset"""
        print("\n2. MISSING VALUES ANALYSIS")
        print("-"*50)
        
        missing = self.df.isnull().sum()
        missing_percent = (missing / len(self.df)) * 100
        
        missing_df = pd.DataFrame({
            'Missing Count': missing,
            'Missing Percentage': missing_percent
        }).sort_values('Missing Percentage', ascending=False)
        
        print("\nMissing Values Summary:")
        print(missing_df[missing_df['Missing Count'] > 0])
        
        # Visualize missing values
        if missing.sum() > 0:
            fig, axes = plt.subplots(1, 2, figsize=(14, 5))
            
            # Heatmap of missing values
            sns.heatmap(self.df.isnull(), cbar=True, yticklabels=False, ax=axes[0])
            axes[0].set_title('Missing Values Heatmap', fontsize=14)
            
            # Bar plot of missing percentages
            missing_plot = missing_df[missing_df['Missing Count'] > 0].sort_values('Missing Percentage')
            if not missing_plot.empty:
                bars = axes[1].barh(missing_plot.index, missing_plot['Missing Percentage'], 
                                   color='coral', alpha=0.7)
                axes[1].set_xlabel('Missing Percentage (%)')
                axes[1].set_title('Missing Values by Column', fontsize=14)
                
                # Add percentage labels
                for i, bar in enumerate(bars):
                    width = bar.get_width()
                    axes[1].text(width + 0.5, bar.get_y() + bar.get_height()/2, 
                                f'{width:.1f}%', va='center', fontsize=10)
            
            plt.tight_layout()
            plt.show()
        
        # Handle missing values
        print("\nHandling Missing Values:")
        print("Filling numerical missing values with median...")
        num_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in num_cols:
            if self.df[col].isnull().any():
                median_val = self.df[col].median()
                self.df[col].fillna(median_val, inplace=True)
                print(f"  - Filled {col} with median: {median_val:.2f}")
        
        print("Filling categorical missing values with mode...")
        cat_cols = self.df.select_dtypes(include=['object']).columns
        for col in cat_cols:
            if self.df[col].isnull().any():
                mode_val = self.df[col].mode()[0]
                self.df[col].fillna(mode_val, inplace=True)
                print(f"  - Filled {col} with mode: {mode_val}")
        
        print(f"\nMissing values after handling: {self.df.isnull().sum().sum()}")
        
    def statistical_summary(self):
        """Generate statistical summary of numerical features"""
        print("\n3. STATISTICAL SUMMARY")
        print("-"*50)
        
        # Numerical features
        num_cols = self.df.select_dtypes(include=[np.number]).columns
        print("\nNumerical Features Statistics:")
        print(self.df[num_cols].describe(percentiles=[.25, .5, .75, .9, .95]).round(2))
        
        # Categorical features
        cat_cols = self.df.select_dtypes(include=['object']).columns
        print("\nCategorical Features Summary:")
        for col in cat_cols:
            print(f"\n{col}:")
            print(self.df[col].value_counts().head())
            
    def outlier_detection(self):
        """Detect and visualize outliers using IQR method"""
        print("\n4. OUTLIER DETECTION")
        print("-"*50)
        
        num_cols = self.df.select_dtypes(include=[np.number]).columns
        # Filter out ID columns and binary columns for better visualization
        num_cols = [col for col in num_cols if col not in ['customer_id', 'churn_risk', 'is_premium']]
        
        # Calculate number of rows and columns for subplots
        n_cols = min(4, len(num_cols))
        n_rows = (len(num_cols) + n_cols - 1) // n_cols
        
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, 4*n_rows))
        if n_rows == 1 and n_cols == 1:
            axes = [axes]
        else:
            axes = axes.flatten()
        
        outlier_counts = {}
        
        for i, col in enumerate(num_cols[:12]):  # Limit to 12 plots
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = self.df[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)]
            outlier_counts[col] = len(outliers)
            
            # Box plot
            self.df.boxplot(column=[col], ax=axes[i])
            axes[i].set_title(f'{col} (Outliers: {len(outliers)})', fontsize=10)
            axes[i].set_xlabel('')
        
        # Remove empty subplots
        for j in range(i+1, len(axes)):
            fig.delaxes(axes[j])
        
        plt.tight_layout()
        plt.show()
        
        print("\nOutlier Counts by Column:")
        for col, count in outlier_counts.items():
            if count > 0:
                print(f"  - {col}: {count} outliers ({count/len(self.df)*100:.1f}%)")
        
    def univariate_analysis(self):
        """Univariate analysis of features"""
        print("\n5. UNIVARIATE ANALYSIS")
        print("-"*50)
        
        # Numerical features
        num_cols = self.df.select_dtypes(include=[np.number]).columns
        num_cols = [col for col in num_cols if col not in ['customer_id', 'churn_risk', 'is_premium']]
        
        # Calculate grid size
        n_cols = min(3, len(num_cols))
        n_rows = (len(num_cols) + n_cols - 1) // n_cols
        
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 4*n_rows))
        if n_rows == 1 and n_cols == 1:
            axes = [axes]
        else:
            axes = axes.flatten()
        
        for i, col in enumerate(num_cols[:9]):  # Limit to 9 plots
            # Histogram with KDE
            self.df[col].hist(bins=30, alpha=0.6, ax=axes[i], color='skyblue', edgecolor='black')
            axes[i].axvline(self.df[col].mean(), color='red', linestyle='--', label=f'Mean: {self.df[col].mean():.2f}')
            axes[i].axvline(self.df[col].median(), color='green', linestyle='--', label=f'Median: {self.df[col].median():.2f}')
            axes[i].set_title(f'{col}\nSkewness: {skew(self.df[col].dropna()):.2f}, Kurtosis: {kurtosis(self.df[col].dropna()):.2f}')
            axes[i].legend(fontsize=8)
        
        # Remove empty subplots
        for j in range(i+1, len(axes)):
            fig.delaxes(axes[j])
        
        plt.tight_layout()
        plt.show()
        
        # Categorical features
        cat_cols = self.df.select_dtypes(include=['object']).columns
        
        n_cols = min(3, len(cat_cols))
        n_rows = (len(cat_cols) + n_cols - 1) // n_cols
        
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 4*n_rows))
        if n_rows == 1 and n_cols == 1:
            axes = [axes]
        else:
            axes = axes.flatten()
        
        for i, col in enumerate(cat_cols[:6]):
            value_counts = self.df[col].value_counts()
            axes[i].bar(value_counts.index, value_counts.values, alpha=0.7, color='lightcoral', edgecolor='black')
            axes[i].set_title(f'{col}')
            axes[i].tick_params(axis='x', rotation=45)
            # Add value labels
            for j, v in enumerate(value_counts.values):
                axes[i].text(j, v + 5, str(v), ha='center', va='bottom', fontsize=8)
        
        # Remove empty subplots
        for j in range(i+1, len(axes)):
            fig.delaxes(axes[j])
        
        plt.tight_layout()
        plt.show()
        
    def bivariate_analysis(self):
        """Bivariate analysis and correlations"""
        print("\n6. BIVARIATE ANALYSIS")
        print("-"*50)
        
        # Correlation matrix
        num_cols = self.df.select_dtypes(include=[np.number]).columns
        corr_matrix = self.df[num_cols].corr()
        
        fig, ax = plt.subplots(figsize=(12, 10))
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
        sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='coolwarm',
                    square=True, linewidths=0.5, ax=ax, cbar_kws={"shrink": 0.8})
        ax.set_title('Correlation Matrix of Numerical Features', fontsize=16)
        plt.tight_layout()
        plt.show()
        
        # Top correlations with target (churn_risk)
        if 'churn_risk' in corr_matrix.columns:
            print("\nTop correlations with churn_risk:")
            correlations = corr_matrix['churn_risk'].sort_values(ascending=False)
            print(correlations[correlations.index != 'churn_risk'].head(10))
        
        # Scatter plots for key relationships
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # Income vs Spending
        axes[0, 0].scatter(self.df['income'], self.df['annual_spending'], alpha=0.6, s=20)
        axes[0, 0].set_xlabel('Income')
        axes[0, 0].set_ylabel('Annual Spending')
        axes[0, 0].set_title('Income vs Spending')
        # Add trend line
        z = np.polyfit(self.df['income'].dropna(), self.df['annual_spending'].dropna(), 1)
        p = np.poly1d(z)
        axes[0, 0].plot(self.df['income'].sort_values(), p(self.df['income'].sort_values()), 
                       "r-", alpha=0.8, label=f'Corr: {self.df["income"].corr(self.df["annual_spending"]):.2f}')
        axes[0, 0].legend()
        
        # Satisfaction vs Churn
        axes[0, 1].scatter(self.df['satisfaction_score'], self.df['churn_risk'], alpha=0.6, s=20)
        axes[0, 1].set_xlabel('Satisfaction Score')
        axes[0, 1].set_ylabel('Churn Risk')
        axes[0, 1].set_title('Satisfaction vs Churn Risk')
        
        # Age vs Engagement
        axes[1, 0].scatter(self.df['age'], self.df['engagement_score'], alpha=0.6, s=20)
        axes[1, 0].set_xlabel('Age')
        axes[1, 0].set_ylabel('Engagement Score')
        axes[1, 0].set_title('Age vs Engagement')
        
        # Purchase Count vs Spending
        axes[1, 1].scatter(self.df['purchase_count'], self.df['annual_spending'], alpha=0.6, s=20)
        axes[1, 1].set_xlabel('Purchase Count')
        axes[1, 1].set_ylabel('Annual Spending')
        axes[1, 1].set_title('Purchase Count vs Spending')
        axes[1, 1].text(0.05, 0.95, f'Corr: {self.df["purchase_count"].corr(self.df["annual_spending"]):.2f}', 
                       transform=axes[1, 1].transAxes, fontsize=12, verticalalignment='top')
        
        plt.tight_layout()
        plt.show()
        
        # Box plots for categorical vs numerical
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # Gender vs Income
        self.df.boxplot(column='income', by='gender', ax=axes[0, 0])
        axes[0, 0].set_title('Income Distribution by Gender')
        axes[0, 0].set_xlabel('')
        
        # Education vs Spending
        self.df.boxplot(column='annual_spending', by='education', ax=axes[0, 1])
        axes[0, 1].set_title('Spending Distribution by Education')
        axes[0, 1].set_xlabel('')
        
        # Employment vs Satisfaction
        self.df.boxplot(column='satisfaction_score', by='employment_status', ax=axes[1, 0])
        axes[1, 0].set_title('Satisfaction by Employment Status')
        axes[1, 0].set_xlabel('')
        
        # Product Category vs Spending
        self.df.boxplot(column='annual_spending', by='preferred_category', ax=axes[1, 1])
        axes[1, 1].set_title('Spending by Preferred Category')
        axes[1, 1].set_xlabel('')
        
        plt.tight_layout()
        plt.show()
        
    def multivariate_analysis(self):
        """Multivariate analysis"""
        print("\n7. MULTIVARIATE ANALYSIS")
        print("-"*50)
        
        # Pairplot for selected features
        selected_features = ['income', 'annual_spending', 'satisfaction_score', 
                            'engagement_score', 'age', 'purchase_count']
        
        # Check if all features exist
        available_features = [f for f in selected_features if f in self.df.columns]
        
        if len(available_features) > 1:
            fig = sns.pairplot(self.df[available_features], diag_kind='kde', 
                              plot_kws={'alpha': 0.6, 's': 20})
            fig.fig.suptitle('Pairplot of Selected Numerical Features', y=1.02, fontsize=16)
            plt.tight_layout()
            plt.show()
        else:
            print("Not enough features for pairplot")
        
        # Heatmap of categorical variables
        print("\nCategorical Variable Analysis:")
        cat_cols = self.df.select_dtypes(include=['object']).columns
        for col in cat_cols:
            print(f"\n{col} distribution by churn risk:")
            cross_tab = pd.crosstab(self.df[col], self.df['churn_risk'], margins=True)
            print(cross_tab)
            cross_tab_percent = pd.crosstab(self.df[col], self.df['churn_risk'], normalize='index') * 100
            print("\nPercentage by category:")
            print(cross_tab_percent.round(2))
            
    def feature_engineering(self):
        """Perform feature engineering"""
        print("\n8. FEATURE ENGINEERING")
        print("-"*50)
        
        # Create new features
        self.df['spending_per_purchase'] = self.df['annual_spending'] / self.df['purchase_count']
        self.df['is_high_value'] = (self.df['annual_spending'] > self.df['annual_spending'].median()).astype(int)
        
        # Handle income categories with duplicate edges - using pd.cut with custom bins instead
        try:
            self.df['income_category'] = pd.qcut(self.df['income'], q=4, labels=['Low', 'Medium-Low', 'Medium-High', 'High'], duplicates='drop')
        except ValueError:
            # If qcut fails, use custom bins based on percentiles
            print("  - Using custom bins for income categories (due to duplicate values)")
            percentiles = self.df['income'].quantile([0, 0.25, 0.5, 0.75, 1]).values
            # Make sure we have unique bin edges
            unique_bins = np.unique(percentiles)
            if len(unique_bins) < 5:
                # If still not enough unique values, use standard bins
                bins = [0, 50000, 80000, 120000, self.df['income'].max() + 1000]
                labels = ['Low', 'Medium-Low', 'Medium-High', 'High']
            else:
                bins = unique_bins
                labels = ['Low', 'Medium-Low', 'Medium-High', 'High'][:len(bins)-1]
            self.df['income_category'] = pd.cut(self.df['income'], bins=bins, labels=labels, include_lowest=True)
        
        # Age groups with proper binning
        self.df['age_group'] = pd.cut(self.df['age'], bins=[17, 30, 45, 60, 81], labels=['Young', 'Middle', 'Mature', 'Senior'])
        self.df['customer_tenure'] = self.df['account_age_months'] / 12  # in years
        
        # Engagement categories
        try:
            self.df['engagement_category'] = pd.cut(self.df['engagement_score'], 
                                                    bins=[0, 33, 66, 100], 
                                                    labels=['Low', 'Medium', 'High'])
        except ValueError:
            # Handle edge cases
            self.df['engagement_category'] = pd.cut(self.df['engagement_score'], 
                                                    bins=[-1, 33, 66, 101], 
                                                    labels=['Low', 'Medium', 'High'])
        
        # Feature interactions
        self.df['income_spending_ratio'] = self.df['annual_spending'] / self.df['income']
        self.df['age_engagement_interaction'] = self.df['age'] * self.df['engagement_score'] / 100
        
        print("New features created:")
        new_features = ['spending_per_purchase', 'is_high_value', 'income_category', 
                       'age_group', 'customer_tenure', 'engagement_category', 
                       'income_spending_ratio', 'age_engagement_interaction']
        for feature in new_features:
            print(f"  - {feature}")
        
        print(f"\nDataset shape after feature engineering: {self.df.shape}")
        
    def advanced_visualizations(self):
        """Create advanced visualizations"""
        print("\n9. ADVANCED VISUALIZATIONS")
        print("-"*50)
        
        # Distribution of key metrics by premium status
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # Income by premium
        self.df.boxplot(column='income', by='is_premium', ax=axes[0, 0])
        axes[0, 0].set_title('Income by Premium Status')
        
        # Spending by premium
        self.df.boxplot(column='annual_spending', by='is_premium', ax=axes[0, 1])
        axes[0, 1].set_title('Spending by Premium Status')
        
        # Satisfaction by premium
        self.df.boxplot(column='satisfaction_score', by='is_premium', ax=axes[1, 0])
        axes[1, 0].set_title('Satisfaction by Premium Status')
        
        # Engagement by premium
        self.df.boxplot(column='engagement_score', by='is_premium', ax=axes[1, 1])
        axes[1, 1].set_title('Engagement by Premium Status')
        
        plt.tight_layout()
        plt.show()
        
        # Time series analysis
        if 'signup_date' in self.df.columns:
            # Convert signup_date to datetime if it's not already
            self.df['signup_date'] = pd.to_datetime(self.df['signup_date'])
            monthly_signups = self.df.groupby(self.df['signup_date'].dt.to_period('M')).size()
            
            fig, axes = plt.subplots(2, 2, figsize=(15, 10))
            
            # Monthly signups
            monthly_signups.plot(kind='line', ax=axes[0, 0], marker='o', color='teal')
            axes[0, 0].set_title('Monthly Signups Over Time')
            axes[0, 0].set_xlabel('Month')
            axes[0, 0].set_ylabel('Number of Signups')
            axes[0, 0].tick_params(axis='x', rotation=45)
            
            # Signup season distribution
            season_counts = self.df['signup_season'].value_counts()
            axes[0, 1].pie(season_counts.values, labels=season_counts.index, autopct='%1.1f%%')
            axes[0, 1].set_title('Signup Season Distribution')
            
            # Average spending by signup season
            season_spending = self.df.groupby('signup_season')['annual_spending'].mean().sort_values()
            axes[1, 0].bar(season_spending.index, season_spending.values, color='lightgreen', edgecolor='black')
            axes[1, 0].set_title('Average Spending by Signup Season')
            axes[1, 0].set_ylabel('Average Annual Spending')
            
            # Churn rate by signup season
            season_churn = self.df.groupby('signup_season')['churn_risk'].mean() * 100
            axes[1, 1].bar(season_churn.index, season_churn.values, color='salmon', edgecolor='black')
            axes[1, 1].set_title('Churn Rate by Signup Season')
            axes[1, 1].set_ylabel('Churn Rate (%)')
            
            plt.tight_layout()
            plt.show()
            
    def insights_summary(self):
        """Generate key insights from the analysis"""
        print("\n10. KEY INSIGHTS AND SUMMARY")
        print("="*50)
        
        insights = []
        
        # Correlations
        if 'churn_risk' in self.df.columns:
            corr_with_churn = self.df.select_dtypes(include=[np.number]).corr()['churn_risk'].sort_values(ascending=False)
            top_positive = corr_with_churn.head(3).index.tolist()
            top_negative = corr_with_churn.tail(3).index.tolist()
            
            insights.append(f"Top positive correlates with churn: {', '.join(top_positive[:3])}")
            insights.append(f"Top negative correlates with churn: {', '.join(top_negative[:3])}")
        
        # Premium customer characteristics
        if 'is_premium' in self.df.columns:
            premium_spending = self.df[self.df['is_premium'] == 1]['annual_spending'].mean()
            non_premium_spending = self.df[self.df['is_premium'] == 0]['annual_spending'].mean()
            if non_premium_spending > 0:
                insights.append(f"Premium customers spend {premium_spending/non_premium_spending:.2f}x more than non-premium")
            
            premium_satisfaction = self.df[self.df['is_premium'] == 1]['satisfaction_score'].mean()
            non_premium_satisfaction = self.df[self.df['is_premium'] == 0]['satisfaction_score'].mean()
            insights.append(f"Premium customers have {premium_satisfaction - non_premium_satisfaction:.2f} higher satisfaction")
        
        # Demographic insights
        top_spending_education = self.df.groupby('education')['annual_spending'].mean().idxmax()
        top_spending_employment = self.df.groupby('employment_status')['annual_spending'].mean().idxmax()
        insights.append(f"Highest spending demographic: {top_spending_education} educated, {top_spending_employment}")
        
        # Print insights
        print("\n🔍 Top Insights from EDA:\n")
        for i, insight in enumerate(insights, 1):
            print(f"{i}. {insight}")
        
        # Feature importance summary
        print(f"\n📊 Dataset Shape: {self.df.shape}")
        print(f"📈 Numerical Features: {len(self.df.select_dtypes(include=[np.number]).columns)}")
        print(f"📋 Categorical Features: {len(self.df.select_dtypes(include=['object']).columns)}")
        print(f"🆕 New Features Engineered: 8")
        
        print("\n✅ EDA Complete! The dataset is ready for modeling.")

    def run_full_eda(self):
        """Execute all EDA steps"""
        self.dataset_overview()
        self.missing_values_analysis()
        self.statistical_summary()
        self.outlier_detection()
        self.univariate_analysis()
        self.bivariate_analysis()
        self.multivariate_analysis()
        self.feature_engineering()
        self.advanced_visualizations()
        self.insights_summary()

if __name__ == "__main__":
    # Create EDA object and run analysis
    eda = CustomerEDA('customer_dataset.csv')
    eda.run_full_eda()