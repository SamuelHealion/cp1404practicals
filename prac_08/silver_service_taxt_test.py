"""
CP1404 Practical 8 - Inheritance
Test program to run the SilverServiceTaxi class
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi('Hummer', 200, 2)
    print(hummer)
    hummer.drive(18)
    print("Your current fare is ${:.2f}".format(hummer.get_fare()))
    print(hummer)


main()
