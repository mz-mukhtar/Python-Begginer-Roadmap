"""
Challenge Solution: Personal Notes Application
Week Four — Session Two
"""

def add_note(note):
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("✅ Note saved.")

def view_notes():
    with open("notes.txt", "r") as f:
        print("\n--- MY NOTES ---")
        print(f.read())

add_note("Finish Week 4 Session 2")
view_notes()
