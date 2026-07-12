#============================== Indexing in N - Dimensional Arrays ==================#
import numpy as np

arr_1d = np.array([15, 30, 45, 60, 75])
print(f'First Element  : {arr_1d[0]}')
print(f'Last Element   : {arr_1d[-1]}')
print(f'Third Element  : {arr_1d[2]}')
print(f'Fourth Element : {arr_1d[-2]}')

arr_2d = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])
print(f'1. {arr_2d[0,0]}')
print(f'2. {arr_2d[1,1]}')
print(f'3. {arr_2d[-1,-1]}')
print(f'4. {arr_2d[-1,0]}')
#---- Negative Indexing -------
print(f'1. {arr_2d[-1,-1]}')
print(f'2. {arr_2d[-1,-2]}')
print(f'3. {arr_2d[-3,-1]}')
print(f'4. {arr_2d[-3,-3]}')

arr_3d = np.array([
                    [
                        [1, 2],
                        [3, 4]
                    ],

                    [
                        [5, 6],
                        [7, 8]
                    ]
                    ])
print(f'1. {arr_3d[0,0,0]}')
print(f'2. {arr_3d[0,1,1]}')
print(f'3. {arr_3d[1,0,0]}')
print(f'4. {arr_3d[1,1,1]}')
#------ Mixed Indexing -------
print(f'1. {arr_3d[0,0,-1]}')
print(f'2. {arr_3d[-1,-1,0]}')
print(f'3. {arr_3d[-1,0,-1]}')
print(f'4. {arr_3d[-2,-1,0]}')

new_2d = np.array([
                    [100,200,300],
                    [400,500,600]
                ])
print(new_2d[-1,-1])

arr = np.array([
    [5,10,15],
    [20,25,30],
    [35,40,45]
])
#--- My Prediction is 40
print(arr[2,1])
#--- My Prediction is 20
print(arr[-2,-3])

new_arr = np.array([
                        [
                            [11,22],
                            [33,44]
                        ],
                        [
                            [55,66],
                            [77,88]
                        ]
                    ])
print(new_arr[-1,-1,0])
print(new_arr[0,-1,-1])