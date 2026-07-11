"""
Exercise 4 Solution: Create Student-Data File
Week Four — Session Two
"""

students = ["Abel", "Sara", "Jon"]
with open("roster.txt", "w") as f:
    for s in students:
        f.write(s + "\n")
print("Roster saved.")
