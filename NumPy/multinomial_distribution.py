#============================================= Multinomial Distribution in NumPy ==========================================#
import numpy as np

arr_01 = np.random.multinomial(n=20, pvals=[0.5,0.3, 0.2], size=1)
print(f'Array : {arr_01}')
print(f'Count : {np.sum(arr_01)}')

arr_02 = np.random.multinomial(30, [1/6]*6, 1)
print(f'Result : {arr_02}')
print(f'Count : {np.sum(arr_02)}')

arr_03 = np.random.multinomial(50, [0.4, 0.35, 0.25], 5)
print(f'Result   : {arr_03}')
print(f'Shape    : {np.shape(arr_03)}')
print(f'Sum Rows : {np.sum(arr_03, axis=1)}')

arr_04 = np.random.multinomial(n = 100, pvals = [0.20, 0.35, 0.30, 0.25], size = 3)
print(f'Result   : {arr_04}')
print(f'Shape    : {np.shape(arr_04)}')
print(f'Sum Row  : {np.sum(arr_04, axis=1)}')

arr_05 = np.random.multinomial(n = 40, pvals = [0.25, 0.30, 0.20, 0.15, 0.10], size = 2) 
print(f'Result   : {arr_05}')
print(f'Shape    : {np.shape(arr_05)}')
print(f'Sum All  : {np.sum(arr_05)}')

arr_06 = np.random.multinomial(n = 100, pvals = [0.65, 0.25, 0.10], size = 10)
print(f'Result   : {arr_06}')
print(f'Shape    : {np.shape(arr_06)}')
print(f'Sum All  : {np.sum(arr_06)}')

arr_07 = np.random.multinomial(n = 60, pvals = [0.5, 0.3, 0.2], size = 4)
print(f'Result   : {arr_07}')
print(f'Shape    : {np.shape(arr_07)}')
print(f'Mean Val : {np.mean(arr_07)}')
print(f'Max  Val : {np.max(arr_07)}')
print(f'Min  Val : {np.min(arr_07)}')
print(f'Sum  all : {np.sum(arr_07)}')