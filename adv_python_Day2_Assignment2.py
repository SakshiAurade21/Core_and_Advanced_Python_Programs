# List of email addresses
emails = ["alice@example.com", "bob@sample.org", "charlie@mydomain.net"]

# Extract domain part using list comprehension
domains = [email.split("@")[1] for email in emails]

# Display the result
print(domains)

'''
Output:
['example.com', 'sample.org', 'mydomain.net']
'''
