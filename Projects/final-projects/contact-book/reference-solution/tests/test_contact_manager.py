"""
Automated Unit Tests for Contact Book
"""

import unittest
from pathlib import Path
from services.contact_manager import ContactManager

class TestContactManager(unittest.TestCase):
    def setUp(self):
        self.test_json = Path("data/test_contacts.json")
        if self.test_json.exists():
            self.test_json.unlink()
        self.manager = ContactManager(self.test_json)

    def tearDown(self):
        if self.test_json.exists():
            self.test_json.unlink()

    def test_crud(self):
        ok, _ = self.manager.add_contact("CON-100", "Abel", "0911", "abel@example.com", "Friend")
        self.assertTrue(ok)
        self.assertEqual(len(self.manager.search_contact("Abel")), 1)
        self.assertTrue(self.manager.delete_contact("CON-100"))

if __name__ == "__main__":
    unittest.main()
