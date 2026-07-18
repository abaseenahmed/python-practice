#====================================== Logarithemic Universal Functions ============================#
import numpy as np

arr_01 = np.random.randint(1, 100000, 500)
natural_log = np.log(arr_01)
mean_original = np.mean(arr_01)
mean_log = np.mean(natural_log)
log_vals = np.sum(natural_log > 10)
print(f'Maximum Log Value is : {np.max(natural_log)}')

arr_02 = np.random.choice([64,128,256,512,1024,2048], (6,8))
log_arr = np.log2(arr_02)
avg_log_val = np.mean(log_arr, axis=1)
high_avg = np.argmax(np.mean(log_arr))
max_log_val = np.max(log_arr)
min_log_val = np.min(log_arr)
# The Largest Log2 Value represents the highest storage size in computer. it shows the exponent of base 2 that makes 1048.

arr_03 = np.random.uniform(0.001, 500, 1000)
log_arr = np.log10(arr_03)
log_vals = np.sum( log_arr > 2)
mean_log = np.mean(log_arr)
std_log = np.std(log_arr)
sml_orig = np.min(arr_03)
sml_log = np.min(log_arr)
# no values can ever produce -inf because there is no such a number whose exponent can occure -inf

arr_04 = np.random.randint(0, 200, (20,30))
log_arr = np.log1p(arr_04)
mean_arr = np.mean(log_arr, axis=1)
max_mean = np.argmax(np.mean(log_arr, axis=1))
val_grt5 = np.sum(log_arr > 5)

data = np.random.randint(1, 5000, 1000)
log_e = np.log(data)
log_2 = np.log2(data)
log_10 = np.log10(data)
print(f'Mean e : {np.mean(log_e)}')
print(f'Mean 2 : {np.mean(log_2)}')
print(f'Mean 10 : {np.mean(log_10)}')
print(f'Std e: {np.std(log_e)}')
print(f'Std 2: {np.std(log_2)}')
print(f'Std 10: {np.std(log_10)}')
print(f'Max e: {np.max(log_e)}')
print(f'Max 2: {np.max(log_2)}')
print(f'Max 10: {np.max(log_10)}')
print(f'Max Avg of All : {np.max([np.mean(log_e), np.mean(log_2), np.mean(log_10)])}')
# The Averae are different due to the different bases of logarithem.
