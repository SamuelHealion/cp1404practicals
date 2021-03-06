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
        new_guitar = Guitar(name, year, cost)
        print(new_guitar, "added.\n")
        guitars.append(new_guitar)

        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # Determine the maximum length of guitar name for string formatting
    max_length = max(len(guitar.name) for guitar in guitars)

    print("These are my guitars:")
    for i, new_guitar in enumerate(guitars, 1):
        # Check to see if the guitar is vintage
        vintage_string = '(vintage)' if new_guitar.is_vintage() else ''

        print("Guitar {}: {Guitar.name:{}} ({Guitar.year}), worth $ {Guitar.cost:10,.2f} {}"
              .format(i, max_length, vintage_string, Guitar=new_guitar))


main()
