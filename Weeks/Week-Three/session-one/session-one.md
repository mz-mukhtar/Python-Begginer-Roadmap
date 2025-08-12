# 📘 Week 3 – Session 1: Functions and Reusability in Python

Welcome to **Week 3 – Session 1**! 🧠📦  
This session is all about making your code **modular**, **reusable**, and **organized** using **functions**. Think of functions as *tools* you create once and use as many times as needed.

---

## ✅ Learning Objectives

By the end of this session, you will:

- Understand what a function is and why it’s useful
- Define and call your own functions
- Pass data into functions using parameters
- Get data out of functions using return values
- Refactor old code into clean, reusable blocks

---

## 🧩 1. What is a Function?

A function is a named block of code that performs a specific task.

### 🔧 Example:

```python
def greet():
    print("Hello!")
```
➕ Calling the function:
```greet()```

---

## 🧪 2. Why Use Functions?

Without functions:
```
print("Welcome")
print("Welcome")
```
With a function:
```
def welcome():
    print("Welcome")

welcome()
welcome()
```
✅ Less repetition
✅ Easier debugging
✅ Clearer code structure

---

## ✍️ 3. Defining and Calling Functions
🧑‍💻 Syntax:
```
def function_name():
    # block of code
    print("I am inside a function.")
```
To run the code inside:
```
function_name()
```

---

## 📦 4. Parameters and Arguments
🎯 A function can take input values:
```
def greet_user(name):
    print("Hello", name)

greet_user("Mahlet")
greet_user("Alemayehu")
```
You can pass multiple parameters:
```
def add(a, b):
    print("Sum =", a + b)

add(3, 5)
```

---

## 🎯 5. Return Values

Functions can also return a result:
```
def square(x):
    return x * x

result = square(4)
print(result)  # 16
```
 Use `return` when you want to send a result back to the caller.

---

## 🧪 6. Practice Tasks
🔹 Task 1: Greet 5 names using a function
```
def greet(name):
    print("Hello", name)

names = ["Mahi", "Sara", "Mike"]
for n in names:
    greet(n)
```
🔹 Task 2: Build a simple calculator with functions
```
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("1. Add\n2. Subtract")
choice = input("Choose: ")

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if choice == "1":
    print("Result:", add(x, y))
elif choice == "2":
    print("Result:", subtract(x, y))
else:
    print("Invalid choice.")
```

---

## 🔄 7. Rewriting Old Projects with Functions

Let’s refactor the login system using a function:
```
def login():
    correct_user = "admin"
    correct_pass = "1234"
    attempts = 3

    while attempts > 0:
        u = input("Username: ")
        p = input("Password: ")

        if u == correct_user and p == correct_pass:
            return True
        else:
            attempts -= 1
            print("Wrong! Attempts left:", attempts)

    return False

# Use the function
if login():
    print("Welcome!")
else:
    print("Access denied.")
```

---

## 🌍 8. Scope: Local vs Global
What is Scope?

Scope refers to the part of a program where a variable is recognized and can be used.

Two main types:

1. Local Scope – variables created inside a function, only accessible there.

2. Global Scope – variables created outside functions, accessible anywhere.

Local Scope Example
```
def greet():
    message = "Hello from local scope"
    print(message)

greet()
# print(message)  # ❌ Error: message not defined here
```
Global Scope Example
```
message = "Hello from global scope"

def greet():
    print(message)

greet()
print(message)  # Works fine
```
Modifying Globals with global

If you want to change a global variable inside a function:
```
counter = 0

def increment():
    global counter
    counter = counter + 1
    print(counter)

increment()
increment()
```
Why Not Always Use Globals?

- Harder to debug

- Functions become less reusable

- Higher risk of accidental changes

💡 Best Practice: Pass variables as function parameters instead of relying on globals.

### Practice

 -  Create a global variable name = "Python".

 -  Make a function that prints it.

 -  Make another that changes it to "Java" using global.

 -  Print name before and after both functions.



---

## 🧠 Homework
📌 Task 1: Create a function that returns the average of a list of numbers
```
def average(numbers):
    return sum(numbers) / len(numbers)

scores = [70, 85, 90, 60]
print("Average score:", average(scores))
```
📌 Task 2: Create a login-signup system using two functions (`signup()` and `login()`)
