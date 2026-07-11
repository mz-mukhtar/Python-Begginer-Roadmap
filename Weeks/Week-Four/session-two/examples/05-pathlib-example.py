"""
Example: Working with file paths using pathlib.
Week Four — Session Two
"""

from pathlib import Path

file_path = Path("sample.txt")
if file_path.exists():
    print("File exists on disk!")
