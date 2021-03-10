"""
Takes in a number of scores and generates some random ones then exports that to a file
"""
import random


def main():
    number_of_scores = int(input("Please enter how many scores you would like: "))
    out_file = open("results.txt", 'w')
    for count in range(number_of_scores):
        score = random.randint(0, 100)
        result = score_result(score)
        print("{} is {}".format(score, result), file=out_file)
    out_file.close()


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
