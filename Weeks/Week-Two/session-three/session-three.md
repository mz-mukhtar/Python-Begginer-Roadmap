# 📘 Week Two – Session Three: Dictionaries, Sets, and Student Information Project

Welcome back! 👋

In Sessions One and Two of Week Two, you learned how to automate repetitive tasks using loops (`while` and `for`) and store ordered collections of items using lists and tuples.

However, lists have a limitation when storing structured records. Look at this list:

```python
student = ["Abel", 20, "Engineering"]
```

Ask yourself: What does `20` mean? Is it the student's age, ID number, or credit hours? When a list stores different types of information together, you have to memorize which index (`0`, `1`, `2`) belongs to which field.

In this session, you will learn how to structure self-describing records using **Dictionaries**, automatically filter unique values using **Sets**, and build the interactive **Student Information Collector** project!

---

## 🎯 Learning Objectives

By the end of this session, you will be able to:
- Explain why key-value dictionaries are ideal for structured records
- Create, access, add, update, and remove items in Python dictionaries
- Iterate through dictionary keys, values, and items using loops
- Manage lists containing multiple dictionaries (`List[Dict]`)
- Create sets to store unique values and remove duplicates automatically
- Choose the right Python collection (List, Tuple, Dictionary, or Set) for any task
- Build, run, and explain the **Student Information Collector** project

---

## 📌 1. Introduction: Why Use Dictionaries?

Instead of storing data by index positions (`0`, `1`, `2`), a **Dictionary** stores data in **Key-Value pairs**.

Let us see how much clearer our student record becomes:

```python
student = {
    "name": "Abel",
    "age": 20,
    "department": "Engineering"
}
```

Now, every value has a descriptive **Key** (`"name"`, `"age"`, `"department"`). Dictionaries are the foundation for saving JSON files (Week Four) and reading internet APIs (Week Eight)!

---

## 🗝️ 2. Creating Dictionaries

Dictionaries are created using curly brackets `{}`. Inside the brackets, we separate each key and value with a colon `:` and separate pairs with commas `,`:

```python
book = {
    "title": "Python for Beginners",
    "author": "Mahi Zeki",
    "pages": 250
}

print(book)
```

---

## 🔍 3. Accessing Values

You can access a dictionary's value by passing its key inside square brackets `[]` or by using the `.get()` method:

```python
student = {
    "name": "Abel",
    "age": 20,
    "department": "Engineering"
}

# Method 1: Square bracket indexing
print("Student Name:", student["name"])

# Method 2: Using .get()
print("Department:", student.get("department"))
```

### What is the difference between `[]` and `.get()`?
- If you ask for a key that does not exist using `student["email"]`, Python crashes with a `KeyError`.
- If you ask for a key using `student.get("email")`, Python safely returns `None` without crashing!

---

## ➕ 4. Adding Values

To add a new key-value pair to an existing dictionary, assign a value to a new key:

```python
student = {
    "name": "Abel",
    "age": 20
}

# Add a new email key
student["email"] = "abel@example.com"

print(student)
```

---

## ✏️ 5. Updating Values

To update an existing value, assign a new value to an existing key:

```python
student = {
    "name": "Abel",
    "department": "Engineering"
}

# Update department
student["department"] = "Computer Engineering"

print("Updated department:", student["department"])
```

---

## 🗑️ 6. Removing Values

To remove a key-value pair from a dictionary, use the `.pop()` method:

```python
student = {
    "name": "Abel",
    "age": 20,
    "department": "Engineering"
}

# Remove the 'age' key and store its value
removed_age = student.pop("age")

print("Student after removal:", student)
print("Removed age:", removed_age)
```

---

## 🔄 7. Useful Dictionary Methods

Python provides three essential methods for looping through dictionaries:
- `.keys()`: Returns all keys
- `.values()`: Returns all values
- `.items()`: Returns both key and value pairs

Let us loop through a dictionary:

```python
student = {
    "name": "Abel",
    "age": 20,
    "department": "Engineering"
}

print("=== Dictionary Items ===")
for key, value in student.items():
    print(key, "->", value)
```

---

## 👥 8. Multiple Student Records (`List of Dictionaries`)

How do we store records for 50 different students? We create a **List** where each item is a **Dictionary**!

```python
student_list = [
    {
        "name": "Abel",
        "age": 20
    },
    {
        "name": "Sara",
        "age": 19
    }
]

# Looping through all student records
for student in student_list:
    print(student["name"], "is", student["age"], "years old.")
```

Notice the structure:
```text
List (Ordered collection of records)
  ↓
Contains multiple Dictionaries
  ↓
Each Dictionary represents one individual student profile
```

---

## 🪆 9. Nested Dictionaries

A dictionary value can also be another dictionary! Here is one simple example:

```python
student = {
    "name": "Abel",
    "contact": {
        "phone": "0911000000",
        "city": "Addis Ababa"
    }
}

print("Student City:", student["contact"]["city"])
```

---

## 🧺 10. Introduction to Sets

A **Set** is an unordered collection that stores **only unique values**. Sets are created using curly brackets `{}` without key-value colons:

```python
courses = {"Math", "Science", "English", "Math", "Science"}
print("Unique courses:", courses)
```

Notice that duplicate entries (`"Math"`, `"Science"`) are automatically removed!

### Useful Set Methods:
- `.add(item)`: Adds a new item to the set
- `.remove(item)`: Removes an item (crashes with `KeyError` if the item is missing)
- `.discard(item)`: Safely removes an item without crashing if it is missing

```python
languages = {"Python", "HTML", "CSS"}

languages.add("JavaScript")
languages.discard("Ruby")  # Does not crash even though Ruby is not in the set

print(languages)
```

---

## 📊 11. When to Use Each Collection

Here is a handy guide to choosing the right Python data collection:

| Collection | Syntax | Duplicates Allowed? | Best Used For |
| :--- | :---: | :---: | :--- |
| **List** | `[item1, item2]` | Yes | Ordered sequences that change over time (e.g., list of student records) |
| **Tuple** | `(item1, item2)` | Yes | Fixed, unchangeable collections (e.g., coordinates, RGB colors) |
| **Dictionary** | `{"key": "value"}` | Unique keys | Structured profiles with descriptive field labels |
| **Set** | `{item1, item2}` | **No** | Filtering duplicates or checking unique membership |

---

## 🛠️ 12. Weekly Project: Student Information Collector

Let us apply loops, lists, dictionaries, sets, and conditions to build our Week Two capstone project: the **Student Information Collector**!

### 📋 Project Description & Requirements
- Use a **List** (`student_list`) to store all student records.
- Use a **Dictionary** for each student (`name`, `age`, `department`).
- Use a **Set** (`unique_departments`) to collect all unique department names without duplicates.
- Allow the user to add multiple students using a `while` loop.
- Display all collected student profiles cleanly.
- Allow the user to search for a student by name.
- *(Note: We use procedural loops here. Next week in Week Three, we will decompose programs into clean functions!)*

### Complete Runnable Code

```python
# ==========================================
# Project: Student Information Collector
# Week Two Capstone Project
# ==========================================

student_list = []
unique_departments = set()

print("=== Welcome to the Student Information Collector ===")

# 1. Loop to collect multiple student records
while True:
    print("\n--- Enter New Student Details ---")
    name = input("Enter student name: ").strip()
    age = int(input("Enter student age: "))
    department = input("Enter student department: ").strip()

    # Create a structured dictionary for the student
    student_record = {
        "name": name,
        "age": age,
        "department": department
    }

    # Add dictionary to the list and department to the set
    student_list.append(student_record)
    unique_departments.add(department)

    # Ask if user wants to add another student
    continue_choice = input("Add another student? (yes/no): ").strip().lower()
    if continue_choice != "yes":
        break

# 2. Display all collected students
print("\n==========================================")
print("       REGISTERED STUDENT PROFILES        ")
print("==========================================")
for student in student_list:
    print("Name:", student["name"], "| Age:", student["age"], "| Department:", student["department"])
print("==========================================")

# 3. Display unique departments
print("\nUnique Departments Represented:", unique_departments)

# 4. Search for a student by name
print("\n--- Student Search ---")
search_name = input("Enter a student name to search: ").strip().lower()
found = False

for student in student_list:
    if student["name"].lower() == search_name:
        print("\n✅ Match Found!")
        print("Name      :", student["name"])
        print("Age       :", student["age"])
        print("Department:", student["department"])
        found = True
        break

if not found:
    print("❌ No student found matching that name.")
```

### Example Output:
```text
=== Welcome to the Student Information Collector ===

--- Enter New Student Details ---
Enter student name: Sara
Enter student age: 20
Enter student department: Computer Science
Add another student? (yes/no): yes

--- Enter New Student Details ---
Enter student name: Abel
Enter student age: 21
Enter student department: Computer Science
Add another student? (yes/no): no

==========================================
       REGISTERED STUDENT PROFILES        
==========================================
Name: Sara | Age: 20 | Department: Computer Science
Name: Abel | Age: 21 | Department: Computer Science
==========================================

Unique Departments Represented: {'Computer Science'}

--- Student Search ---
Enter a student name to search: sara

✅ Match Found!
Name      : Sara
Age       : 20
Department: Computer Science
```

---

## 📝 13. Practice Exercises

Try these exercises to reinforce your skills!

### Beginner
1. **Create a Book Dictionary**: Create a dictionary named `book` with keys `"title"`, `"author"`, and `"year"`. Print each value clearly.
2. **Create a Product Dictionary**: Create a dictionary for a store product (`name`, `price`, `in_stock`). Print whether the item is in stock (`True`/`False`).

### Intermediate
3. **Update Dictionary Values**: Start with a dictionary `car = {"brand": "Toyota", "price": 20000}`. Update the price to `22000` and add a new key `"color"` with value `"Blue"`.
4. **Display Dictionary Information**: Loop through all key-value pairs of your `car` dictionary using `.items()` and print `"Key -> Value"`.
5. **Store Multiple Books**: Create a list holding 3 different book dictionaries. Loop through the list and print only the book titles.

### Challenge
6. **Remove Duplicate Programming Languages**: Ask the user to enter 5 programming languages one by one inside a `for` loop. Add each entered name into a **Set** and print the final set of unique languages.

---

## 🚀 14. Weekly Challenge: Contact Information Collector

Test your Week Two mastery by building a **Contact Information Collector**!

### Requirements:
- Use a `while` loop to collect contacts (`name`, `phone_number`, `email`).
- Store each contact as a dictionary inside a main `contact_list`.
- After collecting contacts, ask the user to enter a name to search.
- Loop through the list and display the contact's phone and email if found.

💡 **Hint**: Use `contact["name"].lower() == search_query.lower()` for case-insensitive searching!

---

## ❓ 15. Review Questions

1. Why are dictionaries better than lists for representing an individual student profile?
2. What happens if you index a missing dictionary key using `[]` versus `.get()`?
3. How do you add a brand-new key-value pair to an existing dictionary?
4. What method returns all key-value tuples from a dictionary inside a loop?
5. How does a set behave when you attempt to add an item that is already inside it?
6. What is the difference between the set `.remove()` and `.discard()` methods?

---

## ✅ 16. Learning Checklist

- [ ] I understand the structure of key-value dictionaries.
- [ ] I can create, access, update, and remove dictionary pairs.
- [ ] I can loop through dictionary keys, values, and items.
- [ ] I can store multiple dictionaries inside a Python list.
- [ ] I can use sets to store unique values and remove duplicates.
- [ ] I can build a complete application combining loops, lists, dictionaries, and sets.

---

## 🏁 17. Session Summary

- **Dictionaries** (`{"key": "value"}`) organize data into readable key-value profiles.
- **Lists of Dictionaries** (`[{}, {}]`) are the standard pattern for handling collections of records.
- **Sets** (`{1, 2, 3}`) automatically eliminate duplicate values and allow fast unique checks.
- Combining loops, lists, dictionaries, and sets allowed us to build our interactive **Student Information Collector**!
