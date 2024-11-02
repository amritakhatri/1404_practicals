"""Program to manage a collection of guitars."""

from guitar import Guitar

def main():
    """Collect guitar details from user and display them."""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.\n")
        name = input("Name: ")

    # Preload sample guitars (for testing purposes)
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
