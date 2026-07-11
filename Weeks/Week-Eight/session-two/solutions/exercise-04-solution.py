"""
Exercise 4 Solution: Display Status Messages
Week Eight — Session Two
"""

def status(success, text):
    print(f"✅ {text}" if success else f"❌ {text}")
status(True, "Operation completed.")
