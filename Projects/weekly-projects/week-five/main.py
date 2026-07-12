"""
Project: Reliable Student Management System
Week Five — Python Beginner Roadmap
Author: Mahi Zeki (EthioNext / Harar Dev Center / Cyber Vanguard)
"""

from student_tools import safe_load_json, safe_save_json, safe_export_csv
from logger_config import log_info


def prompt_safe_int(message):
    """Prompts for an integer safely without crashing on invalid text input."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("❌ Invalid input! Please enter a numeric integer.")


def main():
    log_info("Application started.")
    roster = safe_load_json()

    while True:
        print("")
        print("========================================")
        print("  RELIABLE STUDENT MANAGEMENT (WEEK 5)  ")
        print("========================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save Students")
        print("7. Export Students")
        print("8. Exit")
        print("========================================")

        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            sid = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            age = prompt_safe_int("Enter Age: ")
            dept = input("Enter Department: ").strip()
            roster.append({"student_id": sid, "name": name, "age": age, "department": dept})
            safe_save_json(roster)
            log_info(f"Added student {name} ({sid})")

        elif choice == "2":
            print(f"{'ID':<10} | {'NAME':<18} | {'AGE':<5} | {'DEPARTMENT':<18}")
            print("-" * 55)
            for s in roster:
                print(f"{s['student_id']:<10} | {s['name']:<18} | {s['age']:<5} | {s['department']:<18}")

        elif choice == "3":
            sid = input("Enter Student ID to search: ").strip()
            for s in roster:
                if s["student_id"].lower() == sid.lower():
                    print(f"🎯 FOUND: {s['name']} ({s['age']}) - {s['department']}")
                    break
            else:
                print("❌ Student not found.")

        elif choice == "4":
            sid = input("Enter Student ID to update: ").strip()
            for s in roster:
                if s["student_id"].lower() == sid.lower():
                    s["department"] = input("Enter new department: ").strip()
                    s["age"] = prompt_safe_int("Enter new age: ")
                    safe_save_json(roster)
                    log_info(f"Updated student {sid}")
                    break
            else:
                print("❌ Student not found.")

        elif choice == "5":
            sid = input("Enter Student ID to delete: ").strip()
            roster = [s for s in roster if s["student_id"].lower() != sid.lower()]
            safe_save_json(roster)
            log_info(f"Deleted student {sid}")

        elif choice == "6":
            safe_save_json(roster)

        elif choice == "7":
            safe_export_csv(roster)

        elif choice == "8":
            safe_save_json(roster)
            log_info("Application exited properly.")
            print("Goodbye!")
            break

        else:
            print("❌ Invalid selection.")


if __name__ == "__main__":
    main()
