"""
CP1404 Practical 6 - Classes
Creates a list of guitars using the Guitar class
"""

from prac_06.guitar import Guitar


def main():
    """Get guitar details and display them."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != '':
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        print(guitar, "added.\n")
        guitars.append(guitar)

        name = input("Name: ")

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # Determine the maximum length of guitar name for string formatting
    max_name = 0
    for guitar in guitars:
        if len(guitar.name) > max_name:
            max_name = len(guitar.name)

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        # Check to see if the guitar is vintage
        vintage_string = '(vintage)' if guitar.is_vintage() else ''

        print("Guitar {}: {Guitar.name:{}} ({Guitar.year}), worth $ {Guitar.cost:10,.2f} {}"
              .format(i, max_name, vintage_string, Guitar=guitar))


main()
