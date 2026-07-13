#=================================== Reshape Method in Array ================================#
import numpy as np

arr_01 = np.array([1,2,3,4,5,6])
print(arr_01.reshape(2,3))

print(arr_01.reshape(3,2))

arr_02 = np.array([10,20,30,40,50,60,70,80])
print(arr_02.reshape(2, 4))

print(arr_02.reshape(4,2))

arr_03 = np.array([1,2,3,4,5,6,7,8])
print(arr_03.reshape(2,2,2))

arr_04 = np.arange(1,13)
print(arr_04.reshape(3, 4))

print(arr_04.reshape(2, 6))

print(arr_04.reshape(3, -1))

print(arr_04.reshape(-1, 4))

arr_05 = np.arange(1,25)
print(arr_05.reshape(2,3,4))

arr_06 = np.arange(1,17)
print(arr_06.reshape(4,4))


arr_07 = np.arange(1,13)
arr_07.reshape(2,6)       #Valid: 2 rows, 6 cols, 12 elements
arr_07.reshape(4,3)       #Valid: 4 rows, 3 cols, 12 elements
arr_07.reshape(3,2,2)     #Valid: 3 matrices, 2 rows, 2 cols, 12 elements
arr_07.reshape(5,2)       #Invalid: 5 rows, 2 cols, 10 elements
arr_07.reshape(2,2,3)     #Valid: 1 matrices, 2 rows, 2 cols