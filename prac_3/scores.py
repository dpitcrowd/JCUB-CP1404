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


def out_file(scores, result):
    out_file = open("results.txt", "a")
    print("The random score was {:3d} and {}".format(scores, result), file=out_file)
    out_file.close()


def results(scores):
    """ Print the final score"""
    if scores >= 90:
        result = "your final result is Excellent"
        """ Write both score and result running out_file function"""
        out_file(scores, result)
    elif scores >= 50:
        result = "your final result is Passable"
        """ Write both score and result running out_file function"""
        out_file(scores, result)
    else:
        """ Write both score and result running out_file function"""
        result = "your final result is Bad"
        out_file(scores, result)


def main():
    """ Main function"""
    import random

    num_scores = int(input("Enter the number of scores(MAX entry 100): "))            # Get the number of scores
    while num_scores < 0 or num_scores > 100:
        """ Check input"""
        print("Invalid score")
        num_scores = int(input("Enter the number of scores(MAX entry 100): "))
    for i in range(0, num_scores, 1):
        scores = random.randint(0, 100)
        """ Check the result running result function"""
        results(scores)
    print("You can find your results opening results.txt")

main()