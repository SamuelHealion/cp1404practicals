"""
CP1404 Practical 5
Takes a sentence from the user and counts how many times a word appears using dictionaries
"""


def main():
    """Take user input and count how many times a word appears."""
    user_text = str(input("Text: "))
    split_words = user_text.split()
    all_words = {}
    for word in split_words:
        if word in all_words:
            all_words[word] += 1
        else:
            all_words[word] = 1

    sorted_words = list(all_words.keys())
    sorted_words.sort()
    longest_word = max((len(word) for word in sorted_words))

    for word in sorted_words:
        print("{:{}} : {}".format(word, longest_word, all_words[word]))


main()
