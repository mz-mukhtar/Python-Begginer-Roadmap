"""
Project: Function-Based Student Management System
Week Three — Python Beginner Roadmap
Author: Mahi Zeki (EthioNext / Harar Dev Center / Cyber Vanguard)

Description:
A modular Student Management System structured with single-responsibility functions,
docstrings, and clean parameter passing.
"""

def display_menu():
    """Displays the interactive main menu options."""
    print("")
    print("========================================")
    print("   STUDENT MANAGEMENT SYSTEM (WEEK 3)   ")
    print("========================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("========================================")


def create_student(student_id, name, age, department):
    """Creates and returns a student record dictionary."""
    return {
        "student_id": student_id,
        "name": name,
        "age": age,
        "department": department
    }


def add_student(roster, student_id, name, age, department):
    """Checks for duplicate IDs and adds a new student to the roster list."""
    for s in roster:
        if s["student_id"] == student_id:
            print("❌ Error: Student ID already exists!")
            return False
    record = create_student(student_id, name, age, department)
    roster.append(record)
    print(f"✅ Student {name} added successfully.")
    return True


def view_students(roster):
    """Displays a formatted table of all registered students."""
    print("")
    print("--- REGISTERED STUDENTS ROSTER ---")
    if not roster:
        print("No students registered.")
        return
    print(f"{'ID':<10} | {'NAME':<18} | {'AGE':<5} | {'DEPARTMENT':<18}")
    print("-" * 55)
    for s in roster:
        print(f"{s['student_id']:<10} | {s['name']:<18} | {s['age']:<5} | {s['department']:<18}")


def search_student(roster, query_id):
    """Searches for a student by ID and returns the dictionary record if found."""
    for s in roster:
        if s["student_id"].lower() == query_id.lower():
            return s
    return None


def update_student(roster, student_id, new_department, new_age):
    """Updates an existing student's department and age."""
    student = search_student(roster, student_id)
    if student:
        student["department"] = new_department
        student["age"] = new_age
        print(f"✅ Student {student_id} updated successfully.")
        return True
    print("❌ Student ID not found.")
    return False


def delete_student(roster, student_id):
    """Removes a student from the roster by ID."""
    for i, s in enumerate(roster):
        if s["student_id"].lower() == student_id.lower():
            removed = roster.pop(i)
            print(f"✅ Removed student: {removed['name']}")
            return True
    print("❌ Student ID not found.")
    return False


def main():
    """Main application loop coordinating menu selections."""
    roster = []
    # Add initial demo record
    add_student(roster, "STU-001", "Sara Ahmed", 20, "Computer Science")

    while True:
        display_menu()
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            sid = input("Enter Student ID (e.g., STU-002): ").strip()
            name = input("Enter Student Name: ").strip()
            age_str = input("Enter Age: ").strip()
            age = int(age_str) if age_str.isdigit() else 18
            dept = input("Enter Department: ").strip()
            add_student(roster, sid, name, age, dept)

        elif choice == "2":
            view_students(roster)

        elif choice == "3":
            sid = input("Enter Student ID to search: ").strip()
            found = search_student(roster, sid)
            if found:
                print(f"🎯 FOUND: [{found['student_id']}] {found['name']} ({found['age']}) - {found['department']}")
            else:
                print("❌ No student found with that ID.")

        elif choice == "4":
            sid = input("Enter Student ID to update: ").strip()
            new_dept = input("Enter new department: ").strip()
            new_age_str = input("Enter new age: ").strip()
            new_age = int(new_age_str) if new_age_str.isdigit() else 20
            update_student(roster, sid, new_dept, new_age)

        elif choice == "5":
            sid = input("Enter Student ID to delete: ").strip()
            delete_student(roster, sid)

        elif choice == "6":
            print("Exiting Function-Based Student Management System. Goodbye!")
            break

        else:
            print("❌ Invalid selection. Choose 1 to 6.")


if __name__ == "__main__":
    main()
