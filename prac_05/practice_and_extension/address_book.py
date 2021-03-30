"""
Practice and Extension work for CP1404 Week 5
An address book with the ability to add new entries, change existing ones and look up the ones current stored
"""

MENU = "Please choose which option you would like.\n" \
       "{A} - Enter new name and address\n" \
       "{C} - Change an address for an existing entry\n" \
       "{P} - Print an address for a saved name\n" \
       "{Q} - Quit"


def main():
    """Save names and address's in a dictionary."""
    address_book = {}
    print(MENU)
    choice = input(">>> ")
    while choice.upper() != 'Q':
        if choice.upper() == 'A':
            address, name = get_name_address()
            address_book[name] = address
        elif choice.upper() == 'C':
            name = str(input("Enter the name of the address you would like to change: ")).title()
            if name in address_book:
                check = 'n'
                while check.upper() != 'Y' and check != '':
                    address = str(input("Enter the new address: ")).title()
                    check = input("{} at {}. Is this correct? (Y/n) ".format(name, address))
                address_book[name] = address
        elif choice.upper() == 'P':
            name = str(input("Enter a name: ")).title()
            if name in address_book:
                print("{} lives at {}".format(name, address_book[name]))
            else:
                add_name = str(input("Sorry, that name isn't saved yet, would you like to add it? (Y/n) "))
                if add_name.upper() == 'Y' or add_name == '':
                    address, name = get_name_address()
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ")


def get_name_address():
    """Get a name and address then check if it is correct."""
    valid_address = False
    while not valid_address:
        name = str(input("Enter the name: ")).title()
        address = str(input("Enter the address: ")).title()
        check = input("{} at {}. Is this correct? (Y/n) ".format(name, address))
        if check.upper() == 'Y' or check == '':
            valid_address = True

    return address, name


main()
