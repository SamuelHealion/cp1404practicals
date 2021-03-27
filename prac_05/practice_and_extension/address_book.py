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
    address_book = {}
    print(MENU)
    choice = input(">>> ")
    while choice.upper() != 'Q':
        if choice.upper() == 'A':
            check = 'n'
            while check.upper() != 'Y' and check != '':
                name = str(input("Enter the name: ")).title()
                address = str(input("Enter the address: ")).title()
                check = input("{} at {}. Is this correct? (Y/n) ".format(name, address))
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
                    check = 'n'
                    while check.upper() != 'Y' and check != '':
                        name = str(input("Enter the name: ")).title()
                        address = str(input("Enter the address: ")).title()
                        check = input("{} at {}. Is this correct? (Y/n) ".format(name, address))
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ")


main()