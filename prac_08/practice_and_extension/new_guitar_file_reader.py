"""
CP1404 Practical 8 - Practice and Extension
New version of guitar file reader that makes use of the Guitar class
"""

from guitar import Guitar


def main():
    """Read guitar.csv and store the results as a Guitar object."""
    in_file = open('guitars.csv', 'r')
    guitars = []

    for line in in_file:
        parts = line.strip().split(',')
        year = int(parts[1])
        cost = float(parts[2])
        guitar_to_add = Guitar(parts[0], year, cost)
        guitars.append(guitar_to_add)

    guitars.sort()
    for guitar in guitars:
        print(guitar)


if __name__ == '__main__':
    main()
