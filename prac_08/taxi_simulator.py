from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    total_cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = imput(">>>").lower
    while menu_choice != "q":
        if menu_choice = "c":
            print("selected choose taxis")
        elif menu_choice="d":
            print("selected drive")
        else:
            print("Invalid option")
        print("Bill to date: ${}".format(total_cost))

