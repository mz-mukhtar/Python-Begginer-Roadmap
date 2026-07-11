"""
Exercise 3 Solution: User and Admin
Week Six — Session Three
"""

class User:
    def role(self): return "User"
class Admin(User):
    def role(self): return "Admin"
print(Admin().role())
