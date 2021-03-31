"""
CP1404 Practical 5 - Hex Colours
Takes a user input and compares it to a dictionary with colours
and then prints their hexadecimal code
"""

COLOUR_TO_HEX = {'aliceblue': '#f0f8ff', 'darkgreen': '#006400',
                 'rosybrown': '#bc8f8f', 'salmon': '#fa8072',
                 'tomato1': '#ff6347', 'violetred': '#d02090',
                 'whitesmoke': '#f5f5f5', 'turquoise': '#40e0d0',
                 'sienna': '#a0522d', 'plum': '#dda0dd'}


def main():
    """Ask for a colour then print its hexadecimal code."""
    colour = input("Please enter a colour: ")
    while colour != '':
        if colour.lower() in COLOUR_TO_HEX:
            print("The code for {} is {}".format(colour, COLOUR_TO_HEX[colour]))
        else:
            print("That colour isn't on the list!")
        colour = input("Please enter a colour: ")
    print("Goodbye")


main()
