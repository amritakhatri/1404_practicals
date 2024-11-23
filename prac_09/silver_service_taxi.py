from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A SilverServiceTaxi is a special type of Taxi with higher pricing."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi object."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
