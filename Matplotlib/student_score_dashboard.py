import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic student data
def generate_student_data(num_students=50):
    """
    Generate synthetic student performance data
    """
    # Student names
    first_names = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'James', 'Sophia', 
                   'Oliver', 'Mia', 'Ethan', 'Charlotte', 'Mason', 'Amelia', 
                   'Logan', 'Harper', 'Elijah', 'Evelyn', 'Alexander', 'Abigail',
                   'William', 'Emily', 'Benjamin', 'Elizabeth', 'Lucas', 'Sofia']
    
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia',
                  'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez',
                  'Lopez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore',
                  'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White']
    
    # Generate random student names
    names = []
    for _ in range(num_students):
        first = np.random.choice(first_names)
        last = np.random.choice(last_names)
        names.append(f"{first} {last}")
    
    # Generate random data
    math_scores = np.random.normal(75, 15, num_students).clip(0, 100).astype(int)
    science_scores = np.random.normal(70, 18, num_students).clip(0, 100).astype(int)
    english_scores = np.random.normal(72, 16, num_students).clip(0, 100).astype(int)
    history_scores = np.random.normal(68, 20, num_students).clip(0, 100).astype(int)
    
    # Generate ages (15-18 years)
    current_year = datetime.now().year
    birth_years = np.random.choice([2008, 2009, 2010, 2011], num_students)
    ages = current_year - birth_years
    
    # Generate grades (9-12)
    grades = np.random.choice(['9th', '10th', '11th', '12th'], num_students, 
                             p=[0.25, 0.25, 0.25, 0.25])
    
    # Create DataFrame
    df = pd.DataFrame({
        'Name': names,
        'Age': ages,
        'Grade': grades,
        'Math': math_scores,
        'Science': science_scores,
        'English': english_scores,
        'History': history_scores
    })
    
    # Calculate average score
    df['Average'] = df[['Math', 'Science', 'English', 'History']].mean(axis=1).round(2)
    
    # Add performance category
    conditions = [
        (df['Average'] >= 85),
        (df['Average'] >= 70),
        (df['Average'] >= 60)
    ]
    choices = ['Excellent', 'Good', 'Average']
    df['Performance'] = np.select(conditions, choices, default='Needs Improvement')
    
    return df

# Create the dataset
students_df = generate_student_data(50)

# Display basic statistics
print("=" * 60)
print("STUDENT PERFORMANCE DATA ANALYSIS")
print("=" * 60)
print("\nFirst 5 students:")
print(students_df.head())
print("\nDataset Info:")
print(students_df.info())
print("\nBasic Statistics:")
print(students_df.describe())

# Analysis by grade
print("\n" + "=" * 60)
print("ANALYSIS BY GRADE LEVEL")
print("=" * 60)
grade_stats = students_df.groupby('Grade').agg({
    'Average': ['mean', 'min', 'max', 'count']
}).round(2)
print(grade_stats)

# Performance distribution
print("\n" + "=" * 60)
print("PERFORMANCE DISTRIBUTION")
print("=" * 60)
performance_counts = students_df['Performance'].value_counts()
print(performance_counts)

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Student Performance Analysis Dashboard', fontsize=16, fontweight='bold')

# 1. Subject score distributions
ax1 = axes[0, 0]
subjects = ['Math', 'Science', 'English', 'History']
data = [students_df[subject] for subject in subjects]
ax1.boxplot(data, labels=subjects, patch_artist=True)
ax1.set_title('Subject Score Distribution')
ax1.set_ylabel('Score')
ax1.grid(True, alpha=0.3)

# 2. Average scores by grade
ax2 = axes[0, 1]
grade_avg = students_df.groupby('Grade')['Average'].mean()
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
bars = ax2.bar(grade_avg.index, grade_avg.values, color=colors, edgecolor='black')
ax2.set_title('Average Score by Grade Level')
ax2.set_ylabel('Average Score')
ax2.set_ylim(0, 100)
# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{height:.1f}', ha='center', va='bottom')

# 3. Performance category distribution
ax3 = axes[1, 0]
performance_colors = {'Excellent': '#2ECC71', 'Good': '#3498DB', 
                      'Average': '#F1C40F', 'Needs Improvement': '#E74C3C'}
performance_data = students_df['Performance'].value_counts()
pie_colors = [performance_colors[cat] for cat in performance_data.index]
wedges, texts, autotexts = ax3.pie(performance_data.values, 
                                    labels=performance_data.index,
                                    autopct='%1.1f%%',
                                    colors=pie_colors,
                                    startangle=90)
ax3.set_title('Performance Category Distribution')

# 4. Scatter plot: Math vs Science scores
ax4 = axes[1, 1]
scatter = ax4.scatter(students_df['Math'], students_df['Science'],
                     c=students_df['Average'], cmap='viridis',
                     s=100, alpha=0.7, edgecolors='black', linewidth=0.5)
ax4.set_xlabel('Math Score')
ax4.set_ylabel('Science Score')
ax4.set_title('Math vs Science Scores')
ax4.grid(True, alpha=0.3)
# Add correlation line
z = np.polyfit(students_df['Math'], students_df['Science'], 1)
p = np.poly1d(z)
ax4.plot(students_df['Math'].sort_values(), 
         p(students_df['Math'].sort_values()), 
         "r--", alpha=0.8, label=f'Correlation: r={np.corrcoef(students_df["Math"], students_df["Science"])[0,1]:.2f}')
ax4.legend()
plt.colorbar(scatter, ax=ax4, label='Average Score')

plt.tight_layout()
plt.savefig('student_performance_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Additional analysis: Top performers
print("\n" + "=" * 60)
print("TOP 10 PERFORMERS")
print("=" * 60)
top_10 = students_df.nlargest(10, 'Average')[['Name', 'Grade', 'Average', 'Performance']]
print(top_10)

# Subject correlation matrix
print("\n" + "=" * 60)
print("SUBJECT CORRELATION MATRIX")
print("=" * 60)
correlation_matrix = students_df[['Math', 'Science', 'English', 'History']].corr()
print(correlation_matrix.round(3))

# Save data to CSV
students_df.to_csv('student_data.csv', index=False)
print("\nData saved to 'student_data.csv'")
print("Visualization saved as 'student_performance_analysis.png'")