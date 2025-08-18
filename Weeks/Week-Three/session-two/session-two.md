# Session 6: Mastering Dictionaries in Python

In this session, we’ll dive deeper into **dictionaries**, one of Python’s most powerful and flexible data structures. By the end of this lesson, you’ll not only know how to use dictionaries but also how to **store structured data** effectively for real-world applications.

---

## 1. Introduction to Dictionaries

A **dictionary** in Python is a collection of **key-value pairs**. Unlike lists (which are ordered collections accessed by index), dictionaries store data in pairs where:
- A **key** is a unique identifier.
- A **value** is the data associated with the key.

📌 **Syntax:**
```python
my_dict = {
    "key1": "value1",
    "key2": "value2",
}
```

Example:
```
student = {
    "name": "Mahi",
    "age": 21,
    "major": "Electrical Engineer"
}

print(student["name"])  # Output: Mahi
```

Key Points:

  - Keys must be unique.

  - Keys can be of type: string, number, or tuple (immutable types).

  - Values can be of any data type (string, int, list, another dict, etc.).

---

## 2. Adding, Updating, and Deleting Items in a Dictionary
Adding a new key-value pair:
```
student["university"] = "AAiT"
print(student)
```
Updating a value:
```
student["age"] = 22
print(student)
```
Deleting a key-value pair:
```
del student["major"]
print(student)
```
Using `.pop()`:
```
removed = student.pop("age")
print("Removed:", removed)
print(student)
```

---

## 3. Looping Through a Dictionary

Dictionaries are iterable. You can loop through keys, values, or items (key-value pairs).
Loop through keys:
```
for key in student:
    print(key)
```
Loop through values:
```
for value in student.values():
    print(value)
```
Loop through key-value pairs:
```
for key, value in student.items():
    print(key, ":", value)
```

---

## 4. Dictionary Methods You Should Know

- `dict.keys()` → returns all keys
- `dict.values()` → returns all values
- `dict.items()` → returns all key-value pairs
- `dict.get(key, default)` → returns value for key, or default if not found
- `dict.update({...})` → updates dictionary with new values

Example:
```
student = {"name": "Mahi", "age": 21}

print(student.get("major", "Not Specified"))  
# Output: Not Specified

student.update({"major": "Cybersecurity"})
print(student)
```

---

## 5. Nested Dictionaries

A nested dictionary means a dictionary inside another dictionary. This is useful for representing structured or hierarchical data.
Example: Storing students’ information
```
students = {
    "student1": {"name": "Mahi", "age": 22, "major": "EE"},
    "student2": {"name": "Sara", "age": 22, "major": "IT"},
    "student3": {"name": "Jon", "age": 20, "major": "EE"}
}

# Access nested values:
print(students["student1"]["name"])  # Output: Mahi

# Loop through nested dictionaries:
for student_id, info in students.items():
    print(student_id, "->", info["name"], info["major"])
```

---

## 6. Use Cases of Dictionaries

  1. Storing configuration settings (like app preferences).

  2. Mapping IDs to user data (student ID → student details).

  3. Counting frequency of items in text (word counter).

  4. Representing JSON data (API responses are basically dictionaries in Python).

---

## 7. Big Project Part 3: Store Structured Data Using Dictionaries

Now, let’s build on our To-Do List Manager Project.
So far:

- Part 1: We used variables/lists.

- Part 2: We introduced functions.

Now in Part 3, we’ll use dictionaries to make the system structured and scalable.




























































































