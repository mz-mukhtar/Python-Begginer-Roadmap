"""
StudentManager Service Controller (Reference Solution)
"""

import json
import csv
from pathlib import Path
from models.student import Student

class StudentManager:
    def __init__(self, json_path="data/students.json", csv_path="data/students.csv"):
        self.json_path = Path(json_path)
        self.csv_path = Path(csv_path)
        self.json_path.parent.mkdir(exist_ok=True)
        self.students = self.load()

    def load(self):
        if not self.json_path.exists():
            return []
        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                return [Student.from_dict(d) for d in json.load(f)]
        except Exception:
            return []

    def save(self):
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def add_student(self, sid, name, age, dept, email, courses):
        if any(s.student_id.lower() == sid.lower() for s in self.students):
            return False, "Student ID already exists."
        self.students.append(Student(sid, name, age, dept, email, courses))
        self.save()
        return True, "Student added successfully."

    def search_student(self, query):
        results = []
        for s in self.students:
            if query.lower() in s.student_id.lower() or query.lower() in s.name.lower():
                results.append(s)
        return results

    def update_student(self, sid, new_dept, new_email):
        for s in self.students:
            if s.student_id.lower() == sid.lower():
                s.department = new_dept
                s.email = new_email
                self.save()
                return True
        return False

    def delete_student(self, sid):
        for i, s in enumerate(self.students):
            if s.student_id.lower() == sid.lower():
                del self.students[i]
                self.save()
                return True
        return False

    def export_csv(self):
        with open(self.csv_path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["Student ID", "Name", "Age", "Department", "Email", "Courses"])
            for s in self.students:
                w.writerow([s.student_id, s.name, s.age, s.department, s.email, "; ".join(s.courses)])
        return self.csv_path
