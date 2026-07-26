#================================ Handling Missing Values in Table ===================================#
import pandas as pd
import numpy as np

employees = {
    "Name": ["Ali", "Ahmed", "Sara", "John", "Jane", "Usman", "Ayesha", "Hamza"],
    "Department": [
        "IT",
        "HR",
        np.nan,
        "Finance",
        "IT",
        "HR",
        "Finance",
        np.nan
    ],
    "Age": [24, np.nan, 27, 30, np.nan, 25, 29, 31],
    "Salary": [50000, 45000, np.nan, 70000, 65000, np.nan, 72000, 68000],
    "Experience": [2, 1, np.nan, 5, 4, 2, np.nan, 6]
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

# Question No. 2 To 4 Already Done Above

print(f'The Total Number of NaN Values Are : {df.isnull().sum().sum()}')
print('-'*50)

clean_df = df.dropna()
print('Cleaned DataFrame')
print(clean_df)
print('Original DataFrame')
print(df)
print('-'*50)

filled_df = df.fillna('Unknown')
print(filled_df)
print('-'*50)

df['Age'] = df["Age"].fillna(df["Age"].mean())
print(df["Age"])
print('-'*50)

df['Salary'] = df["Salary"].fillna(df["Salary"].median())
print(df["Salary"])
print('-'*50)

df['Department'] = df["Department"].fillna('Not Assigned')
print(df["Department"])
print('-'*50)

df['Experience'] = df["Experience"].fillna(0)
print(df["Experience"])
print('-'*50)

print('The Final Cleand DataFrame is:')
print(df)

