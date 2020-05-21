"""Sort files by allowing the user to enter a folder name for different file extensions"""
import os
import shutil


def main():
    os.chdir('FilesToSort')
    for directory_name, subdirectories, filenames in os.walk('.'):
        extensions_dict = {}
        for element in filenames:
            files = element.split('.')
            extension = files[1]
            if extension not in extensions_dict:
                folder_name = input("What category would you like to sort {} files into? ".format(files[1]))
                extensions_dict[extension] = folder_name
                try:
                    os.mkdir(folder_name)
                except FileExistsError:
                    pass
            try:
                shutil.move(element, "{}".format(extensions_dict[extension]))
            except shutil.Error:
                pass





main()
