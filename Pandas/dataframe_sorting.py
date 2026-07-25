#============================ Sorting in DataFrame of Pandas ===========================#
import pandas as pd

students = {
    "Name": ["Ali", "Ahmed", "Sara", "John", "Jane", "Usman"],
    "Age": [20, 22, 21, 25, 23, 19],
    "Marks": [90, 85, 95, 78, 88, 91],
    "City": ["Lahore", "Karachi", "Quetta", "Islamabad", "Faisalabad", "Quetta"]
}
df = pd.DataFrame(students)

print(df.sort_values('Marks'))
print(df.sort_values('Marks', ascending=False))
print(df.sort_values('Name'))
print(df.sort_values('Age', ascending=False))
print(df.sort_values(['Marks', 'Age'], ascending=[True, True]))
print(df.sort_values(['Marks', 'Age'], ascending=[False, True]))
print(df.sort_index(ascending=False))

sorted_df = df.sort_values('City')
print(sorted_df)
print(df)
print(df.sort_values('Name', inplace=True))

# Question No. 1: The main difference between sorted_value() and sorted_index() is that the sorted values sort the dataframe by a column while the sort index sorts the dataframe by it's index
# Questions No. 2: the ascending=False sort the column in descending order in dataframe.
# Question No. 3 No the sort_values() does not modefy the original dataframe by default.
# Question No. 4 the inplace=True sorts the original dataframe
# many developers prefer df = df.sort_values(...) instead of inplace=True because in future we can performe so many other operatioins on the same data which is unsorted.
