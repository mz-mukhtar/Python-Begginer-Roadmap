"""
Example: Dedicated StudentStorage repository class.
Week Eight — Session One
"""

import json
from pathlib import Path

class StudentStorage:
    def __init__(self, filename="students.json"):
        self.filename = Path(filename)
