"""
CP1404/CP5632 Practical
Cumulative total income program that asks the user for the number of months of income to enter.
It will then asks for those totals and return the cumulative total of each input
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)

    print_report(incomes, number_of_months)


def print_report(incomes, number_of_months):
    """Prints an income report formatted in a legible layout with the cumulative total of incomes"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(0, number_of_months):
        income = incomes[month]
        total += income
        print("Month {:2} - Income: ${:10.2f} {:5} Total: ${:10.2f}".format(month, income, "", total))


main()
