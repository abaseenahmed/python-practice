#============================ Student Performance Analysis Using Pandas =========================#
import pandas as pd

df = pd.read_csv('student_performance.csv')
seperator = '='*100

# Module 01: Inspecting the dataset
def module_01():
    print(df.head())
    print(seperator)

    print(df.tail())
    print(seperator)

    print(df.info())
    print(seperator)

    print(df.describe())
    print(seperator)

    print(df.columns)
    print(seperator)

    print(df.shape)
    print(seperator)

    print(df.dtypes)
    print(seperator)

    print(df.isnull().sum())
    print(seperator)

#----------------------------------------------------------------
# Observations
# Dataset contains 1,000,000 student records.
# Dataset has 6 columns.
# There are no missing values.
# Numeric columns are stored correctly.
# Grade is stored as an object (categorical).
# Average total score is approximately 84.
# Average attendance is approximately 85%.
# Average weekly self-study time is approximately 15 hours.
# The dataset appears clean and ready for analysis.
#----------------------------------------------------------------

def module_02():
    print(seperator)

    def basic_statistics():
        print(f'The total number of students: {len(df['student_id'])}')
        print(f'The total number of columns are: {len(df.columns)}')
        print(f'The average total score is: {df['total_score'].mean()}')
        print(f'The highest total score is: {df["total_score"].max()}')
        print(f'The lowest total score is: {df["total_score"].min()}')

    def study_hours_analysis():
        print(f'Student who studied the most hours: {df['weekly_self_study_hours'].idxmax()}')
        print(f'Student who studied the least hours: {df['weekly_self_study_hours'].idxmin()}')
        print(f'The average weekly study of students is: {df['weekly_self_study_hours'].mean()}')

    def attendance_analysis():
        print(f'Highest attendance: {df['attendance_percentage'].max()}')
        print(f'Lowest attendance: {df['attendance_percentage'].min()}')
        print(f'Aevrage attendance: {df['attendance_percentage'].mean()}')

    def grade_analysis():
        grade_counts = df["grade"].value_counts()
        print(f'Grade Counts {grade_counts}')
        print("Most Common Grade")
        print(grade_counts.idxmax())
        print("Least Common Grade")
        print(grade_counts.idxmin())

    def score_performance():
        sorted_df = df.sort_values(by='total_score', ascending=False)
        print('The top ten scorer are: ')
        print(sorted_df[:10])
        print('The bottom ten scorer are: ')
        print(sorted_df[-10:])

    def excellent_students():
        excellent_students_df = df[df['total_score'] >= 90]
        print(excellent_students_df.head(10))
        excellent_students_df.to_csv('excellent_students.csv', index=False)
        print('The data of excellent students is saved to file excellent_students.csv')

    basic_statistics()
    print(seperator)
    study_hours_analysis()
    print(seperator)
    attendance_analysis()
    print(seperator)
    basic_statistics()
    print(seperator)
    grade_analysis()
    print(seperator)
    score_performance()
    print(seperator)
    excellent_students()
    print(seperator)

#--------------------------------------------------------------------------------------------------
# Biggest Mistake / Bug Learned is using argmax() instead of idxmax(). top_student = df.loc[df["weekly_self_study_hours"].idxmax()]
# counting rows and columns using the shape of the table and it's indexes
# using slicing instead of using head() and tail() methods for dataframe
# Not using idxmax() idxmin()
#--------------------------------------------------------------------------------------------------

def module_03():
    def grade_distribution():
        students_grade = df.groupby('grade')['grade'].count()
        # Converts the result into a clean DataFrame with rounded numbers
        grade_summary = (df['grade']
                        .value_counts(normalize=True)
                        .multiply(100)
                        .round(2)
                        .reset_index(name='percentage'))
        print(students_grade)
        print(grade_summary)
    def hours_score_relation():
        high_study = df[df['weekly_self_study_hours'] >= 20]
        high_study_average = high_study['total_score'].mean()
        medium_study = df[df['weekly_self_study_hours'].between(10.0 , 20.0)]
        medium_study_average = medium_study['total_score'].mean()
        low_study = df[df['weekly_self_study_hours'] < 10]
        low_study_average = low_study['total_score'].mean()
        print(f'The average Score of students studying more than 20 hours is: {high_study_average.round(2)}')
        print(f'The average Score of students studying between 10 and 20 hours is: {medium_study_average.round(2)}')
        print(f'The average Score of students studying less than 10 hours is: {low_study_average.round(2)}')

    def attendence_analysis():
        regular_students = df[df['attendance_percentage'] >= 90]
        print(f'Number of students having attendance >= 90% are: {regular_students.shape[0]}')
        print(f'The average of score of regular students is: {regular_students['total_score'].mean().round(2)}')
        print(f'The average study hours of regular students is: {regular_students['weekly_self_study_hours'].mean().round(2)}')

        irregular_students = df[df['attendance_percentage'] < 70]
        print(f'Number of students having attendance < 70% are: {irregular_students.shape[0]}')
        print(f'The average of score of irregular students is: {irregular_students['total_score'].mean().round(2)}')
        print(f'The average study hours of irregular students is: {irregular_students['weekly_self_study_hours'].mean().round(2)}')

    def top_students():
        top_count = int(len(df)*0.01)
        top_count = max(1, top_count)
        top1_percent = df.nlargest(top_count, 'total_score')
        print(top1_percent)

    def bottom1_students():
        bottom1_count = int(len(df)*0.01)
        bottom1_count = max(1, bottom1_count)
        bottom1_percent = df.nsmallest(bottom1_count, 'total_score')
        print(bottom1_percent)

    def participation_analysis():
        top_participants = df[df['class_participation'] >= 8.0]
        print(f'The average score of top participating students is: {top_participants['total_score'].mean().round(2)}')
        print(f'The average attendance of top participating students is: {top_participants['attendance_percentage'].mean().round(2)}')
        print(f'The average study hours of top participating students is: {top_participants['weekly_self_study_hours'].mean().round(2)}')

        bottom_participants = df[df['class_participation'] < 3.0]
        print(f'The average score of bottom participating students is: {bottom_participants['total_score'].mean().round(2)}')
        print(f'The average attendance of bottom participating students is: {bottom_participants['attendance_percentage'].mean().round(2)}')
        print(f'The average study hours of bottom participating students is: {bottom_participants['weekly_self_study_hours'].mean().round(2)}')

    def correlation_analysis():
        print(df.corr(numeric_only=True))
        # Answer 1: weekly_self_study_hours has the strongest correlation by a massive margin.Why: The correlation value between total_score and weekly_self_study_hours is 0.812241. This is a very strong, positive linear relationship. It means that as self-study hours increase, a student's total score increases significantly.

        # Answer 2: No, according to this specific dataset, attendance does not affect marks at all.Why: The correlation between attendance_percentage and total_score is -0.001014. This number is almost exactly 0.0, indicating that there is zero linear relationship. Whether a student has high or low attendance has no impact on their final score in this data.

        # Answer 3: Yes, heavily.Why: As mentioned in the first question, the correlation is 0.812241. Because it is a strong positive number close to 1.0, it tells us that independent study time is the primary driving factor behind higher marks in this student group.

        # Answer 4: No, class participation does not affect marks.Why: The correlation between class_participation and total_score is only 0.000684. Because this value is practically 0.0, it proves that a student's level of participation in class has no statistical connection to the marks they earn.

        # Summary of What Else the Matrix Tells Usstudent_id is useless for analysis: Its correlation with total_score is -0.000492 (zero). This makes complete sense because an ID number is just a random label and shouldn't affect academic performance.The variables are isolated: None of the tracking metrics (study hours, attendance, participation) correlate with each other either (all their cross-correlations are near 0.0). For example, students who study more at home do not necessarily attend class more often or participate more.

    def performance():
        def evaluate_performance(score):
            if score >= 90:
                return 'Excellent'
            elif score >= 80:  # Covers everything from 80 up to (but excluding) 90
                return 'Good'
            elif score >= 70:  # Covers everything from 70 up to (but excluding) 80
                return 'Average'
            else:              # Covers anything strictly below 70
                return 'Poor'
        df['performance'] = df['total_score'].apply(evaluate_performance)
        print(df["performance"].value_counts())

    def export_dataset():
        df.to_csv("student_performance_analyzed.csv", index=False)
        print('The data analysis result is exported to a file named student_performance_analyzed.csv')

    grade_distribution()
    hours_score_relation()
    attendence_analysis()
    top_students()
    bottom1_students()
    participation_analysis()
    correlation_analysis()
    performance()
    export_dataset()


module_01()
module_02()
module_03()