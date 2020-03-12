for i in range(1, 21, 2):  # initial loop given as an example
    print(i, end=' ')
print()

for i in range(0, 101, 10):  # counts from 0 to 100 in steps in 10
    print(i, end=' ')
print()

for i in range(20, 0, -1):  # counts down from 20 to 1
    print(i, end=' ')
print()

star_number = int(input("How many stars do you want to see?  "))  # find out how many stars the user wants to see

for i in range(0, star_number, 1):  # prints out an amount of stars equal to star_number
    print('*', end=' ')
print()

for i in range(0, star_number, 1):  # prints out growing line of stars equal to star_number
    print('*' * (i+1))
print()
