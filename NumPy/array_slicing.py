#================================ Array Slicing =================================#
import numpy as np

arr_01 = np.array([10, 20, 30, 40, 50, 60, 70])
print(arr_01[1:4])
print(arr_01[4:])
print(arr_01[:4])
print(arr_01[:])
print(arr_01[::1])
print(arr_01[1::2])
print(arr_01[::-1])

print(arr_01[-4:-1])
print(arr_01[-3:-1])
print(arr_01[-6:-1])

arr_02 = np.array([
                    [10,20,30],
                    [40,50,60],
                    [70,80,90]
                ])
print(arr_02[0:1,:])
print(arr_02[:-1,:])
print(arr_02[:,0:1])
print(arr_02[:,-1])

print(arr_02[0:2, 0:2])
print(arr_02[0:2, 1:])
print(arr_02[1:,])

print(arr_02[1:,1:])

print(arr_02[:,0::2])

arr_03 = arr = np.array([
                            [
                                [1,2],
                                [3,4]
                            ],
                            [
                                [5,6],
                                [7,8]
                            ]
                        ])
print(arr_03[0:1,:,:])
print(arr_03[1:,:,:])
print(arr_03[1:,0:1,:])
print(arr_03[0:1,1:,:])
print(arr_03[0:1,:,1:])
print(arr_03[1:,0:1,:])

arr_04 = arr = np.array([
                            [11,22,33,44],
                            [55,66,77,88],
                            [99,111,122,133],
                            [144,155,166,177]
                        ])
print(arr_04[1:3,1:3])
print(arr_04[:,-1])
print(arr_04[0:2,0:2])
print(arr_04[1:,2:])

print(arr_04[-1,::-1])