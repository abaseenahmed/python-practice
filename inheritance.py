#========================================= Inheritance in Python =================================
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child(Parent):
    def __init__(self, name, age, city):
        super().__init__(name, age)
        self.city = city 

    def display(self):
        print(f"The Child name is {self.name}.")
        print(f"The Child Age is {self.age}.")
        print(f"The Child City is {self.city}.")

child_01 = Child("Kim", 21, "London")
child_01.display()

#--------------------------------------- Practice Question ---------------------------------------#
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Animal Name: {self.name}")
        print(f"Animal Age: {self.age}")

    def eat(self):
        print(f"{self.name} is eating...")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is Barking...")

pet_01 = Dog("Tommy", 1, "German Sheperd")
pet_01.display_info()
pet_01.bark()
pet_01.eat()

#------------------------------------ Practice Question No. 2 ---------------------------------#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Person Name: {self.name}")
        print(f"Person Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.employee_id = emp_id

class Manager(Employee):
    def __init__(self, name, age, emp_id, department, salary):
        super().__init__(name, age, emp_id)
        self.department = department
        self.salary = salary

    def display_manager(self):
        self.display_person()
        print(f"Manager ID: {self.employee_id}")
        print(f"Manager Department: {self.department}")
        print(f"Manager Salary: {self.salary}")

manager_01 = Manager("Ahmed", 22, "ALG-87677", "Information Security", 12000)
manager_01.display_manager()