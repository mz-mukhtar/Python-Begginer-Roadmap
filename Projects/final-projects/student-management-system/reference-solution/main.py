"""
Reference Entrypoint for Student Management System Capstone
"""

from services.student_manager import StudentManager

def main():
    manager = StudentManager()

    while True:
        print("")
        print("========================================")
        print(" STUDENT MANAGEMENT SYSTEM (CAPSTONE)   ")
        print("========================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Export to CSV")
        print("7. Exit")
        print("========================================")

        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            sid = input("Enter ID (e.g., STU-002): ").strip()
            name = input("Enter Name: ").strip()
            age_str = input("Enter Age: ").strip()
            age = int(age_str) if age_str.isdigit() else 18
            dept = input("Enter Department: ").strip()
            email = input("Enter Email: ").strip()
            courses_raw = input("Enter Courses (comma-separated): ").strip()
            courses = [c.strip() for c in courses_raw.split(",") if c.strip()]
            ok, msg = manager.add_student(sid, name, age, dept, email, courses)
            print(f"{'✅' if ok else '❌'} {msg}")

        elif choice == "2":
            for s in manager.students:
                print(s)

        elif choice == "3":
            query = input("Enter search query (ID or Name): ").strip()
            matches = manager.search_student(query)
            for m in matches:
                print(f"🎯 {m}")

        elif choice == "4":
            sid = input("Enter ID to update: ").strip()
            new_dept = input("Enter New Department: ").strip()
            new_email = input("Enter New Email: ").strip()
            print("✅ Updated." if manager.update_student(sid, new_dept, new_email) else "❌ ID not found.")

        elif choice == "5":
            sid = input("Enter ID to delete: ").strip()
            print("✅ Deleted." if manager.delete_student(sid) else "❌ ID not found.")

        elif choice == "6":
            path = manager.export_csv()
            print(f"✅ Exported CSV to {path}")

        elif choice == "7":
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
