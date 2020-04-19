"""
CP1404/CP5632 Practical
List exercises
"""


def main():
    menu = '''
    1. NUMBERS
    2. PASSWORD
    3. EXIT
    '''
    print(menu)
    #menu_choice = input('Choose which exercise --> ')
    menu_choice = check_int()
    #print(menu_choice)
    while menu_choice != 1 or menu_choice != 2 or menu_choice != 3:
        if menu_choice == 1:
            my_numbers()
        elif menu_choice == 2:
            my_password()
        elif menu_choice == 3:
            exit('THANKS')
        else:
            print('Your choice in not in the menu')
        print(menu)
        menu_choice = check_int()


def my_password():
    '''2 Woefully inadequate security checker'''
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    name = input('\nEnter your name --> ')
    if name in usernames:
        print('ACCESS GRANTED')
    else:
        print('!!! ACCESS DENIED !!!')


def my_numbers():
    """1 Numbers """
    numbers = []
    print('\nPlease insert how many numbers')
    choice = check_int()
    for i in range(choice):
        print('\nPlease give me your {}th number'.format(i + 1))
        number = check_int()
        numbers.append(number)
    ''' Show the inserted number'''
    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / len(numbers))


def check_int():
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
