print("Daksh Patel")
print("IIT Madras")
print("Microsoft")

name = "Daksh"
age = 18
dob = 22.11
goal = "big tech internship"
fav_colur = "purple"

print(name)
print(age)
print(dob)
print(goal)
print(fav_colur)


name = input("Type your name here:")
age = int(input("how old are you ?"))
language = input("your favourite language ?")

print("how are you", name, '!')
print("nice to know you are", age, 'year old !')
print('oh very good, you like', language)



# Mini project 

name = input("Enter name :")
age = input("Enter age :")
college = input("Enter college :")


print("welcome", name)
print("Age :", age)
print(college)
print("Best wishes for your Data Science journey!")

# _________________________________________________________


d = "dax"
a = 22
k = 22.11
s = True

print(type(d))
print(type(a))
print(type(k))
print(type(s))

a = "25"
b = 100
c = 10.8

print(int(a))
print(str(b))
print(int(c))

a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a / b)
print(a // b)
print(a % b)
print(a * b)
print(a ** b)

a = int(input("Enter First number :"))
b = int(input("Enter second number : "))

print( 'Adition', a + b)
print('Substraction', a - b)
print("mulatiplication", a * b)
print("divison" , a / b)

num = int(input("Enter number :"))
if num % 2 == 0 :
    print("This is even number")
else:
    print("This is odd number")

marks = int(input("Enter your marks:"))
if marks >= 35 :
    print("Pass")
else:
    print("Fall")

a = int(input("Enter First number :"))  
b = int(input("Enter second number :"))
c = int(input("Enter Third number :"))

if a > b and a > c:
    print(a,'is gretest number')
elif a < b and c < b :
    print(b, "is gretest number")
else :
    print(c, "is gretest number ")


# Mini Project 

name = input("Enter Name:")
Marks = int(input("Enter Marks:"))

print("Hello", name)
print("your marks is ", Marks)

if Marks >= 35:
    print("you are pass")
else :
    print("you are fall") 

if Marks >= 90:
    print('grade A')
elif Marks >= 75:
    print("grade B")
elif Marks >= 60:
    print('grade C')
elif Marks >= 45:
    print('grade D')                     
              