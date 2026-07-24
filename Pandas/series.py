#============================= Series in Pandas =====================================#
import pandas as pd

numbers = [10, 20, 30, 40, 50]
num_col = pd.Series(numbers)
print(num_col)

student_names = ['Ahmed', 'Khan', 'Ali', 'Sara', 'Jane']
name_col = pd.Series(student_names)
print(name_col)

dec_num = [0.5, 2.8, 3.9, 6.2, 1.4]
grad_col = pd.Series(dec_num)
print(grad_col)

marks = [90, 85, 78, 92, 88]
marks_col = pd.Series(marks, index = ['Ali', 'Ahmed', 'Sara', 'John', 'Ayesha'])
print(marks_col)

print(f'Sara Marks = {marks_col['Sara']}')

student = {
    "Ali" : "90",
    "Ahmed" : "85",
    "Sara" : "95",
    "John" : "80"
}
stu_col = pd.Series(student)
print(stu_col)

salary = [100, 200, 300, 400, 500]
salary_col = pd.Series(salary)
print(f'Length    : {len(salary_col)}')
print(f'Data Type : {salary_col.dtype}')
print(f'Shape     : {salary_col.shape}')

prog_lan = ['C++', 'C', 'JavaScript', 'Python', 'Java']
lang_col = pd.Series(prog_lan, index = ['first', 'second', 'third', 'fourth', 'fifth'])
print(lang_col['third'])