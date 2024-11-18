"""
CP1404/CP5632 Practical
Taxi simulator program
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program."""
    print("Let's drive!")
    print(MENU)
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0
    print(">>> ", end="")

    option = input().lower()
    while option != "q":
        if option == "c":
            print("Choose a taxi:")
        elif option == "d":
            print("Drive the taxi:")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        print(">>> ", end="")
        option = input().lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    # Placeholder for displaying taxis

def display_taxis(taxis):
    """Display the list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

    print("Choose a taxi:")
    display_taxis(taxis)

def choose_taxi(taxis):
    """Display available taxis and let the user choose one."""
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input")
    return None


if option == "c":
    current_taxi = choose_taxi(taxis)
