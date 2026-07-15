#=================================== Bi - Nomial Distribution in NumPy ============================#
import numpy as np

arr_01 = np.random.binomial(10, 0.5, 8)
print(f'Array : {arr_01}')
print(f'Mean  : {np.mean(arr_01)}')
print(f'Max   : {np.max(arr_01)}')
print(f'Min   : {np.min(arr_01)}')
print('-'*50)

arr_02 = np.random.binomial(20, 0.8, 10)
print(f'Array : {arr_02}')
print(f'Mean  : {np.average(arr_02)}')
print(f'Max   : {np.max(arr_02)}')
print(f'Min   : {np.min(arr_02)}')
print('-'*50)

arr_03 = np.random.binomial(100, 0.95, 15)
print(f'Array : {arr_03}')
print(f'Mean  : {np.mean(arr_03)}')
print(f'Max   : {np.max(arr_03)}')
print(f'Min   : {np.min(arr_03)}')
print('-'*50)

arr_04 = np.random.binomial(30, 0.7, 12)
print(f'Array : {arr_04}')
print(f'Mean  : {np.average(arr_04)}')
print(f'Max   : {np.max(arr_04)}')
print(f'Min   : {np.min(arr_04)}')
print('-'*50)

arr_05 = np.random.binomial(50, 0.4, 20)
print(f'Array : {arr_05}')
print(f'Mean  : {np.mean(arr_05)}')
print(f'Standard Deviation  : {np.std(arr_05)}')
print('-'*50)

arr_06 = np.random.binomial(25, 0.9, 30) 
print(f'Mean  : {np.mean(arr_06)}')
print(f'Max   : {np.max(arr_06)}')
print(f'Min   : {np.min(arr_06)}')
print(f'Standard Deviation   : {np.std(arr_06)}')
print('-'*50)

arr_07 = np.random.binomial(15, 0.75, 20)
print(f'Array : {arr_07}')
print(f'Mean  : {np.mean(arr_07)}')
print(f'Max   : {np.max(arr_07)}')
print(f'Min   : {np.min(arr_07)}')
print('-'*50)

arr_08 = np.random.binomial(50, 0.6, (4,5))
print(f'Array : {arr_08}')
print(f'Shape : {arr_08.shape}')
print(f'Mean  : {np.mean(arr_08)}')
print(f'Standard Deviation : {np.std(arr_08)}')
print(f'Max   : {np.max(arr_08)} ')
print(f'Min   : {np.min(arr_08)} ')
print('-'*50)

# Question No. 1: 10 means that there are 10 independant trials each has a 0.7 probability of success 70% and this experiment is going to take place 5 times.
# Question NO. 2 B option is the correct.
# Question NO. 3 A. The number of successes will increase.
# Question No. 4 A. More experiments are generated.


arr_09 = np.random.binomial(50, 0.7, 100)
print(f'Average : {np.average(arr_09)}')
print(f'Highest Score : {np.max(arr_09)}')
print(f'Lowest Score : {np.min(arr_09)}')
print(f'Standard Deviation of  Scores : {np.std(arr_09)}')
print('='*50)