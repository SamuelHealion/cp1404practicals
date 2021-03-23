"""
Takes in numbers from a users input until a negative number is entered, then displays information about the list
The second part takes a username and checks it against a list
"""

numbers = []
user_number = int(input("Number 1: "))
while user_number >= 0:
    numbers.append(user_number)
    user_number = int(input("Number {}: ".format(len(numbers) + 1)))

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = str(input("Please enter your username: "))
if name in usernames:
    print("Access granted")
else:
    print("Access denied")
