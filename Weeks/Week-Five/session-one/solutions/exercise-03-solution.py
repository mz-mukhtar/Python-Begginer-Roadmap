"""
Exercise 3 Solution: Safe File Reader
Week Five — Session One
"""

try:
    with open("data.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")
