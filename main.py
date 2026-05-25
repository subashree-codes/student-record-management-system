students = []

while True:
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        usn = input("Enter USN: ")
        marks = input("Enter marks: ")

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
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")