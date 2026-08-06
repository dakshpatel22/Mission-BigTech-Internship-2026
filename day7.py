# bank a/c example

class bankaccount:

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print("Acount Houlder:", self.name)
        print("Balance:", self.balance)

    def deposit(self,amount):
        self.balance += amount
        print("New Balance:", self.balance)

    def withdraw(self,amount):
        self.balance -= amount
        print("New Balance:", self.balance)


a1 = bankaccount("Daksh", 50000)                 

a1.show_balance()

a1.deposit(20000)

a1.withdraw(10000)

# car example

class Car:

    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    def details(self):
        print("Car Name:", self.brand)
        print("Car Color:", self.color)
        print("Car Price:", self.price)

    def change_color(self, new_color):
        self.color = new_color
        print("New Color:", self.color)


a1 = Car("Innova", "Blue", 5000000)

a1.details()

a1.change_color("Purple")

a1.details()


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        print("Employee Name :", self.name)
        print("Salary :", self.salary)

    def imcrease_salary(self,amount):
        self.salary += amount
        print("New Salary :", self.salary)

e1 = Employee("Daksh", 20000000)

e1.details()
e1.imcrease_salary(30000000)

# if + oop example                
        
class bankaccount:

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print("Acount Houlder:", self.name)
        print("Balance:", self.balance)

    def deposit(self,amount):
        self.balance += amount
        print("New Balance:", self.balance)

    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("New Balance:", self.balance)


a1 = bankaccount("Daksh", 50000)                 

a1.show_balance()

a1.deposit(20000)

a1.withdraw(10000)


# one more example of rectangle

class Rectangle:

    def __init__(self, length, width):

        self.length = length
        self.width = width 

    def area(self):
        print(self.length * self.width)

    def perimeter(self):
        print(2 * (self.length + self.width))        

r1 = Rectangle(10, 5)

r1.area()
r1.perimeter()        

 # example of circle

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area", 3.14 * self.radius * self.radius)

    def circumference(self):
        print("Circumference", 2 * 3.14 * self.radius)        

r1 = Circle(4)

r1.area()
r1.circumference()
        

