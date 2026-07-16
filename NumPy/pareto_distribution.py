#================================= Pareto Distribution in NumPy =====================================#
import numpy as np

arr_01 = np.random.pareto(2.5, 365)
print(f'Generated Array : {arr_01}')
print(f'Shape of Array  : {np.shape(arr_01)}')
print(f'Mean Visitors  : {np.mean(arr_01)}')
print(f'Maximum Visitors  : {np.max(arr_01)}')
print(f'Minimum Visitors  : {np.min(arr_01)}')
print(f'Standard Deviation  : {np.std(arr_01)}')
print(f'Number of blog posts with visitor values greater than 2 : {np.sum(arr_01 > 2)}')
print(f'Number of blog posts with visitor values less than or equal to 2 : {np.sum(arr_01 <= 2)}')

arr_02 = np.random.pareto(3, (8, 25))
print(f'Shape of Array : {np.shape(arr_02)}')
print(f'Average Sales of Each Team : {np.mean(arr_02, axis=1)}')
print(f'Team with the highest average sales : {np.argmax(np.mean(arr_02, axis=1))}')
print(f'Team with the lowest average sales : {np.argmin(np.mean(arr_02, axis=1))}')
print(f'Highest Individual Sale : {np.max(arr_02)}')
print(f'Lowest Individual Sale : {np.min(arr_02)}')

arr_03 = np.random.pareto(2, 500)
high_spenders = arr_03[arr_03 > np.mean(arr_03)]
normal_spenders = arr_03[arr_03 <= np.mean(arr_03)]
print(f'Total Customers : {len(arr_03)}')
print(f'High Spenders Count : {len(high_spenders)}')
print(f'Normal Spenders Count : {len(normal_spenders)}')
print(f'Average of High Spenders  : {np.mean(high_spenders)}')
print(f'Average of Normal Spenders : {np.mean(normal_spenders)}')
print(f'Highest Spender : {np.argmax(high_spenders)}')

arr_04 = np.random.pareto(4, (12, 40))
print(f'Shape : {np.shape(arr_04)}')
print(f'Average bug severity for each project: {np.mean(arr_04, axis=1)}')
print(f'Project with the Highest average severity: {np.argmax(np.mean(arr_04, axis=1))}')
print(f'Project with the Lowest average severity: {np.argmin(np.mean(arr_04, axis=1))}')
print(f'Number of bug reports greater than 1.5: {np.sum(arr_04 > 1.5)}')
print(f'Number of bug reports less than 0.5: {np.sum(arr_04 < 0.5)}')

arr_05 = np.random.pareto(1.8, 1000)
print(f'Mean popularity : {np.mean(arr_05)}')
print(f'Standard Deviation : {np.std(arr_05)}')
print(f'Maximum popularity : {np.max(arr_05)}')
print(f'Minimum popularity : {np.min(arr_05)}')
new_arr = arr_05[arr_05 > 3]
print(f'Number of popular influencers : {len(new_arr)}')
print(f'Avg of popular influencers : {np.mean(new_arr)}')
print(f'Max of popular influencers : {np.max(new_arr)}')
print(f'Percentage of Influencers greater than 3 : {(len(arr_05) / len(new_arr)) * 100}')