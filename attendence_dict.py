attendance = {}

# Function to add student attendance
def add_attendance(name, status):
    attendance[name] = status
    print(f"Attendance marked for {name}: {status}")

# Function to update attendance
def update_attendance(name, status):
    if name in attendance:
        attendance[name] = status
        print(f"Attendance updated for {name}: {status}")
    else:
        print("Student not found!")

# Function to display all attendance
def show_attendance():
    if not attendance:
        print("No attendance records found.")
        return

    print("\n--- Attendance List ---")
    for name, status in attendance.items():
        print(f"{name} : {status}")
# Function to count present & absent
def count_attendance():
    present = 0
    absent = 0

    for status in attendance.values():
        if status.lower() == "present":
            present += 1
        else:
            absent += 1

    print("\nTotal Present:", present)
    print("Total Absent:", absent)

# Main Program
while True:
    print("\n1. Add Attendance")
    print("2. Update Attendance")
    print("3. Show Attendance")
    print("4. Count Present & Absent")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        status = input("Enter status (Present/Absent): ")
        add_attendance(name, status)

    elif choice == "2":
        name = input("Enter student name: ")
        status = input("Enter new status (Present/Absent): ")
        update_attendance(name, status)

    elif choice == "3":
        show_attendance()

    elif choice == "4":
        count_attendance()

    elif choice == "5":
        print("Program exited.")
        break

    else:
        print("Invalid choice! Try again.")
