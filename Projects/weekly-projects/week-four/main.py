"""
Project: Persistent Student Management System
Week Four — Python Beginner Roadmap
Author: Mahi Zeki (EthioNext / Cyber Vanguard)

Description:
Adds JSON and CSV persistence using pathlib.
Note: Heavy exception handling is reserved for Week Five.
"""

import json
import csv
from pathlib import Path

DATA_DIR = Path("data")
JSON_FILE = DATA_DIR / "students.json"
CSV_FILE = DATA_DIR / "students.csv"


def ensure_data_folder():
    """Ensures the data directory exists."""
    DATA_DIR.mkdir(exist_ok=True)


def load_students():
    """Loads student list from JSON file if it exists."""
    ensure_data_folder()
    if JSON_FILE.exists():
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                return json.loads(content)
    return []


def save_students(roster):
    """Saves student list to JSON disk file."""
    ensure_data_folder()
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(roster, f, indent=4)
    print(f"✅ Saved {len(roster)} records to {JSON_FILE}")


def export_to_csv(roster):
    """Exports student list to CSV file."""
    ensure_data_folder()
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Student ID", "Name", "Age", "Department"])
        for s in roster:
            writer.writerow([s["student_id"], s["name"], s["age"], s["department"]])
    print(f"✅ Successfully exported {len(roster)} records to {CSV_FILE}")


def display_menu():
    print("")
    print("========================================")
    print(" PERSISTENT STUDENT MANAGEMENT (WEEK 4) ")
    print("========================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Students")
    print("7. Export to CSV")
    print("8. Exit")
    print("========================================")


def main():
    roster = load_students()
    print(f"Loaded {len(roster)} student records from disk.")

    while True:
        display_menu()
        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            sid = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            age_str = input("Enter Age: ").strip()
            age = int(age_str) if age_str.isdigit() else 18
            dept = input("Enter Department: ").strip()
            roster.append({"student_id": sid, "name": name, "age": age, "department": dept})
            save_students(roster)

        elif choice == "2":
            print("")
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
                    save_students(roster)
                    break
            else:
                print("❌ Student not found.")

        elif choice == "5":
            sid = input("Enter Student ID to delete: ").strip()
            roster = [s for s in roster if s["student_id"].lower() != sid.lower()]
            save_students(roster)
            print("✅ Student deleted if existed.")

        elif choice == "6":
            save_students(roster)

        elif choice == "7":
            export_to_csv(roster)

        elif choice == "8":
            save_students(roster)
            print("Exiting Persistent Student Management System. Goodbye!")
            break

        else:
            print("❌ Invalid selection.")


if __name__ == "__main__":
    main()
