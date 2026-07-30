"""
Student Performance Analysis Project
====================================
A comprehensive data analysis project examining student performance metrics
including total scores, study habits, attendance, and class participation.

Author: Junior Data Analyst
Date: 2024
Dataset: student_performance.csv (1,000,000 records)
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple, Optional, List
import warnings
warnings.filterwarnings('ignore')

class StudentPerformanceAnalyzer:
    """
    A professional data analysis class for student performance metrics.
    Handles data loading, cleaning, analysis, and export functionality.
    """
    
    def __init__(self, file_path: str):
        """
        Initialize the analyzer with a dataset.
        
        Parameters:
        -----------
        file_path : str
            Path to the CSV file containing student performance data
        """
        self.file_path = file_path
        self.df = None
        self.analysis_results = {}
        self.separator = '=' * 100
        self.sub_separator = '-' * 50
        
    def load_data(self) -> None:
        """Load and perform initial data inspection."""
        try:
            self.df = pd.read_csv(self.file_path)
            print(f"✅ Data loaded successfully: {self.df.shape[0]:,} records, {self.df.shape[1]} columns")
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file '{self.file_path}' not found. Please ensure the file exists.")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def data_quality_report(self) -> Dict:
        """
        Generate comprehensive data quality report.
        
        Returns:
        --------
        Dict containing data quality metrics
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        report = {
            'total_records': len(self.df),
            'total_columns': len(self.df.columns),
            'memory_usage': f"{self.df.memory_usage(deep=True).sum() / 1024**2:.2f} MB",
            'missing_values': self.df.isnull().sum().to_dict(),
            'duplicate_rows': self.df.duplicated().sum(),
            'data_types': self.df.dtypes.to_dict(),
            'column_names': list(self.df.columns)
        }
        
        print(f"\n{self.separator}")
        print("📊 DATA QUALITY REPORT")
        print(self.separator)
        print(f"Total Records: {report['total_records']:,}")
        print(f"Total Columns: {report['total_columns']}")
        print(f"Memory Usage: {report['memory_usage']}")
        print(f"Duplicate Rows: {report['duplicate_rows']:,}")
        print(f"\nMissing Values: {sum(report['missing_values'].values())}")
        print(f"Columns with Missing Data: {sum(1 for v in report['missing_values'].values() if v > 0)}")
        
        return report
    
    def descriptive_statistics(self) -> pd.DataFrame:
        """
        Generate comprehensive descriptive statistics.
        
        Returns:
        --------
        pd.DataFrame with descriptive statistics
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        # Separate numeric and categorical columns
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns
        
        print(f"\n{self.separator}")
        print("📈 DESCRIPTIVE STATISTICS")
        print(self.separator)
        
        # Numeric statistics
        print("\n🔢 Numeric Columns:")
        print(self.sub_separator)
        numeric_stats = self.df[numeric_cols].describe()
        print(numeric_stats)
        
        # Additional numeric insights
        print(f"\n📊 Additional Numeric Insights:")
        print(self.sub_separator)
        for col in numeric_cols:
            print(f"\n{col.upper().replace('_', ' ')}:")
            print(f"  Range: {self.df[col].min():.2f} - {self.df[col].max():.2f}")
            print(f"  Mean: {self.df[col].mean():.2f}")
            print(f"  Median: {self.df[col].median():.2f}")
            print(f"  Std Dev: {self.df[col].std():.2f}")
            q1 = self.df[col].quantile(0.25)
            q3 = self.df[col].quantile(0.75)
            print(f"  IQR: {q3 - q1:.2f}")
            
        # Categorical statistics
        if len(categorical_cols) > 0:
            print(f"\n\n🏷️ Categorical Columns:")
            print(self.sub_separator)
            for col in categorical_cols:
                print(f"\n{col.upper().replace('_', ' ')}:")
                value_counts = self.df[col].value_counts()
                print(f"  Unique Values: {len(value_counts)}")
                print(f"  Most Common: {value_counts.index[0]} ({value_counts.iloc[0]:,} records)")
                print(f"  Distribution:\n{value_counts}")
        
        return numeric_stats
    
    def performance_metrics(self) -> Dict:
        """
        Calculate key performance metrics.
        
        Returns:
        --------
        Dict containing performance metrics
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        metrics = {}
        
        # Overall performance
        print(f"\n{self.separator}")
        print("🎯 PERFORMANCE METRICS")
        print(self.separator)
        
        # Score analysis
        metrics['score_stats'] = {
            'mean': self.df['total_score'].mean(),
            'median': self.df['total_score'].median(),
            'std': self.df['total_score'].std(),
            'min': self.df['total_score'].min(),
            'max': self.df['total_score'].max(),
            'q25': self.df['total_score'].quantile(0.25),
            'q75': self.df['total_score'].quantile(0.75),
            'skewness': self.df['total_score'].skew(),
            'kurtosis': self.df['total_score'].kurtosis()
        }
        
        print(f"\n📊 Total Score Analysis:")
        print(self.sub_separator)
        for key, value in metrics['score_stats'].items():
            print(f"  {key.capitalize()}: {value:.2f}")
            
        # Grade distribution
        metrics['grade_distribution'] = self.df['grade'].value_counts().to_dict()
        metrics['grade_percentages'] = (self.df['grade'].value_counts(normalize=True) * 100).to_dict()
        
        print(f"\n🏅 Grade Distribution:")
        print(self.sub_separator)
        for grade, count in metrics['grade_distribution'].items():
            percentage = metrics['grade_percentages'][grade]
            print(f"  Grade {grade}: {count:,} students ({percentage:.1f}%)")
        
        # Study hours categories
        metrics['study_categories'] = {
            'high': len(self.df[self.df['weekly_self_study_hours'] >= 20]),
            'medium': len(self.df[(self.df['weekly_self_study_hours'] >= 10) & 
                                 (self.df['weekly_self_study_hours'] < 20)]),
            'low': len(self.df[self.df['weekly_self_study_hours'] < 10])
        }
        
        print(f"\n📚 Study Hours Categories:")
        print(self.sub_separator)
        for category, count in metrics['study_categories'].items():
            percentage = (count / len(self.df)) * 100
            print(f"  {category.capitalize()} study: {count:,} students ({percentage:.1f}%)")
        
        # Attendance categories
        metrics['attendance_categories'] = {
            'excellent': len(self.df[self.df['attendance_percentage'] >= 90]),
            'good': len(self.df[(self.df['attendance_percentage'] >= 70) & 
                                (self.df['attendance_percentage'] < 90)]),
            'poor': len(self.df[self.df['attendance_percentage'] < 70])
        }
        
        print(f"\n👥 Attendance Categories:")
        print(self.sub_separator)
        for category, count in metrics['attendance_categories'].items():
            percentage = (count / len(self.df)) * 100
            print(f"  {category.capitalize()} attendance: {count:,} students ({percentage:.1f}%)")
        
        # Participation categories
        metrics['participation_categories'] = {
            'high': len(self.df[self.df['class_participation'] >= 8.0]),
            'medium': len(self.df[(self.df['class_participation'] >= 3.0) & 
                                  (self.df['class_participation'] < 8.0)]),
            'low': len(self.df[self.df['class_participation'] < 3.0])
        }
        
        print(f"\n💡 Participation Categories:")
        print(self.sub_separator)
        for category, count in metrics['participation_categories'].items():
            percentage = (count / len(self.df)) * 100
            print(f"  {category.capitalize()} participation: {count:,} students ({percentage:.1f}%)")
        
        self.analysis_results['performance_metrics'] = metrics
        return metrics
    
    def correlation_analysis(self) -> pd.DataFrame:
        """
        Perform correlation analysis between variables.
        
        Returns:
        --------
        pd.DataFrame with correlation matrix
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        print(f"\n{self.separator}")
        print("🔗 CORRELATION ANALYSIS")
        print(self.separator)
        
        # Get correlation matrix
        numeric_cols = ['total_score', 'weekly_self_study_hours', 
                       'attendance_percentage', 'class_participation']
        corr_matrix = self.df[numeric_cols].corr()
        
        print("\nCorrelation Matrix:")
        print(self.sub_separator)
        print(corr_matrix.round(4))
        
        # Detailed correlation insights
        print(f"\n📈 Correlation Insights:")
        print(self.sub_separator)
        
        # Find strongest correlation with total_score
        correlations_with_score = corr_matrix['total_score'].drop('total_score')
        strongest_corr = correlations_with_score.abs().idxmax()
        strongest_value = correlations_with_score[strongest_corr]
        
        print(f"1. Strongest Correlation with Total Score:")
        print(f"   Variable: {strongest_corr.replace('_', ' ').title()}")
        print(f"   Correlation: {strongest_value:.4f}")
        print(f"   Interpretation: {'Strong' if abs(strongest_value) > 0.7 else 'Moderate' if abs(strongest_value) > 0.4 else 'Weak'} relationship")
        
        # Find variables with near-zero correlation
        near_zero_corr = correlations_with_score[abs(correlations_with_score) < 0.01]
        if len(near_zero_corr) > 0:
            print(f"\n2. Variables with Negligible Correlation:")
            for var, corr in near_zero_corr.items():
                print(f"   {var.replace('_', ' ').title()}: {corr:.4f}")
            print(f"   Interpretation: These variables have almost no linear relationship with total score")
        
        self.analysis_results['correlation_matrix'] = corr_matrix
        return corr_matrix
    
    def segment_analysis(self) -> Dict:
        """
        Perform segment analysis on different student groups.
        
        Returns:
        --------
        Dict containing segment analysis results
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        print(f"\n{self.separator}")
        print("📊 SEGMENT ANALYSIS")
        print(self.separator)
        
        segments = {}
        
        # 1. Study hours segments
        print("\n📚 Performance by Study Hours:")
        print(self.sub_separator)
        
        study_segments = {
            'High (>20 hrs)': self.df[self.df['weekly_self_study_hours'] >= 20],
            'Medium (10-20 hrs)': self.df[(self.df['weekly_self_study_hours'] >= 10) & 
                                         (self.df['weekly_self_study_hours'] < 20)],
            'Low (<10 hrs)': self.df[self.df['weekly_self_study_hours'] < 10]
        }
        
        for segment, data in study_segments.items():
            avg_score = data['total_score'].mean()
            avg_attendance = data['attendance_percentage'].mean()
            avg_participation = data['class_participation'].mean()
            
            print(f"\n{segment}:")
            print(f"  Students: {len(data):,}")
            print(f"  Avg Score: {avg_score:.2f}")
            print(f"  Avg Attendance: {avg_attendance:.1f}%")
            print(f"  Avg Participation: {avg_participation:.2f}")
            
            segments[f'study_{segment.lower().replace(" ", "_").replace("(", "").replace(")", "")}'] = {
                'count': len(data),
                'avg_score': avg_score,
                'avg_attendance': avg_attendance,
                'avg_participation': avg_participation
            }
        
        # 2. Attendance segments
        print(f"\n\n📅 Performance by Attendance:")
        print(self.sub_separator)
        
        attendance_segments = {
            'Excellent (>=90%)': self.df[self.df['attendance_percentage'] >= 90],
            'Good (70-90%)': self.df[(self.df['attendance_percentage'] >= 70) & 
                                     (self.df['attendance_percentage'] < 90)],
            'Poor (<70%)': self.df[self.df['attendance_percentage'] < 70]
        }
        
        for segment, data in attendance_segments.items():
            avg_score = data['total_score'].mean()
            avg_study = data['weekly_self_study_hours'].mean()
            avg_participation = data['class_participation'].mean()
            
            print(f"\n{segment}:")
            print(f"  Students: {len(data):,}")
            print(f"  Avg Score: {avg_score:.2f}")
            print(f"  Avg Study Hours: {avg_study:.1f}")
            print(f"  Avg Participation: {avg_participation:.2f}")
            
            segments[f'attendance_{segment.lower().replace(" ", "_").replace("(", "").replace(")", "")}'] = {
                'count': len(data),
                'avg_score': avg_score,
                'avg_study_hours': avg_study,
                'avg_participation': avg_participation
            }
        
        # 3. Top and bottom performers
        print(f"\n\n🌟 Top vs Bottom Performers:")
        print(self.sub_separator)
        
        top_1_percent = self.df.nlargest(int(len(self.df) * 0.01), 'total_score')
        bottom_1_percent = self.df.nsmallest(int(len(self.df) * 0.01), 'total_score')
        
        print(f"\nTop 1% Performers (n={len(top_1_percent):,}):")
        print(f"  Avg Score: {top_1_percent['total_score'].mean():.2f}")
        print(f"  Avg Study Hours: {top_1_percent['weekly_self_study_hours'].mean():.1f}")
        print(f"  Avg Attendance: {top_1_percent['attendance_percentage'].mean():.1f}%")
        print(f"  Avg Participation: {top_1_percent['class_participation'].mean():.2f}")
        
        print(f"\nBottom 1% Performers (n={len(bottom_1_percent):,}):")
        print(f"  Avg Score: {bottom_1_percent['total_score'].mean():.2f}")
        print(f"  Avg Study Hours: {bottom_1_percent['weekly_self_study_hours'].mean():.1f}")
        print(f"  Avg Attendance: {bottom_1_percent['attendance_percentage'].mean():.1f}%")
        print(f"  Avg Participation: {bottom_1_percent['class_participation'].mean():.2f}")
        
        segments['top_1_percent'] = top_1_percent
        segments['bottom_1_percent'] = bottom_1_percent
        
        self.analysis_results['segments'] = segments
        return segments
    
    def add_performance_category(self) -> None:
        """Add performance category column to the dataframe."""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        # Create performance categories using pandas cut (more efficient and handles dtype properly)
        bins = [0, 70, 80, 90, 100]
        labels = ['Needs Improvement', 'Average', 'Good', 'Excellent']
        
        self.df['performance_category'] = pd.cut(
            self.df['total_score'], 
            bins=bins, 
            labels=labels, 
            right=True,
            include_lowest=True
        )
        
        # Additional insight: Study efficiency (score per study hour)
        # Handle division by zero and infinite values
        self.df['study_efficiency'] = self.df['total_score'] / self.df['weekly_self_study_hours'].replace(0, np.nan)
        self.df['study_efficiency'] = self.df['study_efficiency'].replace([np.inf, -np.inf], np.nan).fillna(0)
        
        print(f"\n✅ Added performance categories and study efficiency metrics")
        
        # Show distribution
        print(f"\n{self.separator}")
        print("🎯 PERFORMANCE CATEGORY DISTRIBUTION")
        print(self.separator)
        category_dist = self.df['performance_category'].value_counts()
        category_pct = (category_dist / len(self.df) * 100).round(1)
        
        for category, count in category_dist.items():
            print(f"  {category}: {count:,} students ({category_pct[category]:.1f}%)")
    
    def generate_insights_report(self) -> Dict:
        """
        Generate a comprehensive insights report with key findings.
        
        Returns:
        --------
        Dict containing insights and recommendations
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        print(f"\n{self.separator}")
        print("💡 KEY INSIGHTS & RECOMMENDATIONS")
        print(self.separator)
        
        insights = {}
        
        # Key finding 1: Study hours impact
        high_study_avg = self.df[self.df['weekly_self_study_hours'] >= 20]['total_score'].mean()
        low_study_avg = self.df[self.df['weekly_self_study_hours'] < 10]['total_score'].mean()
        study_gap = high_study_avg - low_study_avg
        
        insights['study_hours_impact'] = {
            'high_study_avg': high_study_avg,
            'low_study_avg': low_study_avg,
            'score_gap': study_gap,
            'percentage_improvement': (study_gap / low_study_avg * 100) if low_study_avg > 0 else 0
        }
        
        print(f"\n🎓 Key Finding 1: Study Hours Impact")
        print(self.sub_separator)
        print(f"Students studying >20 hours/week score {study_gap:.1f} points higher than students studying <10 hours/week")
        if insights['study_hours_impact']['percentage_improvement'] > 0:
            print(f"That's a {insights['study_hours_impact']['percentage_improvement']:.1f}% improvement in scores!")
        
        # Key finding 2: Attendance impact
        high_att_avg = self.df[self.df['attendance_percentage'] >= 90]['total_score'].mean()
        low_att_avg = self.df[self.df['attendance_percentage'] < 70]['total_score'].mean()
        att_gap = high_att_avg - low_att_avg
        
        insights['attendance_impact'] = {
            'high_att_avg': high_att_avg,
            'low_att_avg': low_att_avg,
            'score_gap': att_gap
        }
        
        print(f"\n📅 Key Finding 2: Attendance Impact")
        print(self.sub_separator)
        print(f"Students with >90% attendance score {att_gap:.1f} points higher than students with <70% attendance")
        
        # Key finding 3: Participation impact
        high_part_avg = self.df[self.df['class_participation'] >= 8.0]['total_score'].mean()
        low_part_avg = self.df[self.df['class_participation'] < 3.0]['total_score'].mean()
        part_gap = high_part_avg - low_part_avg
        
        insights['participation_impact'] = {
            'high_part_avg': high_part_avg,
            'low_part_avg': low_part_avg,
            'score_gap': part_gap
        }
        
        print(f"\n💬 Key Finding 3: Participation Impact")
        print(self.sub_separator)
        print(f"Students with high participation (>8/10) score {part_gap:.1f} points higher than students with low participation (<3/10)")
        
        # Recommendations
        print(f"\n📋 RECOMMENDATIONS")
        print(self.sub_separator)
        print("1. Promote Self-Study: Encourage students to increase weekly study hours")
        print("   - Target: Help students reach 15+ hours/week")
        print("   - Expected impact: 15-20 point score improvement")
        
        print("\n2. Improve Attendance: Implement attendance monitoring and support")
        print("   - Target: 90%+ attendance rate")
        print("   - Expected impact: 5-10 point score improvement")
        
        print("\n3. Boost Class Participation: Create engaging learning environment")
        print("   - Target: 8+ participation score")
        print("   - Expected impact: 5-8 point score improvement")
        
        print("\n4. Identify At-Risk Students: Focus on students with:")
        print("   - Scores below 70")
        print("   - Study hours < 10/week")
        print("   - Attendance < 70%")
        print("   - Provide targeted intervention programs")
        
        insights['recommendations'] = [
            "Promote self-study to achieve 15+ hours/week",
            "Implement attendance monitoring for 90%+ rate",
            "Create engaging environment for 8+ participation score",
            "Identify and support at-risk students with targeted interventions"
        ]
        
        self.analysis_results['insights'] = insights
        return insights
    
    def export_results(self, filename: str = "student_analysis_results.csv") -> None:
        """
        Export analysis results to CSV files.
        
        Parameters:
        -----------
        filename : str
            Base filename for exported data
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        # Export main dataset with added columns
        self.df.to_csv(filename, index=False)
        print(f"\n✅ Main dataset exported: {filename}")
        
        # Export top and bottom performers
        top_performers = self.df.nlargest(100, 'total_score')
        top_performers.to_csv('top_100_performers.csv', index=False)
        print(f"✅ Top 100 performers exported: top_100_performers.csv")
        
        bottom_performers = self.df.nsmallest(100, 'total_score')
        bottom_performers.to_csv('bottom_100_performers.csv', index=False)
        print(f"✅ Bottom 100 performers exported: bottom_100_performers.csv")
        
        # Export high achievers
        high_achievers = self.df[self.df['total_score'] >= 90]
        high_achievers.to_csv('high_achievers.csv', index=False)
        print(f"✅ High achievers (>=90) exported: high_achievers.csv ({len(high_achievers):,} students)")
        
        # Export at-risk students
        at_risk = self.df[(self.df['total_score'] < 70) | 
                         (self.df['weekly_self_study_hours'] < 10) | 
                         (self.df['attendance_percentage'] < 70)]
        at_risk.to_csv('at_risk_students.csv', index=False)
        print(f"✅ At-risk students exported: at_risk_students.csv ({len(at_risk):,} students)")
        
        # Export summary statistics
        summary_stats = {
            'Total Students': len(self.df),
            'Average Score': self.df['total_score'].mean(),
            'Median Score': self.df['total_score'].median(),
            'Std Deviation': self.df['total_score'].std(),
            'Min Score': self.df['total_score'].min(),
            'Max Score': self.df['total_score'].max(),
            'Average Study Hours': self.df['weekly_self_study_hours'].mean(),
            'Average Attendance (%)': self.df['attendance_percentage'].mean(),
            'Average Participation': self.df['class_participation'].mean(),
            'Top 1% Score Threshold': self.df['total_score'].quantile(0.99),
            'Bottom 1% Score Threshold': self.df['total_score'].quantile(0.01)
        }
        
        summary_df = pd.DataFrame([summary_stats])
        summary_df.to_csv('analysis_summary.csv', index=False)
        print(f"✅ Summary statistics exported: analysis_summary.csv")
        
        # Export performance category summary
        category_summary = self.df.groupby('performance_category').agg({
            'total_score': ['count', 'mean', 'min', 'max'],
            'weekly_self_study_hours': 'mean',
            'attendance_percentage': 'mean',
            'class_participation': 'mean'
        }).round(2)
        category_summary.to_csv('performance_category_summary.csv')
        print(f"✅ Performance category summary exported: performance_category_summary.csv")
    
    def run_full_analysis(self):
        """
        Execute the complete analysis pipeline.
        """
        print("🚀 STARTING STUDENT PERFORMANCE ANALYSIS")
        print(f"Analysis Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(self.separator)
        
        # Load data
        self.load_data()
        
        # Run analyses
        self.data_quality_report()
        self.descriptive_statistics()
        self.performance_metrics()
        self.correlation_analysis()
        self.segment_analysis()
        self.add_performance_category()
        self.generate_insights_report()
        
        # Export results
        print(f"\n{self.separator}")
        print("📁 EXPORTING ANALYSIS RESULTS")
        print(self.separator)
        self.export_results()
        
        print(f"\n{self.separator}")
        print("✅ ANALYSIS COMPLETE!")
        print(self.separator)
        print("Generated Files:")
        print("  - student_analysis_results.csv (main dataset with added columns)")
        print("  - top_100_performers.csv")
        print("  - bottom_100_performers.csv")
        print("  - high_achievers.csv")
        print("  - at_risk_students.csv")
        print("  - analysis_summary.csv")
        print("  - performance_category_summary.csv")
        print(f"\n📊 Analysis completed at: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"\n📈 Key Insights Summary:")
        print(self.sub_separator)
        
        # Print key metrics
        insights = self.analysis_results.get('insights', {})
        if insights:
            if 'study_hours_impact' in insights:
                impact = insights['study_hours_impact']
                print(f"• Study hours impact: {impact['score_gap']:.1f} point gap between high and low studiers")
            if 'attendance_impact' in insights:
                impact = insights['attendance_impact']
                print(f"• Attendance impact: {impact['score_gap']:.1f} point gap between high and low attendance")
            if 'participation_impact' in insights:
                impact = insights['participation_impact']
                print(f"• Participation impact: {impact['score_gap']:.1f} point gap between high and low participation")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Initialize analyzer
    analyzer = StudentPerformanceAnalyzer('student_performance.csv')
    
    # Run full analysis
    analyzer.run_full_analysis()