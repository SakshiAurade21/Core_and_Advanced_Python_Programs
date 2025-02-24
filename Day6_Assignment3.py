# Program to find the factorial of a number using a while loop

# Taking user input
n = int(input("Enter a number: "))
fact = 1

i = 1
while i <= n:
    fact *= i  # Multiply current value of fact by i
    i += 1  # Increment i

# Display the result
print("Factorial of the number:", fact)

'''
Output example:
Enter a number: 5
Factorial of the number: 120
'''
