"""
CP1404 Practical 9 - Files and Exceptions
Sort files into directories by their extension
"""

import os
import shutil


def main():
    """Sort files by their extension."""
    os.chdir('FilesToSort')
    files = os.listdir('.')

    for file in files:
        extension = file.split('.')[-1]
        try:
            os.mkdir(extension)
            shutil.move(file, extension)
        except FileExistsError:
            shutil.move(file, extension)


if __name__ == '__main__':
    main()
