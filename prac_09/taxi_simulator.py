# taxi_simulator.py
"""
CP1404- Taxi Simulator
This program simulates a taxi service where the user can choose a taxi,
drive it, and see the cost of each trip.

The program includes:
- A Taxi class
- A SilverServiceTaxi class
- Polymorphism to handle different types of taxis
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

# Constants for taxi fare and flagfall amounts
REGULAR_FARE = 1.23
FLAGFALL = 4.50
SILVER_SERVICE_FARE = 2.46
LUXURY_FARE = 4.92



def main():
    """Main function to run the taxi simulator."""
    # Create taxi objects
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    bill = 0.00

    # Main menu loop
    while True:
        print(f"Bill to date: ${bill:.2f}")
        option = input("q)uit, c)hoose taxi, d)rive: ").lower()

        if option == 'q':
            print(f"Total trip cost: ${bill:.2f}")
            print("Taxis are now:")
            show_taxis(taxis)
            break
        elif option == 'c':
            current_taxi = choose_taxi(taxis)
        elif option == 'd':
            bill = drive_taxi(current_taxi, bill)
        else:
            print("Invalid option")

# Function to display the available taxis and their details
def show_taxis(taxis):
    """Display the available taxis."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

# Function to process the user's trip choice
def choose_taxi(taxis):
    """Prompt the user to choose a taxi from the list."""
    show_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

# Function to drive the taxi and calculate the trip cost
def drive_taxi(current_taxi, bill):
    """Drive the current taxi and calculate the cost."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive.")
    else:
        try:
            distance = float(input("Drive how far? "))
            cost = current_taxi.drive(distance)
            bill += cost
            print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
        except ValueError:
            print("Invalid distance. Please enter a valid number.")
    return bill

