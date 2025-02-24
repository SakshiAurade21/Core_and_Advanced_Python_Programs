# Program to check whether a number is a palindrome

# Taking user input
n = int(input("Enter a number: "))
orig = n  # Store the original number for comparison
rev = 0

while n > 0:
    d = n % 10  # Extract last digit
    rev = (rev * 10) + d  # Append digit to reversed number
    n = n // 10  # Remove last digit from number

# Check if the original number and reversed number are the same
if orig == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

'''
Output example:
Enter a number: 121
The number is a palindrome.

Enter a number: 123
The number is not a palindrome.
'''
