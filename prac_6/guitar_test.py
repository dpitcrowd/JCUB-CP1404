from prac_6.guitar import Guitar

CURRENT_YEAR = 2020


def main():
    name = 'Blackie'
    year = 1970
    cost = 1000000.00

    guitar = Guitar(name, year, cost)
    new_guitar = Guitar('Fender', 1950, 120000.00)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 2000, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(new_guitar.name, 2000, new_guitar.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(new_guitar.name, False, new_guitar.is_vintage()))


if __name__ == '__main__':
    main()