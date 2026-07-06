print("__________________________ Program 04 Collective Data Types __________________________")
#================================= Lists Data Types ==========================
#------------------------ Question No 1 -----------------------
fav_food = ["Pizza", "Burger", "Pasta", "Ice Cream"]
fav_food.append("Sushi")
fav_food.remove(fav_food[1])
print(f'My favorite foods are: {fav_food}')

#------------------------ Question No 2 -----------------------
my_numbers = [10, 20, 30, 40, 50]
sum_numbers = sum(my_numbers)
print(f'The sum of the numbers in the list {my_numbers} is: {sum_numbers}')
largest_number = max(my_numbers)
print(f'The largest number in the list {my_numbers} is: {largest_number}')
minimum_number = min(my_numbers)
print(f'The minimum number in the list {my_numbers} is: {minimum_number}')
print(f"The Reversed List is: {my_numbers[::-1]}")

#------------------------ Question No 3 -----------------------
shopping_cart = []
for i in range(3):
    item = input(f"Enter item {i + 1} to add to the shopping cart: ")
    shopping_cart.append(item)
print(f'The items in the shopping cart are: {shopping_cart}')
print("Which item would you like to remove from the shopping cart?")
remove_item = input("Enter the item to remove: ")
if remove_item in shopping_cart:
    shopping_cart.remove(remove_item)
    print(f'The updated shopping cart is: {shopping_cart}')

#------------------------ Question No 4 -----------------------
all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in all_numbers if x % 2 == 0]
print(f'The even numbers from the list {all_numbers} \n Are: {even_numbers}')

#------------------------ Question No 5 -----------------------
student_grades = [80, 90, 75, 85, 95]
student_grades.append(68)
avg_grade = sum(student_grades) / len(student_grades)
print(f'The average grade of the students is: {avg_grade}')
above_85 = 0
for i in range(len(student_grades)):
    if student_grades[i] > 85:
        above_85 += 1
        print(f'Student {i + 1} has a grade of {student_grades[i]} and has passed.')
print(f'The number of students who scored above 85 is: {above_85}')
print(f'The Student Grades in Descending Order are: {sorted(student_grades, reverse=True)}')

#------------------------ Question No 6 -----------------------
duplicate_numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 9, 1]
unique_numbers = list(set(duplicate_numbers))
print(f'The unique numbers from the list {duplicate_numbers} are: {unique_numbers}')

#================================ Tuples Data Types ==========================
#------------------------ Question No 1 -----------------------
my_movies = ("Inception", "The Dark Knight", "Interstellar", "The Matrix")
print(f'My favorite movies are: {my_movies}')
print(f'The First Movie is: {my_movies[0]}')
print(f'The Last Movie is: {my_movies[-1]}')

#------------------------ Question No 2 -----------------------
person = ("John", 30, "Engineer")
(name, age, profession) = person
print(f'Name: {name}, Age: {age}, Profession: {profession}')

#------------------------ Question No 3 -----------------------
numbers_tuple = (1, 2, 3, 4, 5)
numbers_list = list(numbers_tuple)
numbers_list.append(6)
numbers_tuple = tuple(numbers_list)
print(f'The updated tuple is: {numbers_tuple}')

#------------------------ Question No 4 -----------------------
fruits_tuple = ("Apple", "Banana", "Mango", "Grapes")
(red, yellow, *green) = fruits_tuple
print(f'The Red Fruid is: {red} The Yellow Fruit is: {yellow} The Green Fruits are: {green}')