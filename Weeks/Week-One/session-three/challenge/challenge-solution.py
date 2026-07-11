"""
Challenge Solution: Smart Student Grade System
Week One — Session Three
"""

student_name = input("Enter student name: ")
score = float(input("Enter exam score (0-100): "))
attendance = float(input("Enter attendance percentage (0-100): "))

if score < 0 or score > 100 or attendance < 0 or attendance > 100:
    print("Error: Invalid input values out of range (0-100)!")
else:
    if score >= 85:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    if score >= 85 and attendance >= 90:
        scholarship = "ELIGIBLE (Merit Scholarship)"
    else:
        scholarship = "STANDARD ENROLLMENT"

    print("==========================================")
    print("       SMART STUDENT GRADE SYSTEM         ")
    print("==========================================")
    print("Student Name   :", student_name)
    print("Exam Score     :", score)
    print("Attendance     :", attendance, "%")
    print("Letter Grade   :", grade)
    print("Scholarship    :", scholarship)
    print("==========================================")
