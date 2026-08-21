import pandas as pd
from scipy import stats
import numpy as np

data = {
    "employee": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "experience": [1, 2, 3, 4, 5, 6, 7, 8],
    "salary": [35, 38, 42, 48, 55, 63, 72, 150],
    "projects": [1, 2, 2, 3, 4, 5, 6, 7],
    "performance": [60, 65, 67, 72, 78, 82, 85, 88]
}

df = pd.DataFrame(data)
print(df.head(5))
print(f'Mean: {df["salary"].mean()}')
print(f'Median: {df["salary"].median()}')
# The median represents the "typical" salary here.
# the mean is affected by extreme high or low numbers, while the median is not. so if there is very large or very small value in this dataset the mean is affected but median remains original.


Q1 = df['salary'].quantile(0.25)
Q3 = df["salary"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["salary"] < lower_bound) | (df["salary"] > upper_bound) ]
print(f'Outliers:\n{outliers}')
print('YES 150 is an Outlier')
print(f'Q1  : {Q1}')
print(f'Q3  : {Q3}')
print(f'IQR : {IQR}')

# The Z-score measures how many standard deviations a data point is from the mean. A standard threshold to isolate outliers is a Z-score greater than 3 or less than -3. You can easily leverage scipy.stats
z_scores = np.abs(stats.zscore(df['salary']))
outliers_z = df[z_scores > 3]
print(outliers_z)

mat = df[['salary', 'experience', 'performance']]
correlation = mat.corr()
print(correlation)
# experience ↔ performance relationship appears strongest
# YES a strong correlation prove that one variable causes the other
# If I plot the salary distribution, the distribution will approximately normal increasing from small to larger values

'''
 Based on the metrics provided for the fraud detection model, here are the calculated values for the confusion matrix and its corresponding performance evaluation metrics.
 
 Confusion Matrix BreakdownTrue 
 Positives (TP): 810 (Fraudulent transactions correctly flagged as fraud)
 False Positives (FP): 455 (Legitimate transactions incorrectly flagged as fraud)
 True Negatives (TN): 8,645 (Legitimate transactions correctly flagged as legitimate: (9,100 - 455)False Negatives (FN): 90 (Fraudulent transactions missed by the model: (900 - 810)

 Performance Evaluation Metrics
 Precision measures the proportion of flagged transactions that were actually fraudulent.
 Formula: ({TP} / {TP}+{FP}})
 Calculation: ({810} / {810 + 455} = {810} / {1,265} 
 Result: 64.03% (0.6403)
 
 Recall (Sensitivity)
 Recall measures the proportion of actual fraudulent transactions that the model successfully caught.
 Formula: {TP}} / {TP}+{FN}}
 Calculation: {810}/{810 + 90} = {810}/{900}
 Result: 90.00% (0.9000)
 
 AccuracyAccuracy measures the overall proportion of transactions that were correctly classified (both legitimate and fraudulent).
 Formula: {TP}+{TN}} / {Total Transactions}
 Calculation: {810 + 8,645} / {10,000} = {9,455} / {10,000}
 Result: 94.55% (0.9455)
'''

