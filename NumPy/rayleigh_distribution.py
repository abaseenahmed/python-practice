#=============================== Rayleigh Distribution In NumPy ====================================#
import numpy as np

arr_01 = np.random.rayleigh(6, 200)
print(f'Array: {arr_01}')
print(f'Shape : {np.shape(arr_01)}')
print(f'Mean Wind Speed : {np.mean(arr_01)}')
print(f'Max Wind Speed  : {np.max(arr_01)}')
print(f'Min Wind Speed  : {np.min(arr_01)}')
print(f'Standard Deviation : {np.std(arr_01)}')
print(f'Number of Wind Speed > 10km/h : {np.sum(arr_01 > 10)}')

arr_02 = np.random.rayleigh(4, (5,8))
print(f'Array: {arr_02}')
print(f'Shape : {np.shape(arr_02)}')
print(f'Average Signal Strength : {np.mean(arr_02, axis=1)}')
print(f'Strongest Signal  : {np.max(arr_02)}')
print(f'Weakest Signal  : {np.min(arr_02)}')
print(f'Strongest Signal Index : {np.argmax(np.mean(arr_02, axis=1))}')

arr_03 = np.random.rayleigh(3, 300)
arr_new1 = arr_03[arr_03 > 5]
arr_new2 = arr_03[arr_03 <= 5]
print(f'Original Waves : {arr_03}')
print(f'Number of High Waves : {len(arr_new1)}')
print(f'Number of Normal Waves : {len(arr_new2)}')
print(f'Mean of High Waves : {np.mean(arr_new1)}')
print(f'Mean of Normal Waves : {np.mean(arr_new2)}')

arr_04 = np.random.rayleigh(12, (6,10))
print(f'Shape : {np.shape(arr_04)}')
print(f'Hour With Highest Average Speed : {np.argmax(np.mean(arr_04, axis=1))}')
print(f'Hour With Lowest Average Speed : {np.argmin(np.mean(arr_04, axis=1))}')
print(f'Number of vehicles traveling faster than 20 : {np.sum(arr_04 > 20)}')
print(f'Number of vehicles traveling slower than 8 : {np.sum(arr_04 < 8)}')

arr_05 = np.random.rayleigh(9, 500)
print(f'Mean : {np.mean(arr_05)}')
print(f'Max : {np.max(arr_05)}')
print(f'Min : {np.min(arr_05)}')
print(f'Std : {np.std(arr_05)}')
print(f'Signals greater than the mean : {np.sum(arr_05 > np.mean(arr_05))}')
print(f'Signals less than the mean : {np.sum(arr_05 < np.mean(arr_05))}')
arr_new3 = arr_05[arr_05 > np.mean(arr_05)]
print(f'Number of Filtered Signal : {np.sum(arr_new3)}')
print(f'Average of Filtered Signal : {np.average(arr_new3)}')
print(f'Maximum Filtered Signal : {np.max(arr_new3)}')