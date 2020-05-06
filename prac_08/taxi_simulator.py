from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    taxi_bill = 0
    choice = None
    while choice != 'q':
        print(MENU)
        choice = input(">>> ")
        if choice == 'c':
            print("Taxis available:")
            for i in taxis:
                print("{} - {}".format(taxis.index(i), i))
            current_taxi = int(input("Choose taxi: "))
            print("Bill to date: {:.2f}".format(taxi_bill))
        if choice == 'd':
            taxis[current_taxi].start_fare()
            drive_distance = int(input("Drive how far? "))
            taxis[current_taxi].drive(drive_distance)
            trip_fare = taxis[current_taxi].get_fare()
            print("Your {} trip cost you ${:.2f}".format(taxis[current_taxi].name, trip_fare))
            taxi_bill += trip_fare
            print("Bill to date: {:.2f}".format(taxi_bill))



main()
