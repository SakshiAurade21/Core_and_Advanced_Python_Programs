# Program to get the largest and smallest number from a list without built-in functions

# Taking user input for list elements
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number: '))
    lst.append(numbers)

# Initialize smallest and largest with the first element
smallest = largest = lst[0]

# Iterate through the list to find the smallest and largest numbers
for num in lst:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

# Display the results
print("Smallest number:", smallest)
print("Largest number:", largest)

'''
Output example:
How many numbers: 5
Enter number: 3
Enter number: 1
Enter number: 9
Enter number: 5
Enter number: 2
Smallest number: 1
Largest number: 9
'''
