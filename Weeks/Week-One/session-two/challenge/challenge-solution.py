"""
Challenge Solution: Student Result Calculator
Week One — Session Two
"""

student_name = input("Enter student name: ")
math_score = float(input("Enter Math score: "))
science_score = float(input("Enter Science score: "))
english_score = float(input("Enter English score: "))

total_score = math_score + science_score + english_score
average_score = total_score / 3

print("==========================================")
print("          STUDENT RESULT REPORT           ")
print("==========================================")
print("Student Name   :", student_name)
print("Total Score    :", total_score, "/ 300")
print("Average Score  :", round(average_score, 2), "%")
print("==========================================")
