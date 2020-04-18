"""
CP1404/CP5632 Practical
List exercises
"""


def main():
    """ Numbers """
    numbers = []
    for i in range(5):
        print('Please give me your {}th number \n'.format(i+1))
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
