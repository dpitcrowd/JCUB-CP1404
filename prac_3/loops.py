"""
c. print n stars. Ask the user for a number, then print that many stars (*), all on one line
Note: this is a very simple loop for repeating n times. We use for loops for "definite" iteration like this. while loops are used for "indefinite" iteration (like repeating while a user input is incorrect).
"""
stars = int(input("How many stars do you need? --> "))
print("print in just one line")
for i in range(stars):
  print("*", end ="")

print()

print("print n lines of increasing stars")
#i = 0
for i in range(stars):
  for j in range(i):
    print("*", end="")
  print()
    
