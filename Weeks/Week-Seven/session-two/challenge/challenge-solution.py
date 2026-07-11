"""
Challenge Solution: Production-Ready Student Model
Week Seven — Session Two
"""

class Student:
    def __init__(self, student_id, name, age, major):
        if age < 0:
            raise ValueError("Age must be positive")
        self.student_id = int(student_id)
        self.name = str(name).strip().title()
        self.age = int(age)
        self.major = str(major).strip()

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "major": self.major
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["student_id"], data["name"], data["age"], data["major"])

    def __str__(self):
        return f"[{self.student_id}] {self.name} | Age: {self.age} | Major: {self.major}"

s = Student(101, "abel tadesse", 20, "CS")
print("Production Student:", s)
