"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            # celsius = 5 / 9 * (fahrenheit - 32)
            fahrenheit = float(input("Fahrenheit: "))  # take user input data as Fahrenheit value
            celsius = fahrenheit_to_celsius(
                fahrenheit)  # use the user given fahrenheit value and recalculate into celsius
            print("Result: {:.2f} C".format(celsius))  # display the calculated value of celsius to 2 decimal points
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


main()