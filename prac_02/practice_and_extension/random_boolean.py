"""
Three different ways to generate random Boolean
"""

import random

print("Press Q to quit")
print("What random function do you want to run: A, B or C? ")
user_input = str(input("> ")).upper()
while user_input != 'Q':
    if user_input == 'A':
        if random.randint(0, 1) == 0:
            print("False")
        else:
            print("True")
    elif user_input == 'B':
        number = random.randrange(1, 11)
        if number % 2 == 0:
            print("True")
        else:
            print("False")
    elif user_input == 'C':
        number = random.randint(0, 100)
        if number > 50:
            print("True")
        else:
            print("False")
    else:
        print("Invalid choice")
    print("Press Q to quit")
    print("What random function do you want to run: A, B or C? ")
    user_input = str(input("> ")).upper()