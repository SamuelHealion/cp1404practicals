"""
CP1404 Practical 8 - Practice and Extension
New version of guitar file reader that makes use of the Guitar class then asks the user for further guitars
"""

from guitar import Guitar

MENU = "(a)dd a new guitar\n(d)isplay all guitars\n(q)uit"


def main():
    """Read guitar.csv and store the results as a Guitar object."""
    guitars = read_guitars()
    print(MENU)
    choice = input(">>> ")
    while choice.lower() != 'q':
        if choice.lower() == 'a':
            guitar_to_add = get_new_guitar()
            guitars.append(guitar_to_add)
            print(guitar_to_add, 'added')
            guitars.sort()
        elif choice.lower() == 'd':
            display_guitars(guitars)
        else:
            print("Invalid choice")
        print('\n' + MENU)
        choice = input(">>> ")
    save_guitars(guitars)


def read_guitars():
    """Open the file guitars.csv and return the contents."""
    guitars = []
    in_file = open('myguitars.csv', 'r')

    for line in in_file:
        parts = line.strip().split(',')
        year = int(parts[1])
        cost = float(parts[2])
        guitar_to_add = Guitar(parts[0], year, cost)
        guitars.append(guitar_to_add)

    return guitars


def get_new_guitar():
    """Get new guitar details from a user."""
    name = input("Enter the guitars name: ")
    year = int(input("What year was it made?  "))
    cost = float(input("How much does it cost? "))

    return Guitar(name, year, cost)


def display_guitars(guitars):
    """Display the list of guitars."""
    for guitar in guitars:
        print(guitar)


def save_guitars(guitars):
    """Open myguitars.csv and save all guitars."""
    out_file = open('myguitars.csv', 'w')
    for guitar in guitars:
        print('{},{},{}'.format(guitar.name, guitar.year, guitar.cost), file=out_file)
    out_file.close()


if __name__ == '__main__':
    main()
