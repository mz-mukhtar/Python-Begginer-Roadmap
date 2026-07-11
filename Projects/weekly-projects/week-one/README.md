# Smart Student Grade System

## 📌 Project Description
The **Smart Student Grade System** is an interactive command-line application that collects a student's name, three subject names, and three examination scores. It calculates the total score, determines the numeric average, checks for score validity, and displays a clean academic report card with Pass/Fail status and letter grade.

---

## 🎯 Learning Objectives
Students will practice:
- Collecting text and numeric input from the user via `input()`
- Performing type conversions (`float()`) and basic arithmetic calculations
- Implementing decision-making logic using `if`, `elif`, and `else` statements
- Validating numeric score boundaries (`0` to `100`)

---

## 🧠 Concepts Used
- **Week 1**: Variables, Strings, Integers, Floats, `input()`, Type Conversion, Arithmetic Operators, Comparison Operators, Logical Operators (`and`, `or`), Conditional Statements (`if`/`elif`/`else`).

---

## ✨ Features
- Interactive user prompts for student identity and subject scores
- Automatic score validation (ensuring scores are between 0 and 100)
- Total and average score computation
- Automatic letter grade classification (A, B, C, D, F)
- Pass/Fail determination (passing threshold: 50.0 average)
- Clean, formatted summary report output

---

## 📂 Project Structure
```text
week-one/
├── README.md
└── student_grade_system.py
```

---

## ▶️ How to Run
Open your terminal and execute:
```bash
python student_grade_system.py
```

---

## 🖥️ Example Output
```text
========================================
    SMART STUDENT GRADE SYSTEM v1.0     
========================================
Enter student's full name: Sara Ahmed
Enter Subject 1 name: Mathematics
Enter score for Mathematics (0-100): 88.5
Enter Subject 2 name: Physics
Enter score for Physics (0-100): 92.0
Enter Subject 3 name: Computer Science
Enter score for Computer Science (0-100): 95.0

========================================
         OFFICIAL ACADEMIC REPORT       
========================================
Student Name : Sara Ahmed
----------------------------------------
Mathematics          : 88.5
Physics              : 92.0
Computer Science     : 95.0
----------------------------------------
Total Score          : 275.5 / 300
Average Score        : 91.83%
Letter Grade         : A
Academic Status      : PASS
========================================
```

---

## 🔍 How the Project Works
1. Prompts the user for their name and stores it as a string variable.
2. Prompts for three individual subject names and scores, converting score strings to floats.
3. Checks if any score falls outside `0.0` to `100.0`. If invalid, flags an error note.
4. Computes `total_score = score1 + score2 + score3` and `average_score = total_score / 3`.
5. Uses `if`/`elif`/`else` to assign a letter grade (`A` >= 85, `B` >= 70, `C` >= 55, `D` >= 50, else `F`).
6. Prints a formatted banner and report card.

---

## 🛠️ Student Improvement Ideas
- Add scholarship eligibility check (e.g., Average >= 90.0 receives `"ELIGIBLE FOR MERIT SCHOLARSHIP"`).
- Add attendance bonus points calculation.
- Support up to five subject entries.

---

## ✅ Project Checklist
- [x] Ask for student name and three subject names/scores
- [x] Calculate total score and average
- [x] Display Pass or Fail status and letter grade
- [x] Validate score range between 0 and 100
- [x] Display a clean, formatted report banner

---

## 🚀 Next Week
Next week, we will introduce **Python Loops and Collections (Lists, Dictionaries, Sets)**, allowing us to store multiple students and display an interactive command-line menu!
