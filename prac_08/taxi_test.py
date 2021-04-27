"""
CP1404 Practical 8 - Inheritance
Program to test inheritance of the taxi class from the car class
"""

from taxi import Taxi


def main():
    prius = Taxi('Prius 1', 100, 1.23)
    prius.drive(40)
    print(prius)
    print("The current fare is ${}".format(prius.get_fare()))
    prius.start_fare()
    prius.drive(100)
    print(prius)
    print("The current fare is ${}".format(prius.get_fare()))


main()
