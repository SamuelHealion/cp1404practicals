"""
CP1404 Practical 5
Stores a users email and name in a dictionary. It will attempt to extract
the name of the user based off the email address
"""


def main():
    """Create a dictionary of user emails and names."""
    saved_emails = {}
    email = input("Email: ")
    while email != '':
        name = get_name(email)
        correct_name = input("Is this name correct? {} (Y/n) ".format(name))
        if correct_name.upper() != 'Y' and correct_name != '':
            name = input("Name: ").title()

        saved_emails[email] = name
        email = input("Email: ")

    for email, name in saved_emails.items():
        print("{} ({})".format(name, email))


def get_name(email):
    """Get a name from an email address."""
    name = email.split('@')
    split_name = name[0].split('.')
    full_name = ' '.join(split_name).title()
    return full_name


main()
