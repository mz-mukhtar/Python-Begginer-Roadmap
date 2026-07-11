"""
Example: Serialization (to_dict) and Deserialization (from_dict).
Week Seven — Session Two
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

s = Student(101, "Abel", "CS")
d = s.to_dict()
s2 = Student.from_dict(d)
print("Restored Student:", s2.name)
