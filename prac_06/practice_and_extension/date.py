"""
CP1404 Practical 6 - Practice and Extension
Define a Date class
"""

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Date:
    """Define a Date class."""

    def __init__(self, day=0, month=0, year=0):
        """Initialise a Date object."""

        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        """Return a string representation of the Date class."""
        return "The date is {Date.day}/{Date.month}/{Date.year}".format(Date=self)

    def add_days(self, n):
        days_left = n
        current_month = self.month - 1
        while self.day + days_left > DAYS_IN_MONTH[current_month]:
            if self.is_leap_year() and current_month == 1:
                days_left -= DAYS_IN_MONTH[current_month] + 1
            else:
                days_left -= DAYS_IN_MONTH[current_month]
            if current_month < 11:
                current_month += 1
            else:
                current_month = 0
                self.year += 1
        self.month = current_month + 1
        self.day += days_left

    def is_leap_year(self):
        if self.year % 4 == 0:
            return True
        else:
            return False


day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))
# day, month, year = 1, 1, 1990

date = Date(day, month, year)
print(date)

extra_days = int(input("How many days would you like to add? "))
date.add_days(extra_days)

print(date)
