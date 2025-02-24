# Function to perform division


# Parameters: a (numerator), b (denominator)
def div(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

# Taking user input
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

# Calling the function with user input
result = div(num1, num2)

# Display the result
print("Division result:", result)

'''
Output 
Enter the numerator: 10
Enter the denominator: 2
Division result: 5.0
'''