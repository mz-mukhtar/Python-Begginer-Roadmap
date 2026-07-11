# 📘 Week 5 – Session 2: Python Modules and Project Improvement

Welcome to **Week 5 – Session 2**! 🚀

In our last session, you learned how to protect your programs from crashing using exception handling (`try` and `except`). Today, we are taking two exciting steps forward:
1. Exploring **Python Modules** (`random`, `math`, and `datetime`) so you can tap into pre-written tools instead of coding everything from zero.
2. Upgrading your existing project with full **Search**, **Update**, and **Delete** features so your application functions like real-world software!

By the end of this session, you will be able to:
- Import and use built-in Python modules (`import module_name`)
- Generate random numbers and random choices using `random`
- Perform everyday calculations using `math`
- Work with live dates and timestamps using `datetime`
- Build a complete, error-safe, file-backed application with Add, View, Search, Update, and Delete features

---

## 📦 1. Introduction to Modules and Import Styles

A **module** is simply a file containing Python code—such as functions, classes, and variables—that can be imported and reused in other programs.

### Why Create Custom Modules?
As your programs grow, writing hundreds of lines of code inside a single `main.py` file becomes confusing. Breaking code into separate modules (for example, `file_helpers.py` or `math_utils.py`):
1. **Keeps code organized**: Each file has a single, clear responsibility.
2. **Promotes code reuse**: You can import helper functions across multiple projects without copying and pasting.
3. **Makes collaboration easier**: Multiple developers can work on different module files simultaneously.

---

### Three Ways to Import Modules

#### 1️⃣ Full Module Import (`import module_name`)
Imports the entire module. You access its functions using dot notation:
```python
import math_utils

result = math_utils.add(10, 5)
```

#### 2️⃣ Specific Function Import (`from module_name import function`)
Imports only the exact functions you need directly into your file:
```python
from math_utils import add, subtract

print(add(10, 5))
print(subtract(10, 5))
```

#### 3️⃣ Module Aliases (`import module_name as alias`)
Gives a module a short nickname to save typing:
```python
import math_utils as mu

print(mu.add(10, 5))
```

---

### Best Practices for Modules
- **Keep modules focused**: A module should handle one area (e.g., database tools or calculation tools).
- **Use clear filenames**: Name your Python files using lowercase letters and underscores (`student_helpers.py`).
- **Avoid circular imports**: Do not make `module_a.py` import `module_b.py` while `module_b.py` simultaneously imports `module_a.py`.

---

## 🎲 2. The `random` Module

The `random` module helps you generate random numbers and pick random items from lists. It is perfect for games, simulations, and quizzes!

Let’s import it and explore two popular functions:

```python
import random

# Generate a random integer between 1 and 10 (inclusive)
lucky_number = random.randint(1, 10)
print("Random Number:", lucky_number)

# Pick a random item from a list
colors = ["Red", "Blue", "Green", "Yellow"]
chosen_color = random.choice(colors)
print("Random Color:", chosen_color)
```

---

### 🎮 Mini-Project: Number Guessing Game

Let’s combine `random.randint()`, loops, functions, and exception handling to build an interactive **Number Guessing Game**!

#### 📋 Requirements:
- Generate a secret random number between `1` and `50`
- Ask the user to guess the number
- Display whether their guess is too high or too low
- Handle invalid input safely if the user types text
- Count how many attempts it took to win

#### 💻 Code:
```python
import random

def play_guessing_game():
    secret_number = random.randint(1, 50)
    attempts = 0
    print("=== Welcome to the Number Guessing Game! ===")
    print("I am thinking of a number between 1 and 50.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number!")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed {secret_number} in {attempts} attempts!")
            break

# Run the game
if __name__ == "__main__":
    play_guessing_game()
```

---

## 🧮 3. The `math` Module

When you need extra mathematical operations beyond basic `+`, `-`, `*`, `/`, you can import Python’s built-in `math` module:

```python
import math
```

Here are three simple, practical `math` functions:

```python
import math

# 1. math.sqrt(x) -> Calculates the square root of a number
print("Square root of 25:", math.sqrt(25))  # 5.0

# 2. math.ceil(x) -> Rounds a decimal UP to the next integer
print("Ceil of 4.2:", math.ceil(4.2))  # 5

# 3. math.floor(x) -> Rounds a decimal DOWN to the previous integer
print("Floor of 4.8:", math.floor(4.8))  # 4
```

---

## 📅 4. The `datetime` Module

In many applications, tracking **when** something happened is essential. You can import `datetime` to get the current date and time:

```python
from datetime import datetime

current_time = datetime.now()
print("Live Timestamp:", current_time)

# Friendly formatting: YYYY-MM-DD
formatted_date = current_time.strftime("%Y-%m-%d")
print("Today's Date:", formatted_date)
```

💡 **How can dates be used in your projects?**
- **Expense Tracker**: Automatically record the exact date every expense was added
- **To-Do List App**: Save the creation date or deadline for each task
- **Student Management System**: Record registration dates for new students

---

## 🛠️ 5. Project Improvement: Search, Update, and Delete

Over the past five weeks, you have learned:
- Variables & Conditions
- Loops & Lists
- Functions & Dictionaries
- Strings & File Handling
- Error Handling & Modules

Now let’s bring all these skills together! A professional application doesn't just add and view records—it lets users **Search**, **Update**, and **Delete** records safely.

Let's see how each operation works conceptually:
- **Search**: Loop through your list of records and display matching items
- **Update**: Find an existing record by ID or name and modify its values
- **Delete**: Remove a record from the list safely and update the saved file
- **Input Validation & Saving**: Ensure every change is immediately saved to disk

---

## 💻 6. Integrated Project Example: Complete Student Management System

Let’s build a complete, runnable **Student Management System** using modular functions, dictionary storage, file persistence (`students.json`), and full error handling!

*(Note: We are using clean functions and dictionaries here. Next week in Week 6, we will introduce Object-Oriented Programming and refactor applications into classes!)*

```python
import json

FILENAME = "students.json"

def load_students():
    """Loads student records from file safely."""
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_students(student_list):
    """Saves student records to file."""
    with open(FILENAME, "w") as file:
        json.dump(student_list, file, indent=4)

def add_student(student_list):
    """Adds a new student safely."""
    name = input("Enter student name: ").strip()
    
    while True:
        try:
            age = int(input("Enter student age: "))
            break
        except ValueError:
            print("Please enter a valid numeric age!")

    major = input("Enter student major/course: ").strip()

    new_student = {
        "id": len(student_list) + 1,
        "name": name,
        "age": age,
        "major": major
    }
    student_list.append(new_student)
    save_students(student_list)
    print(f"✅ Student '{name}' added successfully!")

def view_students(student_list):
    """Displays all registered students."""
    if not student_list:
        print("No students registered yet.")
        return

    print("\n--- Student List ---")
    for student in student_list:
        print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Major: {student['major']}")

def search_student(student_list):
    """Searches for a student by name."""
    search_name = input("Enter student name to search: ").strip().lower()
    found = False

    for student in student_list:
        if search_name in student["name"].lower():
            print(f"Found -> ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Major: {student['major']}")
            found = True

    if not found:
        print("No matching student found.")

def update_student(student_list):
    """Updates an existing student record by ID."""
    view_students(student_list)
    if not student_list:
        return

    try:
        target_id = int(input("Enter the ID of the student to update: "))
    except ValueError:
        print("Invalid ID entered.")
        return

    for student in student_list:
        if student["id"] == target_id:
            print(f"Updating {student['name']}...")
            new_name = input("Enter new name (press Enter to keep current): ").strip()
            if new_name:
                student["name"] = new_name

            new_major = input("Enter new major (press Enter to keep current): ").strip()
            if new_major:
                student["major"] = new_major

            save_students(student_list)
            print("✅ Student updated successfully!")
            return

    print("Student ID not found.")

def delete_student(student_list):
    """Deletes a student record by ID."""
    view_students(student_list)
    if not student_list:
        return

    try:
        target_id = int(input("Enter the ID of the student to delete: "))
    except ValueError:
        print("Invalid ID entered.")
        return

    for i in range(len(student_list)):
        if student_list[i]["id"] == target_id:
            removed_name = student_list[i]["name"]
            student_list.pop(i)
            save_students(student_list)
            print(f"✅ Student '{removed_name}' deleted successfully!")
            return

    print("Student ID not found.")

def main_menu():
    students = load_students()

    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Goodbye! All student data is saved.")
            break
        else:
            print("Invalid selection. Please choose between 1 and 6.")

if __name__ == "__main__":
    main_menu()
```

---

## 🎯 7. Student Project Activity

Now it is your turn! Choose your primary final project track from the **Projects Manual**:
- **Student Management System**
- **Contact Book System**
- **Expense Tracker System**
- **Quiz Application**
- **To-Do List Manager**

### 📋 Activity Checklist:
1. Make sure your project loads and saves data to a file (`.txt` or `.json`)
2. Add a **Search** function so users can find entries easily
3. Add an **Update** function so users can edit existing records
4. Add a **Delete** function so users can remove unwanted records
5. Wrap every numeric input inside `try` and `except` blocks so your project never crashes

---

## 🧪 8. Practice Exercises

1. **Dice Roller Simulator**: Use `random.randint(1, 6)` to simulate rolling two six-sided dice. Allow the user to roll repeatedly until they type `"q"`.
2. **Ceiling Calculator**: Use `math.ceil()` to calculate how many 4-person taxis are needed to transport a group of people (ask the user for total passengers).
3. **Daily Expense Logger**: Use `datetime.now().strftime("%Y-%m-%d")` to stamp the current date automatically whenever a user adds a new expense to their list.
4. **Search by Category**: Add a search function to a To-Do List app that lets users search for tasks containing a specific word.

---

## ✅ 9. Session Summary

- **Modules** (`import module_name`) allow you to reuse pre-built code from Python's standard library.
- The **`random`** module generates random integers (`randint()`) and selects random items (`choice()`).
- The **`math`** module provides everyday tools like square roots (`sqrt()`) and rounding (`ceil()`, `floor()`).
- The **`datetime`** module gives live dates and timestamps (`datetime.now()`).
- Combining **Search**, **Update**, **Delete**, **File Persistence**, and **Error Handling** turns your scripts into complete, professional applications!
