"""
Challenge Solution: Final Student Management System Capstone Application
Week Eight — Session Three
"""

import json
from pathlib import Path

# 1. MODEL
class Student:
    def __init__(self, sid, name, major):
        self.sid = int(sid)
        self.name = str(name).strip().title()
        self.major = str(major).strip()

    def to_dict(self):
        return {"sid": self.sid, "name": self.name, "major": self.major}

    @classmethod
    def from_dict(cls, data):
        return cls(data["sid"], data["name"], data["major"])

# 2. STORAGE
class StudentStorage:
    def __init__(self, file="capstone_students.json"):
        self.file = Path(file)

    def load(self):
        if not self.file.exists(): return []
        try:
            with open(self.file, "r") as f: return json.load(f)
        except json.JSONDecodeError: return []

    def save(self, records):
        with open(self.file, "w") as f: json.dump(records, f, indent=4)

# 3. MANAGER / CONTROLLER
class StudentManager:
    def __init__(self, storage):
        self.storage = storage
        self.students = [Student.from_dict(d) for d in storage.load()]

    def add_student(self, sid, name, major):
        if any(s.sid == sid for s in self.students):
            return False, "Student ID already exists"
        self.students.append(Student(sid, name, major))
        self.storage.save([s.to_dict() for s in self.students])
        return True, "Student registered successfully"

    def get_all(self):
        return self.students

# 4. CAPSTONE RUN
storage = StudentStorage("capstone_test.json")
mgr = StudentManager(storage)
success, msg = mgr.add_student(201, "Abel Tadesse", "Computer Science")
print("Capstone Execution Status:", msg)
print("Registered Count:", len(mgr.get_all()))
