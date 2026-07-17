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

