# 📘 Week 4 – Session 2: Text Files and File Paths

In this session, we’ll learn how to **read and write files** in Python.  
File handling allows us to **save data permanently** (so it doesn’t disappear when the program stops running).  
This is essential for real-world applications like **to-do lists, note apps, and user data storage**.

---

## 1. Opening Files

Python provides the built-in `open()` function to work with files.

### Syntax:
```python
file = open("filename", "mode")
```
- "filename" → The name of the file (e.g., "data.txt").

- "mode" → How we want to use the file:

  - "r" → Read (default mode, error if file doesn’t exist).

  - "w" → Write (creates a new file or overwrites existing one).

  - "a" → Append (adds data to the file without deleting existing content).

  - "b" → Binary mode (for images, videos, etc.).

Example:
```
file = open("example.txt", "w")
file.write("Hello, world!")
file.close()
```

---

## 2. Writing to a File
You can use .write() to save text into a file.

### Example:
```
file = open("notes.txt", "w")
file.write("This is my first note.\n")
file.write("Python makes file handling easy!\n")
file.close()
```
✔ This creates a file called notes.txt and writes two lines into it.
✔ If the file already exists, it will overwrite it.

---

## 3. Reading from a File
To read data, we use .read(), .readline(), or .readlines().

### Example: 
Read the entire file
```
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()
```
Read Line by Line
```
file = open("todo.txt", "r")
for line in file:
    print(line.strip())   # strip() removes \n
file.close()
```

---

## 4. Appending to a File
Appending does not remove existing content.

### Example:
```
file = open("notes.txt", "a")
file.write("This is an extra line.\n")
file.close()
```
✔ Now `notes.txt` keeps the old content plus the new line.

---

## 5. Using `with` Statement (Safe File Handling)

Python provides a safe way to handle files using `with`.  
The `with` statement **automatically closes the file** after the block finishes executing — even if an error occurs inside your program!

### Example:
```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```
✔ No need to call `file.close()`.  
✔ Prevents memory leaks and file corruption.

---

## 6. Relative Versus Absolute File Paths

When opening files, Python needs to know **where** the file is located on your computer:

### 1️⃣ Relative Paths
A **relative path** looks for the file starting from the folder where your Python script is currently running:
```python
# Looks in the same folder as the script
with open("notes.txt", "r") as file:
    pass

# Looks inside a subfolder named 'data'
with open("data/students.txt", "r") as file:
    pass
```

### 2️⃣ Absolute Paths
An **absolute path** specifies the exact location from the root of your hard drive:
```python
# Linux / macOS absolute path
with open("/home/user/documents/notes.txt", "r") as file:
    pass

# Windows absolute path
with open("C:\\Users\\user\\Documents\\notes.txt", "r") as file:
    pass
```

> 💡 *Beginners should start with **relative paths** keeping their text files in the same project folder as their Python code.*

---

## 7. Reading and Writing Structured Data (JSON & CSV Preparation)

Instead of plain text, real applications need to save structured data like lists and dictionaries.
While simple `.txt` files work for basic lists, structured records are best stored in **JSON** or **CSV** formats!

### Example: Save To-Do List as JSON
```
import json

tasks = ["Buy milk", "Finish homework", "Go jogging"]

# --- Plain text approach ---
with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")   # write each task on a new line
print("Tasks saved to tasks.txt")


# --- JSON approach ---
with open("tasks.json", "w") as file:
    json.dump(tasks, file)   # save the whole list as JSON
print("Tasks saved to tasks.json")


```
### Example: How to Read it Back?
Saving is just one part. To use the data later, we read it back:
```
import json

# --- Plain text approach ---
with open("tasks.txt", "r") as file:
    tasks_text = file.read().splitlines()

print("From plain text:", tasks_text)


# --- JSON approach ---
with open("todo.json", "r") as file:
    tasks_json = json.load(file)

print("From JSON:", tasks_json)


```

---

## 8. Big Project Part 4 – Save & Load To-Do List App Data
Let’s upgrade our To-Do List App to store tasks permanently in a file.

> 💡 *Note: In Session Three, we will build a Persistent Student Management System that saves records using JSON and CSV files!*

### Step 1: Save tasks to a file
```
def save_tasks(tasks, filename="todo.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
```
### Step 2: Load tasks from a file
```
def load_tasks(filename="todo.txt"):
    try:
        with open(filename, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []   # return empty list if file doesn’t exist

```
### Step 3: Full Example
```
def save_tasks(tasks, filename="todo.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks(filename="todo.txt"):
    try:
        with open(filename, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Main program
tasks = load_tasks()

while True:
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    choice = input("\nOptions: [a]dd, [d]elete, [q]uit → ")

    if choice == "a":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        save_tasks(tasks)

    elif choice == "d":
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            save_tasks(tasks)

    elif choice == "q":
        print("Goodbye! Your tasks are saved.")
        break

```
✔ Now the To-Do List App saves and loads tasks even after the program is closed.
✔ This makes it more like a real application.

---

## 9. Summary

- `open("file.txt", "mode")` → Open a file with read/write/append mode.
- `.write()` → Save text into a file.
- `.read()` / `.readline()` / `.readlines()` → Read data.
- `with open(...)` → Safest way to handle files.
- Relative vs Absolute file paths help organize files across directories.
- We can store structured data like lists using simple text format.
- Our To-Do List App now saves and loads tasks from a file.

---

## 📝 Mini Practice Exercises

  - Create a program that writes 5 favorite movies into a file and then reads them back.

  - Modify the To-Do app so you can delete a task and save changes to the file.

  - Build a "Notes App" that allows adding, viewing, and saving text notes to a file.
