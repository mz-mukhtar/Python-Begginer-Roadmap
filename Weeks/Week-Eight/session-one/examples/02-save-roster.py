"""
Example: Saving serialized student list to JSON disk file.
Week Eight — Session One
"""

import json

def save_to_disk(filename, student_dicts):
    with open(filename, "w") as f:
        json.dump(student_dicts, f, indent=4)
print("Save function ready.")
