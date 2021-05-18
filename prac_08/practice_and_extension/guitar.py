"""
CP1404 Practical 8 - Practice and Extension
Define the class Guitar - original class taken from week 6 practical
"""
VINTAGE_AGE = 50
CURRENT_YEAR = 2021


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name='', year=0, cost=0.0):
        """Initialise a Guitar instance."""

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar object."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Return the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return whether a Guitar is 50 years old or older."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used to sort guitars by year, from oldest to newest."""
        return self.get_age() > other.get_age()
