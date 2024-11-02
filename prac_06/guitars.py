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
