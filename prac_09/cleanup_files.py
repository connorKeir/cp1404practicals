"""
CP1404/CP5632 Practical
Demos of various os module examples
"""

import os


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # add a loop to rename the files
        for element in filenames:
            new_name = get_fixed_filename(element)
            print("Renaming {} to {}".format(element, new_name))
            old_path = os.path.join(directory_name, element)
            new_path = os.path.join(directory_name, new_name)
            os.rename(old_path, new_path)


demo_walk()
