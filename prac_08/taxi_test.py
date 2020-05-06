from prac_08.taxi import Taxi


def main():
    taxi_test = Taxi(100, 'Prius 1')  # create new taxi with name "Prius 1", 100 units of fuel

    taxi_test.drive(40)  # Drive the taxi 40km

    # print the taxi details and the current fare
    print(taxi_test)
    print('Current fare: ${:.2f}'.format(taxi_test.get_fare()))

    # Restart the meter (start a new fare) and then drive 100km
    taxi_test.start_fare()
    taxi_test.drive(100)

    # print the details and the current fare
    print(taxi_test)
    print('Current fare: ${:.2f}'.format(taxi_test.get_fare()))


main()
