"""
SilverServiceTaxi class for CP1404.
This class extends the Taxi class to include a fanciness multiplier and a flagfall.
"""

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A SilverServiceTaxi is a special type of Taxi with higher pricing."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi object."""
        super().__init__(name, fuel)
        self.fanciness = fanciness

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A SilverServiceTaxi is a special type of Taxi with higher pricing."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi object."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

def get_fare(self):
    """Calculate the fare including the flagfall."""
    return super().get_fare() + self.flagfall

def __str__(self):
    """Return a string representation of the SilverServiceTaxi."""
    return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
