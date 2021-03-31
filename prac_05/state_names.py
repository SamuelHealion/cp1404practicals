"""
CP1404/CP5632 Practical
State names in a dictionary
Reformatted to follow PEP 8 standards and displays all the states neatly
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
               "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria",
               "TAS": "Tasmania"}

for short_state, state in CODE_TO_NAME.items():
    print("{:3} is {}".format(short_state, state))

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
