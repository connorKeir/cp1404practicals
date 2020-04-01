def main():
    """search string and print occurrences of each word"""
    user_string = input("Text: ")
    words = user_string.split()
    word_dict = {}
    for string in words:
        # sort and count each word in the string
        if string not in word_dict:
            word_dict[string] = 1
        elif string in word_dict:
            word_dict[string] += 1
    for key, value in word_dict.items():
        print("{} : {}".format(key, value))


main()
