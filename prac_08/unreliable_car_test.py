from unreliable_car import UnreliableCar

def main():
    high_reliability_car = UnreliableCar("Limo",100,99)
    low_reliability_car = UnreliableCar("Daewoo",100,9)


    high_reliability_car.drive(50)
    low_reliability_car.drive(50)

    print(high_reliability_car)
    print(low_reliability_car)


main()