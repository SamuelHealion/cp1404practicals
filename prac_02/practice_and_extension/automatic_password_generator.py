"""
CP1404 Practice
Automatically generates a password based on choices made by the user
User supplies length and whether the password needs upper/lower/numeric/special characters
"""

import random

LETTERS = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "1234567890"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

valid_password_length = False

print("Automatic Password Generator")

while not valid_password_length:
    password_length = int(input("How long do you need the password? "))
    require_lower = str(input("Do you need lower case characters? Y/N ")).upper()
    require_upper = str(input("Do you need upper case characters? Y/N ")).upper()
    require_numeric = str(input("Do you need numeric characters? Y/N ")).upper()
    require_special = str(input("Do you need special characters? Y/N ")).upper()

    min_length = 0

    if require_lower == 'N' and require_upper == 'N' and require_numeric == 'N' and require_special == 'N':
        print("You need at least one option selected")
    else:
        if require_lower == "Y":
            min_length += 1
            lower_flag = 0
        else:
            lower_flag = 1
        if require_upper == "Y":
            min_length += 1
            upper_flag = 0
        else:
            upper_flag = 1
        if require_numeric == 'Y':
            min_length += 1
            numeric_flag = 0
        else:
            numeric_flag = 1
        if require_special == 'Y':
            min_length += 1
            special_flag = 0
        else:
            special_flag = 1

        if min_length > password_length:
            print("The password is too short to meet the requirements")
        else:
            valid_password_length = True


password = ''
while len(password) < password_length:
    choice = random.randint(0, 3)
    if choice == 0:
        if require_lower == 'Y' and lower_flag == 0:
            password += random.choice(LETTERS)
            lower_flag = 1
        elif require_lower == 'Y' and upper_flag == 1 and numeric_flag == 1 and special_flag == 1:
            password += random.choice(LETTERS)
        else:
            pass
    elif choice == 1:
        if require_upper == 'Y' and upper_flag == 0:
            password += random.choice(LETTERS).upper()
            upper_flag = 1
        elif require_upper == 'Y' and lower_flag == 1 and numeric_flag == 1 and special_flag == 1:
            password += random.choice(LETTERS).upper()
        else:
            pass
    elif choice == 2:
        if require_numeric == 'Y' and numeric_flag == 0:
            password += random.choice(NUMBERS)
            numeric_flag = 1
        elif require_numeric == 'Y' and upper_flag == 1 and lower_flag == 1 and special_flag == 1:
            password += random.choice(NUMBERS)
        else:
            pass
    elif choice == 3:
        if require_special == 'Y' and special_flag == 0:
            password += random.choice(SPECIAL_CHARACTERS)
            special_flag = 1
        elif require_special == 'Y' and upper_flag == 1 and numeric_flag == 1 and lower_flag == 1:
            password += random.choice(SPECIAL_CHARACTERS)
        else:
            pass

print(password)