#============================= Reading and Writing Data Files such as CSV, XlSX, JSON etc ==========================#
import pandas as pd
emoployees_df = pd.read_csv('employees.csv')
print(emoployees_df)

print(emoployees_df.head())
print(emoployees_df.tail())
print(emoployees_df.shape)
print(emoployees_df.columns)
print(emoployees_df.info())
print(emoployees_df.describe())

print(pd.read_csv('employees.csv', usecols=['Name', 'Salary']))

print(pd.read_csv('employees.csv', nrows=3))

print(pd.read_csv('employees.csv', usecols=['Name', 'Department']))

high_salary_df = emoployees_df[emoployees_df['Salary'] > 50000]

high_salary_df.to_csv('high_salary_employees.csv', index=False)

# Why is CSV the most commonly used file format in Data Science?
# CSV is more commonly used file formate because it is easy to read, write and understand both for the computer and humans

# Why should you inspect a dataset before cleaning it?
# One should always inspect the dataset before cleaning and applying operations on it to get an overiew of the dataset and understand what does this data include

# Why is index=False commonly used when saving CSV files?
# the index = False is commonly used for good reading purposes

# When would usecols improve performance?
# the usecols can improve the perfomance and make the program run more fastly by printing only those columns which are required and necessary

# What is the difference between head() and tail()?
# The head() selects the top five rows of dataset while the tail() selects the bottom five rows of dataset.