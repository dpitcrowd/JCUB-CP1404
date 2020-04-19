"""
"Quick Pick" Lottery Ticket Generator
"""

import random

LINE = 6
MIN_NUM = 1
MAX_NUM = 45
MENU = "Choose a number between 1 and 45"

def main():
    """ Random numbers"""
    print(MENU)
    quick_pick = check_int()
    while quick_pick <= 0 or quick_pick > 45:
        print('\nThe number {} inserted is not valid !!!'.format(quick_pick))
        quick_pick = check_int()

    quick_picks = []
    for i in range(quick_pick):
        for j in range(LINE):
            num = random.randint(MIN_NUM, MAX_NUM)
            while num in quick_picks:
                num = random.randint(MIN_NUM, MAX_NUM)
            quick_picks.append(num)
        quick_picks.sort()

    print(quick_picks)


def check_int():
    """ Check input number"""
    number = input("Enter a number --> ")
    check = "False"
    while check == "False":
        try:
            number = int(number)
            check = "True"
            pass
        except ValueError:
            number = input("Please enter an integer --> ")
        return int(number)


main()