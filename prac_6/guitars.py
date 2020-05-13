from prac_6.guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Price: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    guitars.append(Guitar('Fender', 1950, 120000.00))
    guitars.append(Guitar('Blackie', 1970, 1000000.00))

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("\nGuitar {0}: {1.name:<10} {1.year:<4} price ${1.cost:<20,.2f} {2:<10}".format
                  (i + 1, guitar, vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")


main()