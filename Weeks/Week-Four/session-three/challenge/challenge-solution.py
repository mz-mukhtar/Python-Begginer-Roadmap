"""
Challenge Solution: Persistent Student Management System
Week Four — Session Three
"""

import json
from pathlib import Path

FILE = "students.json"

def load_data():
    if Path(FILE).exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

students = load_data()
students.append({"id": len(students)+1, "name": "New Student", "major": "IT"})
save_data(students)
print("✅ Persistent Student System Updated!")
