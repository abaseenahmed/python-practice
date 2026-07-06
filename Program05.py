print("_______________________ Set Data Types _______________________")
#------------------------ Question No 1 -----------------------
duplicate_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 9, 1]
unique_set = set(duplicate_list)
print(f'The unique numbers from the list {duplicate_list} are: {unique_set}')

#------------------------ Question No 2 -----------------------
set_a = {"Ahmed", "Ali", "Sara", "Muhammad", "Fatima", "Omar"}
set_b = {"Ali", "Sara", "Omar", "Hassan", "Aisha"}
common_friends = set_a.intersection(set_b)
print(f'The common friends between set A and set B are: {common_friends}')

#------------------------ Question No 3 -----------------------
str_name = "Programming"
count_vowels = 0
for char in str_name:
    if char.lower() in "aeiou":
        count_vowels += 1
print(f'The number of vowels in the string "{str_name}" is: {count_vowels}')

#------------------------ Question No 4 -----------------------
set_numb1 = {1, 2, 3, 4, 5}
set_numb2 = {4, 5, 6, 7, 8}
set_num3 = set_numb1.symmetric_difference(set_numb2)
print(f'The numbers that are in either set_numb1 or set_numb2 but not in both are: {set_num3}')

#======================== Dictionary Data Types ==========================
#------------------------ Question No 1 -----------------------
student_info = {
    "name": "Ahmed",
    "age": 20,
    "course": "Computer Science",
    "grade": "A"
}
for key, value in student_info.items():
    print(f'{key}: {value}')

#------------------------ Question No 2 -----------------------
person = {"name": "Sara", "city": "Karachi", "job": "Engineer", "age": 28}
print(f'The Person Name is: {person["name"]}')
print(f'The Person City is: {person["city"]}')
print(f'The Person Job is: {person["job"]}')

#------------------------ Question No 3 -----------------------
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
car["color"] = "Red"
print(f'The updated car information is: {car}')

#------------------------ Question No 4 -----------------------
product = {"name": "Laptop", "price": 800, "stock": 10}
product.update({"price": 750, "stock": 15})
print(f'The updated product information is: {product}')

#------------------------ Question No 5 -----------------------
inventory = {"apples": 5, "bananas": 3, "oranges": 7}
if "apples" in inventory:
    print(f'The number of apples in the inventory is: {inventory["apples"]}')