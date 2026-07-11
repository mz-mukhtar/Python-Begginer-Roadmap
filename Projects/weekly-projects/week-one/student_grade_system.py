"""
Project: Smart Student Grade System
Week One — Python Beginner Roadmap
Author: Mahi Zeki (EthioNext / Cyber Vanguard)

Description:
An interactive grade report application built using strictly Week One concepts:
variables, user input, type conversion, arithmetic calculations, and conditional logic.
"""

print("========================================")
print("    SMART STUDENT GRADE SYSTEM v1.0     ")
print("========================================")

# 1. Collect student identification
student_name = input("Enter student's full name: ")

# 2. Collect subject names and scores
subject1 = input("Enter Subject 1 name: ")
score1 = float(input(f"Enter score for {subject1} (0-100): "))

subject2 = input("Enter Subject 2 name: ")
score2 = float(input(f"Enter score for {subject2} (0-100): "))

subject3 = input("Enter Subject 3 name: ")
score3 = float(input(f"Enter score for {subject3} (0-100): "))

# 3. Validate score ranges (between 0 and 100)
scores_valid = True
if score1 < 0 or score1 > 100 or score2 < 0 or score2 > 100 or score3 < 0 or score3 > 100:
    scores_valid = False

print("")
print("========================================")
print("         OFFICIAL ACADEMIC REPORT       ")
print("========================================")

if not scores_valid:
    print("ERROR: One or more entered scores fall outside the valid 0-100 range.")
    print("Please restart the application and enter valid scores.")
else:
    # 4. Perform calculations
    total_score = score1 + score2 + score3
    average_score = total_score / 3

    # 5. Determine letter grade and status using conditions
    if average_score >= 85.0:
        letter_grade = "A"
    elif average_score >= 70.0:
        letter_grade = "B"
    elif average_score >= 55.0:
        letter_grade = "C"
    elif average_score >= 50.0:
        letter_grade = "D"
    else:
        letter_grade = "F"

    if average_score >= 50.0:
        academic_status = "PASS"
    else:
        academic_status = "FAIL"

    # 6. Display report card
    print("Student Name :", student_name)
    print("----------------------------------------")
    print(subject1, ":", score1)
    print(subject2, ":", score2)
    print(subject3, ":", score3)
    print("----------------------------------------")
    print("Total Score          :", round(total_score, 2), "/ 300")
    print("Average Score        :", round(average_score, 2), "%")
    print("Letter Grade         :", letter_grade)
    print("Academic Status      :", academic_status)

print("========================================")
