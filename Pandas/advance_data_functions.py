#======================= Some More Advance Pandas Functions to apply on Datasets =====================#
import pandas as pd

employees = {
    "Name": ["Ali", "Ahmed", "Sara", "John", "Jane", "Usman", "Ayesha", "Hamza"],
    "Department": ["IT", "HR", "IT", "Finance", "IT", "HR", "Finance", "IT"],
    "Gender": ["Male", "Male", "Female", "Male", "Female", "Male", "Female", "Male"],
    "Salary": [50000, 45000, 65000, 70000, 60000, 48000, 72000, 55000],
    "Experience": [2, 1, 4, 5, 3, 2, 6, 2]
}

df = pd.DataFrame(employees)

print(df)
print('='*50)
df['Salary'] = df["Salary"].apply(lambda x: x*1.15)
df['Name'] = df["Name"].apply(str.upper)
df['Gender'] = df["Gender"].map({'Male':1, 'Female':0})
df['Department'] = df["Department"].replace({'HR': 'Human Resource'})
df["Salary"] = df["Salary"].astype(float)
df.rename(columns={'Salary':'Monthly_Salary'})

print(df)
print(f'Unique Departments : {df["Department"].unique()}')
print(f'The Number of Unique Departments : {df["Department"].nunique()}')
print(f'The Number of Employees belonging to each Department are : {df['Department'].value_counts()}')