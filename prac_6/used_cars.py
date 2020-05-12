"""CP1404/CP5632 Practical - Client code to use the Car class."""
"""
Note that  the  import  has a folder ( module ) in it.
I don't  want to rename  my  folders so I changed from 
prac_06.car import Car into from prac_6.car import Car
"""

from prac_6.car import Car


def main():
    """Demo test code to show how to use car class."""
    # Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo = Car(100, 'Limo')

    # Add 20 more units of fuel to this new car object using the add method.
    limo.add_fuel(20)

    # Print the amount of fuel in the car.
    print('\nTotal amount of fuel is --> {}'.format(limo.fuel))

    # Attempt to drive the car 115km using the drive method.
    limo.drive(115)

    # Print the car's odometer reading.
    print('Tha car odometer reading is --> {}'.format(limo.odometer))

    # Now add the __str__ method to the Car class in car.py.
    print("Car {self.fuel}, {self.odometer}".format(self=limo))

    # Now add a name field to the Car class (in car.py), and adjust
    # the __init__ and __str__ methods to set and display this respectively.

    # In your used_cars.py program, just print your car object/s to make sure
    # that the __str__ method is working as expected.
    print('{self.car_name}, {self.fuel}, {self.odometer}'.format(self=limo))
main()