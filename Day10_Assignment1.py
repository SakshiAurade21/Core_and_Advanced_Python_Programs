# Program to sum all the items in a list
# Initialize an empty list to store items
items = []

# Ask the user how many items they want to enter
num_items = int(input("Enter the number of items in the list: "))

# Collect the list items from the user
for i in range(num_items):
    item = int(input(f"Enter item {i+1}: "))  # Get integer input
    items.append(item)

# Initialize the variable to store the sum
list_sum = 0

# Loop through the list and add each item to the sum
for num in items:
    list_sum += num

# Display the sum of the list
print("Sum of the list:", list_sum)

'''
Sample Output:
Enter the number of items in the list: 5
Enter item 1: 3
Enter item 2: 4
Enter item 3: 5
Enter item 4: 2
Enter item 5: 1
Sum of the list: 15
'''