#================================ Filtering Data in Pandas ================================#
import pandas as pd

students = {
    "Name": ["Ali", "Ahmed", "Sara", "John", "Jane", "Usman", "Ayesha"],
    "Age": [20, 22, 21, 25, 23, 19, 24],
    "Marks": [90, 85, 95, 78, 88, 91, 82],
    "City": ["Lahore", "Karachi", "Quetta", "Islamabad", "Faisalabad", "Quetta", "Lahore"]
}
df = pd.DataFrame(students)

#Students With Marks > 90
print(df[df['Marks'] > 90])
print('='*50)

#Students With Age < 22
print(df[df['Age'] > 22])
print('='*50)

#Students With City == Lahore
print(df[df['City'] == 'Lahore'])
print('='*50)

#Students With Marks >= 90
print(df[df['Marks'] >= 90])
print('='*50)

#Students With Marks > 85 & Age < 20
print(df[(df['Age'] < 20) & (df['Marks'] > 85)])
print('='*50)

#Students With City == Lahore | City == Quetta
print(df[(df['City'] == 'Lahore') | (df['City'] == 'Quetta')])
print('='*50)

#Students Not From Karachi
print(df[~(df['City'] == 'Karachi')])
print('='*50)

#Students From Quetta, Lahore, Islamabad
print(df[df['City'].isin(['Quetta', 'Islamabad', 'Lahore'])])
print('='*50)

#students whose marks are between 85 and 91.
print(df[df['Marks'].between(85, 91)])
print('='*50)

#Students With Marks > 85
print(df.loc[df["Marks"] > 85, ["Name", "Marks"]])
print('='*50)