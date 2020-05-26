from prac_8.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """fare"""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return a string"""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)