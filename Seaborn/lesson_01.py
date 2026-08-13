import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Create dataset with additional features
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "score": [45, 50, 58, 65, 70, 78, 85, 92],
    "attendance": [60, 65, 70, 75, 80, 85, 90, 95],
    "assignments": [2, 3, 4, 5, 6, 7, 8, 9]
}

df = pd.DataFrame(data)

# Set the style for better-looking plots
sns.set_style("whitegrid")
sns.set_palette("husl")

# Create a figure with multiple subplots
fig = plt.figure(figsize=(16, 12))

# 1. Scatter Plot - Study Hours vs Score
ax1 = plt.subplot(3, 3, 1)
sns.scatterplot(data=df, x="study_hours", y="score", s=100, alpha=0.7, color="steelblue", ax=ax1)
z = np.polyfit(df["study_hours"], df["score"], 1)
p = np.poly1d(z)
ax1.plot(df["study_hours"], p(df["study_hours"]), "r--", linewidth=2, label="Trend Line")
ax1.set_title("Study Hours vs Exam Score", fontsize=12, fontweight='bold')
ax1.set_xlabel("Study Hours")
ax1.set_ylabel("Exam Score")
ax1.legend()

# 2. Line Plot - Score Progression
ax2 = plt.subplot(3, 3, 2)
sns.lineplot(data=df, x="study_hours", y="score", marker='o', linewidth=2, markersize=8, ax=ax2)
ax2.set_title("Score Progression Over Study Hours", fontsize=12, fontweight='bold')
ax2.set_xlabel("Study Hours")
ax2.set_ylabel("Exam Score")
ax2.grid(True, alpha=0.3)

# 3. Bar Plot - Comparison of metrics
ax3 = plt.subplot(3, 3, 3)
x_pos = np.arange(len(df))
width = 0.25
ax3.bar(x_pos - width, df["study_hours"], width, label="Study Hours", alpha=0.8)
ax3.bar(x_pos, df["score"]/10, width, label="Score (÷10)", alpha=0.8)
ax3.bar(x_pos + width, df["attendance"]/10, width, label="Attendance (÷10)", alpha=0.8)
ax3.set_title("Multi-Metric Comparison", fontsize=12, fontweight='bold')
ax3.set_ylabel("Values")
ax3.set_xlabel("Student")
ax3.legend()
ax3.set_xticks(x_pos)

# 4. Distribution Plot - Score Distribution
ax4 = plt.subplot(3, 3, 4)
sns.histplot(data=df, x="score", kde=True, bins=6, color="coral", ax=ax4)
ax4.set_title("Score Distribution", fontsize=12, fontweight='bold')
ax4.set_xlabel("Exam Score")
ax4.set_ylabel("Frequency")

# 5. Box Plot - Score Statistics
ax5 = plt.subplot(3, 3, 5)
sns.boxplot(data=df, y="score", color="lightblue", ax=ax5)
ax5.set_title("Score Statistics (Box Plot)", fontsize=12, fontweight='bold')
ax5.set_ylabel("Exam Score")

# 6. Violin Plot - Score Distribution
ax6 = plt.subplot(3, 3, 6)
sns.violinplot(data=df, y="score", color="lightgreen", ax=ax6)
ax6.set_title("Score Distribution (Violin Plot)", fontsize=12, fontweight='bold')
ax6.set_ylabel("Exam Score")

# 7. Heatmap - Correlation Matrix
ax7 = plt.subplot(3, 3, 7)
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", 
            square=True, ax=ax7, cbar_kws={"label": "Correlation"})
ax7.set_title("Correlation Matrix", fontsize=12, fontweight='bold')

# 8. Regression Plot - Study Hours vs Score
ax8 = plt.subplot(3, 3, 8)
sns.regplot(data=df, x="study_hours", y="score", scatter_kws={"s": 80}, ax=ax8)
ax8.set_title("Regression Analysis", fontsize=12, fontweight='bold')
ax8.set_xlabel("Study Hours")
ax8.set_ylabel("Exam Score")

# 9. Multi-line Plot - All metrics
ax9 = plt.subplot(3, 3, 9)
ax9.plot(df["study_hours"], df["score"], marker='o', label="Score", linewidth=2)
ax9.plot(df["study_hours"], df["attendance"], marker='s', label="Attendance", linewidth=2)
ax9.plot(df["study_hours"], df["assignments"], marker='^', label="Assignments", linewidth=2)
ax9.set_title("Multi-Metric Trend Analysis", fontsize=12, fontweight='bold')
ax9.set_xlabel("Study Hours")
ax9.set_ylabel("Values")
ax9.legend()
ax9.grid(True, alpha=0.3)

# Add overall title
fig.suptitle("Comprehensive Data Visualization Dashboard", fontsize=16, fontweight='bold', y=0.995)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display statistics
print("=" * 50)
print("DATA ANALYSIS SUMMARY")
print("=" * 50)
print(f"\nScore Statistics:")
print(f"  Mean: {df['score'].mean():.2f}")
print(f"  Median: {df['score'].median():.2f}")
print(f"  Std Dev: {df['score'].std():.2f}")
print(f"  Min: {df['score'].min()}")
print(f"  Max: {df['score'].max()}")

print(f"\nCorrelation Analysis:")
print(f"  Study Hours vs Score: {df['study_hours'].corr(df['score']):.4f}")
print(f"  Attendance vs Score: {df['attendance'].corr(df['score']):.4f}")
print(f"  Assignments vs Score: {df['assignments'].corr(df['score']):.4f}")

# Calculate linear regression statistics
slope, intercept, r_value, p_value, std_err = stats.linregress(df["study_hours"], df["score"])
print(f"\nLinear Regression (Study Hours vs Score):")
print(f"  Slope: {slope:.4f}")
print(f"  Intercept: {intercept:.4f}")
print(f"  R-squared: {r_value**2:.4f}")
print(f"  P-value: {p_value:.6f}")
print("=" * 50)

plt.show()