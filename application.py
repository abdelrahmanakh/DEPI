from student import Student
from course import Course
from teacher import Teacher

def add_students(students):
    while True:
        print("1)Add a student\n2)Return\n")
        choice = input()
        if choice == "1":
            name = input("Enter student name:")
            id = input("Enter student id:")
            age = input("Enter student age:")
            level = input("Enter student level:")
            major = input("Enter student major:")
            students.append(Student(name=name, id=id, age=age, level=level, major=major))
        elif choice == "2":
            return
        else:
            print("Please Enter A Valid Choice!")

def add_teachers(teachers):
    while True:
        print("1)Add a teacher\n2)Return\n")
        choice = input()
        if choice == "1":
            name = input("Enter teacher name:")
            id = input("Enter teacher id:")
            age = input("Enter teacher age:")
            salary = input("Enter teacher salary:")
            department = input("Enter teacher department:")
            teachers.append(Teacher(name=name, id=id, age=age, salary=salary, department=department))
        elif choice == "2":
            return
        else:
            print("Please Enter A Valid Choice!")

def add_courses(courses):
    while True:
        print("1)Add a course\n2)Return\n")
        choice = input()
        if choice == "1":
            name = input("Enter course name:")
            id = input("Enter course id:")
            credit_hours = input("Enter course age:")
            courses.append(Course(name=name, id=id, credit_hours=credit_hours))
        elif choice == "2":
            return
        else:
            print("Please Enter A Valid Choice!")

students  = []
courses = []
teachers = []

while True:
    print("Welcome to the College System!\nAt the beginning you have to do the following:\n1)Add Students\n2)Add courses\n3)Add teachers\n4)Done")
    choice_1 = input()
    if choice_1 == "1":
        add_students(students)
    elif choice_1 == "2":
        add_courses(courses)
    elif choice_1 == "3":
        add_teachers(teachers)
    elif choice_1 == "4":
        break
    else:
        print("Please Enter A valid choice!")

while True:
    print("Now the next step:\n1)")
    