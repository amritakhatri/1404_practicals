"""Guitar class to store details about a guitar.
Estimated time: 1 hour
Start time: 20.50
End time:
"""

class Guitar:
    """Represent a guitar with name, year of manufacture, and cost."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate and return the guitar's age."""
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self.year
