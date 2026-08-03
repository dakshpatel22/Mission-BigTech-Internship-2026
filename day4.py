# Tuple

# Tuple - () - change not possible
# list - []- change not possible

name = ("jinx", "narayan", "harry", "johan", "tiger")
print(type(name))
print(name[3])
print(len(name))

# set

colurs = {'red', 'blue', 'red', 'green'}
print(colurs)  # output {'red','blue','green'}
colurs.add('yellow')
colurs.remove('blue')
print(colurs)

# dictionary 

car = { 'brand' : 'toyota' ,
       'colur' : 'purple'}

print(car["brand"])

car["year"] = 2025
print(car)

car['colur'] = 'black'
print(car)

del car['year']
print(car)

#____________________________________________________________________________________

# mini project 

student = {'name' : input("Enter name :"),
           "age" : int(input("Enter your age:")),
           "collage" : input("Enter your collage:")}

print("\n---------- Student Details ----------")
print("Name:", student["name"])
print("Age:", student["age"])
print("collage:", student["collage"])

