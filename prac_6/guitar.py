# Note: It would be better to get the current year from the system clock
# and you might like to do that: lookup the "datetime" module
YEAR = 2020
VINTAGE = 25


class Guitar:
    """Guitar class"""
    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """String representation"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Calculate age"""
        return YEAR - self.year

    def is_vintage(self):
        """Is the guitar?"""
        return self.get_age() >= VINTAGE
#########################################################################################
    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year