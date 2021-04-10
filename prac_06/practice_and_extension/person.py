"""
CP1404 Practical 6 - Practice and Extension
Define the class Person
"""


class Person:
    """Represents a Person object."""

    def __init__(self, first_name='', last_name='', age=0):
        """Initialise the Person instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """Returns a string representation of a Person object."""
        return "{} {}, {} years old".format(self.first_name, self.last_name, self.age)

    def __lt__(self, other):
        """Less than, used to people by age, from youngest to oldest."""
        return self.age < other.age
