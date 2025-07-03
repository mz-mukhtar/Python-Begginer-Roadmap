# 📘 Week 1 - Session 1: Introduction to Python, Variables, and Basic Calculator

Welcome to your **first Python session**! 🎉

This session is meant to be your gateway into the world of programming with Python. We’ll cover everything from installing Python, writing your first line of code, and building your first small project — a **simple calculator**.

By the end of this session, you’ll understand:
- What Python is and why it’s useful
- How to install and run Python
- How to interact with users using `print()` and `input()`
- How to use variables and basic data types
- How to do arithmetic operations
- How to build a simple calculator app

---

## 📌 1. What is Python?

Python is a powerful, easy-to-learn programming language used for:
- Web development (e.g., Django, Flask)
- Data science and machine learning (e.g., pandas, scikit-learn)
- Scripting and automation
- Game development
- AI and robotics

**Why is Python great for beginners?**
- Simple and clean syntax (it reads like English!)
- Large community and support
- Tons of libraries for every need

Example of Python:
```python
print("Hello, world!")
```

---

## 🛠️ 2. Installing Python
✅ Step-by-Step:

### Download Python:

-  Visit: https://www.python.org/downloads/

- Click the “Download Python 3.x” button

###  Install Python:

- On Windows, make sure to check the box: ✅ Add Python to PATH

  - Click “Install Now”

- Open Your Code Editor:

  - We recommend Visual Studio Code

- Or use online tools like Replit if you don’t want to install anything

### Check Installation:

- Open a terminal (or command prompt) and type:
```
python --version
```

---

## 📤 3. Your First Python Program

Let’s write the classic Hello, World! program.
```
print("Hello, Python!")
```
✅ Output:
```
Hello, Python!
```
- print() is used to display something on the screen.

---

## 🎮 4. Taking User Input with input()

Let’s ask the user for their name and greet them:
```
name = input("What is your name? ")
print("Nice to meet you, " + name + "!")
```
⚡ Breakdown:

- input() pauses and waits for the user to type
- It always returns a string (text)
- You can store it in a variable

---

## 🧠 5. Variables and Data Types

Variables store values. Think of them like containers.
```
age = 17
height = 1.75
name = "Amina"
is_student = True
```
  | Type     |   Example	   |     Type   |
  |----------|---------------|------------| 
  | Integer	 |  17	         |      int   |
  | Float	   |  1.75	       |      float |
  | String   |  "Amina"	     |      str   |
  | Boolean	 |  True/False	 |      bool  |

🔎 You can check a variable’s type using:
```
print(type(age))        # <class 'int'>
print(type(name))       # <class 'str'>
```

---

## ➕ 6. Arithmetic Operators

Python can act like a calculator:

|  Symbol	 |    Name	       |  Example	|   Result |
|----------|-----------------|----------|----------|
|    +	   |     Addition	   |  5 + 3	  |   8
|    -	   |    Subtraction	 |  7 - 2	  |   5
|    *	   | Multiplication	 |  4 * 6	  |   24
|    /	   |    Division	   |  10 / 2	|     5.0
|    //	   |   Floor Division|	10 // 3	|   3
|    %	   |     Modulus	   |  10 % 3	|     1
|    **	   |   Exponent	     |  2 ** 3	|     8

✅ Example:
```
a = 10
b = 3
print("Addition:", a + b)
print("Modulo:", a % b)
```

---

## 💬 7. Comments and Indentation
### Comments

Use # to leave notes for yourself (not executed).

# This is a comment
```
print("Hello!")  # This prints text
```
### Indentation

Python uses indentation (spaces/tabs) to group blocks of code.

Correct:
```
if 5 > 3:
    print("5 is greater")
```
Incorrect (no indentation!):
```
if 5 > 3:
print("5 is greater")  # Will cause error
```

---

## 🧪 8. Practice Tasks

Try these on your own:

 - Age in 10 Years:
```
age = int(input("How old are you? "))
future = age + 10
print("In 10 years, you'll be", future)
```
- Area of a Rectangle:
```
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area =", area)
```
- Check Even or Odd:
```
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

---
## 🧰 9. Final Mini Project: Build a Simple Calculator

Let’s combine everything into your first real-world Python app: a calculator.
🔧 Calculator Requirements:

- Takes 2 numbers from the user
- Takes an operation: +, -, *, /
- Performs the operation and displays result

🧑‍💻 Code:
```
print("Welcome to the Python Calculator!")

num1 = float(input("Enter first number: "))
op = input("Enter an operation (+ - * /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid operation!"

print("Result:", result)
```
✅ Sample Output:
```
Enter first number: 10
Enter an operation (+ - * /): *
Enter second number: 5
Result: 50.0
```
----

### 🧠 Homework
 Build your own version of the calculator that:
 - Shows a welcome message
 - Asks for 2 numbers and an operation
 - Handles invalid inputs (optional)
 - Looks clean and friendly

### Bonus challenge:

Create a program that asks your name and age, and prints:
```
"Hello Mahi, you are 22 years old. In 10 years, you will be 32!"
```
