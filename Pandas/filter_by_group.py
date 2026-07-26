#============================ Filter Data by Gropus in DataFrame using Pandas =================================#
import pandas as pd

employees = {
    "Name": ["Ali", "Ahmed", "Sara", "John", "Jane", "Usman", "Ayesha", "Hamza"],
    "Department": ["IT", "HR", "IT", "Finance", "IT", "HR", "Finance", "IT"],
    "City": ["Lahore", "Karachi", "Lahore", "Quetta", "Karachi", "Quetta", "Lahore", "Karachi"],
    "Salary": [50000, 45000, 65000, 70000, 60000, 48000, 72000, 55000],
    "Experience": [2, 1, 4, 5, 3, 2, 6, 2]
}
df = pd.DataFrame(employees)

print(df.head()) # Prints The Top 5 Rows of DataFrame
print('-'*50)

print(df.info()) # Prints The Details about the DataFrame
print('-'*50)

print(df.isnull().sum()) # Counts the Number of Nan (Missing Values) Values of each column
print('-'*50)

print(df.describe()) # Describes the Basics Stats of the DataFrame
print('-'*50)

#============================================================================

print(df)
print('-'*50)

print(df.groupby('Department')['Salary'].mean())
print('-'*50)

print(df.groupby('Department')['Salary'].sum())
print('-'*50)

print(df.groupby('Department')['Name'].count)
print('-'*50)

print(df.groupby('Department')['Salary'].max())
print('-'*50)

print(df.groupby('Department')['Salary'].min())
print('-'*50)

print(df.groupby('Department')['Salary'].median())
print('-'*50)

print(df.groupby('Department')['Salary'].agg(['mean', 'max', 'min', 'sum', 'count']))
print('-'*50)

print(df.groupby(['Department', 'City'])['Salary'].mean())
print('-'*50)

# the purpose of groupby() is to make a group of similar values in a particular column
# count() return the number of non missing values while size() return the rows
# agg() is useful for finding aggregates with different perspectives such as min, max, mean, median etc
# if you call groupby() without mean(), sum(), or another aggregation it will not return any value unless you define it to return
# groupby() would be helpful for data analysis of different fields such as banks, schoold, universities, etc

