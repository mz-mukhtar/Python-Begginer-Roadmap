# 📘 Week Six – Session Three: Basic Inheritance and OOP Project

Welcome back! 👋

In Sessions One and Two of Week Six, you entered the world of **Object-Oriented Programming (OOP)**. You learned how to design blueprints using **Classes** (`class`), instantiate distinct **Objects**, initialize attributes using `__init__()`, write class **Methods**, and manage collections of objects.

In this session, you will learn one of the most powerful concepts in OOP: **Inheritance**. Inheritance allows a new child class to adopt attributes and methods from an existing parent class—saving you from writing duplicate code! Finally, we will bring our entire Object-Oriented journey together by building the **Object-Oriented Student Management System**!

---

## 🎯 Learning Objectives

By the end of this session, you will be able to:
- Briefly review classes, objects, attributes, methods, `__init__()`, and `self`
- Explain what inheritance is and why child classes reuse parent behavior
- Design a parent class (`User`) and extend it into a child class (`Student`)
- Use `super().__init__()` to initialize parent attributes cleanly inside child constructors
- Identify when inheritance improves code and when to avoid unnecessary inheritance
- Divide architectural responsibilities between data objects (`Student`) and controllers (`StudentManager`)
- Build, run, and explain the **Object-Oriented Student Management System** project

---

## 📌 1. Quick Review: Classes and Objects

Before jumping into inheritance, let us do a 60-second recap:
- **Class**: A blueprint or recipe defining attributes and methods.
- **Object**: A live instance created from a class.
- **`__init__()`**: The constructor automatically called when an object is created.
- **`self`**: Refers to the specific object currently being operated on.

---

## 🧬 2. What Is Inheritance?

Imagine building a university system. You need to represent Students, Teachers, and Librarians.
- Every person has a `name`, `email`, and `user_id`.
- But only a **Student** has a `GPA` and `enroll_course()`.
- Only a **Teacher** has a `salary` and `assign_grade()`.

Instead of copying and pasting `name`, `email`, and `user_id` into three different classes, we create a single parent class named `User`. Then, `Student` and `Teacher` **inherit** from `User`!

```text
       Parent Class: User (name, email)
          /                    \
Child Class: Student        Child Class: Teacher
  (+ course, GPA)             (+ salary, department)
```

> **A child class can reuse attributes and methods from a parent class while adding its own specialized capabilities.**

---

## 🏛️ 3. Creating a Parent Class

Let us create our parent class `User`:

```python
class User:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name: {self.name}")
```

---

## 👶 4. Creating a Child Class

To inherit from a parent class, put the parent class name inside parentheses after the child class name:

```python
class Student(User):
    def study(self):
        print(f"{self.name} is studying.")
```

---

## 🚀 5. Creating Child Objects and Method Reuse

Look at how our `Student` object can immediately call `.display_name()` even though we never wrote `display_name()` inside `class Student`:

```python
student_1 = Student("Abel")

# Reusing parent method
student_1.display_name()

# Calling child-specific method
student_1.study()
```

### Example Output:
```text
Name: Abel
Abel is studying.
```

---

## 🎒 6. Adding Child-Specific Attributes (`super()`)

What if our child class needs its own attributes? We use Python's **`super()`** function to let the parent initialize its own attributes first:

```python
class User:
    def __init__(self, name):
        self.name = name


class Student(User):
    def __init__(self, name, course):
        # Let parent User initialize 'name'
        super().__init__(name)
        # Initialize child-specific 'course'
        self.course = course

    def display_student_profile(self):
        print(f"Student: {self.name} | Enrolled in: {self.course}")


student_2 = Student("Sara", "Computer Science")
student_2.display_student_profile()
```

Think of `super().__init__(name)` as saying: *"Hey parent class, please handle your part of the setup first!"*

---

## ⚖️ 7. When Inheritance Is Useful (And When It Is Not!)

Inheritance is fantastic when two classes share an obvious **"IS-A"** relationship:
- A `Student` **IS A** `User`.
- A `Car` **IS A** `Vehicle`.

> 💡 **Golden Advice**: **Do not use inheritance only because it exists.** If two classes do not share related attributes and behavior (for example, a `Student` and a `FileSaver`), keep them completely separate!

---

## 🏗️ 8. Dividing Class Responsibilities

In professional Object-Oriented software, we divide responsibilities into two distinct types of classes:

```text
Student Class
Stores data and attributes for ONE individual student
  ↓
StudentManager Class
Controls collections of students, disk saving, loading, and menu workflows
```

---

## 🛠️ 9. Weekly Project: Object-Oriented Student Management System

Let us build our complete Week Six capstone project: the **Object-Oriented Student Management System**!

### 📋 Required Classes & Architecture
- **`User` (Parent Class)**: Stores `name` and provides basic identity behavior.
- **`Student` (Child Class)**: Inherits from `User`, adds `age` and `department`, and can convert itself to/from dictionary format for JSON serialization.
- **`StudentManager` (Controller Class)**: Manages our list of `Student` objects, handles JSON disk loading/saving, and runs CRUD operations.

*(Note: To keep everything easy to follow in this lesson, we write our classes in one file. Next week in Week Seven, you will learn how to organize classes across clean multi-file project modules!)*

### Complete Runnable Code

```python
# ==========================================
# Project: Object-Oriented Student Management System
# Week Six Capstone Project
# ==========================================

import json
import os


# 1. PARENT CLASS
class User:
    """Parent blueprint representing a general system user."""
    def __init__(self, name):
        self.name = name


# 2. CHILD CLASS (INHERITING FROM USER)
class Student(User):
    """Child class representing a student with age and department."""
    def __init__(self, name, age, department):
        super().__init__(name)
        self.age = age
        self.department = department

    def to_dict(self):
        """Converts object attributes into a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "age": self.age,
            "department": self.department
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Student object from a dictionary read from JSON."""
        return cls(data["name"], data["age"], data["department"])

    def display_info(self):
        """Prints formatted student profile."""
        print(f"Name: {self.name} | Age: {self.age} | Department: {self.department}")


# 3. CONTROLLER CLASS
class StudentManager:
    """Controller class responsible for managing student collections and disk storage."""
    def __init__(self, filename="students_oop.json"):
        self.filename = filename
        self.students = []
        self.load_from_disk()

    def load_from_disk(self):
        """Loads JSON data and instantiates Student objects."""
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r") as file:
                data_list = json.load(file)
                self.students = [Student.from_dict(item) for item in data_list]
        except Exception as e:
            print(f"⚠️ Could not load file: {e}")

    def save_to_disk(self):
        """Serializes all Student objects to JSON file."""
        try:
            data_list = [student.to_dict() for student in self.students]
            with open(self.filename, "w") as file:
                json.dump(data_list, file, indent=4)
            print("💾 All student objects saved to disk!")
        except Exception as e:
            print(f"❌ Save error: {e}")

    def add_student(self, name, age, department):
        new_student = Student(name, age, department)
        self.students.append(new_student)
        print(f"✅ Registered student '{name}'.")

    def view_all(self):
        print("\n--- Registered Student Profiles ---")
        if not self.students:
            print("No students registered.")
            return

        for idx, student in enumerate(self.students, start=1):
            print(f"{idx}. ", end="")
            student.display_info()

    def search_student(self, query_name):
        for student in self.students:
            if student.name.lower() == query_name.lower():
                print("\n✅ Match Found:")
                student.display_info()
                return
        print(f"❌ No student found named '{query_name}'.")

    def update_student(self, query_name, new_age, new_department):
        for student in self.students:
            if student.name.lower() == query_name.lower():
                student.age = new_age
                student.department = new_department
                print(f"✅ Updated record for '{student.name}'.")
                return
        print(f"❌ No student found named '{query_name}'.")

    def delete_student(self, query_name):
        for student in self.students:
            if student.name.lower() == query_name.lower():
                self.students.remove(student)
                print(f"✅ Removed student '{student.name}'.")
                return
        print(f"❌ No student found named '{query_name}'.")


def display_menu():
    print("\n==========================================")
    print("  OOP STUDENT MANAGEMENT SYSTEM           ")
    print("==========================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Students")
    print("7. Exit")
    print("==========================================")


def main():
    manager = StudentManager()

    while True:
        display_menu()
        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            age = int(input("Enter age: "))
            dept = input("Enter department: ").strip()
            manager.add_student(name, age, dept)
        elif choice == "2":
            manager.view_all()
        elif choice == "3":
            query = input("Enter name to search: ").strip()
            manager.search_student(query)
        elif choice == "4":
            query = input("Enter name to update: ").strip()
            age = int(input("Enter new age: "))
            dept = input("Enter new department: ").strip()
            manager.update_student(query, age, dept)
        elif choice == "5":
            query = input("Enter name to delete: ").strip()
            manager.delete_student(query)
        elif choice == "6":
            manager.save_to_disk()
        elif choice == "7":
            manager.save_to_disk()
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid selection.")


# Start OOP Application
main()
```

---

## 📝 10. Practice Exercises

Try these exercises to practice Object-Oriented inheritance!

### Beginner
1. **`Person` and `Student`**: Create a parent class `Person(name)` and a child class `Student(name, school)`. Create an instance and print both attributes.
2. **`Vehicle` and `Car`**: Create a `Vehicle(brand)` class with a `.drive()` method printing `"Driving forward"`. Create a `Car` child class that inherits `.drive()`.

### Intermediate
3. **`User` and `Admin`**: Create a `User(username)` class. Create an `Admin(username, access_level)` child class that uses `super().__init__(username)` and prints `"Admin access granted"`.
4. **`Product` Class**: Create a `Product(name, price)` class with a `.discount(percent)` method that reduces the price.

### Challenge
5. **Object Collection**: Create a list of 3 `Product` objects. Loop through the list and print only items where `price < 50`.

---

## 🚀 11. Weekly Challenge: Convert an Existing Project to Classes

Choose one of your previous projects (Contact Book or Expense Tracker) and redesign it using OOP:
- Create an individual data class (`Contact` or `Expense`).
- Create a manager class (`ContactManager` or `ExpenseManager`).
- Add a `.to_dict()` method for saving to JSON disk files.

---

## ❓ 12. Review Questions

1. What syntax tells Python that a child class is inheriting from a parent class?
2. What is the purpose of `super().__init__()` inside a child class constructor?
3. Can a child class define methods that do not exist in the parent class?
4. Why is separating `Student` (data model) from `StudentManager` (controller) better than putting everything into one class?
5. When should you avoid using inheritance?

---

## ✅ 13. Learning Checklist

- [ ] I can explain Object-Oriented inheritance and why child classes reuse parent code.
- [ ] I can create parent classes and extend them into specialized child classes.
- [ ] I can use `super().__init__()` to pass parameters up to the parent constructor.
- [ ] I can separate data model classes from controller classes.
- [ ] I can build and explain the Object-Oriented Student Management System.

---

## 🏁 14. Session Summary

- **Inheritance** (`class Child(Parent):`) allows child classes to inherit attributes and methods from a parent class.
- **`super()`** invokes parent class constructors cleanly.
- Separating individual data blueprints (`Student`) from application controllers (`StudentManager`) gave our **Object-Oriented Student Management System** clean, highly maintainable architecture!
