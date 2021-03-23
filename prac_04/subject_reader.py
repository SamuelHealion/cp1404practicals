"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program for taking data from a file and displaying it with context"""
    data = get_data()
    print_data(data)


def get_data():
    """Read data from file with the structure: subject, lecturer, number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data


def print_data(data):
    """Display data in a legible format."""
    for info in data:
        print("{} is taught by {:12} and has {:3} students".format(info[0], info[1], info[2]))


main()
