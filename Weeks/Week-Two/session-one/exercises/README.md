# 🧑💻 Session Exercises

Complete these exercises after reading the lesson and running the examples.

---

## Exercise 1 — Count from 1 to 10

### Goal

Practice writing a simple `for` loop using `range()`.

### Requirements

- Print numbers from 1 to 10 inclusive

### Example Output

```text
1
2
...
10
```

### Starter File

Open:

`starter/exercise-01.py`

### Hint

Remember that `range(1, 11)` stops before 11.

---

## Exercise 2 — Display Even Numbers

### Goal

Practice filtering numbers inside a loop.

### Requirements

- Loop through numbers 1 to 20
- Print only even numbers (`num % 2 == 0`)

### Example Output

```text
2
4
6
...
20
```

### Starter File

Open:

`starter/exercise-02.py`

### Hint

You can either use `if num % 2 == 0` or `range(2, 21, 2)`.

---

## Exercise 3 — Multiplication Table

### Goal

Generate a multiplication table for the number 5.

### Requirements

- Print `5 x 1 = 5` up to `5 x 10 = 50`

### Example Output

```text
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

### Starter File

Open:

`starter/exercise-03.py`

### Hint

Loop `i` from 1 to 10 and print `5 * i`.

---

## Exercise 4 — Password Attempt System

### Goal

Use a `while` loop to give the user 3 login attempts.

### Requirements

- Secret password is `"admin"`
- Stop immediately if correct
- Print failure warning if wrong

### Example Output

```text
Enter password: guest
Wrong! Try again.
Enter password: admin
Access Granted!
```

### Starter File

Open:

`starter/exercise-04.py`

### Hint

Use `break` when login succeeds.

---

## Exercise 5 — Number Total Calculator

### Goal

Use accumulator pattern inside a loop.

### Requirements

- Calculate sum of integers from 1 to 100
- Display total sum (`5050`)

### Example Output

```text
Total sum from 1 to 100 is: 5050
```

### Starter File

Open:

`starter/exercise-05.py`

### Hint

Start with `total = 0` outside the loop and add inside.
