#Import the Guitar class and define the load_guitars function
from guitar import Guitar

def main():
    """Main function to manage guitar input, display, and save to CSV."""
    guitars = load_guitars("guitars.csv")
    display_guitars(guitars)

    guitars.sort()  # Sort the guitars by year
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    new_guitar = get_new_guitar()  # Get new guitar details from user
    guitars.append(new_guitar)  # Add the new guitar to the list
    save_guitars("guitars.csv", guitars)


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, year, cost = line.strip().split(',')
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print("File not found.")
    return guitars

# Define the display_guitars function
def display_guitars(guitars):
    """Display a list of guitars."""
    for guitar in guitars:
        print(guitar)

# Define the sort_guitars function
def sort_guitars(guitars):
    """Sort the guitars list by the year of manufacture (oldest to newest)."""
    guitars.sort()

# Define the get_new_guitar function
def get_new_guitar():
    """Prompt the user to enter details of a new guitar and return a Guitar object."""
    name = input("Enter the guitar name: ")
    year = int(input("Enter the year of manufacture: "))
    cost = float(input("Enter the cost of the guitar: "))
    return Guitar(name, year, cost)

# Define the save_guitars function
def save_guitars(filename, guitars):
    """Save the list of guitars to the CSV file."""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == "__main__":
    main()