"""
Challenge Solution: Number Guessing Game
Week Five — Session Two
"""

import random

secret = random.randint(1, 100)
attempts = 0

print("=== 1-100 Number Guessing Game ===")
while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid integer!")
        continue

    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"🎉 Correct! Secret was {secret} (Guessed in {attempts} turns)")
        break
