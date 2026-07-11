# 📘 Week 4 – Session 1: Strings in Depth

In this session, we will dive deeper into **string manipulation**, which is one of the most important skills in Python programming. Strings are everywhere: user input, file names, messages, data from the web, etc.  
By the end of this session, you’ll be able to clean, transform, format, and validate text effectively.

---

## 1. String Methods: `lower()`, `upper()`, `split()`, `join()`

Python comes with **built-in methods** for working with strings. Let's explore the most useful ones.

### `lower()`
Converts all characters in a string to **lowercase**.

```python
text = "Python is AWESOME!"
print(text.lower())
# Output: python is awesome!
```
### upper()

Converts all characters in a string to uppercase.
```
text = "Python is fun!"
print(text.upper())
# Output: PYTHON IS FUN!
```
### split()

Splits a string into a list of words (or pieces) based on a separator (default: space).
```
sentence = "I love learning Python"
words = sentence.split()
print(words)
# Output: ['I', 'love', 'learning', 'Python']

# Splitting by a comma
data = "apple,banana,grape"
fruits = data.split(",")
print(fruits)
# Output: ['apple', 'banana', 'grape']
```
### join()

Takes a list of strings and joins them back together with a chosen separator.
```
words = ['I', 'love', 'Python']
sentence = " ".join(words)
print(sentence)
# Output: I love Python

csv_format = ",".join(words)
print(csv_format)
# Output: I,love,Python
```
✅ Practice: Write a Python program that:

1. Takes a sentence as input.

2. Converts it to lowercase.

3. Splits it into words.

4. Joins them back with a `-`.

---

## 2. Indexing and Slicing Strings
### Indexing

Each character in a string has a position (index). Indexing starts at 0.
```
word = "Python"
print(word[0])   # Output: P
print(word[3])   # Output: h
print(word[-1])  # Output: n (last character)
```
### Slicing

You can extract a portion (substring) using [start:end].
```
word = "Python"
print(word[0:4])   # Output: Pyth (characters 0–3)
print(word[2:])    # Output: thon (from index 2 to end)
print(word[:3])    # Output: Pyt (from start to index 2)
print(word[-3:])   # Output: hon (last 3 characters)
```
✅ Practice: Write a program that:

- Prints the first 3 characters of "Programming".

- Prints the last 4 characters of "Programming".

- Prints characters 2–6 of "Programming".

---

## 3. Formatting with f-Strings

f-strings allow you to embed variables directly inside strings cleanly and readable.

### Why f-Strings Are Better Than String Concatenation (`+`)
Without f-strings, combining text and numbers requires converting numbers using `str()` and adding spaces carefully:
```python
name = "Sara"
score = 95
# Clunky concatenation (+)
message = "Student " + name + " scored " + str(score) + " points."
```

With **f-strings** (prefix the string with `f`), you simply put curly braces `{}` around variables:
```python
message = f"Student {name} scored {score} points."
print(message)
```

You can even do calculations inside f-strings:
```python
a = 5
b = 3
print(f"{a} + {b} = {a + b}")
# Output: 5 + 3 = 8
```

---

## 4. Input Validation: `isdigit()`, `isalpha()`, `isalnum()`

When building programs that interact with users, you should check text before converting or processing it:

- **`.isdigit()`**: Returns `True` if all characters in the string are digits (`0-9`).
- **`.isalpha()`**: Returns `True` if all characters are alphabetic letters (`a-z`, `A-Z`).
- **`.isalnum()`**: Returns `True` if all characters are letters or numbers (alphanumeric).

### Example: Safe Age Input
```python
age_input = input("Enter your age: ")

if age_input.isdigit():
    age = int(age_input)
    print(f"Next year, you will be {age + 1}!")
else:
    print("❌ Error: Please enter numbers only.")
```

---

## 5. Mini-Project: Text Analysis


We’ll build a small Text Analyzer that does the following:

1. Counts how many words are in a sentence.

2. Checks if a word is a palindrome (reads the same forwards and backwards).

### Step 1: Word Count
```
text = input("Enter a sentence: ")
words = text.split()
print(f"Your sentence has {len(words)} words.")
```
### Step 2: Palindrome Checker
```
word = input("Enter a word to check if it is a palindrome: ")

# Normalize (ignore case)
word = word.lower()

if word == word[::-1]:
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is NOT a palindrome.")
```
### Step 3: Combine Everything – Text Analyzer
```
def text_analyzer():
    text = input("Enter a sentence: ")
    words = text.split()

    print(f"\n--- Text Analysis ---")
    print(f"Total words: {len(words)}")

    # Check for palindrome words
    print("\nPalindrome words found:")
    for word in words:
        word_clean = word.lower()
        if word_clean == word_clean[::-1] and len(word_clean) > 1:
            print(f"- {word}")

# Run the analyzer
text_analyzer()
```

---

## 6. Summary

- `lower()` and `upper()` change string case.
- `split()` and `join()` break apart and combine text.
- Indexing and slicing help extract parts of strings.
- **f-strings** make formatting simple, clean, and powerful.
- **`.isdigit()`**, **`.isalpha()`**, and **`.isalnum()`** validate user input before processing.
- Mini-project: we built a text analyzer to count words and find palindromes.

---

## 🎯 Homework / Practice Tasks

   1. Ask the user for their full name and print:

       - All lowercase

       - All uppercase

       - Initials (first letters of each word)

   2. Write a program that reverses a sentence entered by the user.

   3. Extend the text analyzer project:

       - Count how many times each word appears.

       - Print the longest word in the sentence.

        Print the average word length.
