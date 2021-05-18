"""
CP1404 Practical 9 - Files and Exceptions
Practice using os modules to change filenames
"""
import os


def main():
    """Cleanup filenames for songs to a consistent format."""

    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Changing {} to {}".format(filename, new_name))
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ''
    for i, char in enumerate(filename):
        try:
            if filename[i].islower() and filename[i+1].isupper():
                # When the next character is a capital
                new_name += char + '_'
            elif filename[i].isupper() and filename[i+1].isupper():
                # When two capitals are next to each other
                new_name += char + '_'
            elif filename[i-1] == ' ':
                # Capitalise all characters after a space
                new_name += char.upper()
            else:
                new_name += char
        except IndexError:  # Handle when filename[i+1] is past the end of the string
            new_name += char
    return new_name.replace(" ", "_").replace(".T_X_T", ".txt")


main()
