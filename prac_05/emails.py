def main():
    """store user emails and determine user name"""
    email = input("Email: ")
    email_dict = {}
    while email != '':
        name_guess = get_name(email)
        name_response = input(("Is your name {}? (Y/n) ".format(name_guess))).lower()
        # check if the guessed name
        if name_response == 'y' or name_response == 'yes' or name_response == '':
            name = name_guess
        elif name_response == 'n' or name_response == 'no':
            name = input("Name: ").title()
        email_dict[email] = name
        email = input("Email: ")

    for key, value in email_dict.items():
        print("{} ({})".format(value, key))


def get_name(email):
    """take the users email and deduce users name"""
    first_email_split = email.split('.')
    join_length = ' '
    first_email_join = join_length.join(first_email_split)
    second_email_split = first_email_join.split('@')
    return second_email_split[0].title()






main()
