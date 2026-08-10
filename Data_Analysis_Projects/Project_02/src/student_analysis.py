# ================================ Project 02: Student Performance Analysis ============================= #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../data/student_performance.csv')

def header(text):
    print("\n" + "=" * 80)
    print(text.center(80))
    print("=" * 80 + "\n")
seperator = "-" * 80

header("Student Performance Analysis")
print(df.head(10))
print(df.tail(10))
print(df.describe())
print(df.info())
print(seperator)

header('Data Inspection')
print(f'Number of rows: {df.shape[0]}')
print(f'Number of columns: {df.shape[1]}')
print(f'Column names: {df.columns.tolist()}')
print(f'Data types: \n{df.dtypes}')
print(f'Missing values: \n{df.isnull().sum()}')
print(f'Duplicate rows: {df.duplicated().sum()}')
print(f'Unique values for categorical columns: \n{df.select_dtypes(include=["object"]).nunique()}')
print(f'Number of unique students: {df['student_id'].nunique()}') # The number of actual students are 10000.
print(seperator)

header('Data Cleaning')
print(f'Number of duplicate rows: {df.duplicated().sum()}')
df = df.drop_duplicates()
print(f'Number of duplicate rows after dropping: {df.duplicated().sum()}. All the values are unique.')
print(f'Missing values: \n{df.isnull().sum()}')
df['study_hours'] = df['study_hours'].fillna(df['study_hours'].mean())
df['attendance'] = df['attendance'].fillna(df['attendance'].mean())
df['sleep_hours'] = df['sleep_hours'].fillna(df['sleep_hours'].mean())
df['internet_access'] = df['internet_access'].fillna(df['internet_access'].mode()[0])
df['parental_support'] = df['parental_support'].fillna(df['parental_support'].mode()[0])
print(f'Missing values: \n{df.isnull().sum()}')
print(seperator)

header('Descriptive Statistics')
def des_stats(col):
    print(f'Descriptive statistics for {col}: ')
    print(f'Mean: {np.mean(df[col])}')
    print(f'Median: {np.median(df[col])}')
    print(f'Standard Deviation: {np.std(df[col])}')
    print(f'Minimum: {np.min(df[col])}')
    print(f'Maximum: {np.max(df[col])}')
    print(f'25th Percentile: {np.percentile(df[col], 25)}')
    print(f'75th Percentile: {np.percentile(df[col], 75)}')
    print(f'Interquartile Range (IQR): {np.percentile(df[col], 75) - np.percentile(df[col], 25)}')
    print(f'Variance: {np.var(df[col])}')
    print(f'Skewness: {df[col].skew()}')
    print(f'Kurtosis: {df[col].kurtosis()}')
    print(seperator)

des_stats('age')
des_stats('study_hours')
des_stats('attendance')
des_stats('sleep_hours')
des_stats('previous_score')
des_stats('assignments_completed')
des_stats('class_participation')
des_stats('final_score')

header('Student performance analysis')
print(f'Average final score: {df["final_score"].mean()}')
print(f'Median final score: {df["final_score"].median()}')
print(f'Standard deviation of final score: {df["final_score"].std()}')
print(f'Minimum final score: {df["final_score"].min()}')
print(f'Maximum final score: {df["final_score"].max()}')
df['performance_category'] = pd.cut(df['final_score'], bins=[0, 50, 60, 70, 80, 90, 100], labels=['Poor', 'Below Average', 'Average', 'Good', 'Very Good', 'Excellent'])
print(df.head(10))

header('Study behavior analysis')
study_hours_vs_final_score = df['study_hours'].corr(df['final_score'])
attendance_vs_final_score = df['attendance'].corr(df['final_score'])
sleep_hours_vs_final_score = df['sleep_hours'].corr(df['final_score'])
previous_score_vs_final_score = df['previous_score'].corr(df['final_score'])
assignments_completed_vs_final_score = df['assignments_completed'].corr(df['final_score'])
class_participation_vs_final_score = df['class_participation'].corr(df['final_score'])
print('Table for correlation between study behavior and final score:')
print(f'Study hours vs Final score: {study_hours_vs_final_score}')
print(f'Attendance vs Final score: {attendance_vs_final_score}')
print(f'Sleep hours vs Final score: {sleep_hours_vs_final_score}')
print(f'Previous score vs Final score: {previous_score_vs_final_score}')
print(f'Assignments completed vs Final score: {assignments_completed_vs_final_score}')
print(f'Class participation vs Final score: {class_participation_vs_final_score}')

study_vs_final_score =  np.corrcoef(df['study_hours'], df['final_score'])[0, 1]
print(f'Correlation coefficient between study hours and final score: {study_vs_final_score}')

header('Group analysis')
def avg_final_score(group_col):
    avg_score = df.groupby(group_col)['final_score'].mean()
    print(f'Average final score by {group_col}:')
    print(avg_score)
    print(seperator)
avg_final_score('gender')
avg_final_score('internet_access')
avg_final_score('parental_support')
avg_final_score('performance_category')

header('Study-hour groups')
df['study_group'] = pd.cut(df['study_hours'], bins=[2, 4, 6, 8, 10], labels=['low', 'moderate', 'high', 'very high'])
def avg_score_by_study_group():
    avg_score = df.groupby('study_group')['final_score'].mean()
    print('Average final score by study-hour groups:')
    print(avg_score)
    print('Number of students in each study-hour group:')
    student_count = df["study_group"].value_counts()
    grouped_df = pd.DataFrame({'Study Group': student_count.index, 'Number of Students': student_count.values, 'Average Final Score': avg_score.values})  
    print(grouped_df)
    print(seperator)

avg_score_by_study_group()

header('Academic risk detection')
def academic_risk(score):
    if score < 50:
        return 'High Risk'
    elif score < 60:
        return 'Moderate Risk'
    else:
        return 'Low Risk'

df['academic_risk'] = df['final_score'].apply(academic_risk)
print(f'Number of High Risk students: {df[df["academic_risk"] == "High Risk"].shape[0]}')
print(f'Number of Moderate Risk students: {df[df["academic_risk"] == "Moderate Risk"].shape[0]}')
print(f'Number of Low Risk students: {df[df["academic_risk"] == "Low Risk"].shape[0]}')
print('Percentage of students in each risk group:')
print(df['academic_risk'].value_counts(normalize=True) * 100)
print(seperator)

header('Manual Risk Model')

def compute_risk_score(row):
    score = 0
    if row['final_score'] < 50:
        score += 3
    if row['attendance'] < 60:
        score += 2
    if row['study_hours'] < 2:
        score += 2
    if row['previous_score'] < 50:
        score += 2
    if row['assignments_completed'] < 60:
        score += 1
    if row['class_participation'] < 40:
        score += 1
    return score


def categorize_risk(score):
    if score <= 2:
        return 'Low Risk'
    if score <= 5:
        return 'Medium Risk'
    return 'High Risk'


df['risk_score'] = df.apply(compute_risk_score, axis=1)
df['risk_category'] = df['risk_score'].apply(categorize_risk)

print('Risk score distribution:')
print(df['risk_score'].value_counts().sort_index())
print('\nRisk category counts:')
print(df['risk_category'].value_counts())
print('\nSample risk scores and categories:')
print(df[['student_id', 'final_score', 'attendance', 'study_hours', 'previous_score', 'assignments_completed', 'class_participation', 'risk_score', 'risk_category']].head(10))

header('Finding the most academically vulnerable students top 20')
vulnarable_students = df.sort_values(by='risk_score', ascending=True).head(20)
print(vulnarable_students[['student_id', 'final_score', 'attendance', 'study_hours', 'previous_score', 'assignments_completed', 'class_participation', 'risk_score', 'risk_category']])

header('Finding the most academically talented students top 20')
talented_students = df.sort_values(by='risk_score', ascending=False).head(20)
print(talented_students[['student_id', 'final_score', 'attendance', 'study_hours', 'previous_score', 'assignments_completed', 'class_participation', 'risk_score', 'risk_category']])

header('Outlier analysis')
def detect_outliers(col):
    Q1 = np.percentile(df[col], 25)
    Q3 = np.percentile(df[col], 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q1 + 1.5 * IQR
    number_outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
    outlier_percentage = (((df[col] < lower_bound) | (df[col] > upper_bound)).mean()*100).round(2)
    print(f'Outliers Detection for {col}')
    print(f'Q1 : {Q1.round(2)}') 
    print(f'Q3 : {Q3.round(2)}') 
    print(f'IQR : {IQR.round(2)}') 
    print(f'Lower bound : {lower_bound.round(2)}') 
    print(f'Upper bound : {upper_bound.round(2)}') 
    print(f'Number of Outliers : {number_outliers}') 
    print(f'Percentage of Outliers : {outlier_percentage}%') 
    print(seperator)

detect_outliers('final_score')
detect_outliers('study_hours')
detect_outliers('attendance')
detect_outliers('previous_score')

