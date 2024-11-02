"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car

def main():
    """Demo test code to show how to use the Car class."""

    # Initial car object (my_car) for demo
    my_car = Car("My Car", 180)  # Added name parameter
    my_car.drive(30)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(my_car)  # This will use the __str__ method

    # New car object (limo) as per the practical instructions
    limo = Car("Limo", 100)  # Initialized with a name and 100 units of fuel
    limo.add_fuel(20)  # Add 20 units of fuel to limo
    print(f"{limo.name} fuel level after adding fuel: {limo.fuel}")

    # Attempt to drive limo 115 km
    distance_driven = limo.drive(115)
    print(f"{limo.name} drove {distance_driven} km")
    print(limo)  # This will use the __str__ method to show updated state

main()
