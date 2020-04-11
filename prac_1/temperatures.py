"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def fahrenheit():
    """ Convert Celsius degrees in Fahrenheit degrees"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F \n".format(fahrenheit))


def celsius():
    """ Convert Fahrenheit degrees in Celsius degrees"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (fahrenheit - 32) / (9.0 / 5)
    print("Result: {:.2f} C \n".format(celsius))


def main():
    """ Run my script"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius()
        elif choice == "F":
            fahrenheit()
        else:
            print('Invalid option \n')
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


main()