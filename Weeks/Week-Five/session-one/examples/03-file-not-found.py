"""
Example: Handling FileNotFoundError gracefully.
Week Five — Session One
"""

try:
    with open("missing_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: The requested file does not exist.")
