"""
CP1404/CP5632 - Practical - Suggested Solution
Password checker built from "skeleton" code to help you get started
"""

SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def is_valid_password(password):
    """Determine if the provided password is valid."""

    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    password_upper = 0
    """ Remove # if you want implement also lower case"""
    #password_lower = 0
    special_characters = 0
    digit = 0

    for i in password:
        if i.isdigit():
            digit += 1
        elif i.isupper():
            password_upper += 1
        elif i in SPECIAL_CHARACTERS:
            special_characters += 1

    if UPPER_CASE == "True":
        if password_upper == 0:
            print(password_upper)
            return False
    """ Remove # if you want implement also lower case"""
    #if LOWER_CASE == "True":
        #if password_lower == 0:
            #return False
    if DIGIT == "True":
        if digit == 0:
            return False
    if SPECIAL_CHARS_REQUIRED == "True":
        if special_characters == 0:
            return False

    return True


"""Program to get and check a user's password."""
print("This script allows you to analyze your password and see if it meets the required parameters. ")
MIN_LENGTH = int(input("Enter min length for your password --> "))
MAX_LENGTH = int(input("Enter max length for your password --> "))

while True:
    UPPER_CASE = input("Do you want to use at least one upper case character (y/n) n --> ")
    if UPPER_CASE == "Y" or UPPER_CASE == "y":
        UPPER_CASE = "True"
    else:
        UPPER_CASE = "False"
    break
""" Remove # if you want implement also lower case"""
#while True:
    #LOWER_CASE = input("Do you want to use at least one lower case character (y/n) n --> ")
    #if LOWER_CASE == "Y" or LOWER_CASE == "y":
        #LOWER_CASE = "True"
    #else:
        #LOWER_CASE = "False"
    #break
while True:
    print("Set of special characters", SPECIAL_CHARACTERS)
    SPECIAL_CHARS_REQUIRED = input("Do you want to use a special character (y/n) n --> ")
    if SPECIAL_CHARS_REQUIRED == "Y" or SPECIAL_CHARS_REQUIRED == "y":
        SPECIAL_CHARS_REQUIRED = "True"
    else:
        SPECIAL_CHARS_REQUIRED = "False"
    break
while True:
    DIGIT = input("Do you want to use at least one digit (y/n) n --> ")
    if DIGIT == "Y" or DIGIT == "y":
        DIGIT = "True"
    else:
        DIGIT = "False"
    break

password = input("Enter your password --> ")

while not is_valid_password(password):
    print("Invalid password!")
    password = input("Enter your password --> ")
print("Your password is valid and made of {} characters and is {}".format(len(password), password))
