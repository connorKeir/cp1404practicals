def main():
    """search string and print occurrences of each word"""
    user_string = input("Text: ")
    words = user_string.split()
    format_length = len(max(words, key=len))
    word_dict = {}
    method_name(word_dict, words)
    for key, value in word_dict.items():
        print("{:{}} : {}".format(key, format_length, value))


def method_name(word_dict, words):
    """count words in a text"""
    for string in words:
        # sort and count each word in the string
        if string not in word_dict:
            word_dict[string] = 1
        elif string in word_dict:
            word_dict[string] += 1
    return word_dict


main()