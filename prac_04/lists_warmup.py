# numbers = [3,1,4,5,9,2]


# checks below were done within the python console

# numbers[0] result = 3
# check result = 3

# numbers[-1] result = 2
# check result = 2

# numbers[3] result = 5
# check result = 5

# numbers[:-1} result = 3,1,4,5,9
# check result = 3, 1, 4 , 5, 9

# numbers[3:4] result = 5
# check result = 5

# 5 in numbers result = true
# check result = True

# 7 in numbers result = false
# check result = False

# "3" in numbers result = false
# check result = False

# numbers + [6, 5, 3] result = [3, 1, 4, 5, 9, 6, 5, 3]
# check result = [3, 1, 4, 5, 9, 6, 5, 3]
def main():
    numbers = [3, 1, 4, 5, 9, 2]  # create numbers list

    numbers[0] = "ten"  # change first element to string ten
    numbers[-1] = 1  # change last element to 1
    print(numbers[2:])  # get all elements from numbers except the first two
    print(9 in numbers)  # check if 9 is an element in numbers

    print(numbers)  # print numbers to preform a visual check of the functions


main()
