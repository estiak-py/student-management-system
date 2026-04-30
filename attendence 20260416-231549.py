# Simple Attendance System

students = []

def add_student(name):
    students.append({"name": name, "attendance": []})
    print(f"{name} added successfully!")

def mark_attendance():
    print("\nMark Attendance (P = Present, A = Absent)\n")
    for student in students:
        status = input(f"{student['name']}: ").upper()
        student["attendance"].append(status)

def show_report():
    print("\n--- Attendance Report ---")
    for student in students:
        total_days = len(student["attendance"])
        present_days = student["attendance"].count("P")

        print(f"{student['name']} -> Present: {present_days}/{total_days}")

def menu():
    while True:
        print("\n===== ATTENDANCE SYSTEM =====")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. Show Report")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            add_student(name)

        elif choice == "2":
            if not students:
                print("No students found!")
            else:
                mark_attendance()

        elif choice == "3":
            show_report()

        elif choice == "4":
            print("Exiting system...")
            break

        else:
            print("Invalid choice!")

menu()