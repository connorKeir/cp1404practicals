MIN_LENGTH = 4


def main():
    password = input("Please enter your password that is at least {} characters long: ".format(MIN_LENGTH))

    get_password(password)

    print_asterisk(password)


def print_asterisk(password):
    for i in range(0, len(password), 1):
        print('*', end=' ')


def get_password(password):
    while len(password) < MIN_LENGTH:
        password = input("Please enter your password that is at least {} characters long: ".format(MIN_LENGTH))
    return password


main()
