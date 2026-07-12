#================================ Creating Arrays In NumPy ==============================#
import numpy as np

#------------------------- 1 Dimensional Array ----------------------#
arr_1d = np.array([1, 2, 3, 4, 5])
print("1 - Dimensional Array:")
print(arr_1d)

#------------------------- 2 Dimensional Array ----------------------#
arr_2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("2 - Dimensional Array:")
print(arr_2d)

#------------------------- 3 Dimensional Array ----------------------#
arr_3d = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print("3 - Dimensional Array:")
print(arr_3d)

#------------------------- Check The Number of Dimensions ----------#
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)