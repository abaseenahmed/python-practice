#======================================== Iterating an Array ==================================#
import numpy as np

arr_01 = np.array([10, 20, 30, 40, 50])
for val in arr_01:
    print(val)

arr_02 = np.array([5, 10, 15, 20, 25])
for val in arr_02:
    print(f'Value = {val}')

arr_03 = np.array([
    [10,20,30],
    [40,50,60]
])
for row in arr_03:
    print(row)

for row in arr_03:
    for val in row:
        print(val)

arr_04 = np.array([
    [1,2],
    [3,4],
    [5,6]
])
for row in arr_04:
    for val in row:
        print(f'Element = {val}')

arr_05 = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])
for matrix in arr_05:
    print(matrix)

for matrix in arr_05:
    for row in matrix:
        for val in row:
            print(val)

arr_06 = np.array([
    [100,200],
    [300,400]
])
for val in np.nditer(arr_06):
    print(val)

arr_07 = np.array([
    [
        [11,22],
        [33,44]
    ],
    [
        [55,66],
        [77,88]
    ]
])
for val in np.nditer(arr_07):
    print(val)

arr_08 = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
for row in arr_08:
    print('\nRow:')
    for val in row:
        print(val)

arr_09 = np.array([
    [1,2,3],
    [4,5,6]
])
for row in arr_09:
    for val in row:
        if val %2 == 0:
            print(val)

arr_10 = np.array([
    [10,20],
    [30,40]
])
sum = 0
for val in np.nditer(arr_10):
    sum += val
print(f'Sum = {sum}')