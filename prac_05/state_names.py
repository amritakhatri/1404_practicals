"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {
    "QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
    "WA": "Western Australia", "ACT": "Australian Capital Territory",
    "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"
}

# Display the entire dictionary to verify it's working
print(CODE_TO_NAME)

# Handle user input with EAFP (Easier to Ask Forgiveness than Permission) approach
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# Print all state codes and names in a neatly formatted way
print("\nAll states and their full names:")
for code, name in CODE_TO_NAME.items():
    print(f"{code:<3} is {name}")
