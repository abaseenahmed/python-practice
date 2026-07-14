#===================================== Random Permutation In NumPy ================================#
import numpy as np

arr_01 = np.array([10, 20, 30, 40, 50, 60])
print(f'Original Array: {arr_01}')
np.random.shuffle(arr_01)
print(f'Suffeled Array: {arr_01}')
print('-'*50, end='\n')

arr_02 = np.array([5, 10, 15, 20, 25])
arr_02_permutation = np.random.permutation(arr_02)
print(f'Original Array: {arr_02}')
print(f'Permutation Array: {arr_02_permutation}')
print('-'*50, end='\n')

arr_03 = np.random.permutation(10)
print(f'Random Permutation: {arr_03}')

arr_04 = np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])
print(f'Original Array: \n{arr_04}')
np.random.shuffle(arr_04)
print(f'Shuffled Array: \n{arr_04}')
print('-'*50, end='\n')

arr_05 = np.array([
    [10,20],
    [30,40],
    [50,60]
])
print(f'Original Array: \n{arr_05}')
new_arr = np.random.permutation(arr_05)
print(f'Permutation Array: \n{new_arr}')
print(f'Original Array: \n{arr_05}')
print('-'*50, end='\n')

fruits = np.array([
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Grapes",
    "Peach"
])
np.random.shuffle(fruits)
print(f'Fruits = {fruits}')
permuted_arr = np.random.permutation(fruits)
print(f'Permuted Array: {permuted_arr}')
print('-'*50, end='\n')

students = np.array([
    ["Ali", 85],
    ["Ahmed", 78],
    ["Sara", 92],
    ["Ayesha", 88]
])
print(f'Original Array: {students}')
new_stu = np.random.permutation(students)
print(f'Permuted Array: {new_stu}')
print('-'*50, end='\n')

numbers = np.arange(1, 13)
print(f'Original Array: {numbers}')
numbers.reshape(3,4)
np.random.shuffle(numbers)
print(f'Shuffled Array: {numbers}')
new_arr = np.random.permutation(numbers)
print(f'Permuted Array: {new_arr}')
print(f'Shape of Shuffled Array: {numbers.shape}')
print(f'Shape of Permuted Array: {new_arr.shape}')
print('='*50, end='\n')
# Answers For Bonus Questions
# Question 1 = B
# Question 2 = B
# Question 3 = B
# Question 4 = B