import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# ============================================
# 1. CREATE STUDENT DATASET
# ============================================
def create_student_data():
    """Create sample student performance dataset"""
    np.random.seed(42)
    
    # Student names
    first_names = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'James', 'Sophia', 'Oliver', 
                   'Isabella', 'Benjamin', 'Mia', 'Lucas', 'Charlotte', 'Henry', 'Amelia']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 
                  'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Wilson', 'Anderson']
    
    # Generate 100 students
    n = 100
    names = [f"{np.random.choice(first_names)} {np.random.choice(last_names)}" for _ in range(n)]
    
    # Subjects
    subjects = ['Math', 'Science', 'English', 'History', 'Art']
    
    # Generate scores (0-100)
    math_scores = np.random.normal(72, 15, n).clip(0, 100).round(1)
    science_scores = np.random.normal(68, 18, n).clip(0, 100).round(1)
    english_scores = np.random.normal(75, 12, n).clip(0, 100).round(1)
    history_scores = np.random.normal(70, 16, n).clip(0, 100).round(1)
    art_scores = np.random.normal(65, 20, n).clip(0, 100).round(1)
    
    # Demographics
    genders = np.random.choice(['Male', 'Female'], n, p=[0.5, 0.5])
    ages = np.random.randint(15, 19, n)
    grades = np.random.choice(['9th', '10th', '11th', '12th'], n, p=[0.25, 0.25, 0.25, 0.25])
    
    # Study hours per day
    study_hours = np.random.choice([1, 2, 3, 4, 5, 6], n, p=[0.2, 0.25, 0.2, 0.15, 0.1, 0.1])
    
    # Extra curricular activities
    activities = ['Sports', 'Music', 'Art', 'Science Club', 'Debate', 'None']
    extra_curricular = np.random.choice(activities, n, p=[0.2, 0.15, 0.15, 0.2, 0.1, 0.2])
    
    # Calculate average score
    avg_score = (math_scores + science_scores + english_scores + history_scores + art_scores) / 5
    
    # Assign grades (A, B, C, D, F)
    grade_letter = pd.cut(avg_score, 
                          bins=[0, 60, 70, 80, 90, 100], 
                          labels=['F', 'D', 'C', 'B', 'A'])
    
    # Create DataFrame
    df = pd.DataFrame({
        'student_id': [f'S{str(i).zfill(3)}' for i in range(1, n+1)],
        'name': names,
        'gender': genders,
        'age': ages,
        'grade': grades,
        'math': math_scores,
        'science': science_scores,
        'english': english_scores,
        'history': history_scores,
        'art': art_scores,
        'avg_score': avg_score.round(1),
        'grade_letter': grade_letter,
        'study_hours': study_hours,
        'extra_curricular': extra_curricular
    })
    
    return df

# ============================================
# 2. BASIC STATISTICS
# ============================================
def basic_stats(df):
    """Calculate and display basic statistics"""
    print("=" * 70)
    print("STUDENT PERFORMANCE ANALYSIS")
    print("=" * 70)
    
    print(f"\nTotal Students: {len(df)}")
    print(f"Grade Distribution:")
    print(df['grade'].value_counts().sort_index())
    
    print("\nSubject Score Statistics:")
    subject_stats = df[['math', 'science', 'english', 'history', 'art']].describe()
    print(subject_stats.round(1))
    
    print(f"\nOverall Average Score: {df['avg_score'].mean():.1f}")
    print(f"Highest Average: {df['avg_score'].max():.1f}")
    print(f"Lowest Average: {df['avg_score'].min():.1f}")
    
    return subject_stats

# ============================================
# 3. ANALYSIS BY GROUP
# ============================================
def group_analysis(df):
    """Analyze performance by different groups"""
    print("\n" + "=" * 70)
    print("GROUP ANALYSIS")
    print("=" * 70)
    
    # By Gender
    print("\n1. Performance by Gender:")
    gender_performance = df.groupby('gender')[['math', 'science', 'english', 'history', 'art', 'avg_score']].mean()
    print(gender_performance.round(1))
    
    # By Grade Level
    print("\n2. Performance by Grade Level:")
    grade_performance = df.groupby('grade')[['math', 'science', 'english', 'history', 'art', 'avg_score']].mean()
    print(grade_performance.round(1))
    
    # By Study Hours
    print("\n3. Average Score by Study Hours:")
    study_performance = df.groupby('study_hours')['avg_score'].mean().sort_index()
    print(study_performance.round(1))
    
    # By Extra Curricular Activity
    print("\n4. Average Score by Extra Curricular Activity:")
    activity_performance = df.groupby('extra_curricular')['avg_score'].mean().sort_values(ascending=False)
    print(activity_performance.round(1))
    
    # Grade Distribution
    print("\n5. Grade Letter Distribution:")
    grade_dist = df['grade_letter'].value_counts().sort_index()
    print(grade_dist)
    
    return gender_performance, grade_performance

# ============================================
# 4. CORRELATION ANALYSIS
# ============================================
def correlation_analysis(df):
    """Find correlations between variables"""
    print("\n" + "=" * 70)
    print("CORRELATION ANALYSIS")
    print("=" * 70)
    
    # Correlation between study hours and scores
    corr_study = df[['study_hours', 'math', 'science', 'english', 'history', 'art', 'avg_score']].corr()
    
    print("\nCorrelation between Study Hours and Subjects:")
    print(corr_study['study_hours'].sort_values(ascending=False))
    
    # Correlation between subjects
    print("\nCorrelation between Subjects:")
    subject_corr = df[['math', 'science', 'english', 'history', 'art']].corr()
    print(subject_corr.round(3))
    
    return corr_study

# ============================================
# 5. FIND TOP PERFORMERS
# ============================================
def top_performers(df):
    """Find top and struggling students"""
    print("\n" + "=" * 70)
    print("TOP PERFORMERS")
    print("=" * 70)
    
    # Top 5 students
    print("\n🌟 Top 5 Students Overall:")
    top_5 = df.nlargest(5, 'avg_score')[['student_id', 'name', 'grade', 'avg_score', 'grade_letter']]
    print(top_5)
    
    # Bottom 5 students
    print("\n📉 Bottom 5 Students (Need Improvement):")
    bottom_5 = df.nsmallest(5, 'avg_score')[['student_id', 'name', 'grade', 'avg_score', 'grade_letter']]
    print(bottom_5)
    
    # Subject-wise top performers
    subjects = ['math', 'science', 'english', 'history', 'art']
    print("\n🏆 Subject-wise Top Students:")
    for subject in subjects:
        top = df.nlargest(1, subject)[['student_id', 'name', subject]]
        print(f"{subject.capitalize()}: {top['name'].values[0]} ({top[subject].values[0]:.1f})")

# ============================================
# 6. VISUALIZATIONS
# ============================================
def create_visualizations(df):
    """Create various visualizations"""
    print("\n" + "=" * 70)
    print("CREATING VISUALIZATIONS")
    print("=" * 70)
    
    fig = plt.figure(figsize=(16, 12))
    
    # 1. Score Distribution (Histogram)
    ax1 = plt.subplot(2, 3, 1)
    ax1.hist(df['avg_score'], bins=15, edgecolor='black', alpha=0.7, color='skyblue')
    ax1.axvline(df['avg_score'].mean(), color='red', linestyle='--', linewidth=2, 
                label=f'Mean: {df["avg_score"].mean():.1f}')
    ax1.set_title('Distribution of Average Scores')
    ax1.set_xlabel('Average Score')
    ax1.set_ylabel('Number of Students')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Subject Boxplots
    ax2 = plt.subplot(2, 3, 2)
    subject_cols = ['math', 'science', 'english', 'history', 'art']
    df[subject_cols].boxplot(ax=ax2)
    ax2.set_title('Score Distribution by Subject')
    ax2.set_ylabel('Scores')
    ax2.grid(True, alpha=0.3)
    
    # 3. Study Hours vs Average Score
    ax3 = plt.subplot(2, 3, 3)
    study_avg = df.groupby('study_hours')['avg_score'].mean()
    ax3.bar(study_avg.index, study_avg.values, color='lightgreen', edgecolor='black')
    ax3.set_title('Study Hours vs Average Score')
    ax3.set_xlabel('Study Hours per Day')
    ax3.set_ylabel('Average Score')
    ax3.grid(True, alpha=0.3, axis='y')
    
    # 4. Gender Performance
    ax4 = plt.subplot(2, 3, 4)
    gender_scores = df.groupby('gender')[subject_cols].mean()
    gender_scores.T.plot(kind='bar', ax=ax4)
    ax4.set_title('Performance by Gender')
    ax4.set_xlabel('Subjects')
    ax4.set_ylabel('Average Score')
    ax4.legend(title='Gender')
    ax4.grid(True, alpha=0.3)
    
    # 5. Grade Distribution Pie Chart
    ax5 = plt.subplot(2, 3, 5)
    grade_counts = df['grade_letter'].value_counts().sort_index()
    colors = ['#ff6b6b', '#ffd93d', '#6bcb77', '#4d96ff', '#9b59b6']
    ax5.pie(grade_counts.values, labels=grade_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
    ax5.set_title('Grade Distribution')
    
    # 6. Scatter Plot: Study Hours vs All Subjects
    ax6 = plt.subplot(2, 3, 6)
    scatter = ax6.scatter(df['study_hours'], df['avg_score'], 
                         c=df['age'], cmap='viridis', s=100, alpha=0.6)
    ax6.set_title('Study Hours vs Average Score (Color: Age)')
    ax6.set_xlabel('Study Hours per Day')
    ax6.set_ylabel('Average Score')
    plt.colorbar(scatter, ax=ax6, label='Age')
    ax6.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('student_performance_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("[OK] Visualization saved as 'student_performance_analysis.png'")

# ============================================
# 7. GENERATE SUMMARY
# ============================================
def generate_summary(df):
    """Generate a text summary"""
    print("\n" + "=" * 70)
    print("SUMMARY REPORT")
    print("=" * 70)
    
    summary = f"""
    STUDENT PERFORMANCE SUMMARY
    =============================
    
    Total Students: {len(df)}
    Average Overall Score: {df['avg_score'].mean():.1f}/100
    
    GRADE DISTRIBUTION:
    A: {len(df[df['grade_letter'] == 'A'])} students ({len(df[df['grade_letter'] == 'A'])/len(df)*100:.1f}%)
    B: {len(df[df['grade_letter'] == 'B'])} students ({len(df[df['grade_letter'] == 'B'])/len(df)*100:.1f}%)
    C: {len(df[df['grade_letter'] == 'C'])} students ({len(df[df['grade_letter'] == 'C'])/len(df)*100:.1f}%)
    D: {len(df[df['grade_letter'] == 'D'])} students ({len(df[df['grade_letter'] == 'D'])/len(df)*100:.1f}%)
    F: {len(df[df['grade_letter'] == 'F'])} students ({len(df[df['grade_letter'] == 'F'])/len(df)*100:.1f}%)
    
    GENDER BREAKDOWN:
    Male: {len(df[df['gender'] == 'Male'])} students (Avg Score: {df[df['gender'] == 'Male']['avg_score'].mean():.1f})
    Female: {len(df[df['gender'] == 'Female'])} students (Avg Score: {df[df['gender'] == 'Female']['avg_score'].mean():.1f})
    
    STUDY HOURS INSIGHTS:
    Students studying 5+ hours/day: {len(df[df['study_hours'] >= 5])}
    Average score for 5+ hours: {df[df['study_hours'] >= 5]['avg_score'].mean():.1f}
    Students studying 2 or less hours: {len(df[df['study_hours'] <= 2])}
    Average score for 2 or less hours: {df[df['study_hours'] <= 2]['avg_score'].mean():.1f}
    
    BEST PERFORMING SUBJECT: {df[subject_cols].mean().idxmax()} ({df[subject_cols].mean().max():.1f})
    WORST PERFORMING SUBJECT: {df[subject_cols].mean().idxmin()} ({df[subject_cols].mean().min():.1f})
    """
    
    print(summary)
    
    # Save summary
    with open('student_summary.txt', 'w', encoding='utf-8') as f:
        f.write(summary)
    print("[OK] Summary saved as 'student_summary.txt'")

# ============================================
# MAIN FUNCTION
# ============================================
def main():
    """Main program"""
    print("🎓 STUDENT PERFORMANCE ANALYZER")
    print("=" * 70)
    
    # Create data
    print("\nGenerating student data...")
    df = create_student_data()
    print(f"[OK] Created data for {len(df)} students")
    
    # Analysis
    basic_stats(df)
    group_analysis(df)
    correlation_analysis(df)
    top_performers(df)
    
    # Visualizations
    create_visualizations(df)
    
    # Summary
    generate_summary(df)
    
    print("\n" + "=" * 70)
    print("✅ Analysis Complete!")
    print("📁 Files Generated:")
    print("   - student_performance_analysis.png")
    print("   - student_summary.txt")
    print("=" * 70)

# ============================================
# RUN
# ============================================
if __name__ == "__main__":
    # Fix for Windows console
    subject_cols = ['math', 'science', 'english', 'history', 'art']
    main()