"""
Example: Handling ValueError when converting string to integer.
Week Five — Session One
"""

try:
    age = int("twenty")
except ValueError:
    print("Caught ValueError! Please provide numeric digits.")
