import random

print(random.randint(5, 20))
# Smallest number could have been 5, largest could have been 20

print(random.randrange(3, 10, 2))
# Smallest number could have been 3, largest could have been 9
# This could not have produced a 4 as it steps by two giving only odd numbers

print(random.uniform(2.5, 5.5))
# Smallest number could have been 2.5, largest is 5.5

print(random.randint(1, 100))
# Random number between 1 and 100 inclusive
