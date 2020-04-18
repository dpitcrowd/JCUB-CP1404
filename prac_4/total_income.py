"""
Calculating a List of Cumulative Totals
"""


def show_incomes(incomes, monthly_revenue):
    """ Show the incomes report"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, monthly_revenue + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:1} - Income: ${:2.2f}     Total: ${:2.2f}".format(month, income, total))


def main():
    """ Show incomes report"""
    MONTHS = ["GEN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "SEP", "OCT", "NOV", "DEC"]
    incomes = []    # Empty list of incomes

    monthly_revenue = input("\t Please enter how many months you need to store \n\t --> ")

    """ Check the data entry """
    check = "False"
    while check == "False":
        try:
            monthly_revenue = int(monthly_revenue)
            check = "True"
            pass
        except ValueError:
            monthly_revenue = input("\t Please enter how many months you need to store \n\t --> ")

    """ Collect monthly earnings"""
    for month in range(1, monthly_revenue+1):
        income = float(input("Enter income for month " + str(month) + ": "))
        """ Check the data entry """
        check = "False"
        while check == "False":
            try:
                income = int(income)
                check = "True"
                pass
            except ValueError:
                income = input("\t Please enter how many months you need to store \n\t --> ")
        incomes.append(income)

    show_incomes(incomes, monthly_revenue)


main()