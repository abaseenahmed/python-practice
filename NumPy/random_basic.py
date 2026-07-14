#=============================== Random Numbers in NumPy =====================================#
import numpy as np

arr_01 = np.random.randint(1, 50, 10)
print(f'The 10 Random Integers Are: {arr_01}')
print(f'The Shape of Array is: {arr_01.shape}')
print("-"*40)

arr_02 = np.random.randint(100, 200, (3,4))
print(f'\nThe 2D Array is: {arr_02}')
print(f'The Shape of 2D Array is: {arr_02.shape}')
print("-"*40)

arr_03 = np.random.rand(8)
print(f'The 8 Decimal Numbers Are: {arr_03}')
print(f'Max Number is: {np.max(arr_03)}')
print(f'Min Number is: {np.min(arr_03)}')
print("-"*40)

arr_04 = np.array(["Apple", "Banana", "Orange", "Mango", "Grapes"])
randome_fruit = np.random.choice(arr_04)
print(f'Random Fruit is: {randome_fruit}')
print(f'Five Fruits Are: {np.random.choice(arr_04, 5)}')
print("-"*40)

arr_05 = np.array([10,20,30,40,50,60,70,80])
print(f'Original Array: {arr_05}')
np.random.shuffle(arr_05)
print(f'Shuffled Array: {arr_05}')
print("-"*40)

arr_06 = np.random.randn(10)
print(f'Ten Normal Distribution Numbers Are: {arr_06}')
print(f'Mean: {np.mean(arr_06)}')
print("-"*40)

np.random.seed(42)
arr_07 = np.random.randint(1, 21, 6)
print(f'Random Seed Array: {arr_07}')
print("-"*40)

arr_08 = np.random.randint(1, 101, (4,5))
print(f'\n{arr_08}')
print(f'Shape = {arr_08.shape}')
print(f'Max = {np.max(arr_08)}')
print(f'Min = {np.min(arr_08)}')

np.random.shuffle(arr_08)
print("-"*40)

colors = np.array([
    "Red",
    "Green",
    "Blue",
    "Black",
    "White"
])
print(f'Three Random Colors: {np.random.choice(colors, 3)}')
print("="*40)
# np.random.randint(1, 10, 5)
# Smallest Possible Value = 1 np.min(np.random.randint(1, 10, 5))
# Largest Possible Value = 9 np.max(np.random.randint(1, 10, 5))
# 10 Can not appear because according to it's syntax the ten is not included.

# np.random.rand(4)
# The Smallest Possible Value is 0
# 1 can not be generated
# 1 is not included