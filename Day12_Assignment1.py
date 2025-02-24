# Program to find the number of times 4 appears in the tuple

# Given input tuple
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)

# Initialize counter
count = 0

# Iterate through each element in the tuple
for num in tuplex:
    if num == 4:  # Check if the element is 4
        count += 1  # Increment the counter

# Display the result
print("Output:", count)

'''
Output:
3
'''
