"""
CP1404 Practical 10 - Testing, API, Flask
Practice using the Wikipedia API
"""

import wikipedia


def main():
    """Use Wikipedia API to show summaries of pages"""
    print("Please enter a search phrase for Wikipedia")
    user_input = input(">>> ")
    while not user_input == '':
        try:
            wiki_page = wikipedia.page(user_input, auto_suggest=False)
            print(wiki_page.title)
            print(wiki_page.url)
            print(wiki_page.summary)
        except wikipedia.exceptions.PageError:
            print("Sorry, we couldn't find what you were after.")
        except wikipedia.exceptions.DisambiguationError as e:
            print("Sorry, that search is too ambiguous. Here is a list of what you might be after.")
            print(e.options)
        print("Please enter a search phrase for Wikipedia")
        user_input = input(">>> ")


if __name__ == '__main__':
    main()
