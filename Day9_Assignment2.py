# Program to remove duplicate characters from a given string

# Given input string
inp = "String and String Function"

# Initialize an empty string to store the result without duplicates
out = ""

# Iterate through each character in the input string
for ch in inp:
    if ch not in out:  # Check if the character is already in the output string
        out += ch  # Append the character if it's not a duplicate

# Display the result
print("Output:", out)

'''
Output:
String and Function
'''
