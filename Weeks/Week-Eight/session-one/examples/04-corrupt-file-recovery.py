"""
Example: Recovering gracefully when JSON file is corrupted or empty.
Week Eight — Session One
"""

import json
from pathlib import Path

def safe_load(filename):
    path = Path(filename)
    if not path.exists():
        return []
    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: JSON file corrupted. Initializing empty roster.")
        return []
