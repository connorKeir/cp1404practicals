def main():
    count = 0  # initialise count at 0
    numbers = []  # initialise numbers list
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']  # initialise approved users list

    # basic list operations activities
    while count < 5:  # ask for 5 numbers
        number = int(input("Enter a number: "))  # add user input to number variable
        numbers.append(number)  # add number from user to list
        count += 1
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(average_calculator_list(numbers)))

    print("~~~~~~~~~~~~~")  # create a gap in between exercises

    # Woefully inadequate security checker
    username = input("Enter your username: ")
    security_checker(username, usernames)



def average_calculator_list(list):
    # calculate the average number in a list of integers
    return sum(list) / len(list)

def security_checker(user, usernames):
    # check if the user is an approved user
    if user in usernames:
        print("Access Granted")
    else:
        print("Access denied")


main()
