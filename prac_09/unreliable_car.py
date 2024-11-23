"""
UnreliableCar class for CP1404.
This class extends the Car class to simulate an unreliable car with a chance-based driving mechanism.
"""

from car import Car
import random


class UnreliableCar(Car):
    """A Car subclass that has a chance of not driving, based on its reliability."""

    def __init__(self, name, fuel, reliability):
        """
        Initialise an UnreliableCar instance.

        Args:
            name (str): The car's name.
            fuel (int): The amount of fuel the car starts with.
            reliability (float): The car's reliability percentage (0-100).
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Attempt to drive the car a given distance, based on its reliability.

        Args:
            distance (int): The distance to attempt to drive.

        Returns:
            int: The actual distance driven.
        """
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
