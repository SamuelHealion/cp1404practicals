"""
CP1404 Practical 6 - Practice and Extension
Car simulator program using the Car class
"""
from prac_06.car import Car

MENU = "Menu:\n" \
       "d) drive\n" \
       "r) refuel\n" \
       "q) quit"


def main():
    """Simulate a car drive using Car class."""
    print("Let's drive!")
    name = input("Enter your car name: ")
    car = Car(name, 100)
    print(car)
    print(MENU)
    choice = input("Enter your choice: ")

    while choice.lower() != 'q':
        if choice.lower() == 'd':
            distance = get_valid_distance()
            maximum_distance = car.drive(distance)
            if maximum_distance < distance:
                print("The car drove {}km and ran out of fuel\n".format(maximum_distance))
            else:
                print("The car drove {}km\n".format(distance))

        elif choice.lower() == 'r':
            refuel = get_valid_refuel()
            car.add_fuel(refuel)
            print("Added {} units of fuel.\n".format(refuel))
        else:
            print("Invalid choice\n")

        print(car)
        print(MENU)
        choice = input("Enter your choice: ")

    print("\nGood Bye {}'s driver.".format(car.name))


def get_valid_distance():
    """Get a valid distance."""
    valid_distance = False
    while not valid_distance:
        try:
            distance = int(input("How many km do you wish to drive? "))
            if distance < 0:
                print("Distance must be >= 0")
            else:
                valid_distance = True
        except ValueError:
            print("Please enter a number")
    return distance


def get_valid_refuel():
    """Get a valid refuel number."""
    valid_refuel = False
    while not valid_refuel:
        try:
            refuel = int(input("How many units of fuel do you want to add to the car? "))
            if refuel < 0:
                print("Fuel amount must be >= 0")
            else:
                valid_refuel = True
        except ValueError:
            print("Please enter a number")
    return refuel


main()