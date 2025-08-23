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

## 🔧 4. Basic List Operations
➕ Add Items:
```
students.append("Hana")
```
❌ Remove Items:
```
students.remove("Samuel")
```
🧼 Remove last item:
```
students.pop()
```
🔍 Check if item exists:
```
if "Betty" in students:
    print("Betty is in the list")
```
📊 Length of list:
```
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

---

## 🔐 6. Mini Project: Student Collector

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
### 🧠 Homework
#### 📌 Task 1: Add Scores and Average

- Ask the user how many scores they want to enter

- Collect all the scores in a list

- Print the average score
