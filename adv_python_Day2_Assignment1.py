# List of employee records
employees = [
    {"name": "John Doe", "department": "Sales"},
    {"name": "Jane Smith", "department": "Marketing"},
    {"name": "Emily Johnson", "department": "Sales"},
    {"name": "Michael Brown", "department": "HR"}
]

# Extract names of employees in the Sales department and convert to uppercase
sales_employees = [emp["name"].upper() for emp in employees if emp["department"] == "Sales"]

# Display the result
print(sales_employees)

'''
Output:
['JOHN DOE', 'EMILY JOHNSON']
'''
