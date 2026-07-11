# 📘 Week Three – Session Three: Program Decomposition and Functional Project

Welcome back! 👋

In Sessions One and Two of Week Three, you learned how to define functions using `def`, accept parameters, return values, and organize logic into reusable blocks.

Up until now, our scripts have been relatively short. But what happens when an application grows to 200 or 500 lines of code? If all your logic is written together inside one giant `while` loop, the code becomes tangled, confusing, and difficult to fix.

Remember this golden rule:
> **A large problem can always be divided into smaller, manageable problems.**

In this session, you will learn **Program Decomposition**—how to break down a complex application into focused, single-responsibility functions, eliminate duplicate code, pass data cleanly between functions, and build our **Function-Based Student Management System**!

---

## 🎯 Learning Objectives

By the end of this session, you will be able to:
- Explain what Program Decomposition is and why professional developers use it
- Apply the Single Responsibility Principle (one function = one main task)
- Eliminate repeated code by extracting it into helper functions
- Pass collections (`student_list`) as arguments into functions safely
- Return dictionaries and data structures from builder functions
- Coordinate an application workflow using a `main()` controller function
- Build, run, and explain the **Function-Based Student Management System** project

---

## 📌 1. What Is Program Decomposition?

**Program Decomposition** simply means breaking down a large application into independent, smaller building blocks.

Think about a restaurant kitchen. One chef does not take orders, cook soup, bake bread, wash dishes, and collect money all at once! Tasks are separated.

Let us decompose a **Student Management System**:

```text
Student Management System
  ├── Display Menu
  ├── Add Student
  ├── View Students
  ├── Search Student
  └── Exit Program
```

Each of these distinct responsibilities can become its own clean Python function!

---

## 🎯 2. One Function, One Main Responsibility

When designing functions, follow the **Single Responsibility Principle**: a function should do one thing and do it well.

### ❌ Bad Example (Everything tangled together):
```python
def student_system():
    # Displays menu, collects input, searches list, and prints everything inside one 100-line function
    pass
```

### ✅ Better Example (Clean, modular functions):
```python
def display_menu():
    pass

def add_student(student_list):
    pass

def view_students(student_list):
    pass
```

Why are smaller functions better?
- **Easier to Read**: Each function fits on your screen.
- **Easier to Test**: You can test `add_student()` without running the entire menu loop.
- **Easier to Fix**: If searching is broken, you know exactly which function to inspect.
- **Easier to Reuse**: You can call `display_menu()` anywhere in your program.

---

## ♻️ 3. Avoiding Duplicate Code

If you find yourself copying and pasting the same 5 lines of code in three different places, that is a sign you should create a helper function!

### Before (Repeated formatting code):
```python
print("==========================================")
print("Student Profile:", student_1["name"])
print("==========================================")

print("==========================================")
print("Student Profile:", student_2["name"])
print("==========================================")
```

### After (One reusable helper function):
```python
def print_header(title):
    print("==========================================")
    print(title)
    print("==========================================")

print_header(f"Student Profile: {student_1['name']}")
print_header(f"Student Profile: {student_2['name']}")
```

---

## 🔀 4. Passing Data Between Functions

When you decompose a program, functions need to share information. We pass our main `student_list` into helper functions as an argument:

```python
def view_students(student_list):
    if not student_list:
        print("No students registered yet.")
        return

    print("\n--- Registered Students ---")
    for student in student_list:
        print(f"Name: {student['name']} | Age: {student['age']}")
```

---

## 📤 5. Returning Data From Functions

Functions can also construct and return new data structures. Look at this builder function that captures user input and returns a structured dictionary:

```python
def create_student():
    student_name = input("Enter the student's name: ").strip()
    student_age = int(input("Enter the student's age: "))
    student_department = input("Enter department: ").strip()

    student = {
        "name": student_name,
        "age": student_age,
        "department": student_department
    }
    return student
```

Now, any part of our application can call `new_student = create_student()`!

---

## 📋 6. Creating a Menu Function

Let us extract our menu display into its own readable function:

```python
def display_menu():
    print("\n==========================================")
    print("      STUDENT MANAGEMENT SYSTEM           ")
    print("==========================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    print("==========================================")
```

---

## 🎮 7. The `main()` Controller Function

To bring all our pieces together, we write a `main()` function. This function controls the program flow and holds the master `student_list`:

```python
def main():
    student_list = []
    print("Welcome to the application!")
    # Main menu loop goes here...
```

Let us assemble the complete project!

---

## 🛠️ 8. Weekly Project: Function-Based Student Management System

Let us build our Week Three capstone project: the **Function-Based Student Management System**!

### 📋 Required Features
1. **Add Student**: Prompts for details and adds the record to `student_list`.
2. **View Students**: Displays all registered student profiles.
3. **Search Student**: Finds and displays a student by name.
4. **Exit**: Gracefully ends the application.

### Complete Runnable Code

```python
# ==========================================
# Project: Function-Based Student Management System
# Week Three Capstone Project
# ==========================================

def display_menu():
    """Displays the main application menu."""
    print("\n==========================================")
    print("      STUDENT MANAGEMENT SYSTEM           ")
    print("==========================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    print("==========================================")


def create_student():
    """Captures input and returns a new student dictionary."""
    name = input("Enter student name: ").strip()
    age = int(input("Enter student age: "))
    department = input("Enter student department: ").strip()

    student = {
        "name": name,
        "age": age,
        "department": department
    }
    return student


def add_student(student_list):
    """Creates a student and appends it to the student list."""
    print("\n--- Register New Student ---")
    new_student = create_student()
    student_list.append(new_student)
    print(f"✅ Student '{new_student['name']}' added successfully!")


def view_students(student_list):
    """Displays all students currently in the list."""
    print("\n--- Registered Student Profiles ---")
    if not student_list:
        print("No students registered yet.")
        return

    for index, student in enumerate(student_list, start=1):
        print(f"{index}. Name: {student['name']} | Age: {student['age']} | Department: {student['department']}")


def search_student(student_list):
    """Searches for a student by name (case-insensitive)."""
    print("\n--- Search Student ---")
    if not student_list:
        print("No students registered yet.")
        return

    query = input("Enter student name to search: ").strip().lower()
    found = False

    for student in student_list:
        if student["name"].lower() == query:
            print("\n✅ Student Found!")
            print("Name      :", student["name"])
            print("Age       :", student["age"])
            print("Department:", student["department"])
            found = True
            break

    if not found:
        print(f"❌ No student found with the name '{query}'.")


def main():
    """Main controller loop for the Student Management System."""
    student_list = []
    print("Welcome to the Function-Based Student Management System!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(student_list)
        elif choice == "2":
            view_students(student_list)
        elif choice == "3":
            search_student(student_list)
        elif choice == "4":
            print("\n👋 Thank you for using the Student Management System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 4.")


# Run our controller function
main()
```

### Example Output:
```text
Welcome to the Function-Based Student Management System!

==========================================
      STUDENT MANAGEMENT SYSTEM           
==========================================
1. Add Student
2. View Students
3. Search Student
4. Exit
==========================================
Enter your choice (1-4): 1

--- Register New Student ---
Enter student name: Abel
Enter student age: 21
Enter student department: Engineering
✅ Student 'Abel' added successfully!
```

### Code Explanation
- `display_menu()` encapsulates formatting so our `main()` loop remains uncluttered.
- `create_student()` isolates input capture and returns a ready-to-use dictionary.
- `add_student(student_list)` accepts the list and appends the newly created dictionary.
- `main()` coordinates the workflow and keeps `student_list` alive during the session.

---

## 🛠️ 9. Refactoring Activity

Look at this unorganized script where everything happens in one block:

```python
# Unorganized script
x = int(input("Enter price: "))
y = int(input("Enter quantity: "))
t = x * y
print("Total:", t)
```

Your task: **Decompose this script into two functions**:
1. `calculate_total(price, quantity)` that returns the multiplication result.
2. `main()` that captures input, calls `calculate_total()`, and prints the output.

---

## 📝 10. Practice Exercises

Try these exercises to sharpen your decomposition skills!

### Beginner
1. **Greeting Function**: Write a function `greet_user(name)` that prints `"Welcome back, <name>!"`. Call it three times with different names.
2. **Grade Calculator Function**: Write a function `calculate_average(score1, score2, score3)` that returns the average of three numbers.

### Intermediate
3. **Product Creator Function**: Write a function `create_product()` that asks the user for a product name and price, returning a dictionary `{"name": ..., "price": ...}`.
4. **Search Function**: Write a function `find_book(book_list, title_query)` that searches a list of book dictionaries and returns `True` if found or `False` otherwise.
5. **Menu Function**: Write a function `show_calculator_menu()` that prints 4 arithmetic choices (`1. Add, 2. Subtract, 3. Multiply, 4. Divide`).

### Challenge
6. **Refactor a Calculator**: Take your Week One Session One simple calculator code and refactor it into clean functions (`add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, `divide(a, b)`, and `main()`).

---

## 🚀 11. Weekly Challenge: Adding Update and Delete

Enhance our `Function-Based Student Management System` by adding two new options to `display_menu()`:
- **5. Update Student**: Ask for a student's name, search `student_list`, and allow updating their age and department.
- **6. Delete Student**: Ask for a student's name, search `student_list`, and remove the matching student dictionary.

💡 **Hint**: To delete an item from a list while looping or after finding it, use `student_list.remove(student)`!

---

## ❓ 12. Review Questions

1. What is Program Decomposition?
2. What is the Single Responsibility Principle?
3. Why should a function return data rather than printing everything directly inside the function?
4. How does passing `student_list` as an argument into `view_students(student_list)` work?
5. What is the purpose of a `main()` controller function?

---

## ✅ 13. Learning Checklist

- [ ] I understand how to break large applications into smaller functions.
- [ ] I can apply the Single Responsibility Principle.
- [ ] I can pass lists and dictionaries into helper functions.
- [ ] I can return dictionaries from builder functions.
- [ ] I can organize menu workflows using a `main()` function.
- [ ] I can build and explain the Function-Based Student Management System.

---

## 🏁 14. Session Summary

- **Program Decomposition** divides complex software into small, manageable functions.
- Each function should have **One Main Responsibility** (displaying, creating, searching, or controlling).
- Passing arguments (`student_list`) and returning values (`create_student()`) connects functions cleanly.
- Coordinating workflow through `main()` resulted in our clean, modular **Function-Based Student Management System**!
