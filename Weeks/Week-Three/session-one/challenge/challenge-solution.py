"""
Challenge Solution: Reusable Student Report Functions
Week Three — Session One
"""

def print_header():
    print("==================================")
    print("       STUDENT ACADEMIC LIST      ")
    print("==================================")

def print_student_row(name, score):
    print(f"Student: {name:<12} | Score: {score}")

def print_footer():
    print("==================================")

print_header()
print_student_row("Abel", 88)
print_student_row("Sara", 94)
print_footer()
