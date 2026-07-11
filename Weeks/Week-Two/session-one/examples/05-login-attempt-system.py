"""
Example: Interactive login attempt loop.
Week Two — Session One
"""

secret = "python"
attempts = 0

while attempts < 3:
    guess = input("Enter secret keyword: ")
    if guess == secret:
        print("Login successful!")
        break
    else:
        attempts += 1
        print("Wrong keyword. Attempts left:", 3 - attempts)
