"""
CP1404 Practical 8 - Inheritance
A copy of the car class from the practical in week 6.
"""

from unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class."""
    lemon = UnreliableCar('Bessy', 100, 50)
    print(lemon)
    lemon.drive(40)
    print(lemon)


main()
