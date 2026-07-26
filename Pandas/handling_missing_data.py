#======================================= Handling Missing Data in Table ================================#
import pandas as pd
import numpy as np

students = {
    "Name": ["Ali", "Ahmed", "Sara", "John", "Jane", "Usman"],
    "Age": [20, np.nan, 21, 25, np.nan, 19],
    "Marks": [90, 85, np.nan, 78, 88, np.nan],
    "City": ["Lahore", "Karachi", np.nan, "Islamabad", "Faisalabad", "Quetta"]
}
df = pd.DataFrame(students)
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())
print('-'*50)

print(df)
print('-'*50)
print(df.isnull())
print('-'*50)
print(df.isnull().sum())
print('-'*50)
print(f'Total Numer of Missing Vaues in DataFrame : {df.isnull().sum().sum()}')
print('-'*50)
drop_col_df = df.dropna(axis=1)
print(drop_col_df)
print('-'*50)
print(df.fillna(0))
print('-'*50)
df['Age'] = df["Age"].fillna(18)
print(df["Age"])
print('-'*50)
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
print(df["Marks"])
print('-'*50)
df['City'] = df["City"].fillna('Unknown')
print(df["City"])
print('='*50)
print('The Fianl Data Frame Becomes')
print(df)
# NaN stands for 'Not A Number'
# The dropna() removes all the columns with missing values While fillna() fills all the values with particular variable
# I would use the mean when a column consists of similar values, such as marks, salary, age etc.
# The mode()[0] is more suitable to use because it fills the missing value with the first mode.
# you should check df.isnull().sum() in order to know which columns has how many missing values.
