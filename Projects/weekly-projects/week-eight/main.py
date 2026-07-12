"""
Capstone Entrypoint — Tested Student Management System
Week Eight — Python Beginner Roadmap
Author: Mahi Zeki (EthioNext / Harar Dev Center / Cyber Vanguard)
"""

from utilities.file_manager import StorageRepository
from services.student_manager import StudentManager


def main():
    repo = StorageRepository("data/students.json")
    manager = StudentManager(repo)

    while True:
        print("")
        print("========================================")
        print("   TESTED STUDENT CAPSTONE (WEEK 8)     ")
        print("========================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        print("========================================")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            sid = input("Enter Student ID: ").strip()
            name = input("Enter Name: ").strip()
            major = input("Enter Major: ").strip()
            success, msg = manager.add_student(sid, name, major)
            print(f"{'✅' if success else '❌'} {msg}")

        elif choice == "2":
            for s in manager.get_all():
                print(s)

        elif choice == "3":
            sid = input("Enter ID to search: ").strip()
            found = manager.find_by_id(sid)
            print(f"🎯 MATCH: {found}" if found else "❌ Not found.")

        elif choice == "4":
            sid = input("Enter ID to delete: ").strip()
            print("✅ Deleted." if manager.delete_student(sid) else "❌ Not found.")

        elif choice == "5":
            print("Exiting Capstone. Goodbye!")
            break

        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()
