#========================================= Polymorphism =================================
class Vehicle:
    def start():
        print("Vehicle is starting....")

class Car(Vehicle):
    def start(self):
        print("Car Starts With a Key....")

class Bike(Vehicle):
    def start(self):
        print("Bike Starts with a self-start Button...")
class Airplane(Vehicle):
    def start(self):
        print("Plane Starts it's Engine...")

car = Car()
bike = Bike()
airplane = Airplane()

vehicles = [car, bike, airplane]

for i in vehicles:
    i.start()

#----------------------------------------- Question No. 2 ------------------------------------------
class Payment:
    def pay(self, amount):
        print("Processing Payment ....")

class CreditCard(Payment): 
    def pay(self, amount):
        print(f'Payed ${amount}  using Credit Card.')

class PayPal(Payment):
    def pay(self, amount):
        print(f"Payed ${amount} Using PayPal.")

class Bitcoin(Payment):
    def pay(self, amount):
        print(f"Payed ${amount} Using Bitcoing.")

credit = CreditCard()
papal = PayPal()
bitcoin = Bitcoin()

payment = [credit, papal, bitcoin]
for i in payment:
    i.pay(500)