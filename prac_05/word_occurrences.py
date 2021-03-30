"""
CP1404 Practical 5
Takes a sentence from the user and counts how many times a word appears using dictionaries
"""


def main():
    """Take user input and count how many times a word occurs."""
    words_to_occurrences = {}
    user_text = input("Text: ")
    user_words = user_text.split()
    for word in user_words:
        if word in words_to_occurrences:
            words_to_occurrences[word] += 1
        else:
            words_to_occurrences[word] = 1

    words = list(words_to_occurrences.keys())
    words.sort()
    longest_word = max((len(word) for word in words))

    for word in words:
        print("{:{}} : {}".format(word, longest_word, words_to_occurrences[word]))


main()
