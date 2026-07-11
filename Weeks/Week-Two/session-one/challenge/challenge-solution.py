"""
Challenge Solution: Number Guessing Logic
Week Two — Session One
"""

secret_number = 25
attempts = 0

print("=== Number Guessing Game ===")
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"🎉 Correct! You guessed {secret_number} in {attempts} attempts!")
        break
