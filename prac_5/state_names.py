"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
MENU = """
        PLEASE SELECT ONE THOSE
        
        1. CHOOSE A STATE
        
        2. EXIT
        
"""

STATES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
    }


def main():
    print(MENU)
    choice = input('\t\tSelect your choice >>> ')

    try:
        while choice != '2':
            state = input("\t\tEnter short state: ").upper()

            if state in STATES:
                print('\t\t{} is {}'.format(state, STATES[state]))
                print('\n', MENU)
                choice = input('Select your choice >>> ')
            else:
                print("\t\tInvalid short state")
            state = input("\t\tEnter short state: ").upper()

    except ValueError:
        print(MENU)
        choice = input('\t\tSelect your choice >>> ')


if __name__ == '__main__':
    main()

