from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    test_guitar = Guitar("Test Guitar", 2013, 15)

    print(gibson.get_age())  # Expected 98. Got 98
    print(test_guitar.get_age())  # Expected 7. Got 7

    print(gibson.is_vintage())  # Expected True. Got
    print(test_guitar.is_vintage())  # Expected False. Got

main()
