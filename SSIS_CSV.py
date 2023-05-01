import csv

def add_student():
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        name = input("Enter the student's name: ")
        age = input("Enter the student's age: ")
        grade = input("Enter the student's grade: ")
        writer.writerow([name, age, grade])
        print("Student added successfully")

def edit_student():
    students = []
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            students.append(row)
    name = input("Enter the name of the student you want to edit: ")
    for student in students:
        if student[0] == name:
            student[1] = input("Enter the new age: ")
            student[2] = input("Enter the new grade: ")
            with open('students.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(students)
            print("Student edited successfully")
            return
    print("Student not found")

def delete_student():
    students = []
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            students.append(row)
    name = input("Enter the name of the student you want to delete: ")
    for student in students:
        if student[0] == name:
            students.remove(student)
            with open('students.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(students)
            print("Student deleted successfully")
            return
    print("Student not found")

def display_students():
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0], row[1], row[2], sep='\t')

# Course-related functions
def add_course():
    with open('courses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        course_name = input("Enter the name of the course: ")
        course_code = input("Enter the course code: ")
        course_instructor = input("Enter the name of the instructor: ")
        writer.writerow([course_name, course_code, course_instructor])
        print("Course added successfully")

def edit_course():
    courses = []
    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            courses.append(row)
    course_name = input("Enter the name of the course you want to edit: ")
    for course in courses:
        if course[0] == course_name:
            course[1] = input("Enter the new course code: ")
            course[2] = input("Enter the new instructor name: ")
            with open('courses.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(courses)
            print("Course edited successfully")
            return
    print("Course not found")

def delete_course():
    courses = []
    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            courses.append(row)
    course_name = input("Enter the name of the course you want to delete: ")
    for course in courses:
        if course[0] == course_name:
            courses.remove(course)
            with open('courses.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(courses)
            print("Course deleted successfully")
            return
    print("Course not found")

def display_courses():
    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0], row[1], row[2], sep='\t')

while True:
    print("1. Add student")
    print("2. Edit student")
    print("3. Delete student")
    print("4. Display students")
    print("5. Add course")
    print("6. Edit course")
    print("7. Delete course")
    print("8. Display courses")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        edit_student()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        display_students()
    elif choice == '5':
        add_course()
    elif choice == '6':
        edit_course()
    elif choice == '7':
        delete_course()
    elif choice == '8':
        display_courses()
    elif choice == '9':
        break
    else:
        print("Invalid choice. Please try again.")





