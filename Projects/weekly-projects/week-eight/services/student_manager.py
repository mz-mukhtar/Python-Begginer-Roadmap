"""
StudentManager Service Controller (Week Eight Capstone)
"""

from models.student import Student

class StudentManager:
    def __init__(self, repository):
        self.repo = repository
        self.students = [Student.from_dict(d) for d in self.repo.load()]

    def add_student(self, sid, name, major):
        if any(s.student_id == sid for s in self.students):
            return False, "Student ID already exists."
        self.students.append(Student(sid, name, major))
        self.save()
        return True, "Student added successfully."

    def find_by_id(self, sid):
        for s in self.students:
            if s.student_id == sid:
                return s
        return None

    def delete_student(self, sid):
        for i, s in enumerate(self.students):
            if s.student_id == sid:
                del self.students[i]
                self.save()
                return True
        return False

    def get_all(self):
        return self.students

    def save(self):
        self.repo.save([s.to_dict() for s in self.students])
