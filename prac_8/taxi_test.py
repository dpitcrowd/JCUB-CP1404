from prac_8.taxi import Taxi


def main():
    #new_taxi = Taxi('Prius 1', 100, 1.23)
    new_taxi = Taxi('Prius 1', 100)
    new_taxi.drive(40)
    print(new_taxi)
    new_taxi.drive(100)
    print(new_taxi)


if __name__ == '__main__':
    main()