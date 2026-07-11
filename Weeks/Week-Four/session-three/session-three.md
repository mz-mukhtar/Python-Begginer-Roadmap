# 📘 Week Four – Session Three: JSON, CSV, and Persistent Applications

Welcome back! 👋

In Sessions One and Two of Week Four, you learned how to manipulate strings in depth and read/write plain text files (`.txt`) using the safe `with open(...)` context manager.

Up until now, every time you closed your Python application, all the student records stored inside your `student_list` vanished into thin air! Remember:
> **Programs normally lose information when they stop unless the information is saved to persistent disk storage.**

While plain text files are great for writing notes or paragraphs, storing structured records (like lists of dictionaries) inside a `.txt` file requires manual parsing. In this session, you will learn how to save and load structured application data automatically using **JSON** (`.json`) and **CSV** (`.csv`) formats, and build our **Persistent Student Management System**!

---

## 🎯 Learning Objectives

By the end of this session, you will be able to:
- Explain what data persistence is and why structured file formats are necessary
- Describe the structure of JSON (JavaScript Object Notation) and how it maps to Python
- Save Python lists and dictionaries to disk using `json.dump()`
- Load structured JSON files back into Python using `json.load()`
- Read and write spreadsheet-compatible table data using Python's `csv` module
- Compare JSON vs. CSV and choose the right format for any project
- Build, run, and explain the **Persistent Student Management System** project

---

## 📌 1. What Is JSON?

**JSON** stands for **JavaScript Object Notation**. Despite its name, JSON is a universal file format supported by almost every modern programming language!

Here is what a JSON file looks like:

```json
[
    {
        "name": "Abel",
        "age": 20,
        "department": "Engineering"
    },
    {
        "name": "Sara",
        "age": 19,
        "department": "Computer Science"
    }
]
```

Notice how familiar this looks? JSON syntax is nearly identical to Python dictionaries and lists!

| Python Data Structure | Equivalent JSON Structure |
| :--- | :--- |
| **Dictionary** (`{"key": "val"}`) | **Object** (`{"key": "val"}`) |
| **List** (`["a", "b"]`) | **Array** (`["a", "b"]`) |
| **String** (`"text"`) | **String** (`"text"`) |
| **Number** (`42`, `3.14`) | **Number** (`42`, `3.14`) |
| **Boolean** (`True`, `False`) | **Boolean** (`true`, `false` lowercase) |

---

## 📥 2. Importing `json`

Python includes a built-in module for working with JSON files. To use it, simply add an import statement at the very top of your script:

```python
import json
```

---

## 💾 3. Saving Data With `json.dump()`

To save a Python list or dictionary directly into a `.json` file, we open the file in write mode (`"w"`) and call `json.dump()`:

```python
import json

student_list = [
    {
        "name": "Abel",
        "age": 20,
        "department": "Engineering"
    }
]

with open("students.json", "w") as file:
    json.dump(student_list, file, indent=4)

print("✅ Student records saved to students.json!")
```

🔍 **Breakdown**:
- `student_list`: The Python data structure we want to save.
- `file`: The open file handle returned by `with open(...)`.
- `indent=4`: Formats the JSON file with 4 spaces of indentation so it is clean and readable for humans!

---

## 📂 4. Loading Data With `json.load()`

To read a `.json` file from disk back into live Python dictionaries and lists, open the file in read mode (`"r"`) and call `json.load()`:

```python
import json
import os

filename = "students.json"

# Check if file exists before opening (safe initialization without exceptions!)
if os.path.exists(filename):
    with open(filename, "r") as file:
        loaded_students = json.load(file)
    print("✅ Successfully loaded students from disk:")
    print(loaded_students)
else:
    print("No existing data file found. Starting with an empty list.")
    loaded_students = []
```

*(Note: We check `os.path.exists()` here to prevent missing-file crashes. Next week in Week Five, you will learn how to handle file errors elegantly using `try` and `except`!)*

---

## 📄 5. JSON File Content Example

If you open `students.json` in your code editor after running `json.dump()`, you will see:

```json
[
    {
        "name": "Abel",
        "age": 20,
        "department": "Engineering"
    }
]
```

---

## 📊 6. Introduction to CSV

**CSV** stands for **Comma-Separated Values**. It is a standard plain-text format used by spreadsheet applications like Microsoft Excel and Google Sheets!

In a CSV file:
- Each line represents one **Row** of data.
- Values are separated by commas (columns).
- The first line is usually a **Header row** describing the columns.

Example `students.csv`:
```csv
name,age,department
Abel,20,Engineering
Sara,19,Computer Science
```

---

## 📥 7. The `csv` Module

Python also provides a built-in module for reading and writing CSV files:

```python
import csv
```

---

## ✍️ 8. Writing CSV Files With `csv.DictWriter`

Because our student records are stored as dictionaries, Python's `csv.DictWriter` makes exporting to CSV seamless:

```python
import csv

student_list = [
    {"name": "Abel", "age": 20, "department": "Engineering"},
    {"name": "Sara", "age": 19, "department": "Computer Science"}
]

fieldnames = ["name", "age", "department"]

with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()      # Writes: name,age,department
    writer.writerows(student_list)  # Writes all dictionary rows

print("✅ Successfully exported to students.csv!")
```

*(Note: `newline=""` prevents Windows from adding extra blank lines between rows.)*

---

## 📖 9. Reading CSV Files With `csv.DictReader`

To read a CSV file row by row where each row becomes a dictionary:

```python
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "is in", row["department"])
```

---

## ⚖️ 10. JSON Versus CSV: Which Should You Use?

| Feature | JSON (`.json`) | CSV (`.csv`) |
| :--- | :--- | :--- |
| **Structure Supported** | Nested dictionaries, lists, booleans, integers | Flat tables (rows and columns only) |
| **Data Types** | Preserves numbers (`20`) vs strings (`"20"`) | Everything is read as text strings |
| **Excel / Spreadsheet Support** | Requires conversion | Opens natively in Excel / Google Sheets |
| **Best Used For** | Application save files, config files, web APIs | Reports, data exports, spreadsheet sharing |

---

## 🛠️ 11. Weekly Project: Persistent Student Management System

Let us upgrade our Week Three application by adding automatic JSON loading, saving, and CSV exporting to build the **Persistent Student Management System**!

### 📋 Required Features
1. **Add Student**: Adds a record to `student_list`.
2. **View Students**: Displays all profiles.
3. **Search Student**: Finds a student by name.
4. **Save Students**: Writes `student_list` to `students.json`.
5. **Export Students to CSV**: Exports table report to `students.csv`.
6. **Exit**: Saves automatically before closing!

### Complete Runnable Code

```python
# ==========================================
# Project: Persistent Student Management System
# Week Four Capstone Project
# ==========================================

import json
import csv
import os

DATA_FILE = "students.json"
CSV_FILE = "students_export.csv"


def load_students():
    """Loads student records from JSON disk file safely."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []


def save_students(student_list):
    """Saves student records to JSON disk file."""
    with open(DATA_FILE, "w") as file:
        json.dump(student_list, file, indent=4)
    print(f"\n💾 Data successfully saved to '{DATA_FILE}'!")


def export_to_csv(student_list):
    """Exports student records into a spreadsheet-compatible CSV report."""
    if not student_list:
        print("\n❌ No student records available to export.")
        return

    fieldnames = ["name", "age", "department"]
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(student_list)
    print(f"\n📊 Successfully exported report to '{CSV_FILE}'!")


def display_menu():
    """Displays the interactive application menu."""
    print("\n==========================================")
    print("   PERSISTENT STUDENT MANAGEMENT SYSTEM   ")
    print("==========================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Save Students to JSON")
    print("5. Export Students to CSV")
    print("6. Exit & Save")
    print("==========================================")


def add_student(student_list):
    """Creates a new student profile and appends it to the list."""
    name = input("Enter student name: ").strip()
    age = int(input("Enter student age: "))
    department = input("Enter student department: ").strip()

    student = {
        "name": name,
        "age": age,
        "department": department
    }
    student_list.append(student)
    print(f"✅ Student '{name}' added successfully!")


def view_students(student_list):
    """Displays all registered student profiles."""
    print("\n--- Registered Student Profiles ---")
    if not student_list:
        print("No students registered yet.")
        return

    for index, student in enumerate(student_list, start=1):
        print(f"{index}. Name: {student['name']} | Age: {student['age']} | Department: {student['department']}")


def search_student(student_list):
    """Searches for a student by name."""
    query = input("\nEnter student name to search: ").strip().lower()
    for student in student_list:
        if student["name"].lower() == query:
            print(f"\n✅ Found: {student['name']} (Age: {student['age']}, Dept: {student['department']})")
            return
    print(f"\n❌ No student found matching '{query}'.")


def main():
    """Main controller loop with automatic disk loading and saving."""
    print("Initializing application...")
    student_list = load_students()
    print(f"Loaded {len(student_list)} existing student record(s) from disk.")

    while True:
        display_menu()
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            add_student(student_list)
        elif choice == "2":
            view_students(student_list)
        elif choice == "3":
            search_student(student_list)
        elif choice == "4":
            save_students(student_list)
        elif choice == "5":
            export_to_csv(student_list)
        elif choice == "6":
            save_students(student_list)
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid selection. Please enter 1-6.")


# Start application
main()
```

---

## 📝 12. Practice Exercises

Try these exercises to test your file storage mastery!

### Beginner
1. **Save List to JSON**: Create a list `colors = ["Red", "Green", "Blue"]` and save it to a file named `colors.json` using `json.dump()`.
2. **Load JSON**: Write a script that reads `colors.json` using `json.load()` and prints every color inside a `for` loop.

### Intermediate
3. **Save Contact Book**: Create a list of dictionaries where each dictionary represents a contact (`name`, `phone`). Save it to `contacts.json`.
4. **Create CSV Grade File**: Write a script that writes 3 student grade dictionaries (`name`, `score`) into a file named `grades.csv`.

### Challenge
5. **Read Product Info From CSV**: Create a CSV file `products.csv` with header `product,price`. Read the file using `csv.DictReader`, convert each price string to `float`, and calculate the total cost of all products.

---

## 🚀 13. Weekly Challenge: Expense Tracker Data Storage

Build a **Persistent Expense Tracker** application!
- Ask the user to input expenses (`description`, `category`, `amount`).
- Store all expenses in a Python list of dictionaries.
- Automatically save every new expense to `expenses.json` using `json.dump()`.
- When the program starts, automatically load `expenses.json` so previous spending is preserved!

---

## ❓ 14. Review Questions

1. Why do in-memory variables disappear when a Python program exits?
2. What Python function writes data structure objects into a `.json` file?
3. What Python function reads a `.json` file back into Python dictionaries/lists?
4. What is the purpose of the `indent=4` argument in `json.dump()`?
5. When should you choose CSV format over JSON format?

---

## ✅ 15. Learning Checklist

- [ ] I understand the importance of persistent data storage.
- [ ] I can save Python dictionaries and lists to `.json` files.
- [ ] I can load `.json` files into live Python applications.
- [ ] I can export table reports using `csv.DictWriter`.
- [ ] I can build and explain the Persistent Student Management System.

---

## 🏁 16. Session Summary

- **JSON (`.json`)** preserves complex data structures (lists and dictionaries) exactly as they appear in Python.
- **CSV (`.csv`)** formats tabular data into spreadsheet-friendly rows and columns.
- Integrating `json.load()` at application startup and `json.dump()` upon shutdown gave our **Persistent Student Management System** permanent memory!
