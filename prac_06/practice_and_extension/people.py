"""
CP1404 Practical 6 - Practice and Extension
Create a list of peoples first and last names and the age then sorts them by age
"""
from prac_06.practice_and_extension.person import Person


def main():
    """Get first name, last name and age and display from youngest to oldest."""
    people = []
    max_first_name = 0
    max_last_name = 0

    first_name = input("Enter your first name: ")
    while first_name != '':
        last_name = input("Enter your last name: ")
        age = get_valid_age()

        """Get the longest names for formatting"""
        if len(first_name) > max_first_name:
            max_first_name = len(first_name)
        if len(last_name) > max_last_name:
            max_last_name = len(last_name)

        person = Person(first_name.title(), last_name.title(), age)
        print(person, "added.\n")
        people.append(person)

        first_name = input("Enter your first name: ")

    people.sort()
    for person in people:
        print("{Person.first_name:{}} | {Person.last_name:{}} | {Person.age} years old"
              .format(max_first_name, max_last_name, Person=person))


def get_valid_age():
    """Get a valid age."""
    valid_age = False
    while not valid_age:
        try:
            age = int(input("Enter your age: "))
            if age <= 0:
                print("Age must be greater than zero")
            else:
                valid_age = True
        except ValueError:
            print("Please enter a number")
    return age


main()
