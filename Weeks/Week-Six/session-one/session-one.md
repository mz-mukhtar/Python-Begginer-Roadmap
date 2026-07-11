# 📘 Week 6 – Session 1: Introduction to Object-Oriented Programming

Welcome to **Week 6 – Session 1**! 🎉

Until today, we have written programs using functions, variables, lists, and dictionaries. This style of coding is called **Procedural Programming**. While procedural programming works well for small scripts, it can get disorganized when an application grows larger.

Today, you are going to learn one of the most important concepts in modern software engineering: **Object-Oriented Programming (OOP)**.

By the end of this session, you will be able to:
- Understand the difference between a **Class** and an **Object**
- Define your own Python classes using the `class` keyword
- Initialize object attributes using the `__init__()` method and `self` keyword
- Create multiple independent objects from one blueprint
- Write class **methods** to perform actions on object data
- Convert function-based code into clean, class-based code

---

## 🌍 1. What Is Object-Oriented Programming?

In Object-Oriented Programming (OOP), we organize code around **objects** that represent real-life things. Every real-world object has two characteristics:
1. **Attributes (Data / Characteristics)**: What the object *has* or *is*.
2. **Methods (Actions / Behavior)**: What the object *can do*.

Let’s look at some everyday examples:
- **Student**:
  - *Attributes*: name, age, ID number, course
  - *Methods*: study, take exam, display student info
- **Car**:
  - *Attributes*: brand, color, speed
  - *Methods*: drive, brake, honk
- **Phone**:
  - *Attributes*: model, battery level, phone number
  - *Methods*: make call, send message, recharge
- **Bank Account**:
  - *Attributes*: account owner, balance
  - *Methods*: deposit money, withdraw money

### Blueprint vs. Object
- A **Class** is the **blueprint** (design template).
- An **Object** is an actual item created using that blueprint.

Think of house architectural plans: the drawing on paper is the **Class**. The physical house built from that drawing is the **Object**!

---

## 🏗️ 2. Creating a Class

Let’s create our very first Python class using the `class` keyword. By Python convention, class names start with a Capital letter:

```python
class Student:
    pass
```

🔍 **Breakdown:**
- `class Student:` tells Python we are designing a blueprint named `Student`.
- `pass` is a placeholder keyword that means "empty block for now."

---

## 📦 3. Creating Objects

Now let's create an **object** (also called an *instance*) from our `Student` blueprint:

```python
student_one = Student()
print(student_one)
```

When you run this, Python creates a brand-new `Student` object in memory!

---

## ⚙️ 4. The `__init__()` Method

An empty blueprint isn't very useful yet. We want every `Student` object to start with custom information like `name` and `age`.

To do this, we use a special built-in method called `__init__()` (short for *initialize* / constructor):

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

🔍 **Breakdown:**
- `__init__()` runs **automatically** whenever you create a new object.
- `self.name = name` stores the passed `name` argument inside the object's personal `name` attribute.

### Why Do We Need `self`?
**`self`** represents the specific object instance being manipulated. When you have two objects (`student1` and `student2`), passing `self` automatically tells Python whether to access or modify `student1`'s data or `student2`'s data!

---

## 5. Class Variables Versus Instance Variables

In Python classes, variables can be defined in two places:

### 1️⃣ Instance Variables (Unique to Each Object)
Defined inside `__init__()` using `self.variable_name`. Each object gets its own separate copy:
```python
class Student:
    def __init__(self, name):
        self.name = name  # Instance variable (unique for each student)
```

### 2️⃣ Class Variables (Shared Across All Objects)
Defined directly inside the class body outside `__init__()`. All objects share the same value:
```python
class Student:
    school_name = "Addis Ababa University"  # Class variable (shared across all students)

    def __init__(self, name):
        self.name = name

student1 = Student("Abel")
student2 = Student("Sara")

print(student1.school_name)  # Addis Ababa University
print(student2.school_name)  # Addis Ababa University
```

---

## 6. String Representation (`__str__()`)

If you print an object directly (`print(student1)`), Python displays an unreadable memory address:
```text
<__main__.Student object at 0x7f8b1c2a3e10>
```

To make objects print clean, human-readable text, define the built-in **`__str__()`** method:
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student({self.name}, {self.age} yrs)"

student1 = Student("Abel", 20)
print(student1)  # Prints: Student(Abel, 20 yrs)
```

---

## 7. Adding Methods

Attributes store data, but **Methods** let objects perform actions. A method is simply a function defined inside a class. Remember to always include `self` as the first parameter!

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
```

Let’s call our method on both objects:

```python
student_one = Student("Abel", 20)
student_two = Student("Sara", 19)

print("--- Student 1 ---")
student_one.display_information()

print("--- Student 2 ---")
student_two.display_information()
```

---

## 🧑‍💻 8. OOP Example Project: Simple Class-Based Student Model

Let’s build a clean, beginner-friendly class model for our Student Management System:

```python
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_information(self):
        print(f"Name: {self.name} | Age: {self.age} | Course: {self.course}")

    def update_course(self, new_course):
        self.course = new_course
        print(f"✅ {self.name}'s course updated to {self.course}!")

# Testing our Student class
if __name__ == "__main__":
    student1 = Student("Mahlet", 21, "Electrical Engineering")
    student1.display_information()

    student1.update_course("Computer Science")
    student1.display_information()
```

---

## 🔄 9. Convert a Function-Based Program Into a Class

Let’s compare how we handled data before OOP versus after OOP.

### Before (Function-Based / Dictionaries):
```python
def display_student(name, age):
    print(name)
    print(age)

display_student("Abel", 20)
```
In function-based code, data (`name`, `age`) and logic (`display_student`) are kept separate.

---

### After (Class-Based):
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_information(self):
        print(self.name)
        print(self.age)

student = Student("Abel", 20)
student.display_information()
```

💡 **Why use classes?**
Classes bundle the data (`name`, `age`) and behavior (`display_information`) together into one clean package. 

*(Note: Classes aren't always required for simple 10-line scripts! But when building complete applications with multiple entities, OOP makes code much cleaner and easier to maintain.)*

---

## 🧪 10. Practice Exercises

Try writing these classes on your own:

1. **Create a `Car` Class**:
   - Attributes: `brand`, `model`, `year`
   - Method: `start_engine()` that prints `"The [brand] [model] engine has started!"`
2. **Create a `Book` Class**:
   - Attributes: `title`, `author`, `pages`
   - Method: `summary()` that prints `"Title by Author (Pages pages)"`
3. **Create a `BankAccount` Class**:
   - Attributes: `owner`, `balance`
   - Methods: `deposit(amount)` and `withdraw(amount)` that update the balance safely
4. **Create a `Product` Class**:
   - Attributes: `name`, `price`, `quantity`
   - Method: `total_value()` that returns `price * quantity`
5. **Create Multiple Student Objects**:
   - Create a list holding 3 different `Student` objects and loop through them to call `.display_information()` on each!

---

## ✅ 11. Session Summary

- **Object-Oriented Programming (OOP)** models real-world entities by bundling data and behavior.
- A **Class** (`class`) is a blueprint; an **Object** is an instance created from that blueprint.
- The **`__init__()`** constructor runs automatically when creating an object.
- **`self`** refers to the specific object instance being manipulated.
- **Instance Variables** are unique to each object (`self.name`); **Class Variables** are shared across all objects.
- Implementing **`__str__()`** formats objects as clean, human-readable strings.
- **Attributes** store data (`self.name`), while **Methods** define object actions (`def display_information(self):`).
