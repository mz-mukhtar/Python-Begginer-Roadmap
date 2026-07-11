"""
Challenge Solution: Student System Architecture Prototype
Week Seven — Session One
"""

class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name

def get_demo_roster():
    return [Student(101, "Abel"), Student(102, "Sara")]

def display_roster(roster):
    print("=== SYSTEM ROSTER PROTOTYPE ===")
    for s in roster:
        print(f"[{s.sid}] {s.name}")

display_roster(get_demo_roster())
