from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi('Hummer', 200, 4)
    print(hummer)  # result should resemble "Hummer, fuel=200, odo=0, 0km on current fare, $4.92/km plus flagfall of
    # $4.50

    test = SilverServiceTaxi('Test Silver Taxi', 20, 2)
    test.drive(18)
    print('Current fare: ${:.2f}'.format(test.get_fare()))


main()
