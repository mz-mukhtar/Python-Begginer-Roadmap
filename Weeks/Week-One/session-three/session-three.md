# 📘 Week One – Session Three: Conditions and Weekly Project

Welcome back! 👋

In Sessions One and Two, you learned how to store information in variables, capture interactive input from users (`input()`), convert data types (`int()`, `float()`), and perform calculations using arithmetic operators.

Up until now, every program you wrote executed line by line from top to bottom. But what if you want your program to make intelligent decisions? For example:
- A student passes when their average score is high enough.
- A user receives access when their entered password is correct.
- A person is eligible for a discount when their age or membership meets the required conditions.

In this session, you will learn how programs make decisions using **Boolean values**, **comparison operators**, **conditional statements** (`if`, `elif`, `else`), and **logical operators** (`and`, `or`, `not`). Finally, you will apply everything you have learned in Week One to build the interactive **Smart Student Grade System** project!

---

## 🎯 Learning Objectives

By the end of this session, you will be able to:
- Work with Boolean values (`True` and `False`)
- Compare numbers and text using comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Write branching logic using `if`, `elif`, and `else` blocks
- Combine multiple conditions cleanly using logical operators (`and`, `or`, `not`)
- Use nested conditions to handle step-by-step checks
- Validate user input ranges using conditional logic
- Build, test, and explain the **Smart Student Grade System** project

---

## 📌 1. Introduction to Decision Making

Real-life decisions depend on conditions. If it is raining, you take an umbrella; otherwise, you leave it at home.

In Python, decision-making works exactly the same way. We inspect a condition, evaluate whether it is `True` or `False`, and choose which block of code to run.

---

## ⚖️ 2. Boolean Values

In Python, a **Boolean** is a data type that has only two possible values:
- `True`
- `False`

Notice that both `True` and `False` must begin with a capital letter!

Let us see an example:

```python
is_student = True
has_completed_course = False

print("Is student?", is_student)
print("Has completed course?", has_completed_course)
print("Type of is_student:", type(is_student))
```

### Example Output:
```text
Is student? True
Has completed course? False
Type of is_student: <class 'bool'>
```

Boolean values normally represent yes/no or true/false situations in your application.

---

## 🔍 3. Comparison Operators

How do we generate a Boolean value? We compare two values using **Comparison Operators**.

Here is a clear reference table:

| Operator | Meaning | Example | Result |
| :---: | :--- | :--- | :--- |
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `10 != 5` | `True` |
| `>` | Greater than | `8 > 12` | `False` |
| `<` | Less than | `4 < 9` | `True` |
| `>=` | Greater than or equal to | `15 >= 15` | `True` |
| `<=` | Less than or equal to | `7 <= 3` | `False` |

> 💡 **Important Reminder**: A single equal sign (`=`) assigns a value to a variable (`age = 18`). A double equal sign (`==`) compares two values (`age == 18`).

Let us test comparison operators in Python:

```python
passing_score = 50
student_score = 65

print("Did student pass?", student_score >= passing_score)
print("Is perfect score?", student_score == 100)
```

---

## 🌿 4. The `if` Statement

An `if` statement checks a condition. If the condition evaluates to `True`, Python executes the indented block of code directly below it.

```python
student_score = 80

if student_score >= 50:
    print("The student passed.")
```

🔍 **Breakdown**:
1. **Condition**: `student_score >= 50` is evaluated. Since `80 >= 50` is `True`, Python enters the block.
2. **Colon (`:`)**: Tells Python that an indented code block is starting.
3. **Indentation**: Standard Python indentation is **4 spaces**. All indented lines belong inside the `if` block.

---

## 🔀 5. The `else` Statement

What if the condition is `False`? We use an `else` statement to tell Python what to do when the check fails:

```python
student_score = int(input("Enter the student's score: "))

if student_score >= 50:
    print("The student passed.")
else:
    print("The student failed.")
```

If a student enters `45`, the `if` condition evaluates to `False`, so Python automatically skips to the `else` block and prints `"The student failed."`.

---

## 🪜 6. The `elif` Statement

When you have more than two possible outcomes, use `elif` (short for *else if*). Python checks conditions from top to bottom and runs the first block that evaluates to `True`.

Let us create a grade classifier:
- 90–100 → A
- 80–89 → B
- 70–79 → C
- 60–69 → D
- Below 60 → F

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

> 💡 **Why Order Matters**: Python stops checking as soon as it finds the first `True` condition. If you checked `score >= 60` first, a score of `95` would mistakenly receive a `D`! Always order your numerical ranges from highest to lowest (or lowest to highest).

---

## 🔗 7. Logical Operators

Sometimes a decision requires checking multiple conditions at the same time. We use **Logical Operators**:
- `and`: True only if **both** conditions are True
- `or`: True if **at least one** condition is True
- `not`: Reverses a Boolean (`not True` becomes `False`)

Let us see a real-life example:

```python
student_age = 20
has_student_id = True

# Student must be 18 or older AND possess a student ID
if student_age >= 18 and has_student_id:
    print("Access granted to university library.")
else:
    print("Access denied.")
```

---

## 🪆 8. Nested Conditions

You can place an `if` statement inside another `if` statement. This is called a **Nested Condition**.

```python
is_registered = True
has_paid_tuition = True

if is_registered:
    if has_paid_tuition:
        print("Student can attend classes.")
    else:
        print("Please complete tuition payment.")
else:
    print("Please register first.")
```

Do not worry if this looks new. Nested conditions simply let you perform step-by-step verification!

---

## 🛡️ 9. Input Validation

Before processing data, programs should verify that user input makes sense. For example, a test score should not be negative or greater than 100:

```python
student_score = float(input("Enter the student's score (0-100): "))

if student_score < 0 or student_score > 100:
    print("Error: Please enter a valid score from 0 to 100.")
else:
    print("The score is valid.")
```

*(Note: We use conditional checks here for range validation. In Week Five, you will learn how to handle text errors using exception handling!)*

---

## 🛠️ 10. Weekly Project: Smart Student Grade System

Let us combine variables, user input, type conversion, arithmetic operators, and conditional statements into our complete Week One capstone project: the **Smart Student Grade System**!

### 📋 Project Description & Requirements
- Ask the user for the student's name
- Ask for three numerical subject scores
- Validate that all three scores remain between `0` and `100`
- Calculate the total score and average score
- Display whether the student passed (`Average >= 50`) or failed
- Assign a letter grade (`A`, `B`, `C`, `D`, `F`)
- Award an Honor Distinction if the student's average is `90` or higher

### Step-by-Step Plan
1. Capture the student's name using `input()`.
2. Capture three scores using `float(input())`.
3. Check if any score is `< 0` or `> 100`. If invalid, display an error message.
4. If valid, calculate `total = score1 + score2 + score3` and `average = total / 3`.
5. Use `if-elif-else` to determine the letter grade and pass/fail status.

### Complete Runnable Code

```python
# ==========================================
# Project: Smart Student Grade System
# Week One Capstone Project
# ==========================================

print("=== Welcome to the Smart Student Grade System ===")

# 1. Capture student name
student_name = input("Enter the student's name: ")

# 2. Capture three subject scores
score_math = float(input("Enter Math score (0-100): "))
score_science = float(input("Enter Science score (0-100): "))
score_english = float(input("Enter English score (0-100): "))

# 3. Validate score ranges
if score_math < 0 or score_math > 100 or score_science < 0 or score_science > 100 or score_english < 0 or score_english > 100:
    print("\nError: All scores must be between 0 and 100. Please restart the program.")
else:
    # 4. Calculate total and average
    total_score = score_math + score_science + score_english
    average_score = total_score / 3

    # 5. Determine letter grade
    if average_score >= 90:
        letter_grade = "A"
    elif average_score >= 80:
        letter_grade = "B"
    elif average_score >= 70:
        letter_grade = "C"
    elif average_score >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    # 6. Determine Pass or Fail
    if average_score >= 50:
        result_status = "Pass"
    else:
        result_status = "Fail"

    # 7. Display formatted Report Card
    print("\n==========================================")
    print("            STUDENT REPORT CARD           ")
    print("==========================================")
    print("Student Name:", student_name)
    print("Total Score :", total_score)
    print("Average     :", round(average_score, 2))
    print("Letter Grade:", letter_grade)
    print("Status      :", result_status)

    if average_score >= 90:
        print("Distinction : ⭐ FIRST CLASS HONORS ⭐")
    print("==========================================")
```

### Example Output:
```text
=== Welcome to the Smart Student Grade System ===
Enter the student's name: Sara
Enter Math score (0-100): 92
Enter Science score (0-100): 88
Enter English score (0-100): 94

==========================================
            STUDENT REPORT CARD           
==========================================
Student Name: Sara
Total Score : 274.0
Average     : 91.33
Letter Grade: A
Status      : Pass
Distinction : ⭐ FIRST CLASS HONORS ⭐
==========================================
```

### Code Explanation
- `float(input(...))` converts entered scores into decimal numbers so we can calculate exact averages.
- The `if` statement checking `< 0 or > 100` ensures data integrity before running calculations.
- `round(average_score, 2)` formats the average to two decimal places for readable display.

---

## 📝 11. Practice Exercises

Try to solve these exercises before checking any solutions!

### Beginner
1. **Positive or Negative Number**: Write a script that asks the user for a number and prints whether it is positive, negative, or zero.
2. **Even or Odd Number**: Use the modulo operator (`%`) and an `if-else` block to print whether an entered integer is even (`num % 2 == 0`) or odd.

### Intermediate
3. **Age Eligibility Checker**: Ask the user for their age. If they are `18` or older, print `"Eligible to vote"`. Otherwise, print how many years they have left until they turn 18.
4. **Password Checker**: Store a secret password in a variable (`secret = "python123"`). Ask the user to enter a password and print `"Access Granted"` if it matches or `"Access Denied"` if it does not.
5. **Grade Classifier**: Ask for a single test score and print both the letter grade (`A-F`) and whether the score qualifies for a retake exam (`score < 50`).

### Challenge
6. **Discount Calculator**: A bookstore offers a 15% discount if a customer buys more than 3 books **or** spends over $50. Write a program that asks for total books and total spending, checks discount eligibility using `or`, and outputs the final price.

---

## 🚀 12. Weekly Challenge: Student Scholarship Eligibility System

Put your logic skills to the test with this independent challenge!

### Requirements:
- Ask the user for a student's **average score** (0-100).
- Ask the user for the student's **attendance percentage** (0-100).
- Ask whether the student participates in a school club (`"yes"` or `"no"`).
- A student is eligible for a scholarship if:
  - Their average score is **85 or higher** `and` attendance is **90% or higher**, **OR**
  - Their average score is **80 or higher** `and` they participate in a school club (`"yes"`).

💡 **Hint**: Combine comparison checks inside parentheses:  
`if (score >= 85 and attendance >= 90) or (score >= 80 and club == "yes"):`

---

## ❓ 13. Review Questions

1. What are the only two possible values of a Python Boolean?
2. What is the difference between `=` and `==`?
3. What happens if an `if` condition evaluates to `False` and there is no `else` block?
4. Why does the order of conditions matter when writing an `if-elif-else` chain?
5. When does an `and` logical expression evaluate to `True`?
6. When does an `or` logical expression evaluate to `True`?
7. What is indentation in Python, and why is it mandatory after an `if` statement?

---

## ✅ 14. Learning Checklist

- [ ] I understand Boolean values (`True` and `False`).
- [ ] I can use comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`).
- [ ] I can create conditional branches using `if`, `elif`, and `else`.
- [ ] I understand how to combine conditions using `and`, `or`, and `not`.
- [ ] I can use nested conditions for step-by-step checks.
- [ ] I can validate numerical input ranges using `if` statements.
- [ ] I can build a complete decision-making Python program.

---

## 🏁 15. Session Summary

- **Booleans** represent truth values (`True` or `False`).
- **Comparison Operators** compare values and produce Booleans.
- **`if` / `elif` / `else`** statements allow programs to choose which code block to execute based on conditions.
- **Logical Operators** (`and`, `or`, `not`) combine multiple comparison checks together.
- Combining variables, arithmetic, input validation, and decision logic allowed us to build our first complete application: the **Smart Student Grade System**!
