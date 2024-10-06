"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if the user inputs values that are not valid integers for the numerator or denominator. For example, entering a non-integer or a string.

2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if the user enters a denominator of 0. Division by zero is mathematically undefined.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, we can modify the code to check if the denominator is zero before performing the division. If the denominator is zero,we can handle it differently, such as asking the user to enter a non-zero denominator.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Cannot divide by zero! Please enter a non-zero denominator.")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(f"The result is: {fraction}")

except ValueError:
    print("Numerator and denominator must be valid integers!")

print("Finished.")
