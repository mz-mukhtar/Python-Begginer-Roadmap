"""
Challenge Solution: Robust Student JSON Repository
Week Eight — Session One
"""

import json
from pathlib import Path

class StudentStorage:
    def __init__(self, filename="students_repo.json"):
        self.filename = Path(filename)

    def load(self):
        if not self.filename.exists():
            return []
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("File corrupted. Returning empty roster.")
            return []

    def save(self, records):
        with open(self.filename, "w") as f:
            json.dump(records, f, indent=4)

storage = StudentStorage("test_repo.json")
storage.save([{"id": 1, "name": "Abel"}])
print("Loaded repository records:", len(storage.load()))
