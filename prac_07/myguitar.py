#Import the Guitar class and define the load_guitars function
from guitar import Guitar

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
