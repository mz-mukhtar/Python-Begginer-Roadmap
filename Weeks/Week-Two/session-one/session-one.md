# 📘 Week 2 – Session 1: Loops and Repetition in Python

Welcome to **Week 2 – Session 1**! 🎉

This session is all about one of the most powerful tools in programming: **loops**. Loops allow you to **repeat tasks**, automate processes, and handle lots of data with just a few lines of code.

By the end of this session, you’ll be able to:
- Use `while` and `for` loops
- Loop through numbers and text
- Create simple countdowns and number sequences
- Use `break` and `continue` statements
- Combine loops with logic to build smarter programs

---

## 🧠 Why Loops?

Imagine needing to print:
```
print("Hello!")
print("Hello!")
print("Hello!")
```
That works... but it's repetitive and inefficient.

Instead, you can use a loop:
```
for i in range(3):
    print("Hello!")
```

---

## 🔄 1. The `while` Loop

Repeats while a condition is True.
🧑‍💻 Example:
```
i = 1
while i <= 5:
    print("Count:", i)
    i += 1
```
🔍 Breakdown:

- Starts at `i = 1`

- As long as `i <= 5`, keep printing

- Each time, add 1 to `i`

⚠️ Be careful of infinite loops:
```
while True:
    print("This never ends!")  # Press Ctrl+C to stop
```

---

## 🔁 2. The `for` Loop + `range()`

Use `for` when you know how many times you want to loop.
```
for i in range(5):
    print("i =", i)
```
🧮 `range(start, stop, step)`:
```
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9
```

---

## 🧪 3. Loop Practice Tasks
🔸 Count from 1 to 10
```
for i in range(1, 11):
    print(i)
```
🔸 Countdown
```
i = 5
while i > 0:
    print(i)
    i -= 1
print("Blast off!")
```
🔸 Print even numbers between 1 and 20
```
for i in range(2, 21, 2):
    print(i)
```

---

## 🔄 4. `break` and `continue`
🛑 `break`: Stop the loop early
```
for i in range(10):
    if i == 5:
        break
    print(i)
```
➿ `continue`: Skip the rest of the loop and go to the next cycle
```
for i in range(10):
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)
```

---

## 🔐 5. Login System Using a Loop

Let’s revisit the login system — now with a loop.
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
        print("Incorrect! Attempts left:", attempts)

if attempts == 0:
    print("Account locked.")
```
### 🧠 Homework Tasks
#### Task 1: Print the multiplication table of a number

Input a number and print its table from 1 to 10
```
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
```
#### Task 2: Password Retry

  Ask for a password using a loop. Give unlimited attempts until the user types the correct password.
```
correct = "python123"
while True:
    guess = input("Enter password: ")
    if guess == correct:
        print("Welcome!")
        break
    else:
        print("Try again.")
```
