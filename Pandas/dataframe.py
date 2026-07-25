#============================= Data Frame in Pandas ==================================#
import pandas as pd

person = {
    'Name': ['Ali', 'Ahmed', 'Sara', 'Khan', 'Jane'],
    'Age': [21, 19, 22, 20, 19],
    'City': ['Karachi', 'Quetta', 'Lahore', 'Islamabad', 'Faisalabad']
}
df = pd.DataFrame(person)
print(df)
print('='*50)

cart = {
    'Product' : ['Soap', 'Bread', 'Paste', 'Rice', 'Floor'],
    'Price' : [200, 239, 400, 360, 659],
    'Quantity' : [3, 3, 2, 3, 5]
}
df = pd.DataFrame(cart)
print(df)
print('='*50)

student = {
    'Name':['Ali', 'Ahmed', 'Sara', 'Khan', 'Jane'],
    'Marks' : [80, 89, 76, 92, 88],
    'Grade' : ['A', 'B-', 'A-', 'B+', 'C+']
}
index_val = ['S1', 'S2', 'S3', 'S4', 'S5']
df = pd.DataFrame(student, index=index_val)
print(df)
print('='*50)

print(df['Marks'])
print('='*50)

print(df[["Name", "Grade"]])
print('='*50)

employee = {
    'Name': ['Ali', 'Ahmed', 'Sara', 'Khan', 'Jane'],
    'Department': ['Accounting', 'Management', 'IT', 'Data', 'Security'],
    'Salary': [2100, 1900, 2200, 2000, 1900]
}
df = pd.DataFrame(employee)
print(f'Shape of DataFrame : {df.shape}')
print(f'Number of Columns in DataFrame : {df.columns.size}')
print(f'Data Type of DataFrame : {df.dtypes}')
print(f'Size of DataFrame : {df.size}')
print(f'Lenth of DataFrame : {len(df)}')
print('='*50)

movie_info = {
    'Movie': ['Jungle Book', 'Dark Night', 'Mission Impossible', 'Money Heist', 'Crime Caught'],
    'Year': [2002, 1980, 2004, 2001, 1995],
    'Rating': [4.5, 3.9, 4.7, 4.6, 4.0],
    'Genre': ['Action', 'Adventure', 'Sci-Fi', 'Comedy', 'Thriller'],
}
df = pd.DataFrame(movie_info)
print(df)
print(df['Movie'])
print(df[["Movie", "Rating"]])
print('='*50)