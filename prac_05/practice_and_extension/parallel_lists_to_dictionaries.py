"""
CP1404 Practical 5 Extension
Practice saving parallel lists and converting them into dictionaries
"""

NUMBER_OF_PROMPTS = 1
CURRENT_DATE = [30, 3, 2021]
DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

names = []
date_of_births = []
names_to_birth_dates = {}


def main():
    for i in range(NUMBER_OF_PROMPTS):
        print("Enter your Name")
        # name = str(input(">>> ")).title()
        name = 'Sam'
        date_of_birth = get_valid_age()
        day, month, year = get_age(date_of_birth)
        names_to_birth_dates[name] = (day, month, year)

    print(names_to_birth_dates)


def get_valid_age():
    """Check to see if entered age is valid"""
    valid_age = False
    while not valid_age:
        print("Enter your date of birth as DD/MM/YYYY")
        date_of_birth = str(input(">>> "))
        if '/' in date_of_birth:
            date = date_of_birth.split('/')
            valid_age = is_real_date_of_birth(date)
        else:
            print("Invalid date of birth")
    return date


def is_real_date_of_birth(date):
    if len(date) != 3:      # Check to see the date is the correct length
        print("Invalid format")
        return False
    if date[0].isnumeric() and date[1].isnumeric() and date[2].isnumeric():
        age = convert_date_to_integer(date)
        if age[2] % 4 == 0 and age[1] == 2:
            "Checks for leap years"
            if age[0] > 29 or age[0] < 0:
                print("Out of range of the days/months")
            else:
                return True
        elif age[0] <= 0 or age[1] <= 0 or age[2] <= 0:
            print("Age must be greater than zero")
        elif age[1] <= 12:
            print("Out of range of months")
            if age[0] > DAYS_IN_MONTH[age[1] - 1]:
                print("Out of range of days")
                # TODO Fix this!
        # elif age[0] > CURRENT_DATE[0] and age[1] > CURRENT_DATE[1] and age[2] > CURRENT_DATE[2]:
        #     print("You haven't been born yet!")
        else:
            return True
    else:
        print("Please enter numbers for the date of birth")
    return False


def get_age(age):
    """Calculates the exact age from CURRENT_DATE."""
    age = convert_date_to_integer(age)
    days = CURRENT_DATE[0] - age[0]
    months = CURRENT_DATE[1] - age[1]
    years = CURRENT_DATE[2] - age[2]

    if days < 0:
        months = months - 1
        if age[1] == 2 and age[2] % 4 == 0:
            days = days + 29
        else:
            days = days + DAYS_IN_MONTH[age[1] - 1]

    if months < 0:
        years = years - 1
        months = months + 12

    return days, months, years


def convert_date_to_integer(date_of_birth):
    """Takes in a list of strings and returns them as integers."""
    day_month_year = []
    for date in date_of_birth:
        day_month_year.append(int(date))
    return day_month_year


main()
