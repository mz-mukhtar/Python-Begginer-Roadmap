# 🐍 Python Beginner Cheat Sheet

This quick-reference cheat sheet summarizes essential Python syntax, data types, operators, collections, functions, file handling, Object-Oriented Programming (OOP), and development tools covered across all 8 weeks of the course.

---

## 1. Running Python

Run a Python script from your terminal:

```bash
python file_name.py
```

> **Note**: On Linux or macOS systems, you may need to use `python3`:

```bash
python3 file_name.py
```

---

## 2. Comments

Comments are notes ignored by Python during execution:

```python
# This is a comment explaining the code below
```

---

## 3. Printing

Display text or variable values in the terminal:

```python
print("Hello, Python!")
```

---

## 4. Variables

Variables store data values in memory:

```python
student_name = "Sara"
student_age = 20
student_average = 85.5
is_active = True
```

### Primitive Data Types

| Type | Description | Example |
| --- | --- | --- |
| **String (`str`)** | Text wrapped in quotes | `"Sara"`, `'Engineering'` |
| **Integer (`int`)** | Whole numbers without decimals | `20`, `100`, `-5` |
| **Float (`float`)** | Decimal numbers | `85.5`, `3.14159` |
| **Boolean (`bool`)** | Logical values | `True`, `False` |

---

## 5. Getting User Input

Capture keyboard input from the user:

```python
student_name = input("Enter your name: ")
```

> **Important**: `input()` **always** returns text as a string (`str`).

---

## 6. Type Conversion

Convert values between different data types:

```python
int("20")       # Converts string to integer: 20
float("85.5")   # Converts string to float: 85.5
str(100)        # Converts integer to string: "100"
```

Example converting numeric input immediately:

```python
student_age = int(input("Enter your age: "))
```

---

## 7. Arithmetic Operators

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division (Float) | `10 / 4` | `2.5` |
| `//` | Floor Division | `10 // 4` | `2` |
| `%` | Modulo (Remainder) | `10 % 3` | `1` |
| `**` | Exponentiation (Power) | `2 ** 3` | `8` |

---

## 8. Comparison Operators

Comparison operators evaluate two values and return a boolean (`True` or `False`):

```text
==      Equal to
!=      Not equal to
>       Greater than
<       Less than
>=      Greater than or equal to
<=      Less than or equal to
```

---

## 9. Logical Operators

Combine multiple boolean expressions:

```text
and     Returns True only if BOTH expressions are True
or      Returns True if AT LEAST ONE expression is True
not     Inverts the boolean value (True becomes False, False becomes True)
```

---

## 10. Conditions

Branch program logic based on conditions:

```python
if student_score >= 50:
    print("Pass")
elif student_score >= 40:
    print("Retake")
else:
    print("Fail")
```

---

## 11. While Loops

Repeat a block of code as long as a condition remains `True`:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## 12. For Loops

Iterate over a sequence or a range of numbers:

```python
for number in range(1, 6):
    print(number)
```

---

## 13. Lists

Ordered, mutable collections of items:

```python
student_names = ["Sara", "Abel", "Miki"]
```

### Common List Methods
```text
append(item)    Adds an item to the end of the list
insert(idx, i)  Inserts an item at index idx
remove(item)    Removes the first occurrence of item
pop()           Removes and returns the last item
sort()          Sorts list items in ascending order
reverse()       Reverses the order of items
count(item)     Counts occurrences of item
```

---

## 14. Tuples

Ordered, **immutable** (unchangeable) collections:

```python
student_information = ("Sara", 20, "Engineering")
```

> **Beginner Tip**: Tuples normally store information that should not change during execution.

---

## 15. Dictionaries

Key-value pairings storing structured records:

```python
student = {
    "name": "Sara",
    "age": 20
}
```

### Common Dictionary Methods
```text
get(key)        Safely retrieves value for key (returns None if not found)
keys()          Returns all dictionary keys
values()        Returns all dictionary values
items()         Returns all key-value pairs as tuples
pop(key)        Removes key and returns its value
```

---

## 16. Sets

Unordered collections of **unique** values:

```python
departments = {"Engineering", "Computer Science"}
```

### Common Set Methods
```text
add(item)       Adds unique item to the set
remove(item)    Removes item (raises KeyError if missing)
discard(item)   Safely removes item without error if missing
```

---

## 17. Functions

Define reusable blocks of code:

```python
def greet_student(student_name):
    print(f"Welcome, {student_name}!")
```

---

## 18. Returning Values

Send calculated data back to the caller:

```python
def calculate_average(total_score, subject_count):
    return total_score / subject_count
```

---

## 19. Default Parameters

Provide default values when arguments are omitted:

```python
def greet_student(student_name, course="Python"):
    print(student_name, course)
```

---

## 20. String Methods

Useful methods for manipulating strings:

```text
lower()         Converts all characters to lowercase
upper()         Converts all characters to uppercase
title()         Capitalizes the first letter of each word
capitalize()    Capitalizes only the very first letter
strip()         Removes leading and trailing whitespace
replace(a, b)   Replaces occurrences of substring a with b
split(sep)      Splits string into a list using separator sep
join(list)      Joins list elements into a single string
find(sub)       Returns index of first occurrence of sub (-1 if missing)
count(sub)      Counts non-overlapping occurrences of sub
isdigit()       Returns True if all characters are digits (0-9)
isalpha()       Returns True if all characters are letters
isalnum()       Returns True if all characters are alphanumeric
```

---

## 21. Files

Safely handle text files using `with open()` context managers:

### Reading a File
```python
with open("students.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

### Writing a File (Overwrites existing content)
```python
with open("students.txt", "w", encoding="utf-8") as file:
    file.write("Sara")
```

### Appending to a File
```python
with open("students.txt", "a", encoding="utf-8") as file:
    file.write("\nAbel")
```

---

## 22. JSON

Serialize and deserialize structured dictionary records to local JSON files:

### Saving JSON
```python
import json

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(student_list, file, indent=4)
```

### Loading JSON
```python
import json

with open("students.json", "r", encoding="utf-8") as file:
    student_list = json.load(file)
```

---

## 23. CSV

Write tabular spreadsheet data using Python's `csv` module:

```python
import csv

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Score"])
    writer.writerow(["STU-001", "Sara", 92])
```

---

## 24. Error Handling

Catch and handle exceptions gracefully to prevent application crashes:

```python
try:
    student_age = int(input("Enter age: "))
except ValueError:
    print("Enter a valid number.")
```

### Common Exceptions
```text
ValueError          Raised when a function receives an invalid value type
TypeError           Raised when an operation is applied to an inappropriate type
NameError           Raised when using an undefined variable name
IndexError          Raised when accessing a list index out of range
KeyError            Raised when looking up a missing dictionary key
FileNotFoundError   Raised when trying to open a file that does not exist
ZeroDivisionError   Raised when attempting to divide a number by zero
```

---

## 25. Modules

Import standard library utilities or your own custom Python files:

```python
import math
from datetime import datetime
from calculations import calculate_average
```

---

## 26. Logging

Record diagnostic events and application workflow history:

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logging.info("Student application started successfully.")
```

---

## 27. Classes

Define Object-Oriented blueprints combining attributes and behaviors:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display_information(self):
        print(self.name)
```

---

## 28. Inheritance

Create specialized child classes extending parent functionality:

```python
class User:
    def __init__(self, name):
        self.name = name

class Student(User):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major
```

---

## 29. Virtual Environments

Create an isolated environment for project dependencies:

### Create Virtual Environment
```bash
python -m venv .venv
```

### Activate on Linux/macOS
```bash
source .venv/bin/activate
```

### Activate on Windows PowerShell
```powershell
.venv\Scripts\Activate.ps1
```

---

## 30. Installing Packages

Install external Python packages using `pip`:

```bash
python -m pip install requests
```

---

## 31. Git Commands

Short summary of essential version control commands:

```bash
git status              # Check modified files
git add .               # Stage all changes
git commit -m "Message" # Save snapshot with descriptive message
git push                # Upload commits to remote GitHub repository
```

---

## 32. API Requests

Fetch web resources and JSON payloads from external REST APIs:

```python
import requests

response = requests.get(api_url, timeout=10)
if response.status_code == 200:
    data = response.json()
```

---

## 33. Unit Testing

Write automated tests using Python's built-in `unittest` framework:

```python
import unittest

class TestCalculations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(10 + 5, 15)

if __name__ == "__main__":
    unittest.main()
```

---

## 34. Helpful Python Tips

💡 **Best Practices for Beginners:**
1. **Read errors from the bottom**: Tracebacks explain the failure reason on the very last line.
2. **Check indentation**: Python relies strictly on consistent 4-space indentation levels.
3. **Use clear names**: Choose meaningful variable and function names (`calculate_total` instead of `x`).
4. **Test one feature at a time**: Don't write 200 lines before testing. Run your program frequently after every small change.
5. **Save work often**: Always save modified `.py` files before executing them in the terminal.
6. **Commit changes with Git**: Save logical checkpoints so you can revert if something breaks.
7. **Practice without copying**: Type code out manually rather than copy-pasting so you build muscle memory.
