"""
CP1404/CP5632 Practical
Test program for Taxi class
"""

from taxi import Taxi

def main():
    """Test Taxi class functionality."""
    # Create a new Taxi object
    my_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40 km
    my_taxi.drive(40)

    # Print the taxi's details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")
