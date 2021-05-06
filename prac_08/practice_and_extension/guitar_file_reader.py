"""
CP1404 Practical 8 - Practice and Extension
Reads guitars.csv and stores the result in a list of tuples
"""


def main():
    """Read guitars.csv and stores the result in a list of tuples then displays the result."""
    in_file = open('guitars.csv', 'r')
    guitars = []

    for line in in_file:
        parts = line.strip().split(',')
        guitar_to_add = tuple([part for part in parts])
        guitars.append(guitar_to_add)
    in_file.close()

    for guitar in guitars:
        print(guitar)


if __name__ == '__main__':
    main()
