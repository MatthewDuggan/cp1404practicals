from taxi import Taxi


def main():
    taxi_prius = Taxi("Prius 1", 100)
    taxi_prius.start_fare()
    taxi_prius.drive(40)
    print(taxi_prius)
    print("$", taxi_prius.get_fare())

    taxi_prius.start_fare()
    taxi_prius.drive(100)
    print(taxi_prius.__str__())
    print("$", taxi_prius.get_fare())

main()
