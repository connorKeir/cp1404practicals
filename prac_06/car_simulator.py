from prac_06.car import Car

MENU = """Menu: 
d) drive
r) refuel
q) quit"""


def main():
    print("Lets drive!")
    user_car_name = input("Enter your car name: ")
    user_car = Car(100, user_car_name)

    print(user_car)
    print(MENU)
    choice = input("Enter your choice: ")

    while choice != 'q':
        if choice == 'd':
            variable_check = False
            while not variable_check:
                drive_distance = int(input("How many km do you wish to drive? "))
                if drive_distance < 0:
                    print("Distance must be >= 0")
                else:
                    variable_check = True
            user_car.drive(drive_distance)
            print("The car drove {}km.".format(drive_distance))
        elif choice == 'r':
            variable_check = False
            while not variable_check:
                user_fuel_refill = int(input("How many units of fuel do you want to add to the car? "))
                if drive_distance < 0:
                    print("Fuel amount must be >= 0")
                else:
                    variable_check = True
            user_car.add_fuel(user_fuel_refill)
            print("Added {} units of fuel".format(user_fuel_refill))
        else:
            print("Invalid choice")
        print(' ')
        print(user_car)
        print(MENU)
        choice = input("Enter your choice: ")
    print("Good bye {}'s driver.".format(user_car.name))


if __name__ == '__main__':
    main()
