"""
My shop calculator
A shop requires a small program that would allow them to quickly work out 
the total price for a number of items, each with different prices.

The program allows the user to enter the number of items and the price of 
each different item. Then the program computes and displays the total price 
of those items.

If the total price is over $100, then a 10% discount is applied to that total 
before the amount is displayed on the screen.

The output should look something like (bold text represents user input)
"""

# My variables
num_items = 0
tot = 0

# While loop true at the begining to check items number
while num_items <= 0:
    print("Please a valid number of items")
    num_items = int(input("Number of items: "))
# Loop for for asking the price of every item
for i in range(num_items):
    price = float(input("Please insert price for item " + str(i+1) + " --> "))
    tot = tot + price
# Condition to apply a discount
if tot > 100:
    tot = tot * 0.9

# Print total amount
#print("Total amount for ", num_items, " items is $", tot, sep='')
# Formatting total amount
print("Total price for {} items is ${:.2f}".format(num_items, tot))
