"""
Challenge Solution: Class-Based Contact Manager
Week Six — Session Two
"""

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactBook:
    def __init__(self):
        self.contacts = []
    def add(self, name, phone):
        self.contacts.append(Contact(name, phone))
    def search(self, name):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                return f"{c.name}: {c.phone}"
        return "Not found."

book = ContactBook()
book.add("Abel", "0911000000")
print(book.search("abel"))
