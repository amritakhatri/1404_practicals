"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

# Using f-strings for cleaner formatting
print(f"My guitar: {name}, first made in {year}")

# Reusing variables in f-strings
print(f"My {name} was first made in {year} (that's right, {year}!)")

# Formatting currency with commas and 2 decimal places
print(f"My {name} would cost ${cost:,.2f}")

# Aligning numbers in columns using f-strings
numbers = [1, 19, 123, 456, -25]
for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

# Using f-strings for output with rounded cost
print(f"{year} {name} for about ${cost:,.0f}!")

# Right-aligned numbers with range
for i in range(0, 201, 50):
    print(f"{i:>3}")

