#====================================== OOPS in Python ================================#
print('_____________________________ OOPS Basics in Python ____________________________')

#----------------------------------- Question No.1 -------------------------------------
class student:
    def __init__(self, name, roll_num):
        self.name = name
        self.roll_number = roll_num

    def display_info(self):
        print(f'Student Name: {self.name}. Roll Number: {self.roll_number}.')
    
student_1 = student("Ahmed", 29204)
student_2 = student("Khan", 32893)
student_3 = student("Ali", 38928)

print("The Student Records Are as follow: ")
student_1.display_info()
student_2.display_info()
student_3.display_info()

#------------------------------- Question No. 2 --------------------------------------
class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def car_info(self):
        print(f'The Car is of {self.brand} Brand, {self.model} Model, and {self.year} Year.')


car_1 = car("Toyota", "XLA 77310", 2025)
car_2 = car("Suzuki", "ALG 78893", 2024)

print("The Car Details in Showroom Are: ")
car_1.car_info()
car_2.car_info()

#------------------------------ Question No. 3 --------------------------------------------
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.employee_id = emp_id
        self.salary = salary

    def display_employee(self):
        print("The Employee Details Are: ")
        print(f'Name: {self.name} \n Employee ID: {self.employee_id} \n Salary: {self.salary}')

employee_1 = Employee("Ahmed", "KG-98305", 120000)
employee_2 = Employee("Khan", "AG-78205", 110000)
employee_3 = Employee("Jameel", "LA-74828", 150000)

print("The Employees of the Company Are as Follow: ")
employee_1.display_employee()
employee_2.display_employee()
employee_3.display_employee()

#===================================== Inheritance Topic ======================================
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print("Eating...")

class Dog(Animal): 
    def __init__(self, name, age):
        super().__init__(name, age)
    def bark(self):
        print("Woooof Wof")

    def dog_info(self):
        print(f'The Dog Name is: {self.name} and its Age is: {self.age}.')

dog = Dog("jimy", 4)
dog.eat()
dog.bark()
dog.dog_info()