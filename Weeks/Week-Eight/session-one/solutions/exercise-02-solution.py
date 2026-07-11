"""
Exercise 2 Solution: Load Roster from JSON
Week Eight — Session One
"""

import json
from pathlib import Path
def load_roster(file):
    if not Path(file).exists(): return []
    with open(file, "r") as f: return json.load(f)
print("Load roster implemented.")
