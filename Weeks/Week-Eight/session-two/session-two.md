# 📘 Week Eight – Session Two: Introduction to Testing

Welcome back! 👋

Have you ever fixed a bug in one part of your application, only to discover later that your fix accidentally broke another feature?

Up until now, every time you modified your Student Management System, you probably tested it by running `python main.py`, typing numbers into the menu, and visually checking the screen. Remember:
> **Code working once does not guarantee that it always works.**

As applications grow, testing 20 different menu paths manually every time you change a line of code takes too much time. In this session, you will learn how to verify code automatically—starting with basic **Assertions** (`assert`) and advancing to professional unit tests using Python's built-in **`unittest`** framework!

---

## 🎯 Learning Objectives

By the end of this session, you will be able to:
- Explain why software testing is essential for building reliable programs
- Compare Expected Results vs. Actual Results systematically
- Identify comprehensive manual testing scenarios (valid, invalid, boundary, missing data)
- Write inline code verifications using Python `assert` statements
- Structure automated test suites using the `unittest.TestCase` class
- Run unit tests from the terminal using `python -m unittest`
- Use core assertions (`assertEqual`, `assertTrue`, `assertFalse`, `assertIn`)
- Organize project test files cleanly inside a dedicated `tests/` directory
- Write automated tests for our Student Management System functions

---

## 📌 1. Why Testing Matters

When you build a bridge, engineers inspect every bolt before opening it to traffic. Software engineering requires the exact same rigor!

Testing protects your codebase against regressions—bugs that appear when new changes accidentally break previously working features.

---

## ⚖️ 2. Expected vs. Actual Results

Every test—whether manual or automated—boils down to comparing two values:

| Term | Definition | Example Scenario |
| :--- | :--- | :--- |
| **Expected Result** | What the specification says should happen | Adding `5 + 3` should return `8` |
| **Actual Result** | What your code actually produces when run | Adding `5 + 3` returned `8` |
| **Test Outcome** | **Pass** if Expected == Actual; **Fail** otherwise | `8 == 8` → ✅ **PASS** |

---

## 🧑‍💻 3. Manual Testing Strategy

Before writing automated scripts, good developers think through five key testing scenarios:
1. **Valid Input**: Normal data (e.g., age `20`, score `85`).
2. **Invalid Input**: Wrong data types (e.g., typing `"twenty"` for age).
3. **Empty Input**: Pressing Enter without typing anything (`""`).
4. **Boundary Values**: Edge cases exactly at limits (e.g., scores `0` and `100`).
5. **Missing Files**: Running the app when `students.json` does not exist yet.

---

## 🛑 4. Inline Verification With `assert`

Python includes a built-in statement called **`assert`** that tests whether a condition is `True`. If the condition is `False`, Python immediately halts with an `AssertionError`:

```python
def add_numbers(first_number, second_number):
    return first_number + second_number

# Verify function behavior using assert
assert add_numbers(5, 3) == 8
assert add_numbers(10, -2) == 8
print("✅ All assertions passed successfully!")
```

If you accidentally changed `add_numbers` to use `-` instead of `+`, running the script would stop instantly pointing directly to the failing `assert` line!

---

## 🧪 5. Introduction to `unittest`

While simple `assert` statements are nice, they stop at the first failure. Professional engineers use Python's built-in **`unittest`** testing framework to run dozens of tests and produce a structured summary report!

```python
import unittest
```

---

## 🏗️ 6. Writing Your First Test Case

To create a unit test suite, we define a class inheriting from `unittest.TestCase` and write test methods whose names begin with `test_`:

```python
import unittest

def add_numbers(first_number, second_number):
    return first_number + second_number


class CalculatorTest(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(5, 3)
        self.assertEqual(result, 8)
```

🔍 **Breakdown**:
- **`unittest.TestCase`**: Gives our class access to automated test engine features.
- **`test_add_numbers(self)`**: The test engine automatically discovers and runs any method starting with `test_`.
- **`self.assertEqual(result, 8)`**: Checks if `result` equals `8`. If they match, the test passes!

---

## 🏃 7. Running Tests From the Terminal

To run your tests without modifying your project scripts, run this terminal command:

```bash
# Run a specific test file
python -m unittest test_calculations.py

# Discover and run all test files inside the tests/ folder automatically
python -m unittest discover -s tests
```

### Example Terminal Output:
```text
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

Each dot (`.`) represents one passed test!

---

## 🔧 8. Core `unittest` Assertions

Here are the four most common assertions you will use:

| Assertion Method | Checks | Example |
| :--- | :--- | :--- |
| **`self.assertEqual(a, b)`** | `a == b` | `self.assertEqual(add_numbers(2, 2), 4)` |
| **`self.assertTrue(x)`** | `bool(x) is True` | `self.assertTrue(is_passed(75))` |
| **`self.assertFalse(x)`** | `bool(x) is False` | `self.assertFalse(is_passed(40))` |
| **`self.assertIn(item, list)`** | `item in list` | `self.assertIn("Sara", student_names)` |

---

## 💡 9. Designing Testable Functions

Why are some functions hard to test? Look at this function:

```python
# Hard to test automatically (prints directly to screen):
def check_pass(score):
    if score >= 50:
        print("Pass")
```

Now look at this refactored version:

```python
# Easy to test automatically (returns a clear Boolean value):
def is_passing_score(score):
    return score >= 50
```

> 💡 **Golden Rule**: Functions that **return values** are ten times easier to test than functions that only print to the screen!

---

## 📂 10. Professional Project Test Structure

Keep your production code and automated test scripts separated cleanly:

```text
student-project/
│
├── main.py               <-- Main application CLI entry point
├── calculations.py       <-- Pure calculation and search functions
└── tests/
    └── test_calculations.py  <-- Automated test suite
```

---

## 🛠️ 11. Practical Activity: Testing the Student Management System

Let us write an automated test suite verifying our core calculation and search functions!

### File 1: `calculations.py` (Core Logic)
```python
# calculations.py
def calculate_grade(average_score):
    """Returns letter grade for a numerical average score."""
    if average_score < 0 or average_score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if average_score >= 90:
        return "A"
    elif average_score >= 80:
        return "B"
    elif average_score >= 70:
        return "C"
    elif average_score >= 60:
        return "D"
    else:
        return "F"


def find_student_by_name(student_list, query_name):
    """Searches list of dictionaries for matching student name."""
    for student in student_list:
        if student["name"].lower() == query_name.lower():
            return student
    return None
```

### File 2: `tests/test_calculations.py` (Automated Test Suite)
```python
# tests/test_calculations.py
import unittest
from calculations import calculate_grade, find_student_by_name


class StudentLogicTest(unittest.TestCase):
    def test_calculate_grade_A(self):
        grade = calculate_grade(95)
        self.assertEqual(grade, "A")

    def test_calculate_grade_F(self):
        grade = calculate_grade(45)
        self.assertEqual(grade, "F")

    def test_find_student_success(self):
        students = [
            {"name": "Abel", "age": 20},
            {"name": "Sara", "age": 19}
        ]
        found = find_student_by_name(students, "sara")
        self.assertIsNotNone(found)
        self.assertEqual(found["name"], "Sara")

    def test_find_student_missing(self):
        students = [{"name": "Abel", "age": 20}]
        found = find_student_by_name(students, "David")
        self.assertIsNone(found)


if __name__ == "__main__":
    unittest.main()
```

Run your suite from the terminal:
```bash
python -m unittest tests/test_calculations.py
```

---

## 📝 12. Practice Exercises

Try writing unit tests on your own!

### Beginner
1. **Assertion Practice**: Write a script with `assert len(["apple", "banana"]) == 2` and verify it passes.
2. **First `unittest` Class**: Create a test file verifying that `"python".upper()` equals `"PYTHON"` using `self.assertEqual()`.

### Intermediate
3. **Testing Arithmetic**: Write a function `subtract(a, b)` and create a `unittest.TestCase` verifying positive, negative, and zero results.
4. **Testing Membership**: Create a test verifying that `"Math"` is inside the list `["Math", "Science", "English"]` using `self.assertIn()`.

### Challenge
5. **Testing Dictionary Keys**: Write a unit test verifying that calling your `create_student("Abel", 20, "CS")` builder function returns a dictionary containing the exact keys `"name"`, `"age"`, and `"department"`.

---

## 📋 13. Testing Checklist

Before releasing any Python application, verify:
- [ ] Core business logic functions return values rather than printing directly.
- [ ] Test files are organized inside a clean `tests/` folder.
- [ ] Test methods begin with `test_` so `unittest` discovers them automatically.
- [ ] Both valid successes and missing/edge cases are tested.
- [ ] Running `python -m unittest discover` reports `OK` with zero errors!

---

## ❓ 14. Review Questions

1. Why are automated unit tests better than manual menu testing?
2. What happens when a Python `assert` condition evaluates to `False`?
3. What class must your test suite inherit from (`unittest.TestCase`)?
4. What prefix must every automated test method name have?
5. Why is separating pure calculation logic from CLI menu prints essential for automated testing?

---

## ✅ 15. Learning Checklist

- [ ] I understand the difference between manual testing and automated verification.
- [ ] I can write quick inline checks using `assert`.
- [ ] I can create automated test classes using `unittest.TestCase`.
- [ ] I can verify results using `assertEqual`, `assertTrue`, `assertFalse`, and `assertIn`.
- [ ] I can run test suites from the terminal using `python -m unittest`.

---

## 🏁 16. Session Summary

- **Automated Testing** verifies software correctness rapidly without manual repetitive typing.
- **`unittest.TestCase`** provides a professional framework for grouping and running assertions.
- Functions designed to **return values** are easily testable and reliable.
- Adding automated unit tests to our project guarantees that future feature additions will never break existing Student Management functionality!
