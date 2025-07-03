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

## 📘 1. Conditional Statements: `if`, `elif`, `else`

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
