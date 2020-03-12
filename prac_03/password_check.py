min_length = 4


def main():
    password = get_password()

    while len(password) < min_length:
        password = get_password()

    asterisk_printer(password)


def asterisk_printer(password):
    for i in range(0, len(password), 1):
        print('*', end=' ')


def get_password():
    return input("Please enter your password that is at least {} characters long: ".format(min_length))


main()
