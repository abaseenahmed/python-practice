#======================================== Exponential Distribution in NumPy ======================================#
import numpy as np

arr_01 = np.random.exponential(scale = 8, size = 200)
print(f'Data : {arr_01}')
print(f'Shape : {np.shape(arr_01)}')
print(f'Avg Waiting Time : {np.average(arr_01)}')
print(f'Max Waiting Time : {np.max(arr_01)}')
print(f'Min Waiting Time : {np.min(arr_01)}')
print(f'Waiting Time greater Than 15 : {np.sum(arr_01 > 15)}')

arr_02 = np.random.exponential(3, (5,10))
print(f'Array : \n {arr_02}')
print(f'Shape : {np.shape(arr_02)}')
print(f'Mean : {np.mean(arr_02)}')
print(f'Std : {np.std(arr_02)}')
print(f'Max : {np.max(arr_02)}')
print(f'Min : {np.min(arr_02)}')
print(f'Avg Row : {np.mean(arr_02, axis=1)}')

arr_03 = np.random.exponential(50, 100)
print(f'Lasting > 70 Days  : {np.sum(arr_03 > 70)}')
print(f'Lasting < 20 Days  : {np.sum(arr_03 < 20)}')
print(f'Longest Life Time  : {np.max(arr_03)}')
print(f'Shortest Life Time : {np.min(arr_03)}')
print(f'Average  Life Time : {np.mean(arr_03)}')

arr_04 = np.random.exponential(6, 300)
print(f'Mean : {np.mean(arr_04)}')
print(f'Std : {np.std(arr_04)}')
print(f'Wating Time < 2 : {np.sum(arr_04 < 2)}')
print(f'Wating Time >=  2 <= 6: {np.sum((arr_04 >= 2) & (arr_04 <= 6))}')
print(f'Wating Time > 10 : {np.sum(arr_04 > 10)}')

arr_05 = np.random.exponential(12, (7, 20))
print(f'Array : \n {arr_05}')
print(f'Shape : {np.shape(arr_05)}')
print(f'Avg Day : {np.mean(arr_05, axis=1)}')
print(f'Highest Avg Day : {np.max(np.mean(arr_05, axis=1))}')

arr_06 = np.random.exponential(10, 500)
new_arr = arr_06[arr_06 <= 15]
print(f'Original Count : {len(arr_06)}')
print(f'Filter Count   : {len(new_arr)}')
print(f'Mean of Original : {np.mean(arr_06)}')
print(f'Mean of Filtered : {np.mean(new_arr)}')

arr_07 = np.random.exponential(4, 300)
arr_08 = np.random.exponential(8, 300)
print(f'Mean of A : {np.mean(arr_07)}')
print(f'Mean of B : {np.mean(arr_08)}')
print(f'Max Waiting Time of A : {np.max(arr_07)}')
print(f'Max Waiting Time of B : {np.max(arr_08)}')
print(f'Min Waiting Time of A : {np.min(arr_07)}')
print(f'Min Waiting Time of B : {np.min(arr_08)}')
if np.mean(arr_07) > np.mean(arr_08):
    print('The System B is Faster Than System A.')
else:
    print('The System A is Faster Than System B.')

arr_09 = np.random.exponential(15, (10, 50))
print(f'Shape : {np.shape(arr_09)}')
print(f'Average Waiting Time for Each Hour : {np.mean(arr_09, axis=1)}')
print(f'Hour With Highest average wait : {np.max(np.mean(arr_09, axis=1))}')
print(f'Hour With Lowest  average wait : {np.max(np.min(arr_09, axis=1))}')
print(f'Longest Waiting Passenger : {np.max(arr_09)}')
print(f'Shortest Waiting Passenger : {np.min(arr_09)}')
print(f'No. of Passenger Waiting more than 25 minutes : {np.sum(arr_09 > 25)}')
print(f'No. of Passenger Waiting less than 5 minutes : {np.sum(arr_09 < 5)}')

# Logical Thinking Questions Answeres
# B. scale, B. No, B. Waiting times become larger on average., scale=5 means average waiting time. size=(4,3) means 2D array with 4 rows and 3 columns, resulting shape (4,3) Poisson Distribution tells us the number of events occure in a specific time interval, while Exponential Distribution tells us the average waiting time for that interval to occure.
