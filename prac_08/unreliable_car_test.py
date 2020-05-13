from prac_08.unreliable_car import UnreliableCar


def main():
    unreliable_car = UnreliableCar('Mazda', 100, 0)
    print(unreliable_car)

    reliable_car = UnreliableCar('Ute', 100, 100)
    print(reliable_car)

    # car is completely unreliable and should not drive so odometer will equal 0
    unreliable_car.drive(20)
    print(unreliable_car)

    # car is reliable and should drive so odometer will equal 20
    reliable_car.drive(20)
    print(reliable_car)


main()
