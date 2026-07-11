"""
Reference Entrypoint for Contact Book Capstone
"""

from services.contact_manager import ContactManager

def main():
    manager = ContactManager()

    while True:
        print("")
        print("========================================")
        print("         CONTACT BOOK CAPSTONE          ")
        print("========================================")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export Contacts")
        print("7. Exit")
        print("========================================")

        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            cid = input("Enter ID (e.g., CON-002): ").strip()
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone: ").strip()
            email = input("Enter Email: ").strip()
            cat = input("Enter Category (Work/Personal): ").strip()
            ok, msg = manager.add_contact(cid, name, phone, email, cat)
            print(f"{'✅' if ok else '❌'} {msg}")

        elif choice == "2":
            for c in manager.contacts:
                print(c)

        elif choice == "3":
            query = input("Enter Name or Category to search: ").strip()
            for m in manager.search_contact(query):
                print(m)

        elif choice == "4":
            cid = input("Enter ID to update: ").strip()
            phone = input("Enter New Phone: ").strip()
            email = input("Enter New Email: ").strip()
            print("✅ Updated." if manager.update_contact(cid, phone, email) else "❌ ID not found.")

        elif choice == "5":
            cid = input("Enter ID to delete: ").strip()
            print("✅ Deleted." if manager.delete_contact(cid) else "❌ ID not found.")

        elif choice == "6":
            print(f"✅ Exported CSV to {manager.export_csv()}")

        elif choice == "7":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
