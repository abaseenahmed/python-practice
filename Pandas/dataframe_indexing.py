#================================ DataFrame Indexing Rows & Columns =============================#
import pandas as pd

students = {
    "Name": ["Ali", "Ahmed", "Sara", "John", "Jane"],
    "Age": [20, 22, 21, 25, 23],
    "Marks": [90, 85, 95, 78, 88],
    "City": ["Lahore", "Karachi", "Quetta", "Islamabad", "Faisalabad"]
}
student_df = pd.DataFrame(students)
print(student_df)
print('='*50)

print(student_df['Name'])
print('='*50)

print(student_df[['Name', 'City']])
print('='*50)

print(student_df.loc[2])
print('='*50)

print(student_df.iloc[1])
print('='*50)

print(student_df.loc[0:3])
print('='*50)

print(student_df.iloc[0:4])
print('='*50)


print(student_df.loc[1])
print(student_df.loc[:, 'Marks'])
print('='*50)

print(student_df.iloc[3, 2])
print('='*50)

print(student_df.loc[[0, 3]])
print(student_df.loc[:, ['Name', 'City']])
print('='*50)

print(student_df.iloc[[0, 2, 4]])
print(student_df.iloc[:, [0, 1]])
print('='*50)