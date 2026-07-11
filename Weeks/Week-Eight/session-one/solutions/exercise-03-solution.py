"""
Exercise 3 Solution: Handle Missing File
Week Eight — Session One
"""

from pathlib import Path
p = Path("nonexistent.json")
data = [] if not p.exists() else []
print("Missing file handled.")
