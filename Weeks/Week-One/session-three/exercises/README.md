# 🧑💻 Session Exercises

Complete these exercises after reading the lesson and running the examples.

---

## Exercise 1 — Positive or Negative

### Goal

Check if a number is positive, negative, or zero.

### Requirements

- Ask user for an integer number
- Print `"Positive"` if greater than 0
- Print `"Negative"` if less than 0
- Print `"Zero"` if equal to 0

### Example Output

```text
Enter a number: -5
Negative
```

### Starter File

Open:

`starter/exercise-01.py`

### Hint

Use `if`, `elif`, and `else`.

---

## Exercise 2 — Even or Odd

### Goal

Check if a number is even or odd using modulo `%`.

### Requirements

- Ask user for an integer
- If `number % 2 == 0`, print `"Even"`
- Otherwise print `"Odd"`

### Example Output

```text
Enter number: 8
Even
```

### Starter File

Open:

`starter/exercise-02.py`

### Hint

A number divisible by 2 has remainder 0.

---

## Exercise 3 — Age Eligibility

### Goal

Determine if user can register for a driver's license (18+).

### Requirements

- Collect age as integer
- Print `"Eligible"` if age >= 18, else `"Not Eligible"`

### Example Output

```text
Enter age: 16
Not Eligible
```

### Starter File

Open:

`starter/exercise-03.py`

### Hint

Use simple `if` and `else`.

---

## Exercise 4 — Password Checker

### Goal

Verify secret keyword access.

### Requirements

- Ask user to enter password
- If password equals `"python123"`, print `"Access Granted"`
- Otherwise print `"Access Denied"`

### Example Output

```text
Enter password: admin
Access Denied
```

### Starter File

Open:

`starter/exercise-04.py`

### Hint

Use `==` operator for equality check.

---

## Exercise 5 — Grade Classifier

### Goal

Classify numeric score into letter grades A, B, C, F.

### Requirements

- `score >= 85` -> `"A"`
- `score >= 70` -> `"B"`
- `score >= 50` -> `"C"`
- otherwise -> `"F"`

### Example Output

```text
Enter score: 75
Grade: B
```

### Starter File

Open:

`starter/exercise-05.py`

### Hint

Order your `elif` branches from highest score down.

---

## Exercise 6 — Discount Calculator

### Goal

Calculate store discount based on purchase amount.

### Requirements

- If purchase >= 1000, discount is 20%
- If purchase >= 500, discount is 10%
- Otherwise discount is 0%
- Display final price after discount

### Example Output

```text
Enter purchase amount: 600
Final Price: 540.0
```

### Starter File

Open:

`starter/exercise-06.py`

### Hint

Multiply purchase amount by `(1 - discount_rate)`.
