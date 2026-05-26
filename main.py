#print("PROGRAM STARTED")
def load_students():
    students = []
    try:
        file = open("students.txt", "r")
        for line in file:
            data = line.strip().split(",")
            student = {
                "name": data[0],
                "usn": data[1],
                "marks": int(data[2])
            }
            students.append(student)
        file.close()
    except:
        pass
    return students

def save_students(students):
    file = open("students.txt", "w")
    for student in students:
        file.write(student["name"] + "," +
                   student["usn"] + "," +
                   str(student["marks"]) + "\n")
    file.close()
    
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"


students = load_students()

while True:
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")
    #print("DEBUG choice =", choice)

    if choice == "1":
        name = input("Enter student name: ")
        usn = input("Enter USN: ")
        marks = int(input("Enter marks: "))

        student = {
            "name": name,
            "usn": usn,
            "marks": marks
        }

        students.append(student)

        print("Student added successfully!")
        save_students(students)
        #import os
        #print("Saving in:", os.getcwd())

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            for student in students:
                print("\nName:", student["name"])
                print("USN:", student["usn"])
                print("Marks:", student["marks"])
                print("Grade:", calculate_grade(student["marks"]))

    elif choice == "3":
        search = input("Enter name or USN: ")

        found = False

        for student in students:
            if student["name"] == search or student["usn"] == search:
                print("\nStudent Found:")
                print("Name:", student["name"])
                print("USN:", student["usn"])
                print("Marks:", student["marks"])
                print("Grade:", calculate_grade(student["marks"]))
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        delete_usn = input("Enter USN of student to delete: ")

        new_students = []
        found = False

        for student in students:
            if student["usn"] != delete_usn:
                new_students.append(student)
            else:
                found = True

        if found:
            students = new_students
            save_students(students)
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")