# function without parameter
def my_name():
    print("hello")     # here hello called argument 

my_name()    

# function with parameter 
def greet(name):
    print("hello", name)

greet("jinx")  

# function with two parameter 
def add(a, b):
    print(a + b)

add(22, 11)    

# return , return value ko vapas bhejta he taki phir use kar sake 
def cube(num):
    return num * num * num 

cube_sq = cube(22)
print(cube_sq)
#__________________________________________________________________________________________________________-

# list 


a = [22,11,20,7,33,55,22,]
print(a)

fruits = ["apple", "banana", "mango", "orange"]
print(fruits[0])
print(fruits[2])
print(len(fruits))

student = ['daksh', 'jinx', 'johan', 'jan', ]
student[1] = 'max'
print(student)

#append function add item at last

fruits2 = ["apple", "banana"]
fruits2.append("mango")

print(fruits2)

#insert function add item at secific index

colurs = ["red", "green"]
colurs.insert(1, "blue")

print(colurs)

# remove function remove specific value 

num = [22,11,2007]
num.remove(11)

print(num)

# pop function if pop() like this empty it remove last value in index if it remove value given index pop(2) remove 2 index value

city = ["ahemdabad", "rajkot", "mehasana"]
city.pop()
print(city)

city = ["ahemdabad", "rajkot", "mehasana"]
city.pop(1)
print(city)



# small chalenge by gpt

stu = ["daksh", "aman"] 
stu.append("rahul")
stu.remove("aman")
print(stu)

# strings

# strings functions
'''
slicing
upper()
lower()
capitalize()
replace()
split()
'''

line = "python is very easy"

print(line.split())
