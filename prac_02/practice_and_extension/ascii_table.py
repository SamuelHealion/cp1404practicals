"""
Show the ASCII code for the user input and vice versa
"""
LOWER_LIMIT = 33
UPPER_LIMIT = 127

finished1 = False
finished2 = False
finished3 = False

while not finished1:
    try:
        character_to_ascii = str(input("Enter a character: "))
        print("The ASCII code for {} is {}".format(character_to_ascii, ord(character_to_ascii)))
        finished1 = True
    except TypeError:
        print("Invalid option")

while not finished2:
    try:
        ascii_to_character = int(input("Enter a number between {} and {}: ".format(LOWER_LIMIT, UPPER_LIMIT)))
        if ascii_to_character < LOWER_LIMIT or ascii_to_character > UPPER_LIMIT:
            print("Outside of the range")
        else:
            print("The character for {} is {}".format(ascii_to_character, chr(ascii_to_character)))
            finished2 = True
    except ValueError:
        print("Invalid input")

while not finished3:
    try:
        print("How many columns would you like? ")
        columns = int(input("> "))

        for line in range(LOWER_LIMIT, UPPER_LIMIT + 1, columns):
            for column in range(0, columns):
                if line + column <= 127:
                    print("{:>3} {:>2}".format(line + column, chr(line + column)), end='  |  ')
            print()
        finished3 = True
    except ValueError:
        print("Invalid input")
