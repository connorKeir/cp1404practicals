"""
CP1404/CP5632 Practical
Clean up the file names in Lyric folder
"""

import os


def main():
    """ Clean up file names for neatness and presentation. """
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


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ''
    new_names_char = []
    for i, character in enumerate(filename[:-3]):
        nex_char = filename[i + 1]
        pre_char = filename[i - 1]
        if pre_char == ' ':
            new_names_char.append(character.upper())
        elif character == ' ':
            new_names_char.append('_')
        elif character.islower() and nex_char.isupper():
            new_names_char.append(character + '_')
        elif character.isupper() and nex_char.isupper():
            new_names_char.append(character + '_')
        elif character != '_' and nex_char == '(':
            new_names_char.append(character + '_')
        elif pre_char == '(':
            new_names_char.append(character.upper())

        else:
            new_names_char.append(character)
    new_names_char.append('txt')
    # print(new_names_char)
    for i in new_names_char:
        new_name += i
    return new_name


main()
