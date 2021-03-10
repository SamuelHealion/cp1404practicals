"""
CP1404/CP5632 - Practical
Returns a result based on a users score out of 100
Refactored to use functions
"""

import random


def main():
    score = float(input("Enter score: "))
    result = score_result(score)
    print(result)

    random_score = random.randrange(0, 100)
    result = score_result(random_score)
    print("Random score is: {}".format(random_score))
    print(result)


def score_result(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
