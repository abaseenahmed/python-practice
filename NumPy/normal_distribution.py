#=================================== Normal Distribution in NumPy ================================#
import numpy as np

arr_01 = np.random.normal(loc=70, scale=10, size=20)
print(f'Array = {arr_01}')
print(f'Mean = {np.mean(arr_01)}')
print(f'Standard Deviation = {np.std(arr_01)}')
print('-'*50)

arr_02 = np.random.normal(loc = 50000, scale = 5000, size = 50)
print(f'Salaries = {arr_02}')
print(f'Mean Salary = {np.mean(arr_02)}')
print(f'Maximum Salary = {np.max(arr_02)}')
print(f'Minimum Salary = {np.min(arr_02)}')
print('-'*50)

arr_03 = np.random.normal( loc = 100, scale = 15, size = (4,5))
print(f'Array = {arr_03}')
print(f'Shape = {arr_03.shape}')
print(f'Mean = {np.mean(arr_03)}')
print('-'*50)

arr_04 = np.random.normal( loc = 60, scale = 5, size = 100)
arr_05 = np.random.normal( loc = 60, scale = 5, size = 100,)
print(f'Mean of First Array  : {np.mean(arr_04)}')
print(f'Mean of Second Array : {np.mean(arr_05)}')
print(f'Standard Deviation of First Array  : {np.std(arr_04)}')
print(f'Standard Deviation of Second Array : {np.std(arr_05)}')
print('-'*50)

arr_06 = np.random.normal( loc = 170, scale = 8, size = 200)
print(f'Mean Height = {np.mean(arr_06)}')
print(f'Tallest Student = {np.max(arr_06)}')
print(f'Shortest Student = {np.min(arr_06)}')
print('-'*50)

arr_07 = np.random.normal( loc = 37, scale = 0.5, size = 150)
print(f'Average Temprature = {np.mean(arr_07)}')
print(f'Highest Temprature = {np.max(arr_07)}')
print(f'Lowest Temprature = {np.min(arr_07)}')
print('-'*50)

arr_08 = np.random.normal( loc = 100, scale = 15, size = 500)
print(f'Mean Value = {np.mean(arr_08)}')
print(f'Standard Deviation = {np.std(arr_08)}')
print(f'Number of Values Generated = {len(arr_08)}')
print('-'*50)

arr_09 = np.random.normal( loc = 75, scale = 12, size = (5,4))
print(f'Array : {arr_09}')
print(f'Shape : {arr_09.shape}')
print(f'Mean  : {np.mean(arr_09)}')
print(f'Standard Deviation : {np.std(arr_09)}')
print(f'Maximum Value      : {np.max(arr_09)}')
print(f'Minimum Value      : {np.min(arr_09)}')
print('-'*50)

arr_10 = np.random.normal( loc = 65, scale = 12, size = 500)
print(f'Average Marks = {np.mean(arr_10)}')
print(f'Highest Marks = {np.max(arr_10)}')
print(f'Lowest  Marks = {np.min(arr_10)}')
print('='*50)

# Logical Thinking Questions
# Question 1: The value 50 means that it is the mean value and all other values will be near to it.
# Question 1: The value 10 is the standard deviation. The higher the standard deviation the farther the values will be and the smaller the standard deviation the nearer the values will be while the value 100 represents the size of the array.
# Question 2: scale parameter
# Question 3: B. The values become more spread out.
# Question 4: C. size
# Question 5: YES because the mean is the middle value so it is clearly proved that the values can lie below the mean value.
