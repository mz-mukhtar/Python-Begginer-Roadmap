# 📘 Week 2 – Session 2: Lists and Looping Through Data

Welcome to **Week 2 – Session 2**! 🎉

Now that you understand how to repeat tasks using loops, it’s time to learn about **lists** — one of the most important tools in Python. A list lets you store **multiple values in one variable** — names, scores, groceries, you name it!

By the end of this session, you’ll be able to:
- Create and use Python lists
- Loop through lists using `for` and `while` loops
- Modify lists by adding or removing items
- Access items by index
- Build a student name collector program

---

## 🧺 1. What Is a List?

A list is like a container that holds **a group of items**.

```
fruits = ["apple", "banana", "orange"]
print(fruits)
```

Each item has a position, starting at index 0.
```
print(fruits[0])  # apple
print(fruits[2])  # orange
```

---

## 🛠️ 2. Creating Lists
✅ List of strings:
```
names = ["Ali", "Sara", "Noah"]
```
✅ List of numbers:
```
scores = [85, 90, 78, 92]
```
✅ Mixed list (not recommended for beginners):
```
info = ["Mahi", 21, True]
```

---

## 🎯 3. Looping Through Lists
🔁 Using `for` loop:
```
students = ["Mahi", "Betty", "Samuel"]
for name in students:
    print("Hello", name)
```
🔁 Using `while` loop:
```
i = 0
while i < len(students):
    print("Student", i + 1, "is", students[i])
    i += 1
```

---

## 🔧 4. Basic List Operations & Methods

Here are the essential methods for modifying and inspecting lists:

➕ **Add item to end (`append()`)**:
```python
students.append("Hana")
```

📌 **Insert item at specific index (`insert()`)**:
```python
student_names = ["Abel", "Sara"]
student_names.insert(1, "Miki")
print(student_names)  # ['Abel', 'Miki', 'Sara']
```
> `insert()` adds an item at a selected position.

✏️ **Updating List Values**:
You can change an existing item by assigning a new value to its index:
```python
student_names = ["Abel", "Sara"]
student_names[0] = "Samuel"
print(student_names)  # ['Samuel', 'Sara']
```

✂️ **List Slicing**:
You can select a range of items from start to end index:
```python
student_names = ["Abel", "Sara", "Miki", "Liya"]
print(student_names[1:3])  # ['Sara', 'Miki']
```

❌ **Remove specific item (`remove()`)**:
```python
students.remove("Samuel")
```

🧼 **Remove and return last item (`pop()`)**:
```python
students.pop()
```

🔤 **Sort list alphabetically or numerically (`sort()`)**:
```python
student_names.sort()
```

🔄 **Reverse list order (`reverse()`)**:
```python
student_names.reverse()
```

🔢 **Count item occurrences (`count()`)**:
```python
print(student_names.count("Sara"))
```

📍 **Find item index (`index()`)**:
```python
print(student_names.index("Sara"))
```

🔍 **Check if item exists (`in`)**:
```python
if "Betty" in students:
    print("Betty is in the list")
```

📊 **Length of list (`len()`)**:
```python
print(len(students))
```

---

## 🧪 5. Practice Tasks
#### Task 1: Print all names in a list
```
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print("Welcome", name)
```
#### Task 2: Add 3 new items to a list using `append()`
```
colors = []
colors.append("Red")
colors.append("Blue")
colors.append("Green")
print(colors)
```
#### Task 3: Create a list of 5 numbers and print their sum
```
numbers = [10, 20, 30, 40, 50]
total = 0
for n in numbers:
    total += n
print("Sum:", total)
```

## 📦 6. Introduction to Tuples

A **tuple** is another built-in Python collection similar to a list, but written with **parentheses** `()` instead of square brackets `[]`:

```python
coordinates = (10, 20)
days_of_week = ("Monday", "Tuesday", "Wednesday")
```

### Key Features of Tuples:
- **Ordered values**: Items keep their order.
- **Indexing and Length**: Access items by position (`coordinates[0]`) and check size with `len(days_of_week)`.
- **Looping**: Step through items using a `for` loop:
  ```python
  for day in days_of_week:
      print(day)
  ```
- **Immutable (Cannot be changed)**: Unlike lists, **values in a tuple normally cannot be modified** after creation (`append()`, `remove()`, or item reassignment will raise an error).

### Lists Versus Tuples

| Feature | List (`[]`) | Tuple (`()`) |
| :--- | :--- | :--- |
| **Syntax** | `names = ["Abel", "Sara"]` | `point = (10, 20)` |
| **Can add/remove items?** | ✅ Yes (Mutable) | ❌ No (Immutable) |
| **Can change item values?** | ✅ Yes | ❌ No |
| **Best used for** | Changing collections (student rosters, scores) | Fixed data (coordinates, days of the week) |

---

## 🔐 7. Mini Project: Student Collector

Let’s build a program that:

- Asks the user how many students they want to enter

- Collects each student’s name in a list

- Displays the final list

💻 Example Code:
```
students = []
count = int(input("How many students? "))

for i in range(count):
    name = input(f"Enter name of student {i + 1}: ")
    students.append(name)

print("\nStudent List:")
for student in students:
    print("-", student)
```
✅ Sample Output:
```
How many students? 3
Enter name of student 1: Mahi
Enter name of student 2: Lily
Enter name of student 3: Robel

Student List:
- Mahi
- Lily
- Robel
```

---

## 🔗 8. Preview: Nested Data Structures (Dictionaries Preparation)

As your programs grow, you may want to organize richer student profiles by storing a dictionary inside another dictionary:

```python
student = {
    "name": "Abel",
    "scores": {
        "Python": 90,
        "Networking": 85
    }
}

print(student["scores"]["Python"])  # 90
```

> 💡 *Note: We will study dictionaries in more detail during Session Three!*

---

### 🧠 Homework
#### 📌 Task 1: Add Scores and Average

- Ask the user how many scores they want to enter

- Collect all the scores in a list

- Print the average score
