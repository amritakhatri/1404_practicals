# Question 1
# Write code that asks the user for their name,
# then opens a file called "name.txt" and writes that name to it.
# Remember to close your file.

user_name = input("Enter your name: ")
with open('name.txt', 'w') as name_file:
    name_file.write(user_name)

# Question 2
# Write code that opens "name.txt" and reads the name (as above)
# then prints, "Your name is Bob" (or whatever the name is in the file).

with open('name.txt', 'r') as name_file:
    stored_name = name_file.read()
    print(f"Your name is {stored_name}")

# Question 3
# Create a text file called numbers.txt and save it in your prac directory.
# Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers
# and adds them together then prints the result, which should be... 59.

with open('numbers.txt', 'r') as numbers_file:
    number1 = int(numbers_file.readline())
    number2 = int(numbers_file.readline())
    result = number1 + number2
    print(result)

# Question 4
# Write code that prints the total for all lines in numbers.txt
# or a file with any number of numbers.

total = 0
with open('numbers.txt', 'r') as numbers_file:
    for line in numbers_file:
        total += int(line)

print(total)
