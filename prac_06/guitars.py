from prac_06.guitar import Guitar


def main():
    """Stores users guitars and displays details."""
    print("My guitars!")

    guitars = []

    variable_check = False

    while not variable_check:
        guitar_name = input("Name: ")
        if guitar_name == '':
            variable_check = True
        else:
            guitar_year = int(input("Year: "))
            guitar_cost = float(input("Cost: "))
            print("{} ({}) : ${:.2f} added.".format(guitar_name, guitar_year, guitar_cost))
            guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print(" ")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else:
            vintage_string = ''
        print("Guitar {}: {guitar.name:<20} ({guitar.year}), worth ${guitar.cost:10,.2f}{}".format(i, vintage_string,
                                                                                                   guitar=guitar))


main()
