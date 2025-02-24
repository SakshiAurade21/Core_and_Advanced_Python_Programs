# Program to reverse a number using a while loop

# Taking user input
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10  # Extract last digit
    reverse = (reverse * 10) + digit  # Append digit to reversed number
    num = num // 10  # Remove last digit from number

# Display the result
print("Reversed number:", reverse)

'''
Output example:
Enter a number: 1234
Reversed number: 4321
'''
