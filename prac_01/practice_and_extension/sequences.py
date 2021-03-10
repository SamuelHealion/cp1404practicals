"""
CP1404 Practice - Extension
Menu-Driven number sequence generator requiring a choice of 3 different sequences
Show even numbers between x and y
Show odd numbers between x and y
Show the squares from x to y
"""

# import the math module
from math import sqrt

menu = """Please select which sequence you would like to see
1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares from x to y
4. Exit the program"""

print(menu)
choice = str(input(">>> "))
while choice != '4':
    if choice == '1':
        first_number = int(input("Please enter the first number: "))
        second_number = int(input("Please enter the second number: "))
        for i in range(first_number, second_number + 1):
            if i % 2 == 0:      # Take the modulus of the current number, returning a 0 if even, 1 if odd
                print(i, end=' ')
    elif choice == '2':
        first_number = int(input("Please enter the first number: "))
        second_number = int(input("Please enter the second number: "))
        for i in range(first_number, second_number + 1):
            if i % 2 == 1:      # Take the modulus of the current number, returning a 0 if even, 1 if odd
                print(i, end=' ')
    elif choice == '3':
        first_number = int(input("Please enter the first number: "))
        second_number = int(input("Please enter the second number: "))
        for i in range(first_number, second_number + 1):
            is_number_square = sqrt(i)      # Takes the square-root of the current number
            if is_number_square % 1 == 0:   # Tests to see if the square-root is a whole number
                print(i, end=' ')
    else:
        print("Invalid format")

    print()
    print(menu)
    choice = str(input(">>> "))

print("Finished")
