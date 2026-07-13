#================================ Searching in Array ======================================#
import numpy as np

arr = np.array([15, 25, 35, 45, 55, 35, 75])
indx = np.where(arr == 35)
print(f'Indices For 35: {indx}')

arr = np.array([11, 14, 18, 21, 24, 27, 30, 33])
even_indx = np.where(arr % 2 == 0)
even_num = len(even_indx)
print(f'The Even Number Indices Are: {even_indx}')
print(f'Total Number of Even Numbers Are: {even_num}')

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
item = np.where(arr == 80)
row = item[0]
col = item[1]
print(f'The Index of 80 is : {item}')
print(f'Row = {row}')
print(f'col = {col}')

arr = np.array([10, 20, 30, 40, 50, 60])
indices = np.searchsorted(arr, [25, 55, 5, 100])
print(indices)

arr = np.array([
    [12, 15, 18],
    [21, 24, 27],
    [30, 33, 36]
])
item1 = np.where(arr > 20)
item2 = np.where(arr%3 == 0)
item3 = np.where(arr == 24)

numbers = np.array([5, 10, 15, 20, 25, 30])
indx = np.searchsorted(arr, 17)