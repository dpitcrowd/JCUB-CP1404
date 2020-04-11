"""
My broken score
Someone (it's not polite to say who) was trying to write a program 
to tell the user if their score is invalid, bad, passable or excellent, 
but their code is in the "bad" category and doesn't work.
Rewrite the following programming attempt using the most efficient 
if-elif-else 'ladder' you can.

The intention is that the score must be between 0 and 100 inclusive; 
90 or more is excellent; 50 or more is a pass; below 50 is bad.
"""


def result(score):
    """ Print the final score"""
    if score >= 90:
        print("Your final result is Excellent")
    elif score >= 50:
        print("Your final result is Passable")
    else:
        print("Your final result is Bad")
    print()


def main():
    """ Main function"""
    import random

    score = float(input("Enter score: "))            # Get the score
    while score < 0 or score > 100:
        """ Check input"""
        print("Invalid score")
        score = float(input("Enter score: "))

    """ Run result function to print the final result"""
    result(score)

    """ Run result function to print random result"""
    score = random.randint(0,100)
    result(score)
    print("The random score was {}".format(score))

main()