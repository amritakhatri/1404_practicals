"""Programming Language class for storing details about programming languages.
Estimated time: 1 hour
Start time: 19:40
End time: 20.52
"""

class ProgrammingLanguage:
    """Represent a programming language with typing, reflection capability, and year of creation."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed"""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
