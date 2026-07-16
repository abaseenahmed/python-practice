#================================= Poission Distribution In NumPy ===========================================#
import numpy as np

arr_01 = np.random.poisson(12, 10)
print(f'Array : {arr_01}')
print(f'Mean  : {np.mean(arr_01)}')
print(f'Max   : {np.max(arr_01)}')
print(f'Min   : {np.min(arr_01)}')
print('-'*50)

arr_02 = np.random.poisson(18, 24)
print(f'Array : {arr_02}')
print(f'Mean  : {np.mean(arr_02)}')
print(f'Max   : {np.max(arr_02)}')
print(f'Min   : {np.min(arr_02)}')
print(f'Std   : {np.std(arr_02)}')
print('-'*50)

arr_03 = np.random.poisson(150, 30)
print(f'Array : {arr_03}')
print(f'Mean  : {np.mean(arr_03)}')
print(f'Max   : {np.max(arr_03)}')
print(f'Min   : {np.min(arr_03)}')
print('-'*50)

arr_04 = np.random.poisson(25, 20)
print(f'Array : {arr_04}')
print(f'Mean  : {np.mean(arr_04)}')
print(f'Std   : {np.std(arr_04)}')
print('-'*50)

arr_05 = np.random.poisson(40, 15)
print(f'Array : {arr_05}')
print(f'Max   : {np.max(arr_05)}')
print(f'Min   : {np.min(arr_05)}')
print(f'Avg   : {np.average(arr_05)}')
print('-'*50)

arr_06 = np.random.poisson(60, 48)
print(f'Mean  : {np.mean(arr_06)}')
print(f'Max   : {np.max(arr_06)}')
print(f'Min   : {np.min(arr_06)}')
print(f'Std   : {np.std(arr_06)}')
print('-'*50)

arr_07 = np.random.poisson(3, 20)
print(f'Array : {arr_07}')
print(f'Mean  : {np.mean(arr_07)}')
print(f'Max   : {np.max(arr_07)}')
print(f'Min   : {np.min(arr_07)}')
print('-'*50)

arr_08 = np.random.poisson(30, (4,5))
print(f'Array : {arr_08}')
print(f'Shape : {np.shape(arr_08)}')
print(f'Mean  : {np.mean(arr_08)}')
print(f'Std   : {np.std(arr_08)}')
print(f'Max   : {np.max(arr_08)}')
print(f'Min   : {np.min(arr_08)}')
print('-'*50)

# The lam = 10 means that on average 10 times an event takes place in a fixed interval of time while the size = 8 means perform this experiment 8 times.
# B. lam
# A. More events are expected.
# B. Number of observations increases.

arr_09 = np.random.poisson(250, 365)
print(f'Average : {np.average(arr_09)}')
print(f'Max     : {np.max(arr_09)}')
print(f'Min     : {np.min(arr_09)}')
print(f'Std     : {np.std(arr_09)}')
print(f'Shape   : {np.shape(arr_09)}')
print(f'Count   : {len(arr_09)}')
print('='*50)