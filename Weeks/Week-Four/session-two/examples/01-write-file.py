"""
Example: Writing text to a file using open().
Week Four — Session Two
"""

file = open("sample.txt", "w")
file.write("Hello File Storage!\n")
file.close()
print("Wrote sample.txt")
