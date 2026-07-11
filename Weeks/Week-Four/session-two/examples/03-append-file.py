"""
Example: Appending lines to a file with 'a' mode.
Week Four — Session Two
"""

file = open("sample.txt", "a")
file.write("Second line appended.\n")
file.close()
print("Appended to sample.txt")
