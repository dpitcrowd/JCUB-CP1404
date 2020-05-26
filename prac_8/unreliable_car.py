from prac_8.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_num = randint(1, 100)

        if random_num >= self.reliability:
            distance = 0

        new_distance = super().drive(distance)
        return new_distance