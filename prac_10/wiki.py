import wikipedia


def main():
    user_search_term = input("Enter a Page Title or Search Phrase: ")
    while user_search_term != '':
        try:
            user_page = wikipedia.page(user_search_term)
            print("Title: {}".format(user_page.title))
            print("Summary: {}".format(user_page.summary))
            print("URL: {}".format(user_page.url))
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        user_search_term = input("Enter a Page Title or Search Phrase: ")


main()
