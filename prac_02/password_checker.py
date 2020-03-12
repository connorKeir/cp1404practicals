"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between {} and {} characters, and contain:".format(MIN_LENGTH, MAX_LENGTH))
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: {}".format(SPECIAL_CHARACTERS))
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False

    # the following two if statements as "MIN_LENGTH > len(password) and len(password) > MAX_LENGTH" does not work so
    # two separate if statements are used
    if MIN_LENGTH > len(password):
        return False
    elif MAX_LENGTH < len(password):
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)

        # for each character run a check to see if it is a lowercase, upper case, a digit or if it is in the special
        # characters list
        if char.islower() is True:
            count_lower += 1
        if char.isupper() is True:
            count_upper += 1
        if char.isdigit() is True:
            count_digit += 1
        if char in SPECIAL_CHARACTERS:
            count_special += 1


    # TODO: if any of the 'normal' counts are zero, return False
    if count_lower == 0:
        return False
    elif count_upper == 0:
        return False
    elif count_digit == 0:
        return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
    if SPECIAL_CHARS_REQUIRED:
        if count_special == 0:
            return False


    # if we get here (without returning False), then the password must be valid
    return True


main()