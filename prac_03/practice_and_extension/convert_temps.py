"""
Generates at least 15 floats of any values between -200 and 200
Converts these temperatures to fahrenheit
"""
import random


def main():
    generate_random_temps()

    in_file = open("temps_input.txt", 'r')
    for temperature in in_file:
        celsius = fahrenheit_to_celsius(float(temperature))
        print("{:.2f}".format(celsius))


def generate_random_temps():
    """Generates a list of random fahrenheit temperatures and saves them in temps_input.txt"""
    out_file = open("temps_input.txt", 'w')
    for count in range(random.randint(15, 30)):
        print("{:.2f}".format(random.uniform(-200, 200)), file=out_file)
    out_file.close()


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()