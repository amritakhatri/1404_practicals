"""
Module: project.py
Time Estimate: 20 minutes
This module defines the Project class for the Project Management Program.
"""

class Project:
    """A class to represent a project with relevant attributes."""

    def __init__(self, name, start_date, priority, estimate, completion):
        """Initializes a new Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        """Returns a string representation of a project."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate}, completion: {self.completion}%"


