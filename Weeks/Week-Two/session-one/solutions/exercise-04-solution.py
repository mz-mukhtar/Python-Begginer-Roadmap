"""
Exercise 4 Solution: Password Attempt System
Week Two — Session One
"""

attempts = 0
while attempts < 3:
    pwd = input("Enter password: ")
    if pwd == "admin":
        print("Access Granted!")
        break
    attempts += 1
else:
    print("Account locked.")
