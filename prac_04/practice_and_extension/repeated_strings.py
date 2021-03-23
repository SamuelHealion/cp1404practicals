"""
Takes an indefinite number of strings until an empty string is entered
Will check if any strings were repeated
"""

strings = []
repeated_strings = []
repeats = False

string = str(input("Enter a string: "))
while not string == '':
    if string in strings:
        repeated_strings.append(string)
        repeats = True
    else:
        strings.append(string)
    string = str(input("Enter a string: "))

if repeats:
    print("Strings repeated: {}".format(repeated_strings))
else:
    print("No repeated strings entered")
