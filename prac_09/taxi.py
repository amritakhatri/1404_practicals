"""
CP1404/CP5632 Practical
Taxi class, extends Car
"""

from car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23  # Class variable shared across all Taxi instances

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
