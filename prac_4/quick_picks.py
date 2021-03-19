"""
CP1404 Practical 4
Generates a number of quick picks (6 random numbers between 1 and 45) based on user input
"""
import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_IN_QUICK_PICKS = 6


def main():
    """Generates a set of Quick Picks (random numbers) based on how many the user wants"""
    valid_input = False
    while not valid_input:
        try:
            number_of_quick_picks = int(input("How many quick picks? "))
            if number_of_quick_picks <= 0:
                print("Please enter a number greater than zero")
            else:
                for i in range(number_of_quick_picks):
                    quick_picks = generate_quick_picks()
                    print(quick_picks)
                valid_input = True
        except ValueError:
            print("Please enter a valid input")


def generate_quick_picks():
    """Generates a set of quick picks based off of NUMBERS_IN_QUICK_PICKS
    and then sorts them before returning the list """
    quick_picks = []
    for i in range(NUMBERS_IN_QUICK_PICKS):
        number = random.randint(MINIMUM, MAXIMUM)
        if number not in quick_picks:
            quick_picks.append(number)
    quick_picks.sort()
    return quick_picks


main()
