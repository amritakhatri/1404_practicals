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


