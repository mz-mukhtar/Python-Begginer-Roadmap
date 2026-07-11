"""
Example: Reading text from a file.
Week Four — Session Two
"""

file = open("sample.txt", "r")
content = file.read()
file.close()
print("Read content:", content.strip())
