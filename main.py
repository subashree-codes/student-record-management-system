students = []

while True:
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

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

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            for student in students:
                print("\nName:", student["name"])
                print("USN:", student["usn"])
                print("Marks:", student["marks"])

    elif choice == "3":
        search = input("Enter name or USN: ")

        found = False

        for student in students:
            if student["name"] == search or student["usn"] == search:
                print("\nStudent Found:")
                print("Name:", student["name"])
                print("USN:", student["usn"])
                print("Marks:", student["marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        delete_usn = input("Enter USN of student to delete: ")

        found = False

        for student in students:
            if student["usn"] == delete_usn:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")