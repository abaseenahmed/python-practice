#================================== Functions in Python ===================================
print("_______________________ Functions in Python _______________________")

#------------------------ Question No 1 -----------------------
def welcome():
    print("Welcome to the Python Functions Tutorial!")
welcome()

#------------------------ Question No 2 -----------------------
def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python Functions Tutorial.")
greet_user("Ahmed")

#------------------------ Question No 3 -----------------------
def add_numbers(num1, num2):
    return num1 + num2
result = add_numbers(5, 10)
print(f'The sum of 5 and 10 is: {result}')

#------------------------ Question No 4 -----------------------
def square(number):
    return number ** 2
result = square(4)

#------------------------ Question No 5 -----------------------
def check_even(number):
    if number % 2 == 0:
        print(f'The number {number} is even.')
    else:
        print(f'The number {number} is odd.')
check_even(7)

#------------------------ Question No 6 -----------------------
def max_num(num1, num2):
    if num1 > num2:
        print(f'The maximum number between {num1} and {num2} is: {num1}')
    elif num2 > num1:
        print(f'The maximum number between {num1} and {num2} is: {num2}')
    else:
        print(f'Both numbers are equal: {num1}')
max_num(15, 20)

#------------------------ Question No 7 -----------------------
def temperature_convertor(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
result = temperature_convertor(25)
print(f'The temperature in Fahrenheit for 25°C is: {result}°F')

#------------------------ Question No 8 -----------------------
def student_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    else:
        return 'F'
marks = 83
grade = student_grade(marks)
print(f'The grade for marks {marks} is: {grade}')

#------------------------ Question No 9 -----------------------
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)
result = factorial(5)
print(f'The factorial of 5 is: {result}')

#------------------------ Question No 10 -----------------------
print('Enter First Number: ')
num1 = int(input())
print('Enter Second Number: ')
num2 = int(input())
print('Which operation would you like to perform?')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
operation = int(input('Enter the operation number (1-4): '))
if operation == 1:
    result = lambda x, y: x + y
    print(f'The result of addition is: {result(num1, num2)}')
elif operation == 2:
    result = lambda x, y: x - y
    print(f'The result of subtraction is: {result(num1, num2)}')
elif operation == 3:
    result = lambda x, y: x * y
    print(f'The result of multiplication is: {result(num1, num2)}')
elif operation == 4:
    if num2 != 0:
        result = lambda x, y: x / y
        print(f'The result of division is: {result(num1, num2)}')
    else:
        print('Error: Division by zero is not allowed.')
