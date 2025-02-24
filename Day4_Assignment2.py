num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Check which number is the largest using conditional statements
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the largest number
print("The largest among", num1, ",", num2, "and", num3, "is:", largest)

# Example Output:
# Enter first number: 10
# Enter second number: 20
# Enter third number: 15
# The largest among 10, 20 and 15 is: 20
