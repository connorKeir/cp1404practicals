# Question 1

name = input("Please enter your name: ")  # stores the users name
name_file = open("name.txt", 'w')  # opens the file for writing the users name
print(name, file=name_file)

name_file.close()  # close the file that contains the user name


# Question 2

read_file = open("name.txt", 'r')  # opens the name.txt file in a read only form
print("Your name is", read_file.read())  # reads the whole file and prints. (the code clears every time a new name is
# entered so their will only be one name)

read_file.close() # closes the instance that was used for reading


# Question 3

calculate_file = open("numbers.txt", 'r')  # opens the numbers.txt file as a read only copy
addition = int(calculate_file.readline()) + int(calculate_file.readline())  # converts the first two lines in the file
# to an integer and totals them
print(addition)

calculate_file.close()  # closes the numbers.txt file


# Question 4
total_file = open("numbers.txt", 'r')  # opens file for totaling
total = 0  # starts the variable total
for line in total_file:  # starts a for loop to iterate through all the lines
    total += int(line)  # adds the line of code
print(total)  # displays the total

total_file.close()  # closes the file that was used for totaling

