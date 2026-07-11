"""
Exercise 3 Solution: Book Class
Week Six — Session One
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def summary(self):
        return f"{self.title} by {self.author}"

b = Book("Python 101", "Mahi Zeki")
print(b.summary())
