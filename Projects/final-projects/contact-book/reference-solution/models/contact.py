"""
Contact Domain Model (Reference Solution)
"""

class Contact:
    def __init__(self, contact_id, name, phone, email, category):
        self.contact_id = contact_id
        self.name = name
        self.phone = phone
        self.email = email
        self.category = category

    def to_dict(self):
        return {
            "contact_id": self.contact_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "category": self.category
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["contact_id"], data["name"], data["phone"], data["email"], data["category"])

    def __str__(self):
        return f"[{self.contact_id}] {self.name} | Phone: {self.phone} | Email: {self.email} | Cat: {self.category}"
