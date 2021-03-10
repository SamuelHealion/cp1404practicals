"""
Practice program to check whether a users password is above the MIN_LENGTH
It will then print the length of the valid password in *'s
"""

MIN_LENGTH = 5
valid_password = False

while not valid_password:
    password = str(input("Please enter a password at least {} characters long: ".format(MIN_LENGTH)))
    if len(password) < MIN_LENGTH:
        print("That password isn't long enough")
    else:
        print('*' * len(password))
        # for char in password:
        #     print('*', end='')
        valid_password = True