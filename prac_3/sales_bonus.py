"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""


def main():
    sales = float(input("Please enter your sale = "))
    while sales >= 0:

        if sales >= 1000:
            print("You have 15% OFF")
            print("Your purchase is ", sales - (sales * (15 / 100)))
        else:
            print("You have 10% OFF")
            print("Your purchase is ", sales - (sales * (10 / 100)))
        sales = float(input("Please enter your sale = "))


main()
