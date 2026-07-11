"""
Exercise 4 Solution: Handle Invalid JSON
Week Eight — Session One
"""

import json
try:
    data = json.loads("{broken json")
except json.JSONDecodeError:
    data = []
print("Handled decode error.")
