"""
Add
Update
Display
Percentage
Delete
Exit
"""
from numpy.ma.extras import average

student = {}

def add_student(name,grade):
    student[name] = grade
    print(f"Added {name} with marks {grade}.")

def update_student(name,grade):
    if name in student:
        student[name] = grade
        print(f"{name} with marks are updated {grade}.")
    else:
        print(f"{name} is not found.")

def delete_student(name):
    if name in student:
        del student[name]
    else:
        print(f"{name} is not found.")

def view_students():
    if student:
        for name, grade in student.items():
            print(f"{name} got {grade} marks.")
    else:
        print("No students found.")

def calculate_percentage(name,total_marks):
    if name in student:
        percentage = round(student[name]/total_marks * 100 , 2)
        print(f"Percentage of {name} is {percentage}%.")
    else:
        print(f"{name} is not found.")

def main():
    while True:
        print("\n Student Grades Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display all Students")
        print("5. Percentage of Student")
        print("6. Exit")

        choice = int(input("Enter your choice:"))
        if choice == 1:
            name = input("Enter student name:")
            grade = input("Enter student grade:")
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name:")
            grade = input("Enter student grade:")
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name:")
            delete_student(name)

        elif choice == 4:
            view_students()

        elif choice == 5:
            name = input("Enter student name:")
            total_marks = int(input("Enter the total marks:"))
            calculate_percentage(name, total_marks)

        elif choice == 6:
            print("Closing the program...")
            break

        else:
            print("Invalid choice.")


main()