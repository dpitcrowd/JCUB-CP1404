"""
CP1404/CP5632 - Practical - Suggested Solution
Password checker built from "skeleton" code to help you get started
"""

""" My constants"""
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def get_password(password, MIN_LENGTH, MAX_LENGTH, UPPER_CASE, LOWER_CASE, SPECIAL_CHARS_REQUIRED, DIGIT):
    """Determine if the provided password is valid."""

    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    password_upper = 0
    """ Remove # if you want implement also lower case"""
    password_lower = 0
    special_characters = 0
    digit = 0

    for i in password:
        if i.isdigit():
            digit += 1
        elif i.isupper():
            password_upper += 1
        elif i.islower():
            password_lower += 1
        elif i in SPECIAL_CHARACTERS:
            special_characters += 1

    if UPPER_CASE == "True":
        if password_upper == 0:
            return False
    """ Remove # if you want implement also lower case"""
    if LOWER_CASE == "True":
        if password_lower == 0:
            return False
    if DIGIT == "True":
        if digit == 0:
            return False
    if SPECIAL_CHARS_REQUIRED == "True":
        if special_characters == 0:
            return False

    return True


def main():
    """Program to get and check a user's password."""

    """ My local variables"""
    MIN_LENGTH = 1
    MAX_LENGTH = 1
    UPPER_CASE = "False"
    LOWER_CASE = "False"
    SPECIAL_CHARS_REQUIRED = "False"
    DIGIT = 0

    print("This script allows you to analyze your password and see if it meets the required parameters. ")
    MIN_LENGTH = int(input("Enter min length for your password --> "))
    MAX_LENGTH = int(input("Enter max length for your password --> "))

    while True:
        UPPER_CASE = input("Do you want to use at least one upper case character (y/n) n --> ")
        if UPPER_CASE == "Y" or UPPER_CASE == "y":
            UPPER_CASE = "True"
            MAX_LENGTH += 1
        else:
            UPPER_CASE = "False"
        break
    """ Remove # if you want implement also lower case"""
    while True:
        LOWER_CASE = input("Do you want to use at least one lower case character (y/n) n --> ")
        if LOWER_CASE == "Y" or LOWER_CASE == "y":
            LOWER_CASE = "True"
            MAX_LENGTH += 1
        else:
            LOWER_CASE = "False"
        break
    while True:
        print("Set of special characters", SPECIAL_CHARACTERS)
        SPECIAL_CHARS_REQUIRED = input("Do you want to use a special character (y/n) n --> ")
        if SPECIAL_CHARS_REQUIRED == "Y" or SPECIAL_CHARS_REQUIRED == "y":
            SPECIAL_CHARS_REQUIRED = "True"
            MAX_LENGTH += 1
        else:
            SPECIAL_CHARS_REQUIRED = "False"
        break
    while True:
        DIGIT = input("Do you want to use at least one digit (y/n) n --> ")
        if DIGIT == "Y" or DIGIT == "y":
            DIGIT = "True"
            MAX_LENGTH += 1
        else:
            DIGIT = "False"
        break

    password = input("Enter your password --> ")

    while not get_password(password, MIN_LENGTH, MAX_LENGTH, UPPER_CASE, LOWER_CASE, SPECIAL_CHARS_REQUIRED, DIGIT):
        print("Invalid password!")
        password = input("Enter your password --> ")
    print("Your password is valid and made of {} characters and is {}".format(len(password), password))


main()