import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis, chi2_contingency
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("Set2")

class EmployeeEDA:
    def __init__(self, data_path='employee_attrition_dataset.csv'):
        """Initialize EDA with dataset"""
        self.df = pd.read_csv(data_path)
        self.df_original = self.df.copy()
        self.attrition_column = 'attrition'
        print("="*80)
        print("EMPLOYEE ATTRITION & PERFORMANCE EDA")
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
        """Analyze and handle missing values"""
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
            
            sns.heatmap(self.df.isnull(), cbar=True, yticklabels=False, ax=axes[0])
            axes[0].set_title('Missing Values Heatmap', fontsize=14)
            
            missing_plot = missing_df[missing_df['Missing Count'] > 0].sort_values('Missing Percentage')
            if not missing_plot.empty:
                bars = axes[1].barh(missing_plot.index, missing_plot['Missing Percentage'], 
                                   color='coral', alpha=0.7)
                axes[1].set_xlabel('Missing Percentage (%)')
                axes[1].set_title('Missing Values by Column', fontsize=14)
                
                for i, bar in enumerate(bars):
                    width = bar.get_width()
                    axes[1].text(width + 0.5, bar.get_y() + bar.get_height()/2, 
                                f'{width:.1f}%', va='center', fontsize=10)
            
            plt.tight_layout()
            plt.show()
        
        # Handle missing values
        print("\nHandling Missing Values:")
        num_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in num_cols:
            if self.df[col].isnull().any():
                median_val = self.df[col].median()
                self.df[col].fillna(median_val, inplace=True)
                print(f"  - Filled {col} with median: {median_val:.2f}")
        
        cat_cols = self.df.select_dtypes(include=['object']).columns
        for col in cat_cols:
            if self.df[col].isnull().any():
                mode_val = self.df[col].mode()[0]
                self.df[col].fillna(mode_val, inplace=True)
                print(f"  - Filled {col} with mode: {mode_val}")
        
        print(f"\nMissing values after handling: {self.df.isnull().sum().sum()}")
    
    def statistical_summary(self):
        """Generate statistical summary"""
        print("\n3. STATISTICAL SUMMARY")
        print("-"*50)
        
        num_cols = self.df.select_dtypes(include=[np.number]).columns
        print("\nNumerical Features Statistics:")
        print(self.df[num_cols].describe(percentiles=[.25, .5, .75, .9, .95]).round(2))
        
        cat_cols = self.df.select_dtypes(include=['object']).columns
        print("\nCategorical Features Summary:")
        for col in cat_cols:
            print(f"\n{col}:")
            print(self.df[col].value_counts().head())
            
            if col != 'hire_date' and col != 'last_promotion_date':
                # Show attrition rate by category
                attrition_rate = self.df.groupby(col)[self.attrition_column].mean() * 100
                print("\nAttrition Rate by Category:")
                print(attrition_rate.round(2).sort_values(ascending=False))
    
    def attrition_analysis(self):
        """Deep dive into attrition patterns"""
        print("\n4. ATTRITION ANALYSIS")
        print("-"*50)
        
        overall_attrition = self.df['attrition'].mean() * 100
        print(f"Overall Attrition Rate: {overall_attrition:.2f}%")
        
        # Attrition by department
        print("\nAttrition by Department:")
        dept_attrition = self.df.groupby('department')['attrition'].agg(['count', 'mean']).round(3)
        dept_attrition['attrition_rate'] = dept_attrition['mean'] * 100
        print(dept_attrition.sort_values('attrition_rate', ascending=False))
        
        # Attrition by job role
        print("\nAttrition by Job Role:")
        role_attrition = self.df.groupby('job_role')['attrition'].agg(['count', 'mean']).round(3)
        role_attrition['attrition_rate'] = role_attrition['mean'] * 100
        print(role_attrition.sort_values('attrition_rate', ascending=False))
        
        # Visualizations
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # Department attrition
        dept_attrition_sorted = dept_attrition.sort_values('attrition_rate')
        axes[0, 0].barh(dept_attrition_sorted.index, dept_attrition_sorted['attrition_rate'], 
                       color='lightcoral', edgecolor='black')
        axes[0, 0].set_xlabel('Attrition Rate (%)')
        axes[0, 0].set_title('Attrition Rate by Department')
        for i, v in enumerate(dept_attrition_sorted['attrition_rate']):
            axes[0, 0].text(v + 0.5, i, f'{v:.1f}%', va='center')
        
        # Job role attrition
        role_attrition_sorted = role_attrition.sort_values('attrition_rate')
        axes[0, 1].barh(role_attrition_sorted.index, role_attrition_sorted['attrition_rate'],
                       color='skyblue', edgecolor='black')
        axes[0, 1].set_xlabel('Attrition Rate (%)')
        axes[0, 1].set_title('Attrition Rate by Job Role')
        for i, v in enumerate(role_attrition_sorted['attrition_rate']):
            axes[0, 1].text(v + 0.5, i, f'{v:.1f}%', va='center')
        
        # Attrition by tenure
        tenure_attrition = self.df.groupby('tenure_category')['attrition'].mean() * 100
        axes[1, 0].bar(tenure_attrition.index, tenure_attrition.values, 
                      color='lightgreen', edgecolor='black')
        axes[1, 0].set_xlabel('Tenure Category')
        axes[1, 0].set_ylabel('Attrition Rate (%)')
        axes[1, 0].set_title('Attrition Rate by Tenure')
        axes[1, 0].tick_params(axis='x', rotation=45)
        for i, v in enumerate(tenure_attrition.values):
            axes[1, 0].text(i, v + 1, f'{v:.1f}%', ha='center')
        
        # Attrition by remote work
        remote_attrition = self.df.groupby('remote_work')['attrition'].mean() * 100
        axes[1, 1].bar(remote_attrition.index, remote_attrition.values,
                      color='plum', edgecolor='black')
        axes[1, 1].set_xlabel('Remote Work Status')
        axes[1, 1].set_ylabel('Attrition Rate (%)')
        axes[1, 1].set_title('Attrition Rate by Remote Work Status')
        for i, v in enumerate(remote_attrition.values):
            axes[1, 1].text(i, v + 1, f'{v:.1f}%', ha='center')
        
        plt.tight_layout()
        plt.show()
        
        # Attrition by key continuous variables
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        axes = axes.flatten()
        
        continuous_vars = ['age', 'years_at_company', 'monthly_salary', 
                          'job_satisfaction', 'performance_rating', 'work_life_balance']
        
        for i, var in enumerate(continuous_vars):
            # Boxplot comparing attrition groups
            data_to_plot = [self.df[self.df['attrition'] == 0][var].dropna(),
                           self.df[self.df['attrition'] == 1][var].dropna()]
            axes[i].boxplot(data_to_plot, labels=['Stayed', 'Attrited'])
            axes[i].set_title(f'{var} by Attrition Status')
            axes[i].set_ylabel(var)
            
            # Statistical test (t-test)
            from scipy.stats import ttest_ind
            stayed = self.df[self.df['attrition'] == 0][var].dropna()
            attrited = self.df[self.df['attrition'] == 1][var].dropna()
            if len(stayed) > 0 and len(attrited) > 0:
                t_stat, p_val = ttest_ind(stayed, attrited)
                axes[i].text(0.5, 0.95, f'p-value: {p_val:.4f}', 
                           transform=axes[i].transAxes, ha='center', fontsize=10)
        
        plt.tight_layout()
        plt.show()
    
    def correlation_analysis(self):
        """Correlation analysis and relationships"""
        print("\n5. CORRELATION ANALYSIS")
        print("-"*50)
        
        num_cols = self.df.select_dtypes(include=[np.number]).columns
        corr_matrix = self.df[num_cols].corr()
        
        fig, ax = plt.subplots(figsize=(14, 12))
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
        sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='coolwarm',
                   square=True, linewidths=0.5, ax=ax, cbar_kws={"shrink": 0.8})
        ax.set_title('Correlation Matrix of Employee Features', fontsize=16)
        plt.tight_layout()
        plt.show()
        
        # Top correlations with attrition
        print("\nTop correlations with attrition:")
        correlations = corr_matrix['attrition'].sort_values(ascending=False)
        print(correlations[correlations.index != 'attrition'].head(10))
    
    def performance_analysis(self):
        """Analyze performance patterns"""
        print("\n6. PERFORMANCE ANALYSIS")
        print("-"*50)
        
        # Performance distribution
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # Performance distribution
        self.df['performance_rating'].hist(bins=20, ax=axes[0, 0], color='skyblue', 
                                          edgecolor='black', alpha=0.7)
        axes[0, 0].axvline(self.df['performance_rating'].mean(), color='red', 
                          linestyle='--', label=f"Mean: {self.df['performance_rating'].mean():.2f}")
        axes[0, 0].set_title('Performance Rating Distribution')
        axes[0, 0].set_xlabel('Performance Rating')
        axes[0, 0].legend()
        
        # Performance by department
        dept_perf = self.df.groupby('department')['performance_rating'].mean().sort_values()
        axes[0, 1].barh(dept_perf.index, dept_perf.values, color='lightgreen', edgecolor='black')
        axes[0, 1].set_xlabel('Average Performance Rating')
        axes[0, 1].set_title('Performance by Department')
        for i, v in enumerate(dept_perf.values):
            axes[0, 1].text(v + 0.02, i, f'{v:.2f}', va='center')
        
        # Performance vs Training Hours
        axes[1, 0].scatter(self.df['training_hours'], self.df['performance_rating'], 
                          alpha=0.6, s=30)
        axes[1, 0].set_xlabel('Training Hours')
        axes[1, 0].set_ylabel('Performance Rating')
        axes[1, 0].set_title('Performance vs Training Hours')
        z = np.polyfit(self.df['training_hours'], self.df['performance_rating'], 1)
        p = np.poly1d(z)
        axes[1, 0].plot(self.df['training_hours'].sort_values(), 
                       p(self.df['training_hours'].sort_values()), 
                       "r-", alpha=0.8, label=f'Corr: {self.df["training_hours"].corr(self.df["performance_rating"]):.2f}')
        axes[1, 0].legend()
        
        # Performance by Job Role
        role_perf = self.df.groupby('job_role')['performance_rating'].mean().sort_values()
        axes[1, 1].bar(role_perf.index, role_perf.values, color='coral', edgecolor='black')
        axes[1, 1].set_ylabel('Average Performance Rating')
        axes[1, 1].set_title('Performance by Job Role')
        axes[1, 1].tick_params(axis='x', rotation=45)
        for i, v in enumerate(role_perf.values):
            axes[1, 1].text(i, v + 0.02, f'{v:.2f}', ha='center')
        
        plt.tight_layout()
        plt.show()
    
    def feature_engineering(self):
        """Feature engineering for employee data"""
        print("\n7. FEATURE ENGINEERING")
        print("-"*50)
        
        # Create new features
        self.df['salary_performance_ratio'] = self.df['monthly_salary'] / self.df['performance_rating']
        self.df['age_tenure_ratio'] = self.df['age'] / self.df['years_at_company']
        
        try:
            self.df['tenure_category_detailed'] = pd.cut(self.df['years_at_company'], 
                                                         bins=[0, 2, 5, 10, 25],
                                                         labels=['New', 'Experienced', 'Senior', 'Veteran'])
        except ValueError:
            self.df['tenure_category_detailed'] = pd.cut(self.df['years_at_company'], 
                                                         bins=[0, 2, 5, 10, 25],
                                                         labels=['New', 'Experienced', 'Senior', 'Veteran'])
        
        # Satisfaction composite score
        self.df['overall_satisfaction'] = (self.df['job_satisfaction'] + 
                                          self.df['environment_satisfaction'] + 
                                          self.df['relationship_satisfaction']) / 3
        self.df['overall_satisfaction'] = self.df['overall_satisfaction'].round(1)
        
        # High performer flag
        self.df['is_high_performer'] = (self.df['performance_rating'] >= 4).astype(int)
        
        # Low performer flag
        self.df['is_low_performer'] = (self.df['performance_rating'] <= 2.5).astype(int)
        
        # High attrition risk flag (based on multiple factors)
        self.df['high_attrition_risk'] = (
            (self.df['job_satisfaction'] < 2.5) & 
            (self.df['overtime'] == 1) &
            (self.df['years_at_company'] < 2)
        ).astype(int)
        
        # Salary category
        try:
            self.df['salary_category'] = pd.qcut(self.df['monthly_salary'], q=4, 
                                                 labels=['Low', 'Medium-Low', 'Medium-High', 'High'],
                                                 duplicates='drop')
        except ValueError:
            bins = self.df['monthly_salary'].quantile([0, 0.25, 0.5, 0.75, 1]).values
            unique_bins = np.unique(bins)
            labels = ['Low', 'Medium-Low', 'Medium-High', 'High'][:len(unique_bins)-1]
            self.df['salary_category'] = pd.cut(self.df['monthly_salary'], bins=unique_bins, 
                                                labels=labels, include_lowest=True)
        
        # Experience level
        self.df['experience_level'] = pd.cut(self.df['years_at_company'], 
                                             bins=[0, 3, 7, 15, 30],
                                             labels=['Entry', 'Mid', 'Senior', 'Expert'])
        
        print("New features created:")
        new_features = ['salary_performance_ratio', 'age_tenure_ratio', 
                       'tenure_category_detailed', 'overall_satisfaction',
                       'is_high_performer', 'is_low_performer', 
                       'high_attrition_risk', 'salary_category', 'experience_level']
        for feature in new_features:
            print(f"  - {feature}")
        
        print(f"\nDataset shape after feature engineering: {self.df.shape}")
    
    def categorical_analysis(self):
        """Deep dive into categorical variables"""
        print("\n8. CATEGORICAL ANALYSIS")
        print("-"*50)
        
        cat_cols = self.df.select_dtypes(include=['object']).columns
        cat_cols = [col for col in cat_cols if col not in ['hire_date', 'last_promotion_date']]
        
        fig, axes = plt.subplots(2, 3, figsize=(18, 10))
        axes = axes.flatten()
        
        for i, col in enumerate(cat_cols[:6]):
            # Count plot
            counts = self.df[col].value_counts()
            axes[i].bar(counts.index, counts.values, alpha=0.7, color='lightblue', edgecolor='black')
            axes[i].set_title(f'{col} Distribution')
            axes[i].tick_params(axis='x', rotation=45)
            
            # Add count labels
            for j, v in enumerate(counts.values):
                axes[i].text(j, v + 5, str(v), ha='center', va='bottom')
        
        # Remove empty subplots
        for j in range(i+1, len(axes)):
            fig.delaxes(axes[j])
        
        plt.tight_layout()
        plt.show()
        
        # Chi-square tests for categorical variables vs attrition
        print("\nChi-square test for categorical variables vs attrition:")
        for col in cat_cols:
            if col != self.attrition_column:
                contingency = pd.crosstab(self.df[col], self.df['attrition'])
                chi2, p_val, dof, expected = chi2_contingency(contingency)
                print(f"{col}: chi2={chi2:.2f}, p-value={p_val:.4f}")
    
    def advanced_visualizations(self):
        """Advanced visualizations for employee data"""
        print("\n9. ADVANCED VISUALIZATIONS")
        print("-"*50)
        
        # Pairplot for key features
        selected_features = ['age', 'years_at_company', 'monthly_salary', 
                            'performance_rating', 'job_satisfaction', 'work_life_balance']
        
        available_features = [f for f in selected_features if f in self.df.columns]
        if len(available_features) > 1:
            fig = sns.pairplot(self.df[available_features + ['attrition']], 
                              hue='attrition', diag_kind='kde',
                              plot_kws={'alpha': 0.6, 's': 30})
            fig.fig.suptitle('Pairplot of Key Features by Attrition Status', y=1.02, fontsize=16)
            plt.tight_layout()
            plt.show()
        
        # Salary analysis
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        # Salary distribution by department
        self.df.boxplot(column='monthly_salary', by='department', ax=axes[0])
        axes[0].set_title('Salary Distribution by Department')
        axes[0].set_xlabel('')
        
        # Salary vs Attrition
        self.df.boxplot(column='monthly_salary', by='attrition', ax=axes[1])
        axes[1].set_title('Salary Distribution by Attrition Status')
        axes[1].set_xlabel('0=Stayed, 1=Attrited')
        
        # Salary vs Performance
        axes[2].scatter(self.df['performance_rating'], self.df['monthly_salary'], 
                       alpha=0.6, s=30, c=self.df['attrition'], cmap='coolwarm')
        axes[2].set_xlabel('Performance Rating')
        axes[2].set_ylabel('Monthly Salary')
        axes[2].set_title('Salary vs Performance (Color = Attrition)')
        
        plt.tight_layout()
        plt.show()
        
        # Satisfaction analysis
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        satisfaction_cols = ['job_satisfaction', 'environment_satisfaction', 
                           'relationship_satisfaction']
        
        for i, col in enumerate(satisfaction_cols):
            self.df.boxplot(column=col, by='attrition', ax=axes[i])
            axes[i].set_title(f'{col} by Attrition')
            axes[i].set_xlabel('0=Stayed, 1=Attrited')
        
        plt.tight_layout()
        plt.show()
    
    def insights_summary(self):
        """Generate key insights"""
        print("\n10. KEY INSIGHTS AND SUMMARY")
        print("="*50)
        
        insights = []
        
        # Overall attrition
        overall = self.df['attrition'].mean() * 100
        insights.append(f"Overall attrition rate: {overall:.1f}%")
        
        # Department with highest attrition
        dept_attrition = self.df.groupby('department')['attrition'].mean()
        highest_dept = dept_attrition.idxmax()
        highest_rate = dept_attrition.max() * 100
        insights.append(f"Department with highest attrition: {highest_dept} ({highest_rate:.1f}%)")
        
        # Most common tenure for attrition
        tenure_attrition = self.df[self.df['attrition'] == 1]['tenure_category'].value_counts().index[0]
        insights.append(f"Most common tenure among attrited employees: {tenure_attrition}")
        
        # Key factors correlated with attrition
        corr_with_attrition = self.df.select_dtypes(include=[np.number]).corr()['attrition'].sort_values()
        top_negative = corr_with_attrition.head(2).index.tolist()
        top_positive = corr_with_attrition.tail(2).index.tolist()
        insights.append(f"Top positive factors: {', '.join(top_positive)}")
        insights.append(f"Top negative factors: {', '.join(top_negative)}")
        
        # Satisfaction score for attrited vs stayed
        if 'overall_satisfaction' in self.df.columns:
            stayed_sat = self.df[self.df['attrition'] == 0]['overall_satisfaction'].mean()
            attrited_sat = self.df[self.df['attrition'] == 1]['overall_satisfaction'].mean()
            insights.append(f"Satisfaction gap: Attrited ({attrited_sat:.2f}) vs Stayed ({stayed_sat:.2f})")
        
        print("\n🔍 Top Insights from Employee EDA:\n")
        for i, insight in enumerate(insights, 1):
            print(f"{i}. {insight}")
        
        # Summary statistics
        print(f"\n📊 Dataset Shape: {self.df.shape}")
        print(f"📈 Numerical Features: {len(self.df.select_dtypes(include=[np.number]).columns)}")
        print(f"📋 Categorical Features: {len(self.df.select_dtypes(include=['object']).columns)}")
        print(f"🆕 New Features Engineered: 9")
        
        print("\n✅ Employee EDA Complete! Ready for modeling.")
    
    def run_full_eda(self):
        """Execute all EDA steps"""
        self.dataset_overview()
        self.missing_values_analysis()
        self.statistical_summary()
        self.attrition_analysis()
        self.correlation_analysis()
        self.performance_analysis()
        self.categorical_analysis()
        self.feature_engineering()
        self.advanced_visualizations()
        self.insights_summary()

if __name__ == "__main__":
    eda = EmployeeEDA('employee_attrition_dataset.csv')
    eda.run_full_eda()