# 📘 Week Seven – Session Three: Project Structure and Clean Code

Welcome back! 👋

Throughout earlier sessions, whenever you built a mini-project or capstone application, you wrote all your functions, classes, and controller loops inside a single file named `main.py` or `app.py`.

While a single file is fine for a 50-line script, imagine stuffing a professional 5,000-line application into one file! Scrolling through endless code to find where a class ends and where a helper function begins becomes exhausting and error-prone.

In this session, you will learn how professional developers structure clean, maintainable Python projects—breaking code across modular files, using **`if __name__ == "__main__":`**, writing helpful docstrings and README documentation, and refactoring our Student Management System into a clean **multi-file architecture**!

---

## 🎯 Learning Objectives

By the end of this session, you will be able to:
- Explain why modular project organization improves readability and team collaboration
- Structure multi-file Python projects separating entry points, models, controllers, and data
- Create custom project modules and import functions and classes across files
- Protect executable scripts using the `if __name__ == "__main__":` idiom
- Write clean, self-documenting code following professional naming guidelines
- Document functions and classes using clear Python docstrings (`"""..."""`)
- Write professional project `README.md` files for GitHub repositories
- Build, run, and explain the multi-file **Organized Student Management System**

---

## 📌 1. Why Project Organization Matters

Think about a well-organized toolbox. Screwdrivers go in one slot, wrenches go in another, and screws are kept in labeled bins.

Software architecture works the same way:
- **Models (`student.py`)**: Define the structure of individual data records.
- **Controllers (`student_manager.py`)**: Manage file storage and collections.
- **Entry Points (`main.py`)**: Handle user menus and launch the application.

---

## 🏗️ 2. From One File to Multiple Files

Let us trace the evolution of our application directory:

### Beginner Single-File Structure:
```text
student-project/
└── main.py       <-- Everything (classes, file saving, menu loop) jammed together!
```

### Professional Multi-File Structure:
```text
student-management-system/
│
├── main.py               <-- Entry point running CLI menu loop
├── student.py            <-- Student and User class definitions
├── student_manager.py    <-- StudentManager controller class
├── data/
│   └── students.json     <-- Isolated persistent data folder
├── tests/                <-- Automated test folder (Week Eight!)
├── README.md             <-- Documentation explaining how to run the app
├── requirements.txt      <-- Package dependency list
└── .gitignore            <-- Git exclusion rules
```

Every item has a clear, dedicated purpose!

---

## 🧩 3. Creating Custom Modules

Any `.py` file you create in your project folder is automatically a **Module** that other files can import!

Let us create a helper module named `calculations.py`:

```python
# calculations.py
def calculate_average(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)
```

Now, inside `main.py`, we import our custom module:

```python
# main.py
from calculations import calculate_average

student_scores = [88, 92, 95]
avg = calculate_average(student_scores)
print("Average score:", round(avg, 2))
```

---

## 🚪 4. The `if __name__ == "__main__":` Entry Guard

When you import a module in Python, Python executes all top-level code inside that module immediately. To prevent code from executing unexpectedly during imports, we protect script entry points using **`if __name__ == "__main__":`**:

```python
def main():
    print("Application started.")


if __name__ == "__main__":
    main()
```

### Why does this work?
- When you run `python main.py` directly from your terminal, Python sets the special `__name__` variable to `"__main__"`, so `main()` runs.
- If another script imports your file (`import main`), `__name__` is set to the filename (`"main"`), so `main()` is safely skipped!

---

## 🏷️ 5. Clean Naming Guidelines

Readable variable and function names act as live documentation:

```python
# ❌ Bad Naming (Cryptic and confusing):
def pr(l):
    for x in l:
        print(x)

# ✅ Good Naming (Clear and descriptive):
def print_student_names(student_list):
    for student in student_list:
        print(student.name)
```

---

## 💬 6. Comments vs. Docstrings

- **Comments (`#`)**: Explain *why* tricky logic was written a certain way. Do not write comments stating the obvious!
- **Docstrings (`"""..."""`)**: Placed immediately below function or class definitions to explain *what* the function does, its parameters, and return values.

```python
def calculate_discount(price, percent):
    """
    Calculates discounted final price.
    
    Parameters:
        price (float): Original item price.
        percent (float): Discount percentage (0-100).
    """
    return price * (1 - percent / 100)
```

---

## 🎨 7. Formatting and PEP 8 Basics

Python has an official readability style guide called **PEP 8**. Here are three essential rules to follow:
1. **4 spaces** per indentation level (never mix tabs and spaces!).
2. Use **`snake_case`** for function and variable names (`calculate_average`).
3. Use **`PascalCase`** for class names (`StudentManager`).

---

## 📖 8. Writing Professional README Files

Every GitHub repository needs a `README.md` file! A great project README should include:
- **Project Name & Description**
- **Features List**
- **Requirements (`requirements.txt`)**
- **How to Run Instructions**
- **Author Information**

---

## 🛠️ 9. Weekly Project: Organize the Student Management System

Let us refactor our Week Six Object-Oriented Student Management System into a professional multi-file project!

### File 1: `student.py` (Data Model)
```python
# student.py
class User:
    """Parent class representing a general system user."""
    def __init__(self, name):
        self.name = name


class Student(User):
    """Child class representing an individual student record."""
    def __init__(self, name, age, department):
        super().__init__(name)
        self.age = age
        self.department = department

    def to_dict(self):
        """Converts object into dictionary for JSON serialization."""
        return {
            "name": self.name,
            "age": self.age,
            "department": self.department
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Student instance from a dictionary read from disk."""
        return cls(data["name"], data["age"], data["department"])

    def display_info(self):
        """Prints formatted student profile."""
        print(f"Name: {self.name} | Age: {self.age} | Department: {self.department}")
```

### File 2: `student_manager.py` (Controller)
```python
# student_manager.py
import json
import os
from student import Student


class StudentManager:
    """Controller responsible for managing student collections and disk persistence."""
    def __init__(self, filename="data/students.json"):
        self.filename = filename
        self.students = []
        self.ensure_data_directory()
        self.load_from_disk()

    def ensure_data_directory(self):
        """Ensures the 'data/' folder exists."""
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

    def load_from_disk(self):
        """Loads JSON data from disk."""
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r") as file:
                data_list = json.load(file)
                self.students = [Student.from_dict(item) for item in data_list]
        except Exception as e:
            print(f"⚠️ Could not load data file: {e}")

    def save_to_disk(self):
        """Serializes student objects to JSON file."""
        try:
            data_list = [student.to_dict() for student in self.students]
            with open(self.filename, "w") as file:
                json.dump(data_list, file, indent=4)
            print("💾 Student records saved to disk!")
        except Exception as e:
            print(f"❌ Save error: {e}")

    def add_student(self, name, age, department):
        new_student = Student(name, age, department)
        self.students.append(new_student)
        print(f"✅ Registered student '{name}'.")

    def view_all(self):
        print("\n--- Registered Student Profiles ---")
        if not self.students:
            print("No students registered.")
            return
        for idx, student in enumerate(self.students, start=1):
            print(f"{idx}. ", end="")
            student.display_info()
```

### File 3: `main.py` (Application Entry Point)
```python
# main.py
from student_manager import StudentManager


def display_menu():
    print("\n==========================================")
    print("  MULTI-FILE STUDENT MANAGEMENT SYSTEM    ")
    print("==========================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Save Students")
    print("4. Exit")
    print("==========================================")


def main():
    manager = StudentManager()

    while True:
        display_menu()
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            age = int(input("Enter age: "))
            dept = input("Enter department: ").strip()
            manager.add_student(name, age, dept)
        elif choice == "2":
            manager.view_all()
        elif choice == "3":
            manager.save_to_disk()
        elif choice == "4":
            manager.save_to_disk()
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
```

---

## 📋 10. Project Review Checklist

Before publishing any Python repository to GitHub, verify:
- [ ] Code is separated into logical modules (`student.py`, `student_manager.py`, `main.py`).
- [ ] Entry point is protected with `if __name__ == "__main__":`.
- [ ] Functions and classes have clear docstrings.
- [ ] `.gitignore` excludes `.venv/` and `__pycache__/`.
- [ ] `README.md` explains clearly how to run the application.

---

## 📝 11. Practice Exercises

Try these refactoring exercises!

### Beginner
1. **Module Separation**: Create a file named `greeter.py` defining a function `say_hello(name)`. Create a separate file `app.py` that imports and runs `say_hello("Abel")`.
2. **Entry Guard**: Add `if __name__ == "__main__":` to `app.py` and run it from your terminal.

### Intermediate
3. **Docstring Practice**: Write a docstring for your `calculate_average` function explaining parameters and return values.
4. **README Creation**: Write a Markdown `README.md` file for your Student Management System.

### Challenge
5. **Folder Hierarchy**: Reorganize your project so data files are automatically saved inside a dedicated `data/` subdirectory!

---

## 🚀 12. Weekly Challenge: Organize a Contact Book

Take your Contact Book or Expense Tracker project and organize it into clean multi-file architecture (`models.py`, `services.py`, `main.py`, `README.md`, and `.gitignore`).

---

## ❓ 13. Review Questions

1. Why should large applications be split across multiple `.py` files?
2. What is the purpose of `if __name__ == "__main__":`?
3. What is the difference between a inline comment (`#`) and a docstring (`"""..."""`)?
4. What information should always be included in a GitHub `README.md` file?
5. How does `from student import Student` work across files in the same folder?

---

## ✅ 14. Learning Checklist

- [ ] I understand how to structure professional multi-file Python projects.
- [ ] I can import custom modules across project files.
- [ ] I can protect script entry points using `if __name__ == "__main__":`.
- [ ] I can write self-documenting code with clear docstrings.
- [ ] I can build and explain the multi-file Organized Student Management System.

---

## 🏁 15. Session Summary

- **Modular Project Structure** separates models, controllers, and entry points into clean files.
- **`if __name__ == "__main__":`** prevents unintended execution when importing modules.
- Refactoring our capstone into `student.py`, `student_manager.py`, and `main.py` gave our project professional software engineering architecture!
