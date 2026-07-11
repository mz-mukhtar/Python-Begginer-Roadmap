"""
Student Domain Model (Reference Solution)
"""

class Student:
    def __init__(self, student_id, name, age, department, email, courses=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.department = department
        self.email = email
        self.courses = courses if courses is not None else []

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "email": self.email,
            "courses": self.courses
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["name"],
            data["age"],
            data["department"],
            data["email"],
            data.get("courses", [])
        )

    def __str__(self):
        courses_str = ", ".join(self.courses) if self.courses else "None"
        return f"[{self.student_id}] {self.name} ({self.age}) | Dept: {self.department} | Email: {self.email} | Courses: {courses_str}"
