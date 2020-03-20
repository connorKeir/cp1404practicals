"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    data_formatted(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects_data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        subjects_data.append(parts)  # add the parts lists into the greater subjects_data list
    return subjects_data
    input_file.close()


def data_formatted(messy_data):
    for i in range(0, len(messy_data)):
        # Input data into a formatted text to print
        print("{} is taught by {} and has {} students".format(messy_data[i][0], messy_data[i][1], messy_data[i][2]))


main()
