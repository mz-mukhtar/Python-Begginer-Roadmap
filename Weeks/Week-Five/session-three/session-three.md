# 📘 Week Five – Session Three: Debugging, Logging, and Project Improvement

Welcome back! 👋

In Sessions One and Two of Week Five, you learned how to write fault-tolerant code using `try`, `except`, `else`, and `finally` blocks, and how to import modules from Python's built-in Standard Library (`os`, `sys`, `math`, `random`, `datetime`).

Up until now, when a bug occurred in your code, you might have felt frustrated or stuck. But remember:
> **Errors are a completely normal and inevitable part of software engineering. Do not panic!**

In this session, you will learn the art of **Debugging**—reading tracebacks systematically, using strategic debug prints and editor breakpoints, replacing messy temporary prints with professional **Logging**, and upgrading our application into the **Reliable Student Management System**!

---

## 🎯 Learning Objectives

By the end of this session, you will be able to:
- Explain what debugging is and approach errors with confidence
- Read and dissect Python traceback messages (Error Type, File Name, Line Number, Message)
- Identify and fix common Python errors (`SyntaxError`, `TypeError`, `ValueError`, `KeyError`, etc.)
- Debug scripts using systematic step-by-step reasoning and print statements
- Set breakpoints and step through code using visual debuggers (VS Code / code editors)
- Implement application logging using Python's built-in `logging` module
- Build, run, and explain the **Reliable Student Management System** project

---

## 📌 1. What Is Debugging?

**Debugging** is the systematic process of finding and fixing problems (bugs) in a software program.

Even the world's most experienced engineers write code containing bugs every single day. The difference between a beginner and a senior engineer is not that the senior never writes bugs—it is that the senior knows how to read error tracebacks and isolate problems methodically!

---

## 🔍 2. Reading Python Error Messages

When Python encounters an uncaught error, it prints a **Traceback**. Let us look at a typical traceback:

```text
Traceback (most recent call last):
  File "calculator.py", line 14, in <module>
    result = total_score / student_count
ZeroDivisionError: division by zero
```

How to read this message from bottom to top:
1. **Error Type** (`ZeroDivisionError`): What kind of problem happened.
2. **Error Message** (`division by zero`): Details explaining why it failed.
3. **File Name** (`calculator.py`): Which file contains the error.
4. **Line Number** (`line 14`): Exactly which line Python was executing when it crashed!

---

## 🐞 3. Common Python Errors

Here is a quick reference guide to the errors you will encounter most frequently:

| Error Type | Common Cause | Simple Example |
| :--- | :--- | :--- |
| **`SyntaxError`** | Missing colon, unbalanced parenthesis | `if x == 5 print("yes")` |
| **`NameError`** | Using a variable before defining it | `print(uncreated_var)` |
| **`TypeError`** | Mixing incompatible data types | `"Age: " + 20` |
| **`ValueError`** | Right data type, but invalid value | `int("hello")` |
| **`IndexError`** | Accessing a list index that does not exist | `items = ["a"]; print(items[5])` |
| **`KeyError`** | Accessing a missing dictionary key | `student["phone"]` |
| **`FileNotFoundError`** | Opening a file path that does not exist | `open("missing.json")` |
| **`ZeroDivisionError`** | Dividing any number by zero | `score / 0` |

---

## 🪜 4. Debugging Step by Step

Whenever your program behaves unexpectedly, follow this 6-step debugging checklist:
1. **Read the traceback** carefully from bottom to top.
2. **Find the exact line number** mentioned in the file.
3. **Inspect the code** on that line and the lines immediately above it.
4. **Check variable values** at that exact moment.
5. **Fix one problem at a time** (do not change 5 things at once!).
6. **Run the program again** to verify the fix.

---

## 🖨️ 5. Debugging With `print()`

The simplest way to inspect variables is to insert temporary `print()` statements:

```python
student_score = 80
multiplier = 1.5

# Temporary debug inspection
print("DEBUG: student_score =", student_score, "| multiplier =", multiplier)

final_score = student_score * multiplier
```

> 💡 **Important Reminder**: Always remove or comment out your temporary debug `print()` statements once your code is working!

---

## 🛑 6. Introduction to VS Code Breakpoints

While debug prints are helpful, visual code editors like **Visual Studio Code** offer a built-in **Debugger**:
- **What is a Breakpoint?** A red dot placed on a line of code telling Python to pause execution right before running that line.
- **How to add one:** Click in the margin to the left of the line number in your editor.
- **Stepping through code:** Once paused, you can use step buttons (`Step Over`, `Step Into`) to execute line by line and watch variable values update live!

---

## 📜 7. Introduction to Logging

Instead of leaving messy `print("DEBUG: ...")` statements scattered across your code, professional developers use Python's built-in **`logging`** module!

```python
import logging

# Configure basic logging behavior
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

logging.info("Application initialized successfully.")
logging.warning("Low disk space warning.")
logging.error("Failed to load student data.")
```

### Logging Levels:
- **`DEBUG`**: Detailed diagnostic information for developers.
- **`INFO`**: Confirmation that things are working as expected.
- **`WARNING`**: Indication that something unexpected happened, but the app is still running.
- **`ERROR`**: A serious problem that prevented a specific operation from completing.

---

## ⚖️ 8. Why Logging Is Better Than Leaving Debug Prints

| Feature | Temporary `print()` | Professional `logging` |
| :--- | :--- | :--- |
| **Permanence** | Must be manually deleted after debugging | Can remain safely in production code |
| **Severity Levels** | Every print looks the same | Separates `DEBUG`, `INFO`, `WARNING`, `ERROR` |
| **File Saving** | Prints only to console window | Can easily write logs to a file (`app.log`) |
| **Control** | Cannot be turned off easily | Can silence debug messages with one configuration line |

---

## 🛠️ 9. Weekly Project: Reliable Student Management System

Let us upgrade our student management application by combining robust exception handling (`try-except`), input validation, CRUD operations (Create, Read, Update, Delete), and professional logging into the **Reliable Student Management System**!

### 📋 Interactive Menu
```text
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Save Students
7. Exit
```

### Complete Runnable Code

```python
# ==========================================
# Project: Reliable Student Management System
# Week Five Capstone Project
# ==========================================

import json
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

DATA_FILE = "students.json"


def load_students():
    """Safely loads student records from JSON file with exception handling."""
    if not os.path.exists(DATA_FILE):
        logging.info("No existing data file found. Starting with empty record list.")
        return []

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            logging.info(f"Loaded {len(data)} student record(s) from '{DATA_FILE}'.")
            return data
    except json.JSONDecodeError:
        logging.error(f"File '{DATA_FILE}' contains corrupted JSON. Starting with empty list.")
        return []
    except Exception as e:
        logging.error(f"Unexpected error loading file: {e}")
        return []


def save_students(student_list):
    """Safely saves student records to JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(student_list, file, indent=4)
        logging.info(f"Successfully saved {len(student_list)} record(s) to '{DATA_FILE}'.")
    except Exception as e:
        logging.error(f"Failed to save data to disk: {e}")


def get_valid_integer(prompt):
    """Prompts the user until they enter a valid integer."""
    while True:
        user_input = input(prompt).strip()
        try:
            value = int(user_input)
            if value < 0:
                print("❌ Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")


def display_menu():
    """Displays the main menu."""
    print("\n==========================================")
    print("   RELIABLE STUDENT MANAGEMENT SYSTEM     ")
    print("==========================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Students")
    print("7. Exit")
    print("==========================================")


def add_student(student_list):
    """Registers a new student with input validation."""
    print("\n--- Register New Student ---")
    name = input("Enter student name: ").strip()
    if not name:
        print("❌ Student name cannot be empty.")
        return

    age = get_valid_integer("Enter student age: ")
    department = input("Enter department: ").strip()

    student = {"name": name, "age": age, "department": department}
    student_list.append(student)
    logging.info(f"Added student '{name}'.")
    print(f"✅ Student '{name}' registered successfully!")


def view_students(student_list):
    """Displays all registered students."""
    print("\n--- Registered Students ---")
    if not student_list:
        print("No student records found.")
        return

    for idx, student in enumerate(student_list, start=1):
        print(f"{idx}. Name: {student['name']} | Age: {student['age']} | Department: {student['department']}")


def search_student(student_list):
    """Searches for a student by name."""
    query = input("\nEnter student name to search: ").strip().lower()
    for student in student_list:
        if student["name"].lower() == query:
            print(f"\n✅ Match Found: {student['name']} | Age: {student['age']} | Dept: {student['department']}")
            return
    print(f"❌ No student found matching '{query}'.")


def update_student(student_list):
    """Updates an existing student's age or department."""
    query = input("\nEnter student name to update: ").strip().lower()
    for student in student_list:
        if student["name"].lower() == query:
            print(f"Updating details for '{student['name']}':")
            new_age = get_valid_integer("Enter new age: ")
            new_dept = input("Enter new department: ").strip()

            student["age"] = new_age
            student["department"] = new_dept
            logging.info(f"Updated record for '{student['name']}'.")
            print("✅ Student record updated!")
            return
    print(f"❌ Student matching '{query}' not found.")


def delete_student(student_list):
    """Removes a student record safely."""
    query = input("\nEnter student name to delete: ").strip().lower()
    for student in student_list:
        if student["name"].lower() == query:
            student_list.remove(student)
            logging.info(f"Deleted student '{student['name']}'.")
            print(f"✅ Student '{student['name']}' removed.")
            return
    print(f"❌ Student matching '{query}' not found.")


def main():
    """Main controller loop."""
    student_list = load_students()

    while True:
        display_menu()
        choice = input("Enter selection (1-7): ").strip()

        if choice == "1":
            add_student(student_list)
        elif choice == "2":
            view_students(student_list)
        elif choice == "3":
            search_student(student_list)
        elif choice == "4":
            update_student(student_list)
        elif choice == "5":
            delete_student(student_list)
        elif choice == "6":
            save_students(student_list)
        elif choice == "7":
            save_students(student_list)
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid menu choice. Please select 1 through 7.")


# Run the application
main()
```

---

## 🐞 10. Debugging Activity

Can you find all **3 bugs** in the buggy script below?

```python
# Buggy Script
def calculate_grade(score):
    if score > 90
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"

student_score = input("Enter score: ")
print("Your grade is: " + calculate_grade(student_score))
```

<details>
<summary>🔍 Click to Reveal Debugging Answers</summary>

1. **SyntaxError on Line 3**: Missing colon `:` at the end of `if score > 90`.
2. **TypeError on Line 10**: `input()` returns a string (`"85"`), but `calculate_grade()` compares `score > 90`. Must convert using `int(input("Enter score: "))`.
3. **Logic Flaw on Line 3**: `score > 90` skips `90`! Should be `score >= 90`.
</details>

---

## 📝 11. Practice Exercises

Try these exercises to practice error handling and logging!

### Beginner
1. **Safe Integer Division**: Write a function `safe_divide(a, b)` that returns `a / b` inside a `try-except` block, catching `ZeroDivisionError` and returning `0`.
2. **Basic Logger**: Import `logging`, configure it to level `INFO`, and log three events: `"App started"`, `"User logged in"`, and `"App stopped"`.

### Intermediate
3. **Safe File Reader**: Write a function `read_config(filename)` that attempts to open and print a file. Catch `FileNotFoundError` and print `"Config file missing!"`.
4. **Validating Age Range**: Create a function `get_voting_age()` that loops with `try-except` until the user enters an integer between `18` and `120`.

### Challenge
5. **Log File Output**: Modify `logging.basicConfig(...)` to include `filename="app.log"`. Run your script twice and inspect `app.log` to see your saved log entries!

---

## 🚀 12. Weekly Challenge: Reliable Expense Tracker

Take your Week Four Expense Tracker and make it **bulletproof**:
- Wrap file loading and saving in `try-except` blocks.
- Prevent crashes if `expenses.json` is corrupted or missing.
- Ensure all entered expense amounts are valid positive decimal numbers (`float`).
- Log every added expense using `logging.info()`.

---

## ❓ 13. Review Questions

1. What information can you extract from a Python Traceback?
2. What is the difference between a `SyntaxError` and a `RuntimeError`?
3. Why should you remove temporary `print("DEBUG: ...")` lines before sharing your code?
4. What are the four main severity levels provided by the `logging` module?
5. How does `try-except` prevent an application from crashing when a file is missing?

---

## ✅ 14. Learning Checklist

- [ ] I understand how to read and analyze Python tracebacks.
- [ ] I can identify and fix common Python syntax and runtime errors.
- [ ] I can debug programs systematically using prints and breakpoints.
- [ ] I can implement application logging using the `logging` module.
- [ ] I can build and explain the Reliable Student Management System.

---

## 🏁 15. Session Summary

- **Debugging** is a methodical, step-by-step process of isolating root causes using traceback line numbers.
- **Visual Breakpoints** allow you to pause code execution and inspect variables live.
- **`logging`** provides structured, configurable diagnostics (`INFO`, `WARNING`, `ERROR`) without cluttering output.
- Combining exception handling, input validation, and logging transformed our project into the **Reliable Student Management System**!
