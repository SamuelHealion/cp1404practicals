"""
Practice program to check whether a users password is above the MIN_LENGTH
It will then print the length of the valid password in *'s
"""

MIN_LENGTH = 5


def main():
    password = get_password()
    print_stars(password)


def get_password():
    """Checks whether a password is longer than the MIN_LENGTH required."""
    valid_password = False
    while not valid_password:
        password = str(input("Please enter a password at least {} characters long: ".format(MIN_LENGTH)))
        if len(password) < MIN_LENGTH:
            print("That password isn't long enough")
        else:
            return password


def print_stars(string):
    """Prints * for the length of the string passed."""
    print('*' * len(string))


main()
