"""
CP1404 Practical 5 Stores a users email and name in a dictionary. It will attempt to extract
the name of the user based off the email address
"""


def main():
    """Creates a dictionary of user emails and names"""
    saved_emails = {}
    email = str(input("Email: "))
    while email != '':
        name = get_name(email)
        correct_name = str(input("Is this name correct? {} (Y/n) ".format(name)))
        if correct_name.lower() != 'y' and correct_name != '':
            name = str(input("Name: ")).title()

        saved_emails[email] = name
        email = str(input("Email: "))

    for name, email in saved_emails.items():
        print("{} ({})".format(email, name))


def get_name(email):
    """Gets a name from an email address."""
    name = email.split('@')
    split_name = name[0].split('.')
    full_name = ' '.join(split_name).title()
    return full_name


main()
