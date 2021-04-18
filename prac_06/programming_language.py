"""
CP1404 Practical 6 - Classes
Define the class ProgrammingLanguage
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a Programming Language instance."""

        self.name = name
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return whether a car is Dynamic or not."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of a Programming Language."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing,
                                                                           self.reflection, self.year)
