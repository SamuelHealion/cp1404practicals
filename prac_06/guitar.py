"""
CP1404 Practical 6 - Classes
Define the class Guitar
"""
VINTAGE_AGE = 50
CURRENT_YEAR = 2021


class Guitar:
    """Represents a Guitar object."""

    def __init__(self, name='', year=0, cost=0):
        """Initialise a Guitar instance."""

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string representation of a Guitar object."""
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Returns the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns whether a Guitar is 50 years old or older."""
        return self.get_age() >= VINTAGE_AGE
