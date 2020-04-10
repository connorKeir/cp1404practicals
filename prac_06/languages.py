from prac_06.programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    print("")  # space between two print statements

    languages = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")
    for element in languages:
        if element.is_dynamic():
            print(element.name)


main()