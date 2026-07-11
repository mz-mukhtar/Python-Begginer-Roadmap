# 📘 Week 6 – Session 2: Class Design and Multi-Class Applications

Welcome to **Week 6 – Session 2**! 🚀

In Session 1, you learned how to define basic Python classes and create objects. Today, we will learn how to design professional classes using the **Single Responsibility Principle**, preview **Composition over Inheritance**, and build applications where **multiple classes work together cleanly**.

---

## ✅ Learning Objectives

By the end of this session, you will be able to:
- Explain and apply the **Single Responsibility Principle (SRP)** in class design
- Understand **Composition** (how one object can contain another object)
- Build modular applications using cooperating classes (`Student` and `StudentManager`)
- Prevent bloated classes by splitting responsibilities cleanly

---

## 🎯 1. Single Responsibility Principle (Class Design)

When beginners start writing Object-Oriented code, a common mistake is putting *everything* into one giant class.

### What Is the Single Responsibility Principle?
The **Single Responsibility Principle (SRP)** states that **a class should have only one reason to change**—meaning it should represent **one single concept or entity**.

#### ❌ Bloated Class (Too Many Responsibilities)
```python
class StudentSystem:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def calculate_grade(self):
        pass

    def save_to_json(self):
        pass

    def render_cli_menu(self):
        pass
```
*Why this is problematic:* This class is trying to be a student record, a file database, and a user interface menu all at once!

#### ✅ Clean Separation of Responsibilities
Instead, separate entities into clean, focused classes:
1. **`Student` class**: Holds individual student data (`id`, `name`, `age`, `major`).
2. **`StudentManager` class**: Manages the collection of students (add, search, delete, save/load).

---

## 🧩 2. Composition Over Inheritance (Introductory Preview)

In Object-Oriented Programming, how do we connect different classes?

### What Is Composition?
**Composition** means one class **contains** another class as an attribute—often described as a **"HAS-A"** relationship.

For example:
- A `Student` **HAS-A** `ContactInfo`
- A `University` **HAS-A** list of `Student` objects

```python
class ContactInfo:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

class Student:
    def __init__(self, name, email, phone):
        self.name = name
        # Student contains a ContactInfo object!
        self.contact = ContactInfo(email, phone)

student1 = Student("Abel", "abel@example.com", "0911000000")
print(f"{student1.name}'s email is {student1.contact.email}")
```

> 💡 *Note: Next week in Week 7, we will explore **Inheritance** ("IS-A" relationships). However, modern software engineering favors **Composition over Inheritance** whenever possible because it keeps classes simpler and more modular!*

---

## 🏗️ 3. Structuring Multi-Class Applications

Let's see how separating our Student Management System into two collaborating classes makes our program clean and scalable:

### Class 1: Data Blueprint (`Student`)
```python
class Student:
    """Represents a single student entity."""
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Major: {self.major}"
```

### Class 2: Manager Blueprint (`StudentManager`)
```python
class StudentManager:
    """Manages a collection of Student objects."""
    def __init__(self):
        self.students = []  # List holding Student objects

    def add_student(self, name, age, major):
        new_id = len(self.students) + 1
        student = Student(new_id, name, age, major)
        self.students.append(student)
        print(f"✅ Student '{name}' registered successfully!")

    def list_students(self):
        if not self.students:
            print("No students registered.")
            return
        print("\n--- Student Roster ---")
        for student in self.students:
            print(student)  # Uses Student.__str__() automatically!
```

### Main Application Controller
```python
if __name__ == "__main__":
    manager = StudentManager()

    # Adding students via manager
    manager.add_student("Abel", 20, "Computer Science")
    manager.add_student("Sara", 19, "Electrical Engineering")

    # Displaying all students
    manager.list_students()
```

✅ Output:
```text
✅ Student 'Abel' registered successfully!
✅ Student 'Sara' registered successfully!

--- Student Roster ---
ID: 1 | Name: Abel | Age: 20 | Major: Computer Science
ID: 2 | Name: Sara | Age: 19 | Major: Electrical Engineering
```

---

## 🧪 4. Practice Exercises

### Exercise 1: Single Responsibility Refactor
Look at a script where one class handles user input, calculation, and printing. Refactor it into two classes: `Order` (stores item name and price) and `OrderPrinter` (displays receipt).

### Exercise 2: Composition with Author and Book
Create an `Author` class (`name`, `country`) and a `Book` class (`title`, `author_obj`). Create an author and pass it into a book object. Print the book title alongside the author's country.

---

## 🏁 5. Session Summary

- **Single Responsibility Principle (SRP)**: Each class should represent one single concept or entity.
- **Composition**: Classes can contain instances of other classes ("HAS-A" relationship) to organize structured data cleanly.
- **Multi-Class Applications**: Separating entity models (`Student`) from manager logic (`StudentManager`) makes code modular, maintainable, and easy to test.
