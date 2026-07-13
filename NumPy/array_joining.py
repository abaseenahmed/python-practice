#============================== Joining Arrays in NumPy =====================================#
import numpy as np

arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])
arr3 = np.concatenate((arr1, arr2))
print(arr3)
print(f'Shape of Array: {np.shape(arr3)}')

arr1 = np.array([
    [1,2],
    [3,4]
])

arr2 = np.array([
    [5,6],
    [7,8]
])

arr3 = np.concatenate((arr1, arr2), axis=0)
print(arr3)
print(f'Shape: {np.shape(arr3)}')

arr3 = np.concatenate((arr1, arr2), axis=1)
print(arr3)

arr1 = np.array([100,200,300])
arr2 = np.array([400,500,600])
arr3 = np.hstack((arr1, arr2))
print(arr3)

arr3 = np.vstack((arr1, arr2))
print(arr3)

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.stack((arr1, arr2))
print(arr3)
print(f'Shape = {np.shape(arr3)}')

arr3 = np.dstack((arr1, arr2))
print(arr3)
print(f'Shape = {np.shape(arr3)}')

arr1 = np.array([
    [10,20,30],
    [40,50,60]
])

arr2 = np.array([
    [70,80,90],
    [100,110,120]
])

arr3 = np.concatenate((arr1, arr2), axis=0)
print(arr3)
print(f'Shape = {arr3.shape}')

arr3 = np.concatenate((arr1, arr2), axis=1)
print(arr3)
print(f'Shape = {arr3.shape}')

arr1 = np.array([1,2])
arr2 = np.array([3,4])
arr3 = np.array([5,6])
arr4 = np.concatenate((arr1, arr2, arr3))
print(arr4)

arr1 = np.array([
    [1,2],
    [3,4]
])

arr2 = np.array([
    [5,6],
    [7,8]
])

arr3 = np.array([
    [9,10],
    [11,12]
])

arr4 = np.concatenate((arr1, arr2, arr3), axis=0)
arr4 = np.concatenate((arr1, arr2, arr3), axis=1)
arr4 = np.stack((arr1, arr2, arr3))