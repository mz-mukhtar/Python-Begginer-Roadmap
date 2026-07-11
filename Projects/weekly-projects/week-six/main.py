"""
Project: Object-Oriented Student Management System
Week Six — Python Beginner Roadmap
Author: Mahi Zeki (EthioNext / Cyber Vanguard)

Description:
Demonstrates Object-Oriented Programming (OOP) with User -> Student inheritance
and a coordinating StudentManager class.
"""

import json
from pathlib import Path


class User:
    """Parent base class representing any user entity."""
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email


class Student(User):
    """Child class inheriting from User and adding student-specific major."""
    def __init__(self, user_id, name, email, major):
        super().__init__(user_id, name, email)
        self.major = major

    def to_dict(self):
        """Serializes Student object to dictionary."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "major": self.major
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Student object from dictionary data."""
        return cls(data["user_id"], data["name"], data["email"], data["major"])

    def __str__(self):
        return f"[{self.user_id}] {self.name} ({self.email}) | Major: {self.major}"


class StudentManager:
    """Manager class coordinating student objects and JSON persistence."""
    def __init__(self, storage_file="data/students.json"):
        self.file_path = Path(storage_file)
        self.file_path.parent.mkdir(exist_ok=True)
        self.students = self.load()

    def load(self):
        if not self.file_path.exists():
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Student.from_dict(d) for d in data]
        except Exception:
            return []

    def save(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)
        print("✅ Saved objects to disk.")

    def add_student(self, student):
        if any(s.user_id == student.user_id for s in self.students):
            print("❌ Student ID already exists.")
            return False
        self.students.append(student)
        self.save()
        print(f"✅ Added {student.name}")
        return True

    def view_all(self):
        print("")
        print("--- REGISTERED OOP STUDENTS ---")
        if not self.students:
            print("No students registered.")
            return
        for s in self.students:
            print(s)


def main():
    manager = StudentManager()

    while True:
        print("")
        print("========================================")
        print("  OBJECT-ORIENTED STUDENT SYSTEM (WK 6) ")
        print("========================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Save Students")
        print("4. Exit")
        print("========================================")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            uid = input("Enter ID: ").strip()
            name = input("Enter Name: ").strip()
            email = input("Enter Email: ").strip()
            major = input("Enter Major: ").strip()
            manager.add_student(Student(uid, name, email, major))

        elif choice == "2":
            manager.view_all()

        elif choice == "3":
            manager.save()

        elif choice == "4":
            manager.save()
            print("Goodbye!")
            break

        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()
