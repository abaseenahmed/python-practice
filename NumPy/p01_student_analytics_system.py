#======================================== STUDENT PERFORMANCE ANALYTICS SYSTEM ==============================================#
import numpy as np
import sys

# Generate data
np.random.seed(42)  # For reproducible results
total_students = 500
student_ids = np.array(range(1001, 1501))
student_marks = np.random.randint(0, 101, (len(student_ids), 5))
subjects = ['Physics', 'Chemistry', 'Math', 'English', 'CS']

# Calculate basic metrics
total_marks = np.sum(student_marks, axis=1)
student_percentage = (total_marks / 500) * 100
class_average = np.mean(student_percentage)
class_std = np.std(student_percentage)

# Assign grades
conditions = [
    student_percentage > 90,
    student_percentage > 80,
    student_percentage > 70,
    student_percentage > 60,
    student_percentage > 50
]
grades = np.select(conditions, ['A+', 'A', 'B', 'C', 'D'], default='Fail')

# Performance categories
category_conditions = [
    student_percentage >= 85,
    student_percentage >= 75,
    student_percentage >= 65,
    student_percentage >= 50,
    student_percentage >= 35
]
categories = np.select(category_conditions, ['Excellent', 'Very Good', 'Good', 'Average', 'Poor'], default='Very Poor')

# Rankings
sorted_indices = np.argsort(total_marks)[::-1]
ranks = np.zeros(total_students, dtype=int)
for position, idx in enumerate(sorted_indices, 1):
    ranks[idx] = position

# ======================================== HELPER FUNCTIONS ======================================== #

def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 70)
    print(f"{title:^70}")
    print("=" * 70)

def print_subheader(title):
    """Print a formatted subheader"""
    print("\n" + "-" * 70)
    print(f"{title:^70}")
    print("-" * 70)

def create_histogram(data, labels, max_width=40):
    """Create a text histogram"""
    max_val = np.max(data)
    for label, value in zip(labels, data):
        bar_length = int((value / max_val) * max_width) if max_val > 0 else 0
        bar = '█' * bar_length
        print(f"{label:<8} {bar} {value:>4}")

def get_student_report(student_id):
    """Generate complete report for a single student"""
    idx = np.where(student_ids == student_id)[0]
    if len(idx) == 0:
        return None
    idx = idx[0]
    
    report = {
        'ID': student_id,
        'Physics': student_marks[idx, 0],
        'Chemistry': student_marks[idx, 1],
        'Math': student_marks[idx, 2],
        'English': student_marks[idx, 3],
        'CS': student_marks[idx, 4],
        'Total': total_marks[idx],
        'Percentage': student_percentage[idx],
        'Grade': grades[idx],
        'Category': categories[idx],
        'Rank': ranks[idx],
        'Class Average': class_average,
        'Difference': student_percentage[idx] - class_average,
        'Z-Score': (student_percentage[idx] - class_average) / class_std if class_std > 0 else 0,
        'Percentile': np.percentile(student_percentage, student_percentage[idx]),
        'Strongest': subjects[np.argmax(student_marks[idx])],
        'Weakest': subjects[np.argmin(student_marks[idx])],
        'Pass/Fail': 'Pass' if student_percentage[idx] >= 50 else 'Fail'
    }
    return report

def print_student_report(report):
    """Print a formatted student report"""
    if not report:
        print("Student not found!")
        return
    
    print_header(f"STUDENT REPORT - ID: {report['ID']}")
    print(f"{'Subject':<15} {'Marks':<10} {'Status':<10}")
    print("-" * 40)
    for subject in subjects:
        marks = report[subject]
        status = '✅ Pass' if marks >= 40 else '❌ Fail'
        print(f"{subject:<15} {marks:<10} {status:<10}")
    
    print("-" * 40)
    print(f"{'Total':<15} {report['Total']:<10}")
    print(f"{'Percentage':<15} {report['Percentage']:.2f}%")
    print(f"{'Grade':<15} {report['Grade']:<10}")
    print(f"{'Category':<15} {report['Category']:<10}")
    print(f"{'Rank':<15} {report['Rank']:<10}")
    print(f"{'Class Average':<15} {report['Class Average']:.2f}%")
    print(f"{'Difference':<15} {report['Difference']:+.2f}%")
    print(f"{'Z-Score':<15} {report['Z-Score']:+.2f}")
    print(f"{'Percentile':<15} {report['Percentile']:.2f}th")
    print(f"{'Strongest':<15} {report['Strongest']:<10}")
    print(f"{'Weakest':<15} {report['Weakest']:<10}")
    print(f"{'Status':<15} {report['Pass/Fail']:<10}")

# ======================================== FEATURE FUNCTIONS ======================================== #

def feature_1_subject_toppers():
    """Find topper of each subject"""
    print_header("SUBJECT TOPPERS")
    for i, subject in enumerate(subjects):
        topper_idx = np.argmax(student_marks[:, i])
        print(f"\n{subject} Topper")
        print(f"  Student ID : {student_ids[topper_idx]}")
        print(f"  Marks      : {student_marks[topper_idx, i]}")

def feature_2_subject_fail_analysis():
    """Analyze failures per subject"""
    print_header("SUBJECT FAIL ANALYSIS")
    print(f"{'Subject':<15} {'Failed Students':<20}")
    print("-" * 40)
    for i, subject in enumerate(subjects):
        failed = np.sum(student_marks[:, i] < 40)
        bar = '█' * int((failed / total_students) * 30)
        print(f"{subject:<15} {failed:<20} {bar}")

def feature_3_subject_difficulty():
    """Rank subjects by difficulty"""
    print_header("SUBJECT DIFFICULTY RANKING")
    subject_avg = np.mean(student_marks, axis=0)
    
    print(f"{'Subject':<15} {'Average':<15}")
    print("-" * 35)
    for i, subject in enumerate(subjects):
        print(f"{subject:<15} {subject_avg[i]:.2f}")
    
    hardest_idx = np.argmin(subject_avg)
    easiest_idx = np.argmax(subject_avg)
    
    print(f"\nHardest Subject : {subjects[hardest_idx]} ({subject_avg[hardest_idx]:.2f})")
    print(f"Easiest Subject : {subjects[easiest_idx]} ({subject_avg[easiest_idx]:.2f})")

def feature_4_grade_histogram():
    """Display grade histogram"""
    print_header("GRADE HISTOGRAM")
    unique_grades, counts = np.unique(grades, return_counts=True)
    
    # Sort grades in order: A+, A, B, C, D, Fail
    grade_order = ['A+', 'A', 'B', 'C', 'D', 'Fail']
    ordered_counts = []
    for g in grade_order:
        if g in unique_grades:
            ordered_counts.append(counts[np.where(unique_grades == g)[0][0]])
        else:
            ordered_counts.append(0)
    
    create_histogram(ordered_counts, grade_order)

def feature_5_individual_student_report():
    """Generate report for a specific student"""
    print_header("INDIVIDUAL STUDENT REPORT")
    try:
        student_id = int(input("Enter Student ID (1001-1500): "))
        report = get_student_report(student_id)
        print_student_report(report)
    except ValueError:
        print("Invalid input! Please enter a number.")

def feature_6_scholarship_eligibility():
    """Find students eligible for scholarship"""
    print_header("SCHOLARSHIP ELIGIBILITY")
    print("Rules: Above 85% overall AND No subject below 75")
    print("-" * 50)
    
    eligible = (student_percentage >= 85) & np.all(student_marks >= 75, axis=1)
    eligible_ids = student_ids[eligible]
    eligible_count = np.sum(eligible)
    
    print(f"\nEligible Students: {eligible_count}")
    if eligible_count > 0:
        print("\nEligible Students Details:")
        print(f"{'ID':<10} {'Percentage':<15} {'Subjects':<30}")
        print("-" * 55)
        for idx in np.where(eligible)[0][:10]:
            print(f"{student_ids[idx]:<10} {student_percentage[idx]:<15.2f}% {student_marks[idx]}")
        if eligible_count > 10:
            print(f"... and {eligible_count - 10} more students")

def feature_7_merit_list():
    """Print merit list of top 50 students"""
    print_header("MERIT LIST - TOP 50 STUDENTS")
    print(f"{'Rank':<6} {'ID':<10} {'Percentage':<15} {'Grade':<10} {'Category':<15}")
    print("-" * 65)
    
    for rank in range(1, 51):
        idx = sorted_indices[rank-1]
        print(f"{rank:<6} {student_ids[idx]:<10} {student_percentage[idx]:<15.2f}% "
              f"{grades[idx]:<10} {categories[idx]:<15}")

def feature_8_subject_ranking():
    """Find strongest and weakest subject for each student"""
    print_header("SUBJECT RANKING FOR STUDENTS")
    print("First 10 Students:")
    print(f"{'ID':<10} {'Strongest':<15} {'Weakest':<15} {'Scores':<30}")
    print("-" * 75)
    
    for i in range(min(10, total_students)):
        strongest_idx = np.argmax(student_marks[i])
        weakest_idx = np.argmin(student_marks[i])
        scores_str = ' '.join(str(s) for s in student_marks[i])
        print(f"{student_ids[i]:<10} {subjects[strongest_idx]:<15} "
              f"{subjects[weakest_idx]:<15} {scores_str:<30}")

def feature_9_performance_categories():
    """Display performance category distribution"""
    print_header("PERFORMANCE CATEGORIES")
    unique_categories, counts = np.unique(categories, return_counts=True)
    
    # Order: Excellent, Very Good, Good, Average, Poor, Very Poor
    category_order = ['Excellent', 'Very Good', 'Good', 'Average', 'Poor', 'Very Poor']
    ordered_counts = []
    for cat in category_order:
        if cat in unique_categories:
            ordered_counts.append(counts[np.where(unique_categories == cat)[0][0]])
        else:
            ordered_counts.append(0)
    
    create_histogram(ordered_counts, category_order)

def feature_10_improvement_analysis():
    """Show students improving school average"""
    print_header("STUDENTS IMPROVING SCHOOL AVERAGE")
    diff = student_percentage - class_average
    
    print(f"Class Average: {class_average:.2f}%")
    print("\nTop 10 Improvers:")
    print(f"{'ID':<10} {'Percentage':<15} {'Difference':<15}")
    print("-" * 45)
    
    # Students with highest positive difference
    top_improvers = np.argsort(diff)[::-1][:10]
    for idx in top_improvers:
        print(f"{student_ids[idx]:<10} {student_percentage[idx]:<15.2f}% {diff[idx]:+15.2f}%")
    
    print("\nBottom 10 (Need Improvement):")
    print(f"{'ID':<10} {'Percentage':<15} {'Difference':<15}")
    print("-" * 45)
    bottom_improvers = np.argsort(diff)[:10]
    for idx in bottom_improvers:
        print(f"{student_ids[idx]:<10} {student_percentage[idx]:<15.2f}% {diff[idx]:+15.2f}%")

def feature_11_subject_median():
    """Calculate median for each subject"""
    print_header("SUBJECT-WISE MEDIAN")
    print(f"{'Subject':<15} {'Median':<15}")
    print("-" * 35)
    for i, subject in enumerate(subjects):
        median = np.median(student_marks[:, i])
        print(f"{subject:<15} {median:.2f}")

def feature_12_z_score():
    """Calculate Z-scores for students"""
    print_header("Z-SCORE ANALYSIS")
    z_scores = (student_percentage - class_average) / class_std if class_std > 0 else np.zeros_like(student_percentage)
    
    print(f"Class Average: {class_average:.2f}%")
    print(f"Class Std Dev: {class_std:.2f}%")
    print("\nStudents with Highest Z-Scores (Top Performers):")
    print(f"{'ID':<10} {'Percentage':<15} {'Z-Score':<15}")
    print("-" * 45)
    
    top_z_indices = np.argsort(z_scores)[::-1][:10]
    for idx in top_z_indices:
        print(f"{student_ids[idx]:<10} {student_percentage[idx]:<15.2f}% {z_scores[idx]:+15.2f}")

def feature_13_detect_outliers():
    """Detect statistical outliers"""
    print_header("OUTLIER DETECTION")
    upper_bound = class_average + 2 * class_std
    lower_bound = class_average - 2 * class_std
    
    high_outliers = student_percentage > upper_bound
    low_outliers = student_percentage < lower_bound
    
    print(f"Upper Bound (Mean + 2σ): {upper_bound:.2f}%")
    print(f"Lower Bound (Mean - 2σ): {lower_bound:.2f}%")
    print(f"\nHigh Performers (Above Upper Bound): {np.sum(high_outliers)}")
    if np.sum(high_outliers) > 0:
        print("IDs:", student_ids[high_outliers][:10])
    
    print(f"\nLow Performers (Below Lower Bound): {np.sum(low_outliers)}")
    if np.sum(low_outliers) > 0:
        print("IDs:", student_ids[low_outliers][:10])

def feature_14_class_rank_percentile():
    """Calculate percentile for each student's rank"""
    print_header("CLASS RANK PERCENTILES")
    percentiles = np.percentile(student_percentage, [25, 50, 75, 90, 95, 99])
    
    print("Percentile Distribution:")
    print(f"{'Percentile':<15} {'Value':<15}")
    print("-" * 35)
    for p, val in zip([25, 50, 75, 90, 95, 99], percentiles):
        print( f"{p}th:<15 {val:<15.2f}%" )
    
    print(f"\nTop 10 Students and Their Percentiles:")
    print(f"{'Rank':<6} {'ID':<10} {'Percentage':<15} {'Percentile':<15}")
    print("-" * 55)
    for rank in range(1, 11):
        idx = sorted_indices[rank-1]
        percentile = np.percentile(student_percentage, 
                                   np.where(student_percentage <= student_percentage[idx])[0].size / total_students * 100)
        print(f"{rank:<6} {student_ids[idx]:<10} {student_percentage[idx]:<15.2f}% {percentile:<15.2f}th")

def feature_15_subject_correlation():
    """Analyze subject correlations"""
    print_header("SUBJECT CORRELATION ANALYSIS")
    correlation_matrix = np.corrcoef(student_marks.T)
    
    print("Correlation Matrix:")
    print("           " + " ".join(f"{s[:4]:>8}" for s in subjects))
    for i in range(5):
        print(f"{subjects[i]:<10} " + " ".join(f"{correlation_matrix[i][j]:>8.2f}" for j in range(5)))
    
    print("\nCorrelation Insights:")
    print("-" * 50)
    insights = []
    for i in range(5):
        for j in range(i+1, 5):
            corr = correlation_matrix[i][j]
            if abs(corr) > 0.7:
                strength = "Strong positive"
            elif abs(corr) > 0.4:
                strength = "Moderate positive"
            elif abs(corr) > 0.1:
                strength = "Weak positive"
            else:
                strength = "Weak"
            insights.append((f"{subjects[i]} & {subjects[j]}", corr, strength))
    
    insights.sort(key=lambda x: abs(x[1]), reverse=True)
    for pair, corr, strength in insights[:5]:
        print(f"{pair:<20} {corr:>6.2f}  →  {strength} relationship")

def feature_16_export_report():
    """Export reports to files"""
    print_header("EXPORTING REPORTS")
    
    # Export to CSV
    csv_filename = "student_report.csv"
    with open(csv_filename, 'w') as f:
        f.write("ID,Physics,Chemistry,Math,English,CS,Total,Percentage,Grade,Category,Rank\n")
        for i in range(total_students):
            f.write(f"{student_ids[i]},{student_marks[i,0]},{student_marks[i,1]},{student_marks[i,2]},"
                    f"{student_marks[i,3]},{student_marks[i,4]},{total_marks[i]},{student_percentage[i]:.2f},"
                    f"{grades[i]},{categories[i]},{ranks[i]}\n")
    print(f"✓ CSV report exported to: {csv_filename}")
    
    # Export text report
    txt_filename = "student_report.txt"
    with open(txt_filename, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write("STUDENT PERFORMANCE REPORT\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Total Students: {total_students}\n")
        f.write(f"Class Average: {class_average:.2f}%\n")
        f.write(f"Class Std Dev: {class_std:.2f}%\n\n")
        
        f.write("TOP 20 STUDENTS\n")
        f.write("-" * 50 + "\n")
        f.write(f"{'Rank':<6} {'ID':<10} {'Percentage':<15} {'Grade':<10}\n")
        f.write("-" * 50 + "\n")
        for rank in range(1, 21):
            idx = sorted_indices[rank-1]
            f.write(f"{rank:<6} {student_ids[idx]:<10} {student_percentage[idx]:<15.2f}% {grades[idx]:<10}\n")
    print(f"✓ Text report exported to: {txt_filename}")

def feature_17_18_search_student():
    """Search and display student report"""
    print_header("SEARCH STUDENT")
    try:
        student_id = int(input("Enter Student ID (1001-1500): "))
        report = get_student_report(student_id)
        if report:
            print_student_report(report)
        else:
            print(f"Student ID {student_id} not found!")
    except ValueError:
        print("Invalid input! Please enter a number.")

def feature_19_compare_students():
    """Compare two students"""
    print_header("COMPARE TWO STUDENTS")
    try:
        id1 = int(input("Enter first Student ID: "))
        id2 = int(input("Enter second Student ID: "))
        
        report1 = get_student_report(id1)
        report2 = get_student_report(id2)
        
        if not report1 or not report2:
            print("One or both students not found!")
            return
        
        print(f"\n{'Subject':<15} {id1:<10} {id2:<10} {'Winner':<10}")
        print("-" * 55)
        
        total_wins = [0, 0]
        for subject in subjects:
            m1 = report1[subject]
            m2 = report2[subject]
            winner = "Tie"
            if m1 > m2:
                winner = id1
                total_wins[0] += 1
            elif m2 > m1:
                winner = id2
                total_wins[1] += 1
            print(f"{subject:<15} {m1:<10} {m2:<10} {winner:<10}")
        
        print("-" * 55)
        print(f"{'Total':<15} {report1['Total']:<10} {report2['Total']:<10}")
        print(f"{'Percentage':<15} {report1['Percentage']:.2f}% {report2['Percentage']:.2f}%")
        
        if report1['Percentage'] > report2['Percentage']:
            overall_winner = id1
        elif report2['Percentage'] > report1['Percentage']:
            overall_winner = id2
        else:
            overall_winner = "Tie"
        
        print(f"\nOverall Winner: {overall_winner}")
        print(f"Subject Wins: {id1}: {total_wins[0]}, {id2}: {total_wins[1]}")
    except ValueError:
        print("Invalid input! Please enter numbers.")

def feature_20_dashboard():
    """Display executive dashboard"""
    print_header("SCHOOL ANALYTICS DASHBOARD")
    
    pass_count = np.sum(student_percentage >= 50)
    fail_count = total_students - pass_count
    scholarship_eligible = np.sum((student_percentage >= 85) & np.all(student_marks >= 75, axis=1))
    
    subject_avg = np.mean(student_marks, axis=0)
    top_10_avg = np.mean(student_percentage[sorted_indices[:10]])
    
    outliers = np.sum(np.abs((student_percentage - class_average) / class_std) > 2) if class_std > 0 else 0
    
    print(f"{'Students':<25} : {total_students}")
    print(f"{'Subjects':<25} : {len(subjects)}")
    print(f"{'Class Average':<25} : {class_average:.2f}%")
    print("-" * 50)
    print(f"{'Highest Percentage':<25} : {np.max(student_percentage):.2f}%")
    print(f"{'Lowest Percentage':<25} : {np.min(student_percentage):.2f}%")
    print("-" * 50)
    print(f"{'Pass Students':<25} : {pass_count}")
    print(f"{'Failed Students':<25} : {fail_count}")
    print("-" * 50)
    print(f"{'Topper ID':<25} : {student_ids[sorted_indices[0]]}")
    print(f"{'Top Score':<25} : {total_marks[sorted_indices[0]]}")
    print("-" * 50)
    for i, subject in enumerate(subjects):
        print(f"{f'Average {subject}':<25} : {subject_avg[i]:.2f}")
    print("-" * 50)
    print(f"{'Std Deviation':<25} : {class_std:.2f}%")
    print(f"{'Top 10 Average':<25} : {top_10_avg:.2f}%")
    print("-" * 50)
    print(f"{'Scholarship Eligible':<25} : {scholarship_eligible}")
    print(f"{'Outliers':<25} : {outliers}")
    print("=" * 70)

# ======================================== MENU SYSTEM ======================================== #

def main_menu():
    """Display main menu and handle user input"""
    menu_options = {
        '1': ('View Statistics', feature_1_subject_toppers),
        '2': ('Search Student', feature_17_18_search_student),
        '3': ('Top Students', feature_7_merit_list),
        '4': ('Failed Students', feature_2_subject_fail_analysis),
        '5': ('Subject Analysis', feature_3_subject_difficulty),
        '6': ('Scholarship', feature_6_scholarship_eligibility),
        '7': ('Merit List', feature_7_merit_list),
        '8': ('Subject Toppers', feature_1_subject_toppers),
        '9': ('Grade Distribution', feature_4_grade_histogram),
        '10': ('Performance Categories', feature_9_performance_categories),
        '11': ('Individual Report', feature_5_individual_student_report),
        '12': ('Compare Students', feature_19_compare_students),
        '13': ('Subject Difficulty', feature_3_subject_difficulty),
        '14': ('Subject Median', feature_11_subject_median),
        '15': ('Z-Score Analysis', feature_12_z_score),
        '16': ('Outlier Detection', feature_13_detect_outliers),
        '17': ('Correlation Analysis', feature_15_subject_correlation),
        '18': ('Dashboard', feature_20_dashboard),
        '19': ('Export Reports', feature_16_export_report),
        '20': ('Class Rank Percentile', feature_14_class_rank_percentile),
        '0': ('Exit', None)
    }
    
    while True:
        print("\n" + "=" * 70)
        print("STUDENT PERFORMANCE ANALYTICS SYSTEM - MAIN MENU")
        print("=" * 70)
        print("\n1.  Subject Toppers         11. Individual Report")
        print("2.  Subject Fail Analysis   12. Compare Students")
        print("3.  Subject Difficulty      13. Subject Median")
        print("4.  Grade Histogram         14. Z-Score Analysis")
        print("5.  Performance Categories  15. Outlier Detection")
        print("6.  Improvement Analysis    16. Correlation Analysis")
        print("7.  Subject Ranking         17. Dashboard")
        print("8.  Scholarship Eligibility 18. Export Reports")
        print("9.  Merit List             19. Class Rank Percentile")
        print("10. Search Student          0.  Exit")
        print("-" * 70)
        
        choice = input("\nEnter your choice: ")
        
        if choice == '0':
            print("\nThank you for using the Student Performance Analytics System!")
            break
        
        if choice in menu_options:
            if menu_options[choice][1]:
                menu_options[choice][1]()
            input("\nPress Enter to continue...")
        else:
            print("Invalid choice! Please try again.")

# ======================================== RUN APPLICATION ======================================== #

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("WELCOME TO STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 70)
    print(f"Total Students: {total_students}")
    print(f"Subjects: {', '.join(subjects)}")
    print("=" * 70)
    
    main_menu()