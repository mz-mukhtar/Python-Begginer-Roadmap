# 📘 Week 1 – Session 2: If-Else, Logic, and Building a Login System

Welcome back! 👋 In **Session 2**, you’ll learn how to **make decisions in your code** using conditional statements like `if`, `else`, and `elif`. You’ll also start working on your **first real-world project** — a simple login system and user menu.

Even if you're new to coding, don’t worry — this session is all about thinking logically and solving real problems step-by-step.

---

## ✅ Learning Goals

By the end of this session, you will be able to:

- Use `if`, `elif`, and `else` statements to make decisions
- Use comparison and logical operators
- Handle multiple conditions (nested conditions)
- Build a basic login authentication system
- Create a simple menu system for user interaction
- Add limited login attempts

---

## 💡 1. Boolean Values

In Python, a **Boolean** (`bool`) represents a simple yes/no or true/false answer. There are only two possible Boolean values:

```python
is_student = True
has_completed_course = False
```

- Notice that `True` and `False` must always start with a capital letter.
- Conditions and comparisons often produce Boolean results automatically!

### Example:
```python
student_age = 20
is_adult = student_age >= 18
print(is_adult)
```

✅ Output:
```text
True
```

Because `20 >= 18` is correct, Python evaluates the expression as `True`.

---

## 📘 2. Conditional Statements: `if`, `elif`, `else`

Conditional statements allow your program to decide **what to do next** based on conditions.

### 🧑‍💻 Example:

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
```
---

## 📊 3. Comparison Operators
|    Operator    |    Meaning    |    Example    |
|----------------|---------------|---------------|
|    ==	         |    Equal to	 |    x == 5     |
|    !=	         | Not equal to	 |    x != 5     |
|    >	         | Greater than	 |    x > 5      |  
|    <	         |  Less than    |	  x < 5      |
|    >=	         |Greater or equal | 	x >= 5   |
|    <=	         |  Less or equal |	    x <= 5   |

---

## 🔗 4. Logical Operators

Logical operators allow you to combine multiple Boolean conditions together:

|    Operator    |        Meaning        |        Example        |
|----------------|-----------------------|-----------------------|
|    and         | True if both are true |	age >= 18 and has_id |
|    or          |    True if at least one is true |age > 18 or has_permission|
|    not	     |   Reverses the condition |	not logged_in |

- **`and`** requires **both** conditions to be `True`.
- **`or`** requires **at least one** condition to be `True`.
- **`not`** reverses a Boolean result (`True` becomes `False`).

### Example:
```python
student_age = 20
has_student_id = True

can_enter = student_age >= 18 and has_student_id
print(can_enter)
```

> 💡 *Note: We will use logical operators inside larger decision-making programs during Session Three.*

---

## 🧠 4. Practice Examples
🔸 Even or Odd Checker
```
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```
🔸 Temperature Checker
```
temp = int(input("Enter temperature in °C: "))

if temp >= 30:
    print("It's hot!")
elif temp < 10:
    print("It's cold!")
else:
    print("Weather is moderate.")
```

---

## 📦 6. Nested Conditions

A **nested condition** is simply an `if` statement inside another `if` statement. You use nested conditions when a second check should only happen if the first check succeeds:

```python
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ")

if age >= 18:
    if has_id.lower() == "yes":
        print("Access granted.")
    else:
        print("ID is required.")
else:
    print("You must be 18 or older.")
```

> 💡 *Note: Session Three will be our main practice session where we build complete interactive conditional programs and projects!*

---

## 🔐 7. Building a Basic Login System
🧑‍💻 Step-by-Step Login
```
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Access denied.")
```
You can customize the values or ask users to set them first.

---

## 🔁 8. Add Login Attempts (3 Tries Only)

Let’s improve the login system with a retry limit.
```
correct_user = "admin"
correct_pass = "1234"
attempts = 3

while attempts > 0:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_user and password == correct_pass:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Wrong credentials! Attempts left:", attempts)

if attempts == 0:
    print("Account locked.")
```

---

## 🧪 9. Simple Menu System After Login

Let’s show a fake menu if login is successful.
```
print("1. View Data")
print("2. Add Data")
print("3. Exit")
```
You can take it further like this:
```
option = input("Choose an option: ")

if option == "1":
    print("Showing data...")
elif option == "2":
    print("Adding data...")
elif option == "3":
    print("Goodbye!")
else:
    print("Invalid choice.")
```

### 🧠 Homework (Project Expansion)
🏗️ Build This Program:

-  Ask for username and password
-  Allow only 3 login attempts
-  If login is successful:

   - Show a menu with 3 choices
```
        1. View Students
        2. Add Student
        3. Exit
```
-  Just print a fake response for now (we’ll build real logic later)

🚀 Bonus Challenge:

 - Let users enter their own credentials (sign-up + login flow)

