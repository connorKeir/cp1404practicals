min_length = 7

password = input("Please enter your password that is at least {} characters long: ".format(min_length))

while len(password) < min_length:
    password = input("That was too short, Try again: ")

for i in range(0, len(password), 1):
    print('*', end=' ')
