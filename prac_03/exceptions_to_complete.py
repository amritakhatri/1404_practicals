is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # TODO: Set is_finished to True when a valid integer is entered
    except ValueError:  # TODO - Catch ValueError when input is not a valid integer
        print("Please enter a valid integer.")
print(f"Valid result is: {result}")
