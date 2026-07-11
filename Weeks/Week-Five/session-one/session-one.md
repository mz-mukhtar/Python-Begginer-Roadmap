# 📘 Week 5 – Session 1: Python Error Handling and Input Validation

Welcome to **Week 5 – Session 1**! 🎉

In Week 4, you learned how to save and load data permanently using files. But what happens when things don't go according to plan?
- What if a user types `"twenty"` in letters when your program asks for their age in numbers?
- What if your program tries to open `"students.txt"`, but the file was accidentally deleted?
- What if someone tries to divide a number by zero?

Without preparation, Python will immediately crash and show an angry red error message. In real-world software, programs shouldn't close unexpectedly just because a user made a mistake!

By the end of this session, you will be able to:
- Understand **Syntax Errors**, **Runtime Errors**, and **Logical Errors**
- Protect your programs from crashing using `try` and `except`
- Handle specific exceptions cleanly (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`)
- Use `else` and `finally` for advanced control flow
- Safeguard file operations from missing files
- Build bulletproof **input validation loops** so users can safely retry

---

## 📌 1. Introduction: Why Do Programs Fail?

Programs do not always run successfully in the real world. Even if your logic is great, external factors can cause unexpected problems:
- Users may enter unexpected values (like letters instead of numbers)
- Files may not exist in the folder where Python is searching
- A calculation might attempt to divide by zero
- Network connections or devices might fail

When Python encounters something it cannot execute safely, it stops immediately and raises an **error** (or **exception**). Preparing your programs to handle these situations gracefully makes your code professional, friendly, and crash-proof.

---

## ❌ 2. What Is an Error?

In programming, an error happens when Python cannot execute a piece of code correctly. There are three main types of errors every beginner should know:

### 1. Syntax Error
A **Syntax Error** happens when code is written incorrectly according to Python's grammar rules. Python cannot understand code with typos, missing parentheses, or incorrect indentation.

🧑‍💻 Example:
```python
print("Hello"
```
❌ Why it fails: Notice that the closing parenthesis `)` is missing. Python detects this before running the program and stops immediately with a `SyntaxError`.

---

### 2. Runtime Error
A **Runtime Error** happens when the code is written with correct syntax, but an illegal operation occurs while the program is actively running.

🧑‍💻 Example:
```python
number = 10 / 0
```
❌ Why it fails: In mathematics, dividing any number by zero is impossible. When Python reaches this line during execution, it crashes and raises a `ZeroDivisionError`.

---

### 3. Logical Error
A **Logical Error** occurs when the program runs completely from start to finish without crashing, but it produces the **wrong result** because the programmer used the wrong formula or logic.

🧑‍💻 Example:
```python
length = 10
width = 5

area = length + width

print(area)
```
❌ Why it fails: The program runs fine and prints `15`. But the formula for the area of a rectangle is `length * width` (`50`), not `length + width`! Python cannot catch logical errors for you because the math syntax is valid.

---

## 🛡️ 3. Introduction to Exception Handling

When a runtime error occurs in Python, we call it an **Exception**. 

**Exception Handling** is a technique that allows your program to "catch" an exception when something goes wrong and choose how to respond—instead of stopping and crashing.

To handle exceptions, we wrap the risky code inside a `try` block and specify what should happen if an error occurs inside an `except` block:

```python
try:
    # Code that may cause an error
    risky_operation()

except:
    # Code that runs when an error occurs
    print("Oops! Something went wrong, but the program is still running.")
```

---

## 🧑‍💻 4. Using `try` and `except`

Let’s look at a common beginner problem: asking a user for their age as an integer.

Without exception handling, if the user types `"twenty"`, `int()` crashes. Let’s protect it using `try` and `except`:

```python
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")

except:
    print("Please enter a valid number.")
```

🔍 **Breakdown:**
1. Python attempts to run the lines inside the `try` block.
2. If the user types `21`, `int("21")` succeeds, Python prints `"You are 21 years old."`, and the `except` block is skipped completely.
3. If the user types `"twenty"`, `int("twenty")` raises an error immediately. Python jumps straight to the `except` block and prints `"Please enter a valid number."` without crashing!

---

## 🎯 5. Handling Specific Errors

Using a plain `except:` block catches *every* possible error. But as a good programmer, it is better to catch **specific exceptions** so you can give the user clear, helpful feedback.

Here are four common Python exceptions:
- `ValueError`: Raised when a function gets data of the right type but wrong format (e.g., `int("abc")`)
- `ZeroDivisionError`: Raised when dividing by `0`
- `FileNotFoundError`: Raised when trying to read a file that does not exist
- `TypeError`: Raised when combining incompatible types (e.g., `"Age: " + 20`)

Let’s look at an example that handles specific exceptions:

```python
try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    answer = first_number / second_number
    print(answer)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("A number cannot be divided by zero.")
```

💡 **Why is specific exception handling better?**
If you use only `except:`, the user gets a generic message and won't know whether they typed letters instead of numbers or accidentally divided by zero. Handling specific errors tells the user exactly what went wrong!

---

## ➕ 6. Using `else`

You can add an `else` block after `except`. The `else` block runs **only when no error happens** inside the `try` block.

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input. That was not a number.")

else:
    print(f"Success! You entered {number}.")
```

🔍 **Breakdown:**
- Putting only the risky operation (`int(...)`) in the `try` block keeps it clean.
- If no error happens, Python runs the `else` block to process the successful result.

---

## 🏁 7. Using `finally`

The `finally` block runs **always**—whether an error occurred or not! It is perfect for cleanup tasks, such as showing a closing message or freeing resources.

```python
try:
    number = int(input("Enter your lucky number: "))
    print(f"Your lucky number is {number}")

except ValueError:
    print("That was not a valid number.")

finally:
    print("Thank you for using our number checker!")
```

Whether the user typed `7` or `"seven"`, the final message `"Thank you for using our number checker!"` will always print.

---

## 📂 8. Error Handling With Files

In Week 4, you learned how to read and write files using `with open(...)`. But what if your program tries to open `"students.txt"` before the file has been created?

Let’s safeguard file reading using `FileNotFoundError`:

```python
try:
    with open("students.txt", "r") as file:
        students = file.read()
        print("--- Student Records ---")
        print(students)

except FileNotFoundError:
    print("The student file does not exist yet. Please add a student first.")
```

Now, instead of crashing when `students.txt` is missing, your app gives a friendly message explaining what to do!

---

## 🔁 9. Input Validation

Often, when a user makes a mistake, we don't want to just print an error and stop—we want to **keep asking** until they type a valid answer!

We can combine a `while True` loop with `try` and `except` to build an input validation loop:

```python
while True:
    try:
        age = int(input("Enter your age: "))
        break  # Exit the loop if conversion succeeds!

    except ValueError:
        print("Please enter a valid number.")

print(f"Your age is {age}.")
```

🔍 **Breakdown:**
1. The `while True` loop keeps repeating forever until it hits `break`.
2. Inside `try`, Python asks for `age`.
3. If the user types `"abc"`, `int("abc")` raises a `ValueError`. Python jumps to `except`, prints the warning, and the loop repeats.
4. When the user types a valid integer like `20`, `int("20")` succeeds and Python executes `break` to exit the loop safely.

---

## 🧰 10. Practical Project: Error-Safe Calculator

Let’s combine everything into a complete, menu-driven **Error-Safe Calculator** using functions!

### 🔧 Project Requirements:
- Ask for two numbers safely
- Ask the user to select an operation (`+`, `-`, `*`, `/`)
- Perform addition, subtraction, multiplication, or division
- Prevent invalid number input using `try` / `except`
- Prevent division by zero safely
- Continue running until the user chooses to exit (`q`)

### 🧑‍💻 Complete Code:
```python
def get_valid_number(prompt_message):
    """Repeatedly asks the user for a float number until valid input is given."""
    while True:
        try:
            return float(input(prompt_message))
        except ValueError:
            print("Error: Please enter a valid number!")

def calculate(first_number, second_number, operation):
    """Performs the arithmetic operation and handles zero division safely."""
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        try:
            return first_number / second_number
        except ZeroDivisionError:
            return "Error: Cannot divide by zero!"
    else:
        return "Error: Invalid operation selected!"

def run_calculator():
    print("=== Welcome to the Error-Safe Calculator ===")
    
    while True:
        print("\nOperations: [+] Add  [-] Subtract  [*] Multiply  [/] Divide  [q] Quit")
        choice = input("Select an operation: ").strip().lower()

        if choice == "q":
            print("Thank you for using Error-Safe Calculator. Goodbye!")
            break

        if choice not in ["+", "-", "*", "/"]:
            print("Invalid selection. Please choose +, -, *, /, or q.")
            continue

        num1 = get_valid_number("Enter the first number: ")
        num2 = get_valid_number("Enter the second number: ")

        result = calculate(num1, num2, choice)
        print(f"Result: {result}")

# Run the project
if __name__ == "__main__":
    run_calculator()
```

### 💡 Student Improvement Challenges:
1. Add a **Modulus (`%`)** operation and protect it against modulo by zero.
2. Add an **Exponent (`**`)** operation.
3. Save every successful calculation to a history file named `calc_history.txt`.

---

## 🧪 11. Practice Exercises

Try solving these beginner exercises on your own:

1. **Safe Age Input**: Write a program that asks for the user's age and prints how old they will be in 5 years. Use `try` / `except` so it prints `"Invalid age!"` if they enter text.
2. **Safe Division Program**: Ask the user for a total bill amount and the number of people splitting the bill. Safely calculate each person's share, handling both non-numeric input and zero people.
3. **Safe File Reader**: Write a function `read_note(filename)` that prints the contents of a file if it exists, or prints `"Note file not found."` if it doesn't.
4. **Validate a Student's Score**: Create a loop that asks a teacher to input a exam score between `0` and `100`. If the input is not a number or is outside `0–100`, show an error message and repeat.
5. **Improve an Old Project**: Take your simple calculator from Week 1 Session 1 and replace all `input()` conversions with error-safe `try` / `except` blocks.

---

## ✅ 12. Session Summary

- **Syntax Errors** happen when Python grammar is broken; **Runtime Errors** happen when illegal operations run; **Logical Errors** happen when code runs but uses wrong logic.
- **Exceptions** are runtime errors that can be caught using `try` and `except`.
- Catching **specific exceptions** (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`) allows you to give helpful messages to users.
- `else` runs when no exception happens; `finally` runs no matter what.
- Combining `while True` with `try` and `except` creates robust **input validation loops**.
