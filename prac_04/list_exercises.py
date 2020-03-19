def main():
    count = 0
    numbers = []
    while count < 5:  # ask for 5 numbers
        number = int(input("Enter a number: "))  # add user input to number variable
        numbers.append(number)  # add number from user to list
        count += 1
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(average_calculator_list(numbers)))


def average_calculator_list(list):
    # calculate the average number in a list of integers
    return sum(list) / len(list)


main()
