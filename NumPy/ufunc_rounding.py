#==================================== Rounding Universal Functions ===================================#
import numpy as np

arr_01 = np.random.uniform(2500, 12000, 500)
arr_01 = np.round(arr_01, 2)
avg_bonus = np.average(arr_01)
high_bonuses = np.sum(arr_01 > 900)
max_bonus = np.max(arr_01)
min_bonus = np.min(arr_01)
print(f'Average Bonus : {avg_bonus}')
print(f'Number of Bonuses > 9000 : {high_bonuses}')
print(f'Maximum Bonus : {max_bonus}')
print(f'Minimum Bonus : {min_bonus}')

arr_02 = np.random.normal(loc=35.5, scale=1.8, size=(10,6))
arr_02a = np.floor(arr_02)
arr_02b = np.ceil(arr_02)
print(f'Array A : {arr_02a}')
print(f'Array B : {arr_02b}')
print(f'Difference Betwee Overall Mean : {np.subtract(np.mean(arr_02a), np.mean(arr_02b))}')
print(f'Number of Elements Changed : {np.sum(arr_02 != arr_02a)}')