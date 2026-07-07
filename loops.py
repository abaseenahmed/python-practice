#================================= Loops in Python =================================#
print("-------------------------------- Loops in Python ---------------------------------")

#-------------------------------- Question No. 1 --------------------------------#
print("Question No. 1: Print numbers from 1 to 20 using a for loop.")
for i in range(1, 21):
    print(i, end=' ')

#-------------------------------- Question No. 2 --------------------------------#
print("\n\nQuestion No. 2: Print even numbers from 1 to 50 using a for loop.")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')

#-------------------------------- Question No. 3 --------------------------------#
print("\n\nQuestion No. 3: Print odd numbers from 1 to 50 using a for loop.")
for i in range(i, 51, 2):
    print(i, end=' ')

#------------------------------- Question No. 4 --------------------------------#
print("\n\nQuestion No. 4: Print the multiplication table of a given number using a for loop.")
number = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f'{number} X {i} = {number * i}')

#------------------------------ Question No. 5 --------------------------------#
print('\nQuestion No. 5: Print the first 10 Fibonacci numbers using a for loop.')
a = 0
b = 1
print(a, end=' ')
for i in range(1, 10):
    print(b, end=' ')
    a, b = b, a+b

#------------------------------ Question No. 6 --------------------------------#
print('\n\nQuestion No. 6: Print the sum of all numbers from 1 to 100 using a for loop.')
total_sum = 0
for i in range(1, 101):
    total_sum += i
print(f'The sum of all numbers from 1 to 100 is: {total_sum}')

#------------------------------ Question No. 7 --------------------------------#
print('\nQuestion No. 7: Print the factorial of a given number using a for loop.')
number = int(input("Enter a number to calculate its factorial: "))
for i in range(1, number):
    number *= i
print(f'The factorial of the given number is: {number}')

#------------------------------ Question No. 8 --------------------------------#
print('\nQuestion No. 8: Print the reverse of a given number using a for loop.')
number = int(input("Enter a number to reverse: "))
for i in range(len(str(number))):
    digit = number % 10
    print(digit, end='')
    number //= 10

#------------------------------ Question No. 9 --------------------------------#
print('\n\nQuestion No. 9: Print the sum of digits of a given number using a for loop.')
number = int(input("Enter a number to calculate the sum of its digits: "))
for i in range(len(str(number))):
    digit = number % 10
    total_sum += digit
    number //= 10
print(f'The sum of the digits of the given number is: {total_sum}')

#------------------------------ Question No. 10 --------------------------------#
print("Guess The Number....")
num = 8
gues = int(input("Guess the number between 1 to 10: "))
while gues != num:
    print("Wrong Guess! Try Again")
    gues = int(input("Guess the number between 1 to 10: "))
if gues == num:
    print("Congratulations! You guessed the correct number.")

#------------------------------ Question No. 11 --------------------------------#
correct_username = "admin"
correct_password = 12345

username = input("Please Enter The User Name: ")
password = input("Please Enter The Password: ")

if username == correct_username & password == correct_password:
    print("Logged In Successfully.")
elif username != correct_username | password != correct_password:
    print("Login Failed! Invalid User Name or Password.")

    