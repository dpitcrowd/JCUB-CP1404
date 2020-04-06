"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0

while not finished:
    try:
        my_int = int(input("Insert a valid integer. "))
        result = result + my_int
    except ValueError:
        print("Please enter a valid integer.")
    finished = True
print("Valid result is:", result)