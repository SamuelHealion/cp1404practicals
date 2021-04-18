"""
CP1404 Practical 6 - Classes
Short program to check that the Guitar class works
"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
other_guitar = Guitar("Other Guitar", 2013, 400)

print("{} get_age() - Expected 99. Got {}".format(gibson.name, gibson.get_age()))
print("{} get_age() - Expected 8. Got {}".format(other_guitar.name, other_guitar.get_age()))
print("{} is_vintage() - Expected True. Got {}".format(gibson.name, gibson.is_vintage()))
print("{} is_vintage() - Expected False. Got {}".format(other_guitar.name, other_guitar.is_vintage()))
