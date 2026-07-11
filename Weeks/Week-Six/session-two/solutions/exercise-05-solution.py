"""
Exercise 5 Solution: Create Manager Class
Week Six — Session Two
"""

class ContactManager:
    def __init__(self):
        self.contacts = []
    def add_contact(self, name):
        self.contacts.append(name)

cm = ContactManager()
cm.add_contact("Abel")
print("Contacts count:", len(cm.contacts))
