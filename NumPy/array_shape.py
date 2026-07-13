#============================================ Shape of Array in NumPy =======================================#
import numpy as np

arr_01 = np.array([5, 10, 15, 20, 25])
#------ Expected Answer is (5,)
print(arr_01.shape)

arr_02 = np.array([
    [10,20,30],
    [40,50,60]
])
#------ Expected Answer is (2,3)
#------ 1D Array With 5 Elements
print(arr_02.shape)

arr_03 = np.array([
    [1,2],
    [3,4],
    [5,6]
])
#------ Expected Answer is (3,2)
#------ Rows = 3, Columns = 2
print(arr_03.shape)

arr_04 = np.array([
    [11,22,33,44],
    [55,66,77,88],
    [99,111,122,133]
])
#------ Expected Answer is (3, 4)
#------ Rows = 3, Columns = 5
print(arr_04.shape)

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
#------- Expected Answer is (2, 2, 2)
#------ Matrices = 2, Rows = 2, Columns = 2
print(arr_05.shape)

arr_06 = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
])
#--------- Expected Answer is (2, 2, 3)
#------ Matrices = 2, Rows = 2, Columns = 3
print(arr_06.shape)

arr_07 = np.array([
    [
        [1],
        [2],
        [3]
    ],
    [
        [4],
        [5],
        [6]
    ]
])
#-------- Expected Answer is (2, 3, 1)
#------ Matrices = 2, Rows = 3, Columns = 1
print(arr_07.shape)

arr_08 = np.array([
    [
        [10,20],
        [30,40],
        [50,60]
    ],
    [
        [70,80],
        [90,100],
        [110,120]
    ]
])
#------ Expected Answer is (2, 3, 2)
#------ Matrices = 2 Rows = 3, Columns = 2
print(arr_08.shape)

arr_09 = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]
])
#------- Expected Answer is (5, 4)
#------ Rows = 5, Columns = 4
print(arr_09.shape)

arr_10 = np.array([
    [
        [1,2,3,4],
        [5,6,7,8]
    ],
    [
        [9,10,11,12],
        [13,14,15,16]
    ],
    [
        [17,18,19,20],
        [21,22,23,24]
    ]
])
#------ Expected Shape is (3, 2, 4)
#------ Matrices = 3, Rows = 2, Columns = 4
print(arr_10.shape)