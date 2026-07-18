#=============================== Exponential Universal Functions ================================ #
import numpy as np

population = np.random.randint(1, 8, 250)
new_pop = np.exp(population)
avg_exp = np.mean(new_pop)
high_vals = np.sum(new_pop > 500)
lg_indx = np.argmax(new_pop)
original_indx = population[lg_indx]

sensor = np.random.uniform(0.1, 2.5, (8, 10))
new_arr = np.expm1(sensor)
avg_val = np.mean(new_arr, axis=1)
high_row = np.argmax(new_arr, axis=1)
count_val = np.sum(new_arr > 3)
max_val = np.max(new_arr)

growth_A = np.random.uniform(0, 3, 300)
growth_B = np.random.uniform(0, 4, 300)
growth_C = np.random.uniform(0, 5, 300)
exp_A = np.exp(growth_A)
exp_B = np.exp(growth_B)
exp_C = np.exp(growth_C)
mean_A = np.mean(exp_A)
mean_B = np.mean(exp_B)
mean_C = np.mean(exp_C)
largest_growth = np.argmax([mean_A, mean_B, mean_C])
count_A = np.sum(exp_A > 100)
count_B = np.sum(exp_B > 100)
count_C = np.sum(exp_C > 100)

numbers = np.random.randint(1, 8, 200)
arr_01 = np.power(numbers, 3)
arr_02 = np.exp(numbers)
mean_01 = np.mean(arr_01)
mean_02 = np.mean(arr_02)
if mean_01 > mean_02:
    print(f'Power Array has high average')
else:
    print(f'Exponent Array with base e has higher average')
if np.max(arr_01) > np.max(arr_02):
    print(f'Power Array has Larger maximum')
else: 
    print(f'Exponent Array with base e has larger maximum')

count_a = np.sum(arr_01 > 100)
count_b = np.sum(arr_02 > 100)

performance = np.random.uniform(0.5, 4.0, (12, 25))
arr_05 = np.exp(performance)
avg_score = np.mean(arr_05, axis=1)
dept_hscore = np.argmax(arr_05, axis=1)
count_vals = np.sum(arr_05 > 20)
max_val = np.max(arr_05)
min_val = np.min(arr_05)
lg_values = (np.sum(arr_05 > avg_score) / len(arr_05))*100