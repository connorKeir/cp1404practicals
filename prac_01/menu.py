name = input("Please enter you name: ")
menu = """(H)ello
(G)oodbye
(Q)uit"""

print(menu)
choice= input(">>> ")

while choice != 'Q':
    if choice == 'H':
        print("Hello ", name)
    elif choice  == 'G':
        print("Goodbye", name)
    else:
        print("Invalid input")
    print(menu)
    choice = input(">>> ")
print("Finished")
