MENU = """(E)ven numbers
(O)dd numbers
(S)quares
(Q)uit"""


def main():
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print(MENU)
    choice = input(">>> ")

    while choice != 'Q':
        if choice == 'E':
            for i in range(x, y):
                if i % 2 == 0:
                    print(i)
        if choice == 'O':
            for i in range(x, y):
                if i % 2 == 1:
                    print(i)
        if choice == 'S':
            for i in range(x, y):
                print(i ** 2)
        x = int(input("Enter First Number: "))
        y = int(input("Enter Second Number: "))
        print(MENU)
        choice = input(">>> ")


main()