class Mobile:
    pass

m1 = Mobile()
m2 = Mobile()
m1.brand = "Samsung"
m1.price = 25000 

m2.brand = "vivo"
m2.price = 40000



print(m1.brand)
print(m1.price)
print(m2.brand)
print(m2.price)


# __init__()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Daksh", 18)

print(s1.name)
print(s1.age)

class person:

    def introduce(self):
        print("I am the person")

class student(person):
    pass

s = student()
s.introduce()

class vehicle:
    def start(self):
        print("started")

class Bike(vehicle):
    pass

b = Bike()
b.start()



class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def detail(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

s1 = Book("Deep work", "Cal Newport", 500)
s1.detail()