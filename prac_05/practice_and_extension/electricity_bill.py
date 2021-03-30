"""
CP1404 Practice Week 5
Calculate the electricity bill based on provided cents per kWh, daily use and number of billing days
Changed to use dictionaries for the tariffs
"""

TARIFFS = {11: 0.244618, 31: 0.136928, 45: 0.385294, 91: 0.374825, 33: 0.299485}

print("Electricity bill estimator 2.0")
print("Which tariff are you on?")
for tariff, cost in TARIFFS.items():
    print("Tariff {} at {} per kWh".format(tariff, cost))
valid_tariff = False
while not valid_tariff:
    try:
        which_tariff = int(input(">>> "))
        if which_tariff in TARIFFS.keys():
            valid_tariff = True
        else:
            print("Not a valid tariff")
    except ValueError:
        print("Please enter a number")

daily_use = float(input("Enter daily use in kWh: "))
number_of_days = float(input("Enter number of billing days: "))

estimated_bill = TARIFFS[which_tariff] * daily_use * number_of_days

print("Estimated bill: ${:.2f}".format(estimated_bill))

"""
Original version
print("Electricity bill estimator")
cents_per_kwh = float(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
number_of_days = float(input("Enter number of billing days: "))

estimated_bill = (cents_per_kwh / 100) * daily_use * number_of_days
print("Estimated bill: ${:.2f}".format(estimated_bill))
"""
