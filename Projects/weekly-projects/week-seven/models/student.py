"""
Student Domain Model
Week Seven — Python Beginner Roadmap
"""

class Student:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "major": self.major
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["student_id"], data["name"], data["major"])

    def __str__(self):
        return f"[{self.student_id}] {self.name} - {self.major}"
