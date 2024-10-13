# List of numbers
numbers = [3, 1, 4, 1, 5, 9, 2]

# Predicted answers to expressions
# numbers[0]      -> 3
# numbers[-1]     -> 2
# numbers[3]      -> 1
# numbers[:-1]    -> [3, 1, 4, 1, 5, 9]
# numbers[3:4]    -> [1]
# 5 in numbers    -> True
# 7 in numbers    -> False
# "3" in numbers  -> False (string vs integer mismatch)
# numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Check actual output
print(numbers[0])         # Output: 3
print(numbers[-1])        # Output: 2
print(numbers[3])         # Output: 1
print(numbers[:-1])       # Output: [3, 1, 4, 1, 5, 9]
print(numbers[3:4])       # Output: [1]
print(5 in numbers)       # Output: True
print(7 in numbers)       # Output: False
print("3" in numbers)     # Output: False
print(numbers + [6, 5, 3])  # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Modify the list according to the instructions
numbers[0] = "ten"  # Change the first element to "ten"
numbers[-1] = 1     # Change the last element to 1

# Print all
print(numbers[2:])  # Output: [4, 1, 5, 9, 1]

# Check if 9 is in the list
print(9 in numbers)  # Output: True
