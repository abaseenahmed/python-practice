#================================== Arithmetic Universal Functions ===============================#
import numpy as np

arr1 = np.array([15, 25, 35])
arr2 = np.array([5, 10, 15])
print(f'Result : {np.add(arr1, arr2)}')
print(f'Shape  : {np.shape(np.add(arr1, arr2))}')

arr1 = np.array([100, 80, 60, 40])
arr2 = np.array([10, 20, 30, 40])
result = np.subtract(arr1, arr2)
print(f'Result : {result}')
print(f'Maximum : {np.max(result)}')
print(f'Minimum : {np.min(result)}')

arr1 = np.array([
    [2,3],
    [4,5]
])

arr2 = np.array([
    [10,20],
    [30,40]
])
result = np.multiply(arr1, arr2)
print(f'Result : {result}')
print(f'Shape : {np.shape(result)}')
print(f'Sum : {np.sum(result)}')

arr1 = np.array([120, 150, 200, 250])
arr2 = np.array([2, 5, 4, 10])
result = np.divide(arr1, arr2)
print(f'Result  : {result}')
print(f'Average : {np.mean(result)}')
print(f'Maximum : {np.max(result)}')
print(f'Minimum : {np.min(result)}')

base = np.array([2,3,4,5])
exp = np.array([3,2,3,2])
result = np.power(base, exp)
print(f'Result   : {result}')
print(f'Largest  : {np.max(result)}')
print(f'Smallest : {np.min(result)}')

arr1 = np.array([25,38,47,56,69])
arr2 = np.array([4,5,6,7,8])
result = np.mod(arr1, arr2)
print(f'Result = {result}')
print(f'No of Zeros : {np.sum(result == 0)}')
print(f'No of Non Zeros : {np.sum(result != 0)}')

marks = np.array([55,65,75,85,95])
result = np.add(marks, 5)
result = np.multiply(result, 2)
result = np.divide(result, 5)
print(f'Array : {result}')
print(f'Mean : {np.mean(result)}')

sales = np.array([
    [100,120,150],
    [200,220,250],
    [300,320,350]
])
result = np.add(sales, 50)
result = np.multiply(result, 1.1)
result = np.divide(result, 2)
print(f'Final Array : {result}')
print(f'Shape : {np.shape(result)}')
print(f'Mean : {np.mean(result)}')
print(f'Maximum : {np.max(result)}')
print(f'Minimum : {np.min(result)}')