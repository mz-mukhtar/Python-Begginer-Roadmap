"""
Exercise 5 Solution: Grade Classifier
Week One — Session Three
"""

score = float(input("Enter score: "))
if score >= 85:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F")
