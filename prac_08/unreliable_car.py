"""
CP1404 Practical 8 - Inheritance
Define the class UnreliableCar using inheritance from the Car class.
"""

from car import Car
from random import randrange


class UnreliableCar(Car):
    """Specialised version of the Car class that has a reliability rating."""

    def __init__(self, name, fuel, reliability=0.0):
        """Initialise an UnreliableCar instance, based on parent Car class."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string representation of an UnreliableCar object."""
        return "{}, fuel={}, odometer={}, Is reliable {}% of the time."\
            .format(self.name, self.fuel, self.odometer, self.reliability)

    def drive(self, distance):
        """Drive like the parent class but check to see if it will fail."""
        if self.reliability >= randrange(0, 100):
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
            print("She didn't make it, better call RACQ")
        return distance_driven
