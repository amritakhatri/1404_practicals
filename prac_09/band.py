"""
Band class for CP1404.
Represents a music band, which is a collection of musicians.
"""

class Band:
    """Band class"""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        """Return a string showing each musician in the band playing their instruments."""
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return "\n".join(result)
