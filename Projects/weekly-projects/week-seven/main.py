"""
Entrypoint for Professionally Organized Student Management System
Week Seven — Python Beginner Roadmap
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
        print(" ORGANIZED STUDENT MANAGEMENT (WEEK 7)  ")
        print("========================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        print("========================================")

        choice = input("Enter choice (1-3): ").strip()

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
            print("Goodbye!")
            break

        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()
