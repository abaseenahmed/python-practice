print("________________ Hello This is a Simple Varaibales and Data Types Program in Python ___________________")
print("My Profile Information is as follows:")
my_name = 'Abaseen Ahmed'
my_age = 21
my_height = 5.7
likes_piza = False
print(f'My Name is: {my_name}. I am {my_age} years old. My height is {my_height} feet. Do I like pizza? {likes_piza}.')

#Reciept Generator For a Store
item1_name = 'Shirts'
item1_price = 500
item1_quantity = 3
item1_subtotal = item1_price * item1_quantity

item2_name = 'Pants'
item2_price = 700
item2_quantity = 2
item2_subtotal = item2_price * item2_quantity

item3_name = 'Shoes'
item3_price = 1200
item3_quantity = 4
item3_subtotal = item3_price * item3_quantity

total_bill = item1_subtotal + item2_subtotal + item3_subtotal

tax_rate = 0.10
tax_amount = total_bill * tax_rate
final_bill = total_bill + tax_amount

print("_________________________ Reciept _________________________")
print('------------------------------------------------------------------')
print(f'Item1: {item1_name}, Price: {item1_price}, Quantity: {item1_quantity}, Subtotal: {item1_subtotal}')
print(f'Item2: {item2_name}, Price: {item2_price}, Quantity: {item2_quantity}, Subtotal: {item2_subtotal}')
print(f'Item3: {item3_name}, Price: {item3_price}, Quantity: {item3_quantity}, Subtotal: {item3_subtotal}')
print('------------------------------------------------------------------')
print(f'Total Bill: {total_bill}')
print(f'Tax Amount: {tax_amount}')
print('------------------------------------------------------------------')
print(f'Final Bill: {final_bill}')
print('Thankyou For your shopping.')

print('___________________________ Numbers Data Types ____________________')
age = 21
height = 5.7
salary = 78000
age_in_days = age * 365
height_in_inches = height * 12
salary_in_year = salary * 12
print(f'My age in days is: {age_in_days} days.')
print(f'My Height in inches is: {height_in_inches} Inches.')
print(f'My Salary in Year is: {salary_in_year} .')

