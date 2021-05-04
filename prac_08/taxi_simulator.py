"""
CP1404 Practical 8 - Inheritance
Program to simulate taxi's using the Taxi and SilverServiceTaxi classes.
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Simulate taxi service using Taxi and SilverServiceTaxi Classes."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ")
    while choice.lower() != 'q':
        if choice.lower() == 'c':
            print("Taxis available:")
            taxis_available(taxis)
            current_taxi = get_valid_taxi(taxis)
        elif choice.lower() == 'd':
            if current_taxi:    # Check that there is a currently selected taxi
                if current_taxi.fuel == 0:
                    print("Sorry, that taxi is all out of fuel. Please choose another Taxi first.")
                else:
                    distance = get_valid_distance()
                    # if distance != 0:
                    # else:
                    current_taxi.start_fare()
                    current_taxi.drive(distance)
                    trip_fare = current_taxi.get_fare()
                    print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_fare))
                    bill_to_date += trip_fare
            else:
                print("No taxi selected, please choose a taxi first")
        else:
            print("Invalid choice")
        print("Bill to date: ${:.2f}".format(bill_to_date))
        print(MENU)
        choice = input(">>> ")
    print("Taxis are now:")
    taxis_available(taxis)


def taxis_available(taxis):
    """Display the details of the taxis available."""
    for i, car in enumerate(taxis):
        print("{} - {}".format(i, car))


def get_valid_distance():
    """Get a valid input for distance."""
    valid_distance = False
    while not valid_distance:
        try:
            distance = float(input("Drive how far? "))
            if distance <= 0:
                print("Invalid distance, please enter a distance greater than zero")
            else:
                valid_distance = True
        except ValueError:
            print("Invalid distance, please enter a number")
    return distance


def get_valid_taxi(taxis):
    """Get a valid choice for current taxi."""
    try:
        choice = int(input("Choose taxi: "))
        if choice < 0 or choice >= len(taxis):
            print("Invalid choice")
        else:
            return taxis[choice]
    except ValueError:
        print("Invalid choice")


main()
