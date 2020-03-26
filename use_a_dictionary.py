ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

ages_dict[user_name] = user_age   # add user name and user age to directory

for name in ages_dict:
    print("{} - {}".format(name, ages_dict[name]))