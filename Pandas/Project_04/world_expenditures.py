"""
================================================================================
WORLD GOVERNMENT EXPENDITURE ANALYTICS PLATFORM
================================================================================
Advanced Data Analysis System for Government Spending Patterns
Author: Data Analytics Team
Version: 2.0
Last Updated: 2026

This professional platform provides comprehensive analysis of government
expenditure data across 200+ countries with advanced statistical methods,
trend forecasting, and business intelligence insights.
================================================================================
"""

import pandas as pd
import numpy as np
import warnings
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import sys

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Configuration Constants
SEPARATOR = '█'*100
THIN_SEPARATOR = '─'*100
ANALYSIS_VERSION = '2.0'
OUTPUT_DIR = './analytics_output/'

class GovernmentExpenditureAnalytics:
    """
    Professional analytics engine for government expenditure data.
    Provides advanced statistical analysis, trend detection, and business intelligence.
    """
    
    def __init__(self, filepath: str):
        """
        Initialize the analytics engine with data loading and preprocessing.
        
        Args:
            filepath: Path to the CSV data file
        """
        self.start_time = datetime.now()
        self.filepath = filepath
        self.df = None
        self.cleaned_df = None
        self.statistical_summary = {}
        self.correlation_matrix = None
        self.outliers_detected = None
        
        print(SEPARATOR)
        print("🏛️  GOVERNMENT EXPENDITURE ANALYTICS PLATFORM")
        print(f"📊 Version: {ANALYSIS_VERSION}")
        print(f"⏰ Analysis Started: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(SEPARATOR)
        
        self._load_data()
        self._preprocess_data()
        self._perform_advanced_statistics()
        
    def _load_data(self) -> None:
        """Load data with error handling and initial validation."""
        print("\n📂 LOADING DATA...")
        try:
            self.df = pd.read_csv(self.filepath)
            print(f"✅ Data loaded successfully!")
            print(f"   Shape: {self.df.shape}")
            print(f"   Memory usage: {self.df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
            
            # Remove unnamed column if exists
            if 'Unnamed: 0' in self.df.columns:
                self.df.drop(columns=['Unnamed: 0'], inplace=True)
                print("   Removed 'Unnamed: 0' column")
                
        except FileNotFoundError:
            print("❌ ERROR: File not found!")
            sys.exit(1)
        except Exception as e:
            print(f"❌ ERROR loading data: {str(e)}")
            sys.exit(1)
            
    def _preprocess_data(self) -> None:
        """
        Advanced preprocessing with intelligent data cleaning and feature engineering.
        """
        print("\n🧹 PREPROCESSING PIPELINE...")
        self.cleaned_df = self.df.copy()
        
        # 1. Duplicate Handling with Detailed Logging
        initial_rows = len(self.cleaned_df)
        duplicates = self.cleaned_df.duplicated()
        duplicate_count = duplicates.sum()
        
        if duplicate_count > 0:
            self.cleaned_df = self.cleaned_df[~duplicates]
            print(f"   ✅ Removed {duplicate_count} duplicate records")
            
        # 2. Missing Value Analysis and Smart Imputation
        missing_before = self.cleaned_df.isnull().sum()
        print(f"   📊 Missing values before imputation: {missing_before.sum()}")
        
        # Intelligent imputation based on column type
        for col in self.cleaned_df.columns:
            if self.cleaned_df[col].dtype in ['float64', 'int64']:
                if self.cleaned_df[col].isnull().any():
                    # Use median for skewed distributions
                    median_val = self.cleaned_df[col].median()
                    self.cleaned_df[col].fillna(median_val, inplace=True)
                    print(f"   ✓ Imputed '{col}' with median: {median_val:.2f}")
            else:
                # For categorical columns, use mode
                if self.cleaned_df[col].isnull().any():
                    mode_val = self.cleaned_df[col].mode()[0]
                    self.cleaned_df[col].fillna(mode_val, inplace=True)
                    print(f"   ✓ Imputed '{col}' with mode: {mode_val}")
                    
        # 3. Column Renaming for Professional Standards
        self.cleaned_df.rename(columns={
            'Expenditure(million USD)': 'Expenditure_USD_Million',
            'GDP(%)': 'GDP_Percentage'
        }, inplace=True)
        
        # 4. Data Type Optimization
        self.cleaned_df['Year'] = self.cleaned_df['Year'].astype('int32')
        self.cleaned_df['Expenditure_USD_Million'] = self.cleaned_df['Expenditure_USD_Million'].astype('float32')
        self.cleaned_df['GDP_Percentage'] = self.cleaned_df['GDP_Percentage'].astype('float32')
        
        # 5. Feature Engineering: Create derived metrics
        self._engineer_features()
        
        print(f"   ✅ Preprocessing complete!")
        print(f"   Final shape: {self.cleaned_df.shape}")
        
    def _engineer_features(self) -> None:
        """
        Create advanced derived features for deeper insights.
        """
        # 1. Expenditure per GDP ratio (efficiency metric)
        self.cleaned_df['Expenditure_GDP_Ratio'] = (
            self.cleaned_df['Expenditure_USD_Million'] / 
            (self.cleaned_df['GDP_Percentage'] + 0.001)  # Avoid division by zero
        )
        
        # 2. Spending category tiers
        conditions = [
            self.cleaned_df['Expenditure_USD_Million'] > 100000,
            self.cleaned_df['Expenditure_USD_Million'] >= 50000,
            self.cleaned_df['Expenditure_USD_Million'] >= 10000,
            self.cleaned_df['Expenditure_USD_Million'] < 10000
        ]
        choices = ['Mega Spender', 'Major Spender', 'Moderate Spender', 'Low Spender']
        self.cleaned_df['Spending_Tier'] = np.select(conditions, choices, default='Low Spender')
        
        # 3. GDP Contribution Level
        gdp_conditions = [
            self.cleaned_df['GDP_Percentage'] > 10,
            self.cleaned_df['GDP_Percentage'] >= 5,
            self.cleaned_df['GDP_Percentage'] >= 2,
            self.cleaned_df['GDP_Percentage'] < 2
        ]
        gdp_choices = ['Critical', 'Significant', 'Moderate', 'Minimal']
        self.cleaned_df['GDP_Contribution'] = np.select(gdp_conditions, gdp_choices, default='Minimal')
        
        # 4. Decade classification
        self.cleaned_df['Decade'] = (self.cleaned_df['Year'] // 10) * 10
        
        # 5. Year-over-year growth (will be calculated later)
        self.cleaned_df['Growth_Indicator'] = 'Not Calculated'
        
    def _perform_advanced_statistics(self) -> None:
        """
        Perform comprehensive statistical analysis.
        """
        print("\n📈 ADVANCED STATISTICAL ANALYSIS...")
        
        # 1. Descriptive Statistics with Enhanced Metrics
        self.statistical_summary = {
            'basic_stats': self.cleaned_df[['Expenditure_USD_Million', 'GDP_Percentage']].describe(),
            'skewness': self.cleaned_df[['Expenditure_USD_Million', 'GDP_Percentage']].skew(),
            'kurtosis': self.cleaned_df[['Expenditure_USD_Million', 'GDP_Percentage']].kurtosis()
        }
        
        # 2. Outlier Detection using IQR method
        self._detect_outliers()
        
        # 3. Correlation Analysis
        self.correlation_matrix = self.cleaned_df[['Year', 'Expenditure_USD_Million', 
                                                   'GDP_Percentage', 'Expenditure_GDP_Ratio']].corr()
        
        print("   ✅ Statistical analysis complete!")
        
    def _detect_outliers(self) -> None:
        """
        Detect outliers using IQR method with detailed reporting.
        """
        numeric_cols = ['Expenditure_USD_Million', 'GDP_Percentage']
        self.outliers_detected = {}
        
        for col in numeric_cols:
            Q1 = self.cleaned_df[col].quantile(0.25)
            Q3 = self.cleaned_df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = self.cleaned_df[(self.cleaned_df[col] < lower_bound) | 
                                       (self.cleaned_df[col] > upper_bound)]
            
            self.outliers_detected[col] = {
                'count': len(outliers),
                'percentage': (len(outliers) / len(self.cleaned_df)) * 100,
                'lower_bound': lower_bound,
                'upper_bound': upper_bound
            }
            
    def country_analysis(self) -> Dict:
        """
        Comprehensive country-level analysis with ranking and metrics.
        """
        print("\n🌍 COUNTRY PERFORMANCE ANALYSIS")
        print(THIN_SEPARATOR)
        
        # 1. Country Aggregations
        country_metrics = self.cleaned_df.groupby('Country').agg({
            'Expenditure_USD_Million': ['sum', 'mean', 'std', 'min', 'max'],
            'GDP_Percentage': ['mean', 'max'],
            'Year': 'count'
        }).round(2)
        
        # 2. Top 10 Countries by Total Expenditure
        top_10_exp = self.cleaned_df.groupby('Country')['Expenditure_USD_Million'].sum()\
                                   .sort_values(ascending=False).head(10)
        
        # 3. Most Efficient Countries (Best Expenditure/GDP Ratio)
        country_efficiency = self.cleaned_df.groupby('Country')['Expenditure_GDP_Ratio'].mean()\
                                          .sort_values(ascending=False).head(10)
        
        # 4. Top 5 Countries by GDP Percentage
        top_5_gdp = self.cleaned_df.groupby('Country')['GDP_Percentage'].mean()\
                                  .sort_values(ascending=False).head(5)
        
        # Print results
        print("\n🏆 TOP 10 COUNTRIES BY TOTAL EXPENDITURE:")
        for i, (country, amount) in enumerate(top_10_exp.items(), 1):
            print(f"   {i:2}. {country:30} ${amount:>15,.0f} million")
            
        print("\n📊 TOP 10 MOST EFFICIENT SPENDING COUNTRIES:")
        for i, (country, ratio) in enumerate(country_efficiency.items(), 1):
            print(f"   {i:2}. {country:30} {ratio:>15.2f} (Expenditure/GDP ratio)")
            
        print("\n💰 TOP 5 COUNTRIES BY GDP PERCENTAGE:")
        for i, (country, gdp) in enumerate(top_5_gdp.items(), 1):
            print(f"   {i:2}. {country:30} {gdp:>15.2f}% of GDP")
            
        return {
            'top_10_expenditure': top_10_exp,
            'efficiency_ranking': country_efficiency,
            'top_5_gdp': top_5_gdp
        }
        
    def sector_analysis(self) -> Dict:
        """
        Advanced sector analysis with trends and projections.
        """
        print("\n🏢 SECTOR PERFORMANCE ANALYSIS")
        print(THIN_SEPARATOR)
        
        # 1. Sector Aggregations
        sector_metrics = self.cleaned_df.groupby('Sector').agg({
            'Expenditure_USD_Million': ['sum', 'mean', 'std'],
            'GDP_Percentage': ['mean', 'max']
        }).round(2)
        
        # 2. Top Sectors by Expenditure
        top_sectors = self.cleaned_df.groupby('Sector')['Expenditure_USD_Million'].sum()\
                                    .sort_values(ascending=False).head(10)
        
        # 3. Sector Growth Patterns
        sector_growth = self.cleaned_df.groupby(['Year', 'Sector'])['Expenditure_USD_Million'].sum()\
                                      .unstack(fill_value=0).pct_change().mean() * 100
        
        # 4. Sector Concentration (Top 5 sectors percentage of total)
        total_expenditure = self.cleaned_df['Expenditure_USD_Million'].sum()
        top_5_concentration = top_sectors.head(5).sum() / total_expenditure * 100
        
        print("\n📊 TOP 10 SECTORS BY EXPENDITURE:")
        for i, (sector, amount) in enumerate(top_sectors.items(), 1):
            percentage = (amount / total_expenditure) * 100
            print(f"   {i:2}. {sector:30} ${amount:>15,.0f} million ({percentage:>5.1f}%)")
            
        print(f"\n🔄 TOP 5 SECTORS CONCENTRATION: {top_5_concentration:.1f}% of total expenditure")
        
        print("\n📈 SECTOR GROWTH RATES (Average Year-over-Year):")
        growth_sorted = sector_growth.sort_values(ascending=False).head(10)
        for sector, growth in growth_sorted.items():
            if not np.isnan(growth):
                print(f"   {sector:30} {growth:>15.2f}%")
                
        return {
            'top_sectors': top_sectors,
            'sector_growth': sector_growth,
            'concentration_rate': top_5_concentration
        }
        
    def temporal_analysis(self) -> Dict:
        """
        Time series analysis with trend detection and forecasting.
        """
        print("\n📅 TEMPORAL TREND ANALYSIS")
        print(THIN_SEPARATOR)
        
        # 1. Yearly Aggregations
        yearly_trends = self.cleaned_df.groupby('Year').agg({
            'Expenditure_USD_Million': ['sum', 'mean', 'std'],
            'GDP_Percentage': ['mean']
        }).round(2)
        
        # 2. Year-over-Year Growth
        yearly_total = self.cleaned_df.groupby('Year')['Expenditure_USD_Million'].sum()
        yoy_growth = yearly_total.pct_change() * 100
        
        # 3. Identify Growth Years
        growth_years = yoy_growth[yoy_growth > 5]  # Years with >5% growth
        
        # 4. Decade Analysis
        decade_trends = self.cleaned_df.groupby('Decade').agg({
            'Expenditure_USD_Million': 'sum',
            'GDP_Percentage': 'mean'
        }).round(2)
        
        # 5. Seasonality (Monthly patterns - using year as proxy for seasonality)
        # Calculate average expenditure by year pattern
        year_pattern = self.cleaned_df.groupby('Year')['Expenditure_USD_Million'].mean()
        
        print("\n📊 YEARLY EXPENDITURE TRENDS:")
        print(f"   Total Years Analyzed: {len(yearly_trends)}")
        print(f"   Minimum Year: {yearly_trends.index.min()}")
        print(f"   Maximum Year: {yearly_trends.index.max()}")
        
        print("\n📈 YEAR-OVER-YEAR GROWTH (Top 5 Years):")
        growth_sorted = yoy_growth.sort_values(ascending=False).head(5)
        for year, growth in growth_sorted.items():
            if not np.isnan(growth):
                print(f"   {year}: {growth:>10.2f}% growth")
                
        print(f"\n🚀 HIGH GROWTH YEARS (>5% growth): {len(growth_years)} years identified")
        
        print("\n📆 DECADE-WISE ANALYSIS:")
        for decade, row in decade_trends.iterrows():
            print(f"   {decade}s: ${row['Expenditure_USD_Million']:,.0f} million | "
                  f"Avg GDP: {row['GDP_Percentage']:.2f}%")
                  
        # 6. Trend Direction
        years = yearly_trends.index
        expenditure_trend = yearly_trends[('Expenditure_USD_Million', 'sum')]
        
        # Simple linear regression for trend detection
        if len(years) > 1:
            x = np.arange(len(years))
            z = np.polyfit(x, expenditure_trend.values, 1)
            slope = z[0]
            trend_direction = "INCREASING" if slope > 0 else "DECREASING"
            print(f"\n🔍 OVERALL TREND: {trend_direction} (slope: {slope:,.2f})")
            
        return {
            'yearly_trends': yearly_trends,
            'yoy_growth': yoy_growth,
            'growth_years': growth_years,
            'decade_trends': decade_trends
        }
        
    def advanced_insights(self) -> Dict:
        """
        Generate business intelligence insights and recommendations.
        """
        print("\n💡 ADVANCED BUSINESS INSIGHTS")
        print(THIN_SEPARATOR)
        
        insights = {}
        
        # 1. Identify Best and Worst Performing Countries
        country_avg = self.cleaned_df.groupby('Country')['Expenditure_USD_Million'].mean()
        global_avg = self.cleaned_df['Expenditure_USD_Million'].mean()
        
        above_avg = country_avg[country_avg > global_avg]
        below_avg = country_avg[country_avg < global_avg]
        
        print(f"\n🏅 COUNTRY PERFORMANCE BENCHMARK:")
        print(f"   Global Average Expenditure: ${global_avg:,.2f} million")
        print(f"   Countries Above Average: {len(above_avg)} ({len(above_avg)/len(country_avg)*100:.1f}%)")
        print(f"   Countries Below Average: {len(below_avg)} ({len(below_avg)/len(country_avg)*100:.1f}%)")
        
        # 2. Sector Efficiency Analysis
        sector_efficiency = self.cleaned_df.groupby('Sector').agg({
            'Expenditure_USD_Million': 'sum',
            'GDP_Percentage': 'mean'
        })
        sector_efficiency['Efficiency_Score'] = (
            sector_efficiency['Expenditure_USD_Million'] / 
            (sector_efficiency['GDP_Percentage'] + 0.01)
        )
        
        print(f"\n💼 SECTOR EFFICIENCY RANKING:")
        top_efficient = sector_efficiency.nlargest(5, 'Efficiency_Score')
        for sector, row in top_efficient.iterrows():
            print(f"   {sector:30} Score: {row['Efficiency_Score']:,.2f}")
            
        # 3. Concentration Risk Analysis
        # Check if any country/sector is too dominant
        country_concentration = self.cleaned_df.groupby('Country')['Expenditure_USD_Million'].sum()
        top_country_share = country_concentration.max() / country_concentration.sum() * 100
        
        sector_concentration = self.cleaned_df.groupby('Sector')['Expenditure_USD_Million'].sum()
        top_sector_share = sector_concentration.max() / sector_concentration.sum() * 100
        
        print(f"\n⚠️ CONCENTRATION RISK METRICS:")
        print(f"   Top Country Share: {top_country_share:.1f}% of total expenditure")
        print(f"   Top Sector Share: {top_sector_share:.1f}% of total expenditure")
        
        if top_country_share > 20:
            print("   ⚠️  High country concentration risk detected!")
        if top_sector_share > 30:
            print("   ⚠️  High sector concentration risk detected!")
            
        # 4. Growth Opportunities
        print(f"\n🚀 GROWTH OPPORTUNITIES:")
        
        # Fastest growing sectors
        sector_growth = self.cleaned_df.groupby(['Year', 'Sector'])['Expenditure_USD_Million'].sum()\
                                     .unstack(fill_value=0).pct_change().mean()
        fast_growth = sector_growth.nlargest(5)
        for sector, growth in fast_growth.items():
            if not np.isnan(growth):
                print(f"   {sector:30} {growth:>10.2f}% average growth")
                
        # Countries with potential
        country_growth = self.cleaned_df.groupby(['Year', 'Country'])['Expenditure_USD_Million'].sum()\
                                      .unstack(fill_value=0).pct_change().mean()
        high_potential = country_growth.nlargest(5)
        print("\n   Fastest Growing Countries:")
        for country, growth in high_potential.items():
            if not np.isnan(growth):
                print(f"   {country:30} {growth:>10.2f}% average growth")
                
        return {
            'country_benchmark': {'above_avg': len(above_avg), 'below_avg': len(below_avg)},
            'top_efficient_sectors': top_efficient,
            'concentration_risk': {'country': top_country_share, 'sector': top_sector_share}
        }
        
    def generate_professional_reports(self) -> None:
        """
        Generate and export professional reports with formatted outputs.
        """
        print("\n📄 GENERATING PROFESSIONAL REPORTS")
        print(THIN_SEPARATOR)
        
        # 1. Executive Summary Report
        executive_summary = pd.DataFrame({
            'Metric': [
                'Total Records Analyzed',
                'Countries Covered',
                'Sectors Covered',
                'Years Range',
                'Total Expenditure (Billion USD)',
                'Global Average Expenditure',
                'Highest Expenditure Country',
                'Highest Expenditure Sector',
                'Average GDP Percentage'
            ],
            'Value': [
                f"{len(self.cleaned_df):,}",
                self.cleaned_df['Country'].nunique(),
                self.cleaned_df['Sector'].nunique(),
                f"{self.cleaned_df['Year'].min()} - {self.cleaned_df['Year'].max()}",
                f"{self.cleaned_df['Expenditure_USD_Million'].sum() / 1000:,.2f}",
                f"${self.cleaned_df['Expenditure_USD_Million'].mean():,.2f} million",
                self.cleaned_df.groupby('Country')['Expenditure_USD_Million'].sum().idxmax(),
                self.cleaned_df.groupby('Sector')['Expenditure_USD_Million'].sum().idxmax(),
                f"{self.cleaned_df['GDP_Percentage'].mean():.2f}%"
            ]
        })
        
        executive_summary.to_csv('Executive_Summary.csv', index=False)
        print("✅ Generated: Executive_Summary.csv")
        
        # 2. Detailed Statistical Summary
        statistical_report = pd.DataFrame({
            'Statistic': ['Mean', 'Median', 'Std Dev', 'Min', 'Max', 'Skewness', 'Kurtosis'],
            'Expenditure (Million USD)': [
                self.cleaned_df['Expenditure_USD_Million'].mean(),
                self.cleaned_df['Expenditure_USD_Million'].median(),
                self.cleaned_df['Expenditure_USD_Million'].std(),
                self.cleaned_df['Expenditure_USD_Million'].min(),
                self.cleaned_df['Expenditure_USD_Million'].max(),
                self.cleaned_df['Expenditure_USD_Million'].skew(),
                self.cleaned_df['Expenditure_USD_Million'].kurtosis()
            ],
            'GDP (%)': [
                self.cleaned_df['GDP_Percentage'].mean(),
                self.cleaned_df['GDP_Percentage'].median(),
                self.cleaned_df['GDP_Percentage'].std(),
                self.cleaned_df['GDP_Percentage'].min(),
                self.cleaned_df['GDP_Percentage'].max(),
                self.cleaned_df['GDP_Percentage'].skew(),
                self.cleaned_df['GDP_Percentage'].kurtosis()
            ]
        })
        
        statistical_report.to_csv('Statistical_Report.csv', index=False)
        print("✅ Generated: Statistical_Report.csv")
        
        # 3. Top Performers Report
        top_countries = self.cleaned_df.groupby('Country')['Expenditure_USD_Million'].sum()\
                                     .sort_values(ascending=False).head(20).reset_index()
        top_countries.columns = ['Country', 'Total_Expenditure_USD_Million']
        top_countries.to_csv('Top_Performers_Report.csv', index=False)
        print("✅ Generated: Top_Performers_Report.csv")
        
        # 4. Sector Performance Report
        sector_performance = self.cleaned_df.groupby('Sector')['Expenditure_USD_Million']\
                                           .agg(['sum', 'mean', 'std']).round(2).reset_index()
        sector_performance.columns = ['Sector', 'Total_Expenditure', 'Average_Expenditure', 'Std_Dev']
        sector_performance.to_csv('Sector_Performance_Report.csv', index=False)
        print("✅ Generated: Sector_Performance_Report.csv")
        
        # 5. Outlier Report
        outlier_records = pd.DataFrame()
        for col in ['Expenditure_USD_Million', 'GDP_Percentage']:
            Q1 = self.cleaned_df[col].quantile(0.25)
            Q3 = self.cleaned_df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = self.cleaned_df[(self.cleaned_df[col] < lower_bound) | 
                                      (self.cleaned_df[col] > upper_bound)]
            if len(outliers) > 0:
                outlier_records = pd.concat([outlier_records, outliers])
        
        if len(outlier_records) > 0:
            outlier_records.to_csv('Outlier_Report.csv', index=False)
            print("✅ Generated: Outlier_Report.csv")
            
    def run_complete_analysis(self) -> None:
        """
        Execute the complete analytics pipeline including Pakistan analysis.
        """
        print("\n" + SEPARATOR)
        print("🔍 STARTING COMPLETE ANALYTICS PIPELINE")
        print(SEPARATOR)
        
        # Run all analyses
        country_results = self.country_analysis()
        sector_results = self.sector_analysis()
        temporal_results = self.temporal_analysis()
        insights_results = self.advanced_insights()
        pakistan_results = self.pakistan_detailed_analysis()  # Add this line
        
        # Generate reports
        self.generate_professional_reports()
        
        # Final summary
        self.print_final_summary()
        
        # Execution time
        end_time = datetime.now()
        execution_time = end_time - self.start_time
        print(f"\n⏱️  Total Execution Time: {execution_time.total_seconds():.2f} seconds")
        print(f"✅ Analysis Complete at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(SEPARATOR)
        
    def print_final_summary(self) -> None:
        """
        Print comprehensive final summary with key insights.
        """
        print("\n" + "="*100)
        print("📊 FINAL EXECUTIVE SUMMARY")
        print("="*100)
        
        # Key Statistics
        total_exp = self.cleaned_df['Expenditure_USD_Million'].sum() / 1000
        avg_gdp = self.cleaned_df['GDP_Percentage'].mean()
        
        print(f"""
📌 KEY METRICS:
   • Total Government Expenditure Analyzed: ${total_exp:,.2f} Billion
   • Average GDP Allocation: {avg_gdp:.2f}%
   • Number of Countries: {self.cleaned_df['Country'].nunique():,}
   • Number of Sectors: {self.cleaned_df['Sector'].nunique():,}
   • Time Period: {self.cleaned_df['Year'].min()} - {self.cleaned_df['Year'].max()}
   • Total Records: {len(self.cleaned_df):,}

🏆 TOP PERFORMERS:
   • Top Spending Country: {self.cleaned_df.groupby('Country')['Expenditure_USD_Million'].sum().idxmax()}
   • Top Spending Sector: {self.cleaned_df.groupby('Sector')['Expenditure_USD_Million'].sum().idxmax()}
   • Highest GDP Country: {self.cleaned_df.groupby('Country')['GDP_Percentage'].mean().idxmax()}

📈 TRENDS:
   • Overall Expenditure Trend: {'Increasing' if self.cleaned_df.groupby('Year')['Expenditure_USD_Million'].sum().diff().mean() > 0 else 'Decreasing'}
   • Fastest Growing Sector: {self.cleaned_df.groupby(['Year', 'Sector'])['Expenditure_USD_Million'].sum().unstack(fill_value=0).pct_change().mean().nlargest(1).index[0]}

⚠️  RISK INDICATORS:
   • Outlier Records: {sum([v['count'] for v in self.outliers_detected.values()])}
   • Country Concentration Risk: {'High' if max(self.cleaned_df.groupby('Country')['Expenditure_USD_Million'].sum() / self.cleaned_df['Expenditure_USD_Million'].sum() * 100) > 20 else 'Low'}
""")
        
        print("="*100)

def pakistan_detailed_analysis(self) -> Dict:
    """
    Comprehensive analysis of Pakistan's government expenditure with deep insights.
    Includes sector-wise breakdown, temporal trends, GDP analysis, and international comparisons.
    """
    print("\n" + "="*100)
    print("🇵🇰 PAKISTAN GOVERNMENT EXPENDITURE - COMPREHENSIVE ANALYSIS")
    print("="*100)
    
    # Filter Pakistan data
    pakistan_df = self.cleaned_df[self.cleaned_df['Country'] == 'Pakistan']
    
    if len(pakistan_df) == 0:
        print("\n❌ No data found for Pakistan in the dataset.")
        return {}
    
    print(f"\n📊 DATA OVERVIEW:")
    print(f"   Total Records: {len(pakistan_df)}")
    print(f"   Years Covered: {pakistan_df['Year'].min()} - {pakistan_df['Year'].max()}")
    print(f"   Unique Sectors: {pakistan_df['Sector'].nunique()}")
    print(THIN_SEPARATOR)
    
    # 1. OVERALL EXPENDITURE STATISTICS
    print("\n💰 OVERALL EXPENDITURE STATISTICS:")
    total_expenditure = pakistan_df['Expenditure_USD_Million'].sum()
    avg_expenditure = pakistan_df['Expenditure_USD_Million'].mean()
    max_expenditure = pakistan_df['Expenditure_USD_Million'].max()
    min_expenditure = pakistan_df['Expenditure_USD_Million'].min()
    std_expenditure = pakistan_df['Expenditure_USD_Million'].std()
    
    print(f"   Total Expenditure: ${total_expenditure:,.2f} million USD")
    print(f"   Average Expenditure: ${avg_expenditure:,.2f} million USD")
    print(f"   Maximum Expenditure: ${max_expenditure:,.2f} million USD ({pakistan_df[pakistan_df['Expenditure_USD_Million'] == max_expenditure]['Year'].iloc[0]})")
    print(f"   Minimum Expenditure: ${min_expenditure:,.2f} million USD ({pakistan_df[pakistan_df['Expenditure_USD_Million'] == min_expenditure]['Year'].iloc[0]})")
    print(f"   Standard Deviation: ${std_expenditure:,.2f} million USD")
    print(THIN_SEPARATOR)
    
    # 2. GDP ANALYSIS
    print("\n📈 GDP PERCENTAGE ANALYSIS:")
    avg_gdp = pakistan_df['GDP_Percentage'].mean()
    max_gdp = pakistan_df['GDP_Percentage'].max()
    min_gdp = pakistan_df['GDP_Percentage'].min()
    std_gdp = pakistan_df['GDP_Percentage'].std()
    
    print(f"   Average GDP Percentage: {avg_gdp:.2f}%")
    print(f"   Maximum GDP Percentage: {max_gdp:.2f}% ({pakistan_df[pakistan_df['GDP_Percentage'] == max_gdp]['Year'].iloc[0]})")
    print(f"   Minimum GDP Percentage: {min_gdp:.2f}% ({pakistan_df[pakistan_df['GDP_Percentage'] == min_gdp]['Year'].iloc[0]})")
    print(f"   Standard Deviation: {std_gdp:.2f}%")
    
    # GDP Trend
    gdp_trend = pakistan_df.groupby('Year')['GDP_Percentage'].mean()
    gdp_slope = np.polyfit(range(len(gdp_trend)), gdp_trend.values, 1)[0]
    print(f"   GDP Trend Direction: {'INCREASING' if gdp_slope > 0 else 'DECREASING'} (slope: {gdp_slope:.4f})")
    print(THIN_SEPARATOR)
    
    # 3. SECTOR-WISE ANALYSIS
    print("\n🏢 SECTOR-WISE EXPENDITURE BREAKDOWN:")
    sector_stats = pakistan_df.groupby('Sector').agg({
        'Expenditure_USD_Million': ['sum', 'mean', 'std'],
        'GDP_Percentage': ['mean']
    }).round(2)
    
    # Sort by total expenditure
    sector_stats_sorted = sector_stats.sort_values(('Expenditure_USD_Million', 'sum'), ascending=False)
    
    print("\n   Top 10 Sectors by Total Expenditure:")
    print(f"   {'Sector':<40} {'Total (Million USD)':<20} {'Avg (Million)':<15} {'GDP %':<10}")
    print("   " + "-"*85)
    
    for idx, (sector, row) in enumerate(sector_stats_sorted.head(10).iterrows(), 1):
        total = row[('Expenditure_USD_Million', 'sum')]
        avg = row[('Expenditure_USD_Million', 'mean')]
        gdp = row[('GDP_Percentage', 'mean')]
        percentage = (total / total_expenditure) * 100
        print(f"   {idx:2}. {sector[:38]:<38} ${total:>12,.2f}    ${avg:>10,.2f}    {gdp:>6.2f}% ({percentage:>5.1f}%)")
    
    print(THIN_SEPARATOR)
    
    # 4. TEMPORAL TREND ANALYSIS
    print("\n📅 YEARLY TREND ANALYSIS:")
    yearly_exp = pakistan_df.groupby('Year')['Expenditure_USD_Million'].sum()
    yearly_gdp = pakistan_df.groupby('Year')['GDP_Percentage'].mean()
    
    print("\n   Year-by-Year Breakdown:")
    print(f"   {'Year':<10} {'Expenditure (Million USD)':<25} {'GDP (%)':<12} {'Growth Rate (%)':<15}")
    print("   " + "-"*62)
    
    previous_exp = None
    for year in sorted(yearly_exp.index):
        exp = yearly_exp[year]
        gdp = yearly_gdp[year]
        if previous_exp is not None:
            growth = ((exp - previous_exp) / previous_exp) * 100
            growth_str = f"{growth:>10.2f}%"
        else:
            growth_str = "N/A"
        print(f"   {year:<10} ${exp:>18,.2f}    {gdp:>8.2f}    {growth_str:>15}")
        previous_exp = exp
    
    # Calculate average growth rate
    growth_rates = yearly_exp.pct_change().dropna() * 100
    avg_growth = growth_rates.mean()
    print(f"\n   Average Year-over-Year Growth: {avg_growth:.2f}%")
    
    # Identify growth years
    high_growth_years = growth_rates[growth_rates > 5]
    negative_growth_years = growth_rates[growth_rates < 0]
    
    print(f"   Years with High Growth (>5%): {len(high_growth_years)} years")
    if len(high_growth_years) > 0:
        for year, growth in high_growth_years.items():
            print(f"      • {year}: {growth:.2f}% growth")
    
    print(f"   Years with Negative Growth: {len(negative_growth_years)} years")
    if len(negative_growth_years) > 0:
        for year, growth in negative_growth_years.head(3).items():
            print(f"      • {year}: {growth:.2f}% decline")
    
    print(THIN_SEPARATOR)
    
    # 5. SECTOR CONCENTRATION ANALYSIS
    print("\n🎯 SECTOR CONCENTRATION ANALYSIS:")
    sector_concentration = pakistan_df.groupby('Sector')['Expenditure_USD_Million'].sum()
    sector_concentration_pct = (sector_concentration / total_expenditure) * 100
    
    # Calculate Herfindahl-Hirschman Index (HHI) for sector concentration
    hhi = (sector_concentration_pct ** 2).sum()
    
    print(f"   Sector Concentration (HHI): {hhi:.2f}")
    if hhi < 1500:
        print("   Concentration Level: LOW (Competitive market structure)")
    elif hhi < 2500:
        print("   Concentration Level: MODERATE (Some concentration)")
    else:
        print("   Concentration Level: HIGH (Concentrated market)")
    
    # Top 3 sectors concentration
    top3_concentration = sector_concentration_pct.head(3).sum()
    top5_concentration = sector_concentration_pct.head(5).sum()
    
    print(f"   Top 3 Sectors Account for: {top3_concentration:.1f}% of total expenditure")
    print(f"   Top 5 Sectors Account for: {top5_concentration:.1f}% of total expenditure")
    
    # Identify dominant sectors
    dominant_sectors = sector_concentration_pct[sector_concentration_pct > 10]
    print(f"\n   Dominant Sectors (>10% of total):")
    if len(dominant_sectors) > 0:
        for sector, pct in dominant_sectors.items():
            print(f"      • {sector}: {pct:.1f}%")
    else:
        print("      No single sector dominates (>10%)")
    
    print(THIN_SEPARATOR)
    
    # 6. INTERNATIONAL COMPARISON
    print("\n🌍 INTERNATIONAL COMPARISON:")
    
    # Global averages
    global_avg_exp = self.cleaned_df['Expenditure_USD_Million'].mean()
    global_avg_gdp = self.cleaned_df['GDP_Percentage'].mean()
    
    # Top countries comparison
    top_countries = self.cleaned_df.groupby('Country')['Expenditure_USD_Million'].sum()\
                                 .sort_values(ascending=False).head(10)
    
    pakistan_rank = list(top_countries.index).index('Pakistan') + 1 if 'Pakistan' in top_countries.index else None
    
    print(f"\n   Pakistan's Global Position:")
    print(f"   • Total Expenditure Rank: #{pakistan_rank if pakistan_rank else 'N/A'} among countries")
    print(f"   • Average Expenditure: ${avg_expenditure:,.2f} million vs Global Avg: ${global_avg_exp:,.2f} million")
    print(f"   • Average GDP Percentage: {avg_gdp:.2f}% vs Global Avg: {global_avg_gdp:.2f}%")
    
    # Compare with regional peers (South Asian countries)
    south_asia = ['India', 'Pakistan', 'Bangladesh', 'Sri Lanka', 'Nepal', 'Afghanistan']
    regional_df = self.cleaned_df[self.cleaned_df['Country'].isin(south_asia)]
    
    if len(regional_df) > 0:
        regional_stats = regional_df.groupby('Country')['Expenditure_USD_Million'].sum().sort_values(ascending=False)
        print(f"\n   Regional Comparison (South Asia):")
        print(f"   {'Country':<20} {'Total Expenditure (Million USD)':<30} {'Rank'}")
        print("   " + "-"*60)
        for rank, (country, exp) in enumerate(regional_stats.items(), 1):
            marker = "👑" if country == 'Pakistan' else "  "
            print(f"   {marker} {country:<18} ${exp:>18,.2f}    #{rank}")
    
    print(THIN_SEPARATOR)
    
    # 7. EXPENDITURE EFFICIENCY ANALYSIS
    print("\n⚡ EXPENDITURE EFFICIENCY ANALYSIS:")
    
    # Efficiency metrics
    pakistan_efficiency = pakistan_df.groupby('Sector').agg({
        'Expenditure_USD_Million': 'sum',
        'GDP_Percentage': 'mean'
    })
    pakistan_efficiency['Efficiency_Score'] = (
        pakistan_efficiency['Expenditure_USD_Million'] / 
        (pakistan_efficiency['GDP_Percentage'] + 0.01)
    )
    
    print("\n   Most Efficient Sectors (Highest Expenditure per GDP %):")
    efficient_sectors = pakistan_efficiency.nlargest(5, 'Efficiency_Score')
    for sector, row in efficient_sectors.iterrows():
        print(f"      • {sector}: {row['Efficiency_Score']:,.2f} million USD per 1% GDP")
    
    print("\n   Least Efficient Sectors (Lowest Expenditure per GDP %):")
    inefficient_sectors = pakistan_efficiency.nsmallest(5, 'Efficiency_Score')
    for sector, row in inefficient_sectors.iterrows():
        print(f"      • {sector}: {row['Efficiency_Score']:,.2f} million USD per 1% GDP")
    
    print(THIN_SEPARATOR)
    
    # 8. PREDICTIVE INSIGHTS
    print("\n🔮 PREDICTIVE INSIGHTS & RECOMMENDATIONS:")
    
    # Identify trends and patterns
    recent_trend = yearly_exp.tail(5).mean() - yearly_exp.head(5).mean()
    trend_direction = "upward" if recent_trend > 0 else "downward"
    
    print(f"\n   1. Recent Trend (Last 5 years vs First 5 years):")
    print(f"      Pakistan's expenditure is showing a {trend_direction} trend.")
    
    # Identify sectors with growth potential
    sector_growth = pakistan_df.groupby(['Year', 'Sector'])['Expenditure_USD_Million'].sum()\
                             .unstack(fill_value=0).pct_change().mean()
    fast_growing = sector_growth.nlargest(5)
    slow_growing = sector_growth.nsmallest(5)
    
    print(f"\n   2. Sector Growth Opportunities:")
    print(f"      Fastest Growing Sectors:")
    for sector, growth in fast_growing.items():
        if not np.isnan(growth):
            print(f"      • {sector}: {growth:.1f}% average growth")
    
    print(f"\n      Declining Sectors (Need attention):")
    for sector, growth in slow_growing.items():
        if not np.isnan(growth) and growth < 0:
            print(f"      • {sector}: {growth:.1f}% average decline")
    
    # Diversification recommendation
    print(f"\n   3. Diversification Recommendation:")
    if hhi > 2500:
        print(f"      ⚠️  Pakistan's expenditure is highly concentrated (HHI: {hhi:.2f})")
        print(f"      Recommendation: Diversify spending across more sectors to reduce risk")
    else:
        print(f"      ✅ Pakistan's expenditure is well diversified (HHI: {hhi:.2f})")
    
    # GDP efficiency recommendation
    if avg_gdp < global_avg_gdp:
        print(f"\n   4. GDP Allocation Recommendation:")
        print(f"      ⚠️  Pakistan's GDP allocation ({avg_gdp:.2f}%) is below global average ({global_avg_gdp:.2f}%)")
        print(f"      Recommendation: Consider increasing government expenditure as % of GDP")
    
    print(THIN_SEPARATOR)
    
    # 9. SUMMARY STATISTICS DICTIONARY
    print("\n📊 COMPREHENSIVE PAKISTAN DATA SUMMARY:")
    
    pakistan_summary = {
        'Country': 'Pakistan',
        'Total_Records': len(pakistan_df),
        'Years_Analyzed': f"{pakistan_df['Year'].min()} - {pakistan_df['Year'].max()}",
        'Total_Expenditure_Million_USD': total_expenditure,
        'Average_Expenditure_Million_USD': avg_expenditure,
        'Max_Expenditure_Million_USD': max_expenditure,
        'Min_Expenditure_Million_USD': min_expenditure,
        'Average_GDP_Percentage': avg_gdp,
        'Max_GDP_Percentage': max_gdp,
        'Min_GDP_Percentage': min_gdp,
        'Number_of_Sectors': pakistan_df['Sector'].nunique(),
        'HHI_Concentration': hhi,
        'Average_Growth_Rate': avg_growth,
        'Global_Rank': pakistan_rank,
        'Trend_Direction': trend_direction,
        'Top_3_Sector_Concentration': top3_concentration,
        'Top_5_Sector_Concentration': top5_concentration,
        'Efficiency_Score': pakistan_efficiency['Efficiency_Score'].mean()
    }
    
    print("\n   Key Metrics:")
    for key, value in pakistan_summary.items():
        if isinstance(value, (int, float)):
            if 'Million' in key or 'Expenditure' in key:
                print(f"   • {key}: ${value:,.2f}")
            elif 'Percentage' in key or 'GDP' in key:
                print(f"   • {key}: {value:.2f}%")
            else:
                print(f"   • {key}: {value}")
        else:
            print(f"   • {key}: {value}")
    
    print("\n" + "="*100)
    print("🇵🇰 PAKISTAN ANALYSIS COMPLETE")
    print("="*100)
    
    # Export Pakistan-specific report
    self._export_pakistan_report(pakistan_df, pakistan_summary)
    
    return pakistan_summary

def _export_pakistan_report(self, pakistan_df: pd.DataFrame, summary: Dict) -> None:
    """
    Export comprehensive Pakistan analysis report.
    """
    print("\n📄 GENERATING PAKISTAN REPORT...")
    
    # 1. Full Pakistan dataset
    pakistan_df.to_csv('Pakistan_Full_Data.csv', index=False)
    print("✅ Exported: Pakistan_Full_Data.csv")
    
    # 2. Sector-wise summary
    sector_summary = pakistan_df.groupby('Sector').agg({
        'Expenditure_USD_Million': ['sum', 'mean', 'std', 'min', 'max'],
        'GDP_Percentage': ['mean', 'min', 'max']
    }).round(2)
    sector_summary.to_csv('Pakistan_Sector_Summary.csv')
    print("✅ Exported: Pakistan_Sector_Summary.csv")
    
    # 3. Yearly summary
    yearly_summary = pakistan_df.groupby('Year').agg({
        'Expenditure_USD_Million': ['sum', 'mean', 'std'],
        'GDP_Percentage': ['mean', 'std']
    }).round(2)
    yearly_summary.to_csv('Pakistan_Yearly_Summary.csv')
    print("✅ Exported: Pakistan_Yearly_Summary.csv")
    
    # 4. Executive summary
    summary_df = pd.DataFrame([summary])
    summary_df.to_csv('Pakistan_Executive_Summary.csv', index=False)
    print("✅ Exported: Pakistan_Executive_Summary.csv")
    
    # 5. Top sectors report
    top_sectors = pakistan_df.groupby('Sector')['Expenditure_USD_Million'].sum()\
                           .sort_values(ascending=False).head(10).reset_index()
    top_sectors.columns = ['Sector', 'Total_Expenditure_Million_USD']
    top_sectors['Percentage_of_Total'] = (top_sectors['Total_Expenditure_Million_USD'] / 
                                         top_sectors['Total_Expenditure_Million_USD'].sum()) * 100
    top_sectors.to_csv('Pakistan_Top_Sectors.csv', index=False)
    print("✅ Exported: Pakistan_Top_Sectors.csv")
    
    print("\n📁 All Pakistan reports exported successfully!")


def main():
    """
    Main execution function.
    """
    try:
        # Initialize analytics engine
        analytics = GovernmentExpenditureAnalytics('WorldExpenditures.csv')
        
        # Run complete analysis
        analytics.run_complete_analysis()
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("   Please check your data file and try again.")
        sys.exit(1)


if __name__ == "__main__":
    main()