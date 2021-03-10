"""
CP1404 Practice
Calculate the electricity bill based on provided cents per kWh, daily use and number of billing days
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

estimated_bill = 0

print("Electricity bill estimator 2.0")
which_tariff = int(input("Which tariff? 11 or 31: "))
daily_use = float(input("Enter daily use in kWh: "))
number_of_days = float(input("Enter number of billing days: "))

if which_tariff == 11:
    estimated_bill = TARIFF_11 * daily_use * number_of_days
elif which_tariff == 31:
    estimated_bill = TARIFF_31 * daily_use * number_of_days

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
