# Initialize an empty list to store user input
data = []

# Ask the user for the number of elements they want to input
num_elements = int(input("Enter the number of elements in the list: "))

# Collect elements from the user
for i in range(num_elements):
    element = input(f"Enter element {i+1}: ")  # Get string input (can be any data type)
    data.append(element)

# Initialize an empty list to store duplicates
duplicates = []

# Initialize an empty list to track seen elements
seen = []

# Loop through the data to find duplicates
for item in data:
    if item in seen:  # If item is already in the seen list, it's a duplicate
        duplicates.append(item)
    else:
        seen.append(item)  # Otherwise, add the item to the seen list

# Check if there are duplicates and print the result
if duplicates:
    print("Duplicate values found:", duplicates)
else:
    print("No duplicate values found.")

'''
Sample Output:
Enter the number of elements in the list: 5
Enter element 1: 3
Enter element 2: 4
Enter element 3: 3
Enter element 4: 6
Enter element 5: 7
Duplicate values found: ['3']
'''
