"""
CP1404 Practical
Multiple test of loops for practice
"""

# Odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Counts up in 10's from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Counts down from 20 to 1
for i in range(0, 20):
    print(20 - i, end=' ')
print()

# Prints the number of stars from user input on one line
number_of_stars = int(input('Number of stars: '))
for i in range(0, number_of_stars):
    print('*', end='')
print()

# Prints the number of stars from user input, increasing the number of stars per line
for i in range(number_of_stars):
    for j in range(i + 1):
        print('*', end='')
    print()
