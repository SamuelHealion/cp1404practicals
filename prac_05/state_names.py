"""
CP1404/CP5632 Practical
State names in a dictionary
Reformatted to follow PEP 8 standards and displays all the states neatly
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales",
               "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria",
               "TAS": "Tasmania"}

for short_state, state in STATE_NAMES.items():
    print("{:3} is {}".format(short_state, state))

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in STATE_NAMES:
        print(state_code, "is", STATE_NAMES[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
