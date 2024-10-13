import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def generate_quick_pick():
    """Generates a sorted list of 6 unique random numbers between 1 and 45."""
    numbers = set()  # Use a set to avoid duplicates
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        numbers.add(number)  # Add number to the set
    return sorted(numbers)  # Return sorted list

def main():
    """Main function to run the quick pick generator."""
    # Ask the user for the number of quick picks
    num_picks = int(input("How many quick picks? "))

    # Generate and print the quick picks
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        # Print the numbers in the required format
        print(" ".join(f"{num:2}" for num in quick_pick))

if __name__ == "__main__":
    main()
