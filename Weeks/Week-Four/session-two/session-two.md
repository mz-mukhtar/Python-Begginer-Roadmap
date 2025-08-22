# Session 8 – File Handling in Python

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

file = open("todo.txt", "a")
file.write("Go for a walk\n")
file.close()

Now the file keeps the old data and adds the new one.
5. Using with Statement

Python provides a safe way to handle files using with.
This automatically closes the file, even if errors happen.

with open("todo.txt", "r") as file:
    content = file.read()
    print(content)

No need to call file.close() manually!
6. Writing Structured Data

Instead of plain text, sometimes we need structured data like lists and dictionaries.
Python has the json module for this.
Example: Save To-Do List as JSON

import json

todos = ["Buy milk", "Complete Python homework", "Go for a walk"]

with open("todo.json", "w") as file:
    json.dump(todos, file)   # saves list to file

7. Reading Structured Data

import json

with open("todo.json", "r") as file:
    todos = json.load(file)

print(todos)

Output:

['Buy milk', 'Complete Python homework', 'Go for a walk']

8. Updating the To-Do List App (Big Project Part 4)

Now we’ll extend our To-Do List App to save tasks to a file and load them back.
Code Example:

import json

FILENAME = "todos.json"

# Load existing tasks
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # return empty list if file doesn't exist

# Save tasks
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)

# Add a new task
def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added: {task}")

# Show all tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

🔑 Key Takeaways

    Use open(filename, mode) to work with files.

    Always close files (or use with).

    "w" overwrites, "a" appends, "r" reads.

    Use the json module for structured data.

    Saving data makes programs persistent across runs.

📝 Mini Practice Exercises

    Create a program that writes 5 favorite movies into a file and then reads them back.

    Modify the To-Do app so you can delete a task and save changes to the file.

    Build a "Notes App" that allows adding, viewing, and saving text notes to a file.
