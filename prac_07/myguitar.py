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
