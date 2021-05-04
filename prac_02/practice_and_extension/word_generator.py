"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def first_version():
    """Requires c and v only"""
    print("Please enter the word format: C for Consonants, V for Vowels")
    word_format = str(input("> ").lower())
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        elif kind == "v":
            word += random.choice(VOWELS)
        else:
            print("Invalid input")
            break

    print(word)


def second_version():
    """Uses wild cards but also accepts regular inputs
    # for vowels, % for consonants and * for either"""

    print("Random word generator that includes your characters but uses:")
    print("Enter # for Vowels, % for Consonants or * for either")
    word_format = str(input("> "))
    word = ""
    for kind in word_format:
        if kind == "%":
            word += random.choice(CONSONANTS)
        elif kind == "#":
            word += random.choice(VOWELS)
        elif kind == "*":
            word += random.choice(CONSONANTS + VOWELS)
        else:
            word += kind

    print(word)


def third_version():
    """Automatically generates the word_format for a random length between 1 and 20"""

    word_length = random.randint(0, 20)
    word_format = ''
    for i in range(word_length):
        word_format += random.choice('%' + '#')
    word = ""
    for kind in word_format:
        if kind == "%":
            word += random.choice(CONSONANTS)
        elif kind == "#":
            word += random.choice(VOWELS)

    print(word)


user_input = ''
while user_input != 'Q':
    print("Press Q to quit")
    print("What version would you like to run? 1, 2 or 3")
    user_input = str(input(">>> ")).upper()

    if user_input == '1':
        first_version()
    elif user_input == '2':
        second_version()
    elif user_input == '3':
        third_version()
    else:
        print("Invalid option")
