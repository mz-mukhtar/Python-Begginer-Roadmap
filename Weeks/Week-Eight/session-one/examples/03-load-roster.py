"""
Example: Loading JSON records from disk.
Week Eight — Session One
"""

import json
from pathlib import Path

def load_from_disk(filename):
    if not Path(filename).exists():
        return []
    with open(filename, "r") as f:
        return json.load(f)
print("Load function ready.")
