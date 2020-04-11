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
score = 0
score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Enter score: "))

if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
