"""
CP1404 Practical 9 - Practice and Extension
This program checks which lyric text files don't contain copyright information
"""

import os


def main():
    os.chdir('..')
    os.chdir('Lyrics')
    subdirectories = os.listdir('.')
    for subdirectory in subdirectories:
        os.chdir(subdirectory)
        print(os.getcwd())
        for filename in os.listdir('.'):
            with open(filename, 'r') as in_file:
                if '.i ' not in in_file.read():
                    print(filename)
        os.chdir('..')


if __name__ == '__main__':
    main()
