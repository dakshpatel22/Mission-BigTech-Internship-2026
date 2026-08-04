# File Handaling

file = open("myname.txt", "w")
file.write("Daksh Patel")
file.close()

file = open("myname.txt", "r")
print(file.read())
file.close() 

with open("myname.txt", "r") as file:
    print(file.read())

with open("myname.txt", "a") as file:
    file.write("\nToday I learned file handaling.")

with open("skills.txt", "w") as file:
    file.write("\npython")
    file.write("\nGithub")
    file.write("\nLinkdin")

with open("skills.txt", 'r') as file:
    print(file.read())

with open("skills.txt", "a") as file:
    file.write("\nMachine Learning")    

with open("skills.txt", 'r') as file:
    print(file.read())

# Exception Handling 


try :
    n = int(input())
    print(22/n)
except: ZeroDivisionError
print("cannot divide by zero")

try :
    age = int(input())
    print(age)
except :
    print("enter valid age")   


#__________________________________________________________________________________________


# CSV files = Coma sparated Value

import csv

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "salary", "city"])
    writer.writerow(["Daksh", "50000", "Ahemdabad"])
    writer.writerow(["jinx", "45000", "surat"])
    writer.writerow(["munfah", "60000", "mumbai"])

import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)




    