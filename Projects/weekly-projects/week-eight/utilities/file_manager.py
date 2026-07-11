"""
File Storage Repository Utility (Week Eight Capstone)
"""

import json
from pathlib import Path

class StorageRepository:
    def __init__(self, filename="data/students.json"):
        self.file_path = Path(filename)
        self.file_path.parent.mkdir(exist_ok=True)

    def load(self):
        if not self.file_path.exists():
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def save(self, data_list):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data_list, f, indent=4)
