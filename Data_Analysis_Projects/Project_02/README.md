# Student Performance Analysis

A data analysis project that explores student academic performance, identifies relationships between academic factors, detects potentially at-risk students, performs statistical analysis, and visualizes important findings using **NumPy, Pandas, and Matplotlib**.

This project was built as part of my hands-on journey toward becoming an **AI/ML Engineer**, with a focus on developing practical skills in data analysis, exploratory data analysis (EDA), numerical computing, feature engineering, and data visualization.

---

## Project Overview

The goal of this project is to analyze student academic data and answer questions such as:

* What is the overall distribution of student final scores?
* How strongly are study hours related to final scores?
* Does attendance have a relationship with academic performance?
* How does previous academic performance relate to final scores?
* Does parental support appear to be associated with student performance?
* How do different study-hour groups perform?
* Which students may be academically at risk?
* What are the statistical characteristics of the dataset?
* Are there significant outliers in important numerical variables?

The project follows a basic data-analysis workflow:

```text
Raw Dataset
     ↓
Data Inspection
     ↓
Data Cleaning
     ↓
Descriptive Statistics
     ↓
Exploratory Data Analysis
     ↓
Correlation Analysis
     ↓
Feature Engineering
     ↓
Academic Risk Analysis
     ↓
Outlier Detection
     ↓
Data Visualization
     ↓
Final Dashboard
```

---

## Technologies Used

* **Python**
* **NumPy** - numerical and statistical computations
* **Pandas** - data manipulation, cleaning, grouping, and analysis
* **Matplotlib** - data visualization

No machine learning libraries such as Scikit-learn were used in this project.

---

## Dataset

The dataset contains information about students and their academic characteristics.

### Main Columns

| Column                  | Description                             |
| ----------------------- | --------------------------------------- |
| `student_id`            | Unique identifier for each student      |
| `gender`                | Student gender                          |
| `age`                   | Student age                             |
| `study_hours`           | Average study hours                     |
| `attendance`            | Attendance percentage                   |
| `sleep_hours`           | Average daily sleep                     |
| `previous_score`        | Previous academic score                 |
| `assignments_completed` | Percentage of assignments completed     |
| `class_participation`   | Class participation percentage          |
| `internet_access`       | Whether the student has internet access |
| `parental_support`      | Level of parental support               |
| `final_score`           | Final academic score                    |

The dataset intentionally contains missing values and duplicate records so that data-cleaning techniques can be practiced.

---

## Project Structure

```text
project_02_student_performance/
│
├── data/
│   └── student_performance.csv
│
├── src/
│   ├── generate_data.py
│   └── student_analysis.py
│
├── visualizations/
│   ├── final_score_distribution.png
│   ├── study_hours_vs_final_score.png
│   ├── attendance_vs_final_score.png
│   ├── previous_score_vs_final_score.png
│   ├── average_score_by_study_groups.png
│   ├── average_score_by_parental_support.png
│   ├── average_score_by_performance_category.png
│   ├── academic_risk_distribution.png
│   ├── correlation_matrix.png
│   └── student_performance_dashboard.png
│
├── README.md
└── requirements.txt
```

---

## Data Inspection

The project begins by inspecting the dataset using Pandas.

The analysis includes:

* Number of rows and columns
* Column names
* Data types
* Missing values
* Duplicate records
* Unique values in categorical columns
* Number of unique students
* General dataset statistics

Functions such as:

```python
df.shape
df.columns
df.dtypes
df.isnull().sum()
df.duplicated()
df.nunique()
```

are used to understand the structure and quality of the dataset.

---

## Data Cleaning

The dataset contains intentionally introduced data-quality issues.

The project handles:

### Duplicate Records

Duplicate rows are identified and removed.

```python
df.drop_duplicates()
```

### Missing Numerical Values

Missing values in numerical columns are handled using statistical values such as the mean.

### Missing Categorical Values

Missing categorical values are handled using the mode of the respective column.

This provides practical experience with common data-cleaning operations required before performing analysis or machine learning.

---

## Descriptive Statistics

The project calculates descriptive statistics using NumPy, including:

* Mean
* Median
* Standard deviation
* Minimum
* Maximum
* 25th percentile
* 75th percentile
* Interquartile range (IQR)
* Variance
* Skewness
* Kurtosis

These statistics are calculated for important numerical variables such as:

* Age
* Study hours
* Attendance
* Sleep hours
* Previous score
* Assignments completed
* Class participation
* Final score

---

## Performance Analysis

Students are categorized according to their final scores:

| Score Range | Category      |
| ----------- | ------------- |
| 90–100      | Excellent     |
| 80–89       | Very Good     |
| 70–79       | Good          |
| 60–69       | Average       |
| 50–59       | Below Average |
| 0–49        | Poor          |

A new feature called:

```text
performance_category
```

is created using Pandas.

---

## Correlation Analysis

The project investigates relationships between different academic variables and the final score.

The following relationships are analyzed:

* Study hours vs final score
* Attendance vs final score
* Sleep hours vs final score
* Previous score vs final score
* Assignments completed vs final score
* Class participation vs final score

Correlation is calculated using both Pandas and NumPy.

For example:

```python
df['study_hours'].corr(df['final_score'])
```

and:

```python
np.corrcoef(df['study_hours'], df['final_score'])
```

The results are then compared to understand how the two libraries perform correlation analysis.

---

## Group Analysis

Average final scores are analyzed across different groups, including:

* Gender
* Internet access
* Parental support
* Performance category
* Study-hour groups

This helps identify differences in academic performance between various student groups.

---

## Feature Engineering

Several new analytical features are created from existing data.

### Performance Category

```text
performance_category
```

categorizes students according to their final scores.

### Study Group

Students are grouped according to their study hours:

```text
Low
Moderate
High
Very High
```

### Academic Risk

Students are classified based on their final score:

```text
High Risk
Moderate Risk
Low Risk
```

### Manual Risk Score

A rule-based risk score is also created using multiple academic indicators.

Risk points are assigned based on factors such as:

* Final score
* Attendance
* Study hours
* Previous score
* Assignment completion
* Class participation

A final `risk_score` and `risk_category` are generated for each student.

> This is a manually designed rule-based scoring system, not a machine learning model.

---

## Outlier Detection

The project uses the **Interquartile Range (IQR)** method to identify potential outliers.

Outlier analysis is performed on:

* Final score
* Study hours
* Attendance
* Previous score

The following values are calculated:

```text
Q1
Q3
IQR
Lower Bound
Upper Bound
Number of Outliers
Percentage of Outliers
```

The standard IQR method is used:

```text
IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR
```

---

## Visualizations

Matplotlib is used to create multiple visualizations.

### 1. Final Score Distribution

A histogram showing how final scores are distributed among students.

### 2. Study Hours vs Final Score

A scatter plot used to examine the relationship between study time and academic performance.

### 3. Attendance vs Final Score

A scatter plot showing the relationship between attendance and final score.

### 4. Previous Score vs Final Score

A scatter plot examining the relationship between previous academic performance and final performance.

### 5. Average Score by Study Group

A bar chart comparing average final scores across different study-hour groups.

### 6. Average Score by Parental Support

A bar chart comparing academic performance across different parental-support levels.

### 7. Performance Analysis

A visualization of student performance categories.

### 8. Academic Risk Analysis

A visualization of students categorized according to academic risk.

### 9. Correlation Matrix

A Matplotlib heatmap displaying correlations between important numerical variables.

---

## Final Dashboard

The project combines several important visualizations into a single dashboard.

The dashboard contains:

* Final score distribution
* Study hours vs final score
* Attendance vs final score
* Average score by study group
* Academic risk analysis
* Correlation matrix

The final dashboard is saved as:

```text
visualizations/student_performance_dashboard.png
```

---

## Key Learning Outcomes

Through this project, I practiced:

### NumPy

* Statistical calculations
* Mean and median
* Standard deviation
* Variance
* Percentiles
* IQR
* Correlation
* Array operations
* Matrix operations

### Pandas

* CSV loading
* Dataset inspection
* Missing-value handling
* Duplicate removal
* Grouping and aggregation
* Filtering
* Sorting
* Categorical analysis
* Feature creation
* Correlation analysis
* Data transformation

### Matplotlib

* Histograms
* Scatter plots
* Bar charts
* Heatmaps using `imshow()`
* Multiple axes
* Subplots
* Figure customization
* Saving high-resolution figures
* Dashboard creation

---

## What I Learned

This project helped me understand that data analysis is not simply about applying Pandas methods to a CSV file.

A useful analytical workflow requires:

1. Understanding the dataset
2. Identifying data-quality problems
3. Cleaning the data carefully
4. Choosing appropriate statistical methods
5. Looking for relationships between variables
6. Creating meaningful features
7. Detecting unusual observations
8. Visualizing patterns
9. Interpreting the results
10. Thinking about how the analysis could eventually support machine learning

The project also reinforced an important principle:

> **Correlation does not imply causation.**

A strong correlation between two variables does not automatically mean that one variable causes the other.

---

## Future Improvements

This project is intentionally focused on NumPy, Pandas, and Matplotlib.

Future versions could include:

* More advanced statistical analysis
* Better feature engineering
* Automated data-quality checks
* Interactive dashboards
* Machine learning models
* Student performance prediction
* Academic-risk prediction
* Model evaluation
* Feature importance analysis
* Deployment as a web application

These improvements will be explored in later projects as the learning path progresses toward machine learning and AI engineering.

---

## How to Run

Clone the repository and install the required libraries:

```bash
pip install -r requirements.txt
```

Generate the dataset:

```bash
python generate_data.py
```

Then run the analysis:

```bash
python student_analysis.py
```

The analysis results will be displayed in the terminal and the generated visualizations will be saved inside the `visualizations/` directory.

---

## Author

**Abaseen Ahmed**

Aspiring AI/ML Engineer focused on building practical skills in:

```text
Python
Data Analysis
Machine Learning
Artificial Intelligence
```

This project is part of my hands-on journey toward becoming an AI/ML Engineer.
