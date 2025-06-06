students = {}


def add_student():
    name = input("Enter student name: ")
    if name in students:
        print("Student already exists.")
    else:
        marks = input("Enter marks: ")
        if marks.isdigit():
            students[name] = int(marks)
            print(name + " added with marks " + str(marks) + ".")

        else:
            print("Invalid marks. Only numbers allowed.")


def view_students():
    if not students:
        print("No student records found.")
    else:
        print("\n--- Student List ---")
        for name in students:
            print(name, ":", students[name])


def search_student():
    name = input("Enter student name to search: ")
    if name in students:
        print(name + " added with marks " + str(marks) + ".")

    else:
        print("Student not found.")


def update_marks():
    name = input("Enter student name to update marks: ")
    if name in students:
        new_marks = input("Enter new marks: ")
        if new_marks.isdigit():
            students[name] = int(new_marks)
            print("Marks updated successfully.")
        else:
            print("Invalid input. Only numbers allowed.")
    else:
        print("Student not found.")


def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print(f"{name} has been removed.")
    else:
        print("Student not found.")


def find_topper():
    if not students:
        print("No student records available.")
    else:
        topper = ""
        highest = -1
        for name in students:
            if students[name] > highest:
                highest = students[name]
                topper = name
        print(f"Topper: {topper} with {highest} marks.")


def find_average():
    if not students:
        print("No student records available.")
    else:
        total = 0
        count = 0
        for marks in students.values():
            total += marks
            count += 1
        average = total / count
        print(f"Average Marks: {average}")


def passed_students():
    print("Students who passed (marks >= 15):")
    found = False
    for name in students:
        if students[name] >= 15:
            print(name, ":", students[name])
            found = True
    if not found:
        print("No passed students.")


def failed_students():
    print("Students who failed (marks < 15):")
    found = False
    for name in students:
        if students[name] < 15:
            print(name, ":", students[name])
            found = True
    if not found:
        print("No failed students.")


def main():
    while True:
        print("\n=== Student Marks Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Find Topper")
        print("7. Find Average Marks")
        print("8. List Passed Students")
        print("9. List Failed Students")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_marks()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            find_topper()
        elif choice == '7':
            find_average()
        elif choice == '8':
            passed_students()
        elif choice == '9':
            failed_students()
        elif choice == '10':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()
