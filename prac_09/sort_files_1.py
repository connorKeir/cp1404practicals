"""Sort files by creating a new directory for each new extension and sorting files with same extension into relevant
  directories."""
import os
import shutil


def main():
    os.chdir('FilesToSort')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for element in filenames:
            files = element.split('.')
            try:
                os.mkdir(files[1])
            except FileExistsError:
                pass
            shutil.move(element, files[1])


main()
