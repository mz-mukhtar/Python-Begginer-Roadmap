"""
Example: User -> Admin hierarchy.
Week Six — Session Three
"""

class User:
    def get_role(self):
        return "Standard User"

class Admin(User):
    def get_role(self):
        return "Administrator"

print(Admin().get_role())
