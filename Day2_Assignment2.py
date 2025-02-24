# Declare two variables
x = int(input("Enter first variable: "))
y = int(input("Enter second variable: "))

# Find and print the largest variable using a ternary operator
largest = x if x > y else y
print("The largest variable is:", largest)

# Example Output:
# Enter first variable: 8
# Enter second variable: 12
# The largest variable is: 12