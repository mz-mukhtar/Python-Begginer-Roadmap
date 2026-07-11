# 📘 Week 3 – Session 2: Return Values, Scope, and Function Design

Welcome to **Week 3 – Session 2**! 🎉  

In Session 1, you learned how to define and call basic functions. Now we will take the next step toward professional Python craftsmanship: understanding **variable scope**, writing **clean docstrings**, and **organizing multi-function programs**.

---

## ✅ Learning Objectives

By the end of this session, you will be able to:
- Explain the difference between **local scope** and **global scope**
- Avoid relying on global variables by passing arguments and returning values
- Write informative **docstrings** (`"""..."""`) for your functions
- Apply best practices for clean function naming and design
- Structure a multi-function program cleanly using a main controller flow

---

## 🌍 1. Local Versus Global Scope

**Scope** refers to the area of your Python program where a variable exists and can be accessed.

### 1️⃣ Local Scope
When you create a variable inside a function, it is **local** to that function. It is created when the function runs and forgotten as soon as the function finishes:

```python
def create_welcome_message():
    message = "Hello from inside the function!"
    print(message)

create_welcome_message()
# print(message)  # ❌ Error: NameError - 'message' is not defined outside!
```

### 2️⃣ Global Scope
Variables created outside of all functions belong to the **global scope**. They can be read from anywhere in the file:

```python
school_name = "Addis Ababa Institute of Technology"

def show_school():
    print("Welcome to", school_name)

show_school()
```

### 💡 Best Practice for Beginners
While it is possible to modify global variables using the `global` keyword, **relying heavily on global variables makes programs hard to debug and test**.

Instead, always prefer:
- **Passing data in** using **parameters**
- **Sending results out** using **`return`**

#### Bad Pattern (Relying on globals):
```python
total = 0

def add_ten():
    global total
    total += 10
```

#### Clean & Reusable Pattern (Parameters and Return):
```python
def add_ten(current_total):
    return current_total + 10

my_total = 0
my_total = add_ten(my_total)
```

---

## 📝 2. Docstrings and Good Function Design

Professional code should explain itself clearly.

### 1️⃣ Writing Docstrings (`"""..."""`)
A **docstring** (documentation string) is a multi-line string placed immediately below the `def` line to explain what the function does:

```python
def calculate_area(length, width):
    """
    Calculates and returns the area of a rectangle.
    """
    return length * width
```

When someone uses your function or inspects it in an editor, Python shows this docstring automatically!

### 2️⃣ Best Practices for Function Design
- **Do one clear job**: A function should perform a single, well-defined task.
- **Use descriptive names**: Name functions with action verbs that explain their purpose (`calculate_total()`, `format_student_name()`) rather than vague names (`do_it()`, `stuff()`).
- **Keep functions short**: If a function becomes longer than 25–30 lines, consider breaking it into smaller helper functions.

---

## 🏗️ 3. Organizing Multi-Function Programs

Let's see how breaking a task into 3 clear functions makes our program organized and readable.

Imagine we want to collect a student's score, determine their grade letter (`A`, `B`, `C`, `F`), and display the final report.

### Step 1: Input Function (`get_student_score()`)
```python
def get_student_score():
    """Prompts the user to enter a valid exam score."""
    score = float(input("Enter exam score (0-100): "))
    return score
```

### Step 2: Processing Function (`calculate_grade()`)
```python
def calculate_grade(score):
    """Returns the letter grade corresponding to a numeric score."""
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"
```

### Step 3: Display Function (`display_result()`)
```python
def display_result(score, grade):
    """Displays the student's formatted grade report."""
    print("\n--- Student Grade Report ---")
    print("Score Entered:", score)
    print("Letter Grade :", grade)
    print("----------------------------")
```

### Step 4: Connecting the Flow
We coordinate the flow by calling each function sequentially:

```python
# Main Program Flow
student_score = get_student_score()
student_grade = calculate_grade(student_score)
display_result(student_score, student_grade)
```

✅ Sample Output:
```text
Enter exam score (0-100): 88

--- Student Grade Report ---
Score Entered: 88.0
Letter Grade : A
----------------------------
```

> 💡 *Note: In Session Three, we will take Program Decomposition even further and organize our controller logic inside a clean `main()` function!*

---

## 🧪 4. Practice Exercises

### Task 1: Area Calculator with Docstring
Write a function `calculate_triangle_area(base, height)` that includes a clear docstring and returns `(base * height) / 2`.

### Task 2: Multi-Function Temperature Converter
Write two separate functions:
1. `celsius_to_fahrenheit(c)` that returns `(c * 9/5) + 32`
2. `display_temperature(c)` that calls `celsius_to_fahrenheit(c)` and prints both temperatures clearly.

---

## 🏁 5. Session Summary

- **Local scope** protects variables inside functions; **global scope** is outside all functions.
- Pass values in via **parameters** and send them out via **`return`**.
- Write clear **docstrings** (`"""..."""`) to document function purpose.
- Name functions descriptively (`calculate_grade()` instead of `calc()`).
- Decompose programs into clear input, processing, and display functions!
