from prac_8.silver_service_taxi import SilverServiceTaxi


def main():
    """TEST"""
    taxi = SilverServiceTaxi("My Test Taxi", 10, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


if __name__ == '__main__':
    main()