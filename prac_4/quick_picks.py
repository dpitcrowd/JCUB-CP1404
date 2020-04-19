"""
"Quick Pick" Lottery Ticket Generator
"""

import random

#LINE = 1
MIN_NUM = 1
MAX_NUM = 45
MENU = """
       Choose a number between 1 and 45
       then how  many lines you need to
            (by default is 6 line)
       """


def main():
    """ Random numbers"""
    LINE = 0
    print(MENU)
    quick_pick = check_int()
    #LINE = check_int()
    while int(quick_pick) <= 0 or int(quick_pick) > 45:
        print('\nThe number {} inserted is not valid !!!'.format(quick_pick))
        quick_pick = check_int()
    LINE = check_int()
    if int(LINE) < 6:
        LINE = 6

    quick_picks = []
    for i in range(quick_pick):
        for j in range(LINE):
            num = random.randint(MIN_NUM, MAX_NUM)
            while num in quick_picks:
                num = random.randint(MIN_NUM, MAX_NUM)
            quick_picks.append(num)
        quick_picks.sort()

        print(" ".join("{:2}".format(number) for number in quick_picks))


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
    return number


main()