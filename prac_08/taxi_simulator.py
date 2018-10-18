from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    total_cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    display_taxis(taxis)
    print(MENU)
    menu_choice = input(">>>").lower
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose Taxi:"))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            print("selected drive")
        else:
            print("Invalid option")
        print("Bill to date: ${}".format(total_cost))
        menu_choice = input(">>>")
    print("Total trip cost:",format(total_cost))
    display_taxis(taxis)



def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))

main()