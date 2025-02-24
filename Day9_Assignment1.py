# Program to count letters, digits, and special symbols in a given string

# Given input string
inp = "P@#yn26at^&i5ve"

# Initialize counters
chars = digits = symbols = 0

# Iterate through each character in the string
for ch in inp:
    if ch.isalpha():  # Check if the character is a letter
        chars += 1
    elif ch.isdigit():  # Check if the character is a digit
        digits += 1
    else:  # If not a letter or digit, it is a special symbol
        symbols += 1

# Display the results
print("Chars =", chars)
print("Digits =", digits)
print("Symbols =", symbols)

'''
Output:
Chars = 8
Digits = 3
Symbols = 4
'''
