"""
Student Exam Performance Analysis
A small data analysis project using pandas and numpy essentials
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==================== 1. CREATE SAMPLE DATA ====================
print("="*50)
print("STUDENT EXAM PERFORMANCE ANALYSIS")
print("="*50)

# Create sample data
np.random.seed(42)  # For reproducible results

students = {
    'Student_ID': [f'S{str(i).zfill(3)}' for i in range(1, 51)],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack',
             'Karen', 'Leo', 'Mia', 'Noah', 'Olivia', 'Peter', 'Quinn', 'Rachel', 'Sam', 'Tina',
             'Ulysses', 'Vera', 'Will', 'Xena', 'Yara', 'Zane', 'Amy', 'Brian', 'Cathy', 'Dylan',
             'Elena', 'Felix', 'Gina', 'Hugo', 'Iris', 'Jake', 'Kyle', 'Laura', 'Mark', 'Nina',
             'Oscar', 'Paula', 'Ricky', 'Sara', 'Tom', 'Uma', 'Victor', 'Wendy', 'Xavier', 'Yvonne'],
    'Gender': np.random.choice(['M', 'F'], 50, p=[0.5, 0.5]),
    'Age': np.random.randint(18, 25, 50),
    'Attendance': np.random.randint(60, 100, 50),  # Percentage
    'Study_Hours': np.random.uniform(1, 8, 50).round(1),
    'Previous_GPA': np.random.uniform(2.0, 4.0, 50).round(2),
    'Math_Score': np.random.randint(45, 100, 50),
    'Science_Score': np.random.randint(40, 98, 50),
    'English_Score': np.random.randint(50, 99, 50)
}

df = pd.DataFrame(students)

# Add some missing values for practice
df.loc[7, 'Study_Hours'] = np.nan  # Missing value
df.loc[12, 'Attendance'] = np.nan
df.loc[25, 'Previous_GPA'] = np.nan

# ==================== 2. DATA EXPLORATION ====================
print("\n📊 1. DATA OVERVIEW")
print("-"*50)

# Basic info
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# ==================== 3. DATA CLEANING ====================
print("\n🧹 2. DATA CLEANING")
print("-"*50)

# Fill missing values with mean/median
df['Study_Hours'] = df['Study_Hours'].fillna(df['Study_Hours'].mean())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].median())
df['Previous_GPA'] = df['Previous_GPA'].fillna(df['Previous_GPA'].mean())

# Create new derived columns
df['Total_Score'] = df['Math_Score'] + df['Science_Score'] + df['English_Score']
df['Average_Score'] = df['Total_Score'] / 3
df['Average_Score_Rounded'] = df['Average_Score'].round(2)

# Grade classification using numpy
conditions = [
    df['Average_Score'] >= 85,
    df['Average_Score'] >= 70,
    df['Average_Score'] >= 60,
    df['Average_Score'] >= 50
]
grades = ['A', 'B', 'C', 'D']
df['Grade'] = np.select(conditions, grades, default='F')

# Performance status
df['Performance'] = np.where(df['Average_Score'] >= 70, 'Pass', 'Fail')

print("After cleaning:")
print(f"Missing values remaining: {df.isnull().sum().sum()}")
print("\nNew columns added:")
print("- Total_Score, Average_Score, Grade, Performance")

# ==================== 4. DATA ANALYSIS ====================
print("\n📈 3. KEY INSIGHTS")
print("-"*50)

# Group by Gender
gender_stats = df.groupby('Gender').agg({
    'Average_Score': ['mean', 'std', 'min', 'max'],
    'Study_Hours': 'mean',
    'Attendance': 'mean'
})
print("\nGender Statistics:")
print(gender_stats)

# Group by Grade
grade_counts = df['Grade'].value_counts().sort_index()
print("\nGrade Distribution:")
print(grade_counts)

# Performance by grade
perf_by_grade = df.groupby('Grade')['Performance'].value_counts()
print("\nPerformance by Grade:")
print(perf_by_grade)

# Correlation analysis
numeric_cols = ['Age', 'Attendance', 'Study_Hours', 'Previous_GPA', 
                'Math_Score', 'Science_Score', 'English_Score', 'Average_Score']
correlation = df[numeric_cols].corr()
print("\nCorrelation Matrix (key insights):")
print("Correlation with Average_Score:")
print(correlation['Average_Score'].sort_values(ascending=False))

# ==================== 5. ADDITIONAL ANALYSIS ====================
print("\n🔍 4. ADDITIONAL ANALYSIS")
print("-"*50)

# Top performing students
top_5 = df.nlargest(5, 'Average_Score')[['Name', 'Average_Score', 'Grade', 'Study_Hours']]
print("\nTop 5 Students:")
print(top_5)

# Bottom performing students
bottom_5 = df.nsmallest(5, 'Average_Score')[['Name', 'Average_Score', 'Grade', 'Study_Hours']]
print("\nBottom 5 Students:")
print(bottom_5)

# Study hours vs performance
study_hours_stats = df.groupby(pd.cut(df['Study_Hours'], bins=[0, 3, 5, 8]))['Average_Score'].mean()
print("\nAverage Score by Study Hours Range:")
print(study_hours_stats)

# Attendance categories
attendance_categories = pd.cut(df['Attendance'], bins=[0, 70, 85, 100], 
                               labels=['Low', 'Medium', 'High'])
df['Attendance_Category'] = attendance_categories
attendance_perf = df.groupby('Attendance_Category')['Average_Score'].mean()
print("\nAverage Score by Attendance Category:")
print(attendance_perf)

# ==================== 6. ADVANCED PANDAS/NUMPY OPERATIONS ====================
print("\n🎯 5. ADVANCED OPERATIONS")
print("-"*50)

# Using numpy for vectorized operations
# Standardize scores
math_mean = np.mean(df['Math_Score'])
math_std = np.std(df['Math_Score'])
df['Math_Zscore'] = (df['Math_Score'] - math_mean) / math_std

# Conditional indexing with numpy
# Identify students who need attention (low performance, low attendance)
low_performers = df[(df['Average_Score'] < 60) & (df['Attendance'] < 75)]
print(f"Students needing attention: {len(low_performers)}")
if len(low_performers) > 0:
    print(low_performers[['Name', 'Average_Score', 'Attendance', 'Grade']])

# Percentile ranks
df['Score_Percentile'] = df['Average_Score'].rank(pct=True) * 100

# Create summary statistics using numpy arrays
scores_array = df[['Math_Score', 'Science_Score', 'English_Score']].to_numpy()
subject_means = np.mean(scores_array, axis=0)
subject_stds = np.std(scores_array, axis=0)

print("\nSubject Statistics:")
print(f"Mean scores - Math: {subject_means[0]:.2f}, Science: {subject_means[1]:.2f}, English: {subject_means[2]:.2f}")
print(f"Std scores - Math: {subject_stds[0]:.2f}, Science: {subject_stds[1]:.2f}, English: {subject_stds[2]:.2f}")

# ==================== 7. EXPORT RESULTS ====================
print("\n💾 6. EXPORTING RESULTS")
print("-"*50)

# Save cleaned data to CSV
df.to_csv('student_performance_cleaned.csv', index=False)
print("✓ Cleaned data saved to 'student_performance_cleaned.csv'")

# Save summary statistics
summary = df.groupby('Grade').agg({
    'Average_Score': ['count', 'mean', 'std', 'min', 'max'],
    'Study_Hours': 'mean',
    'Attendance': 'mean'
})
summary.to_csv('grade_summary.csv')
print("✓ Summary statistics saved to 'grade_summary.csv'")

# ==================== 8. VISUALIZATION ====================
print("\n📊 7. GENERATING VISUALIZATIONS...")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Grade Distribution
grade_counts.plot(kind='bar', ax=axes[0,0], color='skyblue')
axes[0,0].set_title('Grade Distribution')
axes[0,0].set_xlabel('Grade')
axes[0,0].set_ylabel('Number of Students')

# Plot 2: Attendance vs Average Score
axes[0,1].scatter(df['Attendance'], df['Average_Score'], alpha=0.6)
axes[0,1].set_title('Attendance vs Average Score')
axes[0,1].set_xlabel('Attendance (%)')
axes[0,1].set_ylabel('Average Score')

# Plot 3: Study Hours vs Average Score
axes[1,0].scatter(df['Study_Hours'], df['Average_Score'], alpha=0.6, color='green')
axes[1,0].set_title('Study Hours vs Average Score')
axes[1,0].set_xlabel('Study Hours')
axes[1,0].set_ylabel('Average Score')

# Plot 4: Subject Scores Box Plot
subject_data = [df['Math_Score'], df['Science_Score'], df['English_Score']]
axes[1,1].boxplot(subject_data, labels=['Math', 'Science', 'English'])
axes[1,1].set_title('Subject Score Distribution')
axes[1,1].set_ylabel('Score')

plt.tight_layout()
plt.savefig('performance_analysis.png', dpi=100)
print("✓ Visualization saved to 'performance_analysis.png'")
# plt.show()  # Uncomment to display

# ==================== 9. FINAL SUMMARY ====================
print("\n" + "="*50)
print("✅ ANALYSIS COMPLETED SUCCESSFULLY!")
print("="*50)
print("\n📋 KEY FINDINGS:")
print(f"• Total Students: {len(df)}")
print(f"• Average Score: {df['Average_Score'].mean():.2f}")
print(f"• Pass Rate: {(df['Performance'] == 'Pass').sum() / len(df) * 100:.1f}%")
print(f"• Most Common Grade: {df['Grade'].mode()[0]}")
print(f"• Best Subject: {['Math', 'Science', 'English'][np.argmax(subject_means)]} (avg: {np.max(subject_means):.2f})")
print(f"• Weakest Subject: {['Math', 'Science', 'English'][np.argmin(subject_means)]} (avg: {np.min(subject_means):.2f})")

print("\n📁 Generated Files:")
print("• student_performance_cleaned.csv - Cleaned dataset")
print("• grade_summary.csv - Summary statistics by grade")
print("• performance_analysis.png - Visualization plots")

print("\n💡 Analysis Complete! Explore the files for deeper insights.")