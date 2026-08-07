class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_details(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Course:", self.course)


students = []

n = int(input("Enter Number of Students: "))

for i in range(n):
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Student Course: ")

    student = Student(name, age, course)
    students.append(student)

print("\nStudent Details")
print("=" * 30)

for i, student in enumerate(students, start=1):
    print(f"Student {i}")
    print("-" * 30)
    student.show_details()
    print()


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Exit")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Update Course")
    print("7. Total Student")

    choice = int(input("Enter Choice: "))


    if choice == 1:
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        course = input("Enter Student Course: ")

        student = Student(name, age, course)

        students.append(student)

        print("Student Added Successfully!")

    elif choice == 2:

        if len(students) == 0:
            print("No Student data found.")    

        else:
            print("\nStudent Details")
            print("=" * 30)

            for student in students:
                student.show_details()
                print("-" * 30)    

    elif choice == 3:
        print("Thank You!")
        break


    elif choice == 4:
        search_student = input("Enter Student name: ")

        found = False

        for student in students:
            if student.name.lower() == search_student.lower():
                student.show_details()
                found = True

        if not found:
            print("Student not found")         

    elif choice == 5:
        del_student = input("Enter Student name to delete: ")

        found = False

        for student in students:
            if student.name.lower() == del_student.lower():
                students.remove(student)
                print("Student Deleted sucessfully")
                found = True
                break
        if not found:
            print("Student not found")  

    elif choice == 6:
        student_name = input("Enter Student name which course we want to change : ")

        found = False

        for student in students:
            if student.name.lower() == student_name.lower():
                student.course = input("Enter updated course: ")
                print("Course Updated Successfully")
                found = True
                break

        if not found:
            print("Student Not Found")

    elif choice == 7:
        print("Total Student is", len(students))        
                                  
    else:
        print("Invalid Choice! Please try again.")            

        