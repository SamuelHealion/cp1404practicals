try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
1. When will a ValueError occur?
ValueError will occur when the user attempts to input anything that isn't an integer

2. When will a ZeroDivisionError occur?
When the user enters a 0 for the denominator

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
By adding an if statement before performing the calculation of the fraction we can avoid the ZeroDivisionError
This is effectively the same response, but we have addressed it with control rather than the system returning the error
itself.
"""