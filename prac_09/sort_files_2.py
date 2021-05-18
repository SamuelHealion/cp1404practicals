"""
CP1404 Practical 9 - Files and Exceptions
Sort files by their extension and let the user control the subdirectories
"""

import os
import shutil


def main():
    """Sort files by their extension into user controlled categories."""
    extensions_to_categories = {}
    categories = []

    os.chdir('FilesToSort')
    files = os.listdir('.')

    for file in files:
        extension = file.split('.')[-1]
        if extension not in extensions_to_categories:
            category = input("What category would you like to sort {} files into? ".format(extension))
            extensions_to_categories[extension] = category
            if category not in categories:
                os.mkdir(category)
                categories.append(category)
        shutil.move(file, extensions_to_categories[extension])


if __name__ == '__main__':
    main()
