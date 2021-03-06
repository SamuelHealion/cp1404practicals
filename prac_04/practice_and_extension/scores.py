"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    sorted_scores = sort_scores(score_values)
    display_scores(sorted_scores, subjects)


def sort_scores(score_values):
    """Sort scores by subject."""
    subject_scores = []
    for i in range(len(score_values[0])):
        scores_for_subject = []
        for score in score_values:
            scores_for_subject.append(score.pop(0))
        subject_scores.append(scores_for_subject)
    return subject_scores


def display_scores(sorted_scores, subjects):
    """Display the scores in formatted table."""
    for i in range(len(subjects)):
        print(subjects[i], "Scores:")
        for score in sorted_scores[i]:
            print(score)
        print("Max:", max(sorted_scores[i]))
        print("Min:", min(sorted_scores[i]))
        print("Avg:", sum(sorted_scores[i]) / len(sorted_scores[i]))
        print()


main()
