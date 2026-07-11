"""
Example: Safe file handling using 'with open()'.
Week Four — Session Two
"""

with open("sample.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())
