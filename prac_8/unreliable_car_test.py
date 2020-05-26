from prac_8.unreliable_car import UnreliableCar


def main():
    new_good_car = UnreliableCar('GOOD', 100, 100)
    new_bad_car = UnreliableCar("BAD", 100, 10)

    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(new_good_car.name, new_good_car.drive(i)))
        print("{:12} drove {:2}km".format(new_bad_car.name, new_bad_car.drive(i)))

    print(new_good_car)
    print(new_bad_car)
    

if __name__ == '__main__':
    main()

