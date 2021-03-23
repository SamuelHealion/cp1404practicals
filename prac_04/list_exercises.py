"""
Asks the user for 5 numbers and then will display various things about this list of numbers
"""
NUMBER_OF_INPUTS = 5

numbers = []
for i in range(0, NUMBER_OF_INPUTS):
    user_number = int(input("Number: "))
    numbers.append(user_number)

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
