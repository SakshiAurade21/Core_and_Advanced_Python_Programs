
year = int(input("Enter a year: "))

# Leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# Example Output:
# Enter a year: 2024
# 2024 is a leap year.
