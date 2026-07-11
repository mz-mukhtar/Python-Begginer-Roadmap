# ⚠️ Common Python Errors and How to Fix Them

> Errors are a normal part of programming. Every programmer sees errors. The important skill is learning how to read and fix them.

When your program stops and displays an error traceback, do not worry! Python is simply telling you what happened and where it encountered a problem so you can fix it.

---

## How to Read an Error

Whenever Python encounters a failure, it prints a **traceback report** to the terminal. Always look for four key elements:
1. **File name**: The exact file where the error happened.
2. **Line number**: The specific line of code that triggered the failure.
3. **Error type**: The category of exception raised (`ValueError`, `SyntaxError`, etc.).
4. **Error message**: The detailed description explaining why the failure occurred.

### Example Traceback
```text
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    student_age = int(input("Enter age: "))
ValueError: invalid literal for int() with base 10: 'abc'
```

> **Beginner Tip**: Start reading from the final line because it normally tells you the error type.

---

## Common Errors

### SyntaxError

- **Meaning**: Python cannot understand the grammatical structure of your code.
- **Example**:
  ```python
  print("Hello"
  ```
- **Why It Happens**: You forgot a closing parenthesis `)`, bracket `]`, brace `}`, quotation mark `"`, or colon `:` at the end of a statement.
- **How to Fix It**: Check the end of the line (or the line immediately above the reported error number) and ensure all punctuation marks and brackets match correctly.
- **Beginner Tip**: Editors like VS Code often highlight unmatched brackets with colored underlines.

---

### IndentationError

- **Meaning**: The code indentation does not follow Python's block structure rules.
- **Example**:
  ```python
  def greet():
  print("Hello")
  ```
- **Why It Happens**: Code inside a function, `if` statement, or loop was not indented, or you mixed tabs and spaces.
- **How to Fix It**: Indent all code blocks consistently using 4 spaces per indentation level.
- **Beginner Tip**: Configure your editor to automatically convert tabs to spaces.

---

### NameError

- **Meaning**: You attempted to use a variable or function name that has not been defined yet.
- **Example**:
  ```python
  print(student_score)
  ```
- **Why It Happens**: You misspelled the variable name, forgot to assign it before using it, or tried to access a local function variable outside its scope.
- **How to Fix It**: Check variable spelling carefully and ensure the variable is defined before calling it.
- **Beginner Tip**: Python is case-sensitive (`Score` and `score` are completely different variables).

---

### TypeError

- **Meaning**: An operation or function was applied to an incompatible data type.
- **Example**:
  ```python
  print("Age: " + 20)
  ```
- **Why It Happens**: You tried to concatenate a string with an integer directly, or called a non-callable object.
- **How to Fix It**: Convert incompatible types explicitly using `str()`, `int()`, or format strings (`f"Age: {20}"`).
- **Beginner Tip**: Use `type(variable)` to inspect what data type you are working with.

---

### ValueError

- **Meaning**: A function received an argument with the right data type but an inappropriate or invalid value.
- **Example**:
  ```python
  number = int("abc")
  ```
- **Why It Happens**: You tried to convert non-numeric letters into an integer or float.
- **How to Fix It**: Wrap user input conversion inside a `try`/`except ValueError` block or validate the text first using `.isdigit()`.
- **Beginner Tip**: Always expect end users to type letters accidentally when asked for numbers.

---

### ZeroDivisionError

- **Meaning**: Your code attempted to divide a number by zero (`0`).
- **Example**:
  ```python
  average = total_score / 0
  ```
- **Why It Happens**: A divisor variable or count variable reached `0` during division calculations.
- **How to Fix It**: Check if the divisor is greater than `0` before performing the division:
  ```python
  if count > 0:
      average = total / count
  ```
- **Beginner Tip**: Empty lists have a length (`len()`) of `0`. Always verify lists aren't empty before calculating averages!

---

### IndexError

- **Meaning**: You tried to access an item at a list or tuple index that does not exist.
- **Example**:
  ```python
  items = ["Sara", "Abel"]
  print(items[5])
  ```
- **Why It Happens**: List indexes are 0-indexed (`0` to `len(items) - 1`). Asking for index `5` in a 2-item list exceeds the range.
- **How to Fix It**: Make sure your index is strictly less than `len(items)`.
- **Beginner Tip**: Remember that the last item in a list is at index `len(items) - 1` or `-1`.

---

### KeyError

- **Meaning**: You tried to access a dictionary value using a key that does not exist in the dictionary.
- **Example**:
  ```python
  student = {"name": "Sara"}
  print(student["email"])
  ```
- **Why It Happens**: The requested dictionary key is missing or misspelled.
- **How to Fix It**: Use the `.get("email", "Not Provided")` method or check `if "email" in student:` first.
- **Beginner Tip**: `.get()` returns `None` (or a fallback default) instead of crashing your program.

---

### FileNotFoundError

- **Meaning**: Python could not find the specified file path on your hard drive.
- **Example**:
  ```python
  with open("missing_file.txt", "r") as f:
      content = f.read()
  ```
- **Why It Happens**: The file name is misspelled, or your terminal's current working directory is different from where the file is stored.
- **How to Fix It**: Check the file spelling and use `pathlib.Path` or absolute paths when opening files.
- **Beginner Tip**: Run `pwd` (Linux/macOS) or `cd` (Windows) in your terminal to see which directory you are currently working in.

---

### ModuleNotFoundError

- **Meaning**: Python cannot find the external module or package you are trying to import.
- **Example**:
  ```python
  import requests
  ```
- **Why It Happens**: The third-party package has not been installed yet, or your virtual environment is not activated.
- **How to Fix It**: Run `python -m pip install <package_name>` inside your activated virtual environment.
- **Beginner Tip**: Check `pip list` to see all packages currently installed in your environment.

---

### AttributeError

- **Meaning**: You tried to access an attribute or call a method that does not exist on that object.
- **Example**:
  ```python
  name = "Sara"
  name.append("X")
  ```
- **Why It Happens**: You called a list method (`append`) on a string (`str`), or misspelled an object method name.
- **How to Fix It**: Check the object's data type and verify the method name spelling.
- **Beginner Tip**: Use the `dir(object)` function or Python documentation to see valid methods for an object.

---

### JSONDecodeError

- **Meaning**: Python's `json.load()` failed to parse invalid or corrupted JSON data (`json.JSONDecodeError`).
- **Example**:
  ```python
  import json
  # When students.json contains incomplete text or trailing commas
  with open("students.json", "r") as f:
      data = json.load(f)
  ```
- **Why It Happens**: The JSON file is empty, has syntax errors (like single quotes instead of double quotes), or has trailing commas.
- **How to Fix It**: Catch `json.JSONDecodeError` and return an empty default list or dictionary safely.
- **Beginner Tip**: Valid JSON requires double quotation marks around all string keys and values.

---

### ImportError

- **Meaning**: Python found the module file but could not import the specific function or class name requested.
- **Example**:
  ```python
  from math import calculate_sum
  ```
- **Why It Happens**: The function name does not exist inside that module, or you have circular imports between two files.
- **How to Fix It**: Verify the exact function or class name exported by the module.
- **Beginner Tip**: Avoid naming your personal script files after built-in modules (e.g., never name your file `math.py` or `random.py`).

---

## Git and Environment Problems

### `python` command not found
- **Why It Happens**: Python is not installed on your system PATH, or your OS uses `python3` instead of `python`.
- **How to Fix It**: Try typing `python3 --version`. If installed, use `python3`. Otherwise, reinstall Python and check the box **"Add Python to PATH"**.

### `pip` command not found
- **Why It Happens**: Pip was not included in your PATH configuration.
- **How to Fix It**: Run `python -m pip --version` or `python3 -m pip --version` directly through Python.

### Package installed but cannot be imported
- **Why It Happens**: You installed the package into your global system Python instead of your active virtual environment.
- **How to Fix It**: Activate your project's virtual environment first (`source .venv/bin/activate`), then run `pip install -r requirements.txt`.

### Virtual environment not activated
- **Why It Happens**: You opened a new terminal window and forgot to activate the environment.
- **How to Fix It**: Look for `(.venv)` at the start of your command prompt line. If missing, run the activation script before executing your app.

### Wrong working directory
- **Why It Happens**: You ran `python main.py` while located in the parent root folder rather than inside the project directory.
- **How to Fix It**: Use `cd Projects/weekly-projects/week-four/` before running your program.

### File path not found
- **Why It Happens**: Relative file paths depend on where the terminal command was launched.
- **How to Fix It**: Use `pathlib.Path(__file__).parent` to construct paths relative to your Python script location.

---

## Debugging Checklist

Before asking for help, run through this systematic debugging checklist:

```text
[ ] Read the final error line
[ ] Find the line number
[ ] Check spelling
[ ] Check indentation
[ ] Check quotation marks
[ ] Check parentheses
[ ] Check variable names
[ ] Check data types
[ ] Print values temporarily
[ ] Test one small part
[ ] Run the program again
```

---

## How to Ask for Help

When you get stuck and need to ask an instructor, classmate, or online community for help, always provide these five clear details:
1. **Error message**: Copy and paste the full traceback message.
2. **Relevant code**: Include the exact function or lines around where the error occurred.
3. **Expected result**: Explain what you wanted the program to do.
4. **Actual result**: Explain what happened instead.
5. **What you already tried**: Mention what steps or edits you tested so far.

> **CRITICAL SAFETY RULE**: Never share passwords, API keys, tokens, or private information when asking for help.
