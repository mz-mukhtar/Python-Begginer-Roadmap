"""
ContactManager Service Controller
"""

import json
import csv
from pathlib import Path
from models.contact import Contact

class ContactManager:
    def __init__(self, json_path="data/contacts.json", csv_path="data/contacts.csv"):
        self.json_path = Path(json_path)
        self.csv_path = Path(csv_path)
        self.json_path.parent.mkdir(exist_ok=True)
        self.contacts = self.load()

    def load(self):
        if not self.json_path.exists():
            return []
        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                return [Contact.from_dict(d) for d in json.load(f)]
        except Exception:
            return []

    def save(self):
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4)

    def add_contact(self, cid, name, phone, email, cat):
        if any(c.contact_id == cid for c in self.contacts):
            return False, "Contact ID already exists."
        self.contacts.append(Contact(cid, name, phone, email, cat))
        self.save()
        return True, "Contact added successfully."

    def search_contact(self, query):
        return [c for c in self.contacts if query.lower() in c.name.lower() or query.lower() in c.category.lower()]

    def update_contact(self, cid, new_phone, new_email):
        for c in self.contacts:
            if c.contact_id == cid:
                c.phone = new_phone
                c.email = new_email
                self.save()
                return True
        return False

    def delete_contact(self, cid):
        for i, c in enumerate(self.contacts):
            if c.contact_id == cid:
                del self.contacts[i]
                self.save()
                return True
        return False

    def export_csv(self):
        with open(self.csv_path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["Contact ID", "Name", "Phone", "Email", "Category"])
            for c in self.contacts:
                w.writerow([c.contact_id, c.name, c.phone, c.email, c.category])
        return self.csv_path
