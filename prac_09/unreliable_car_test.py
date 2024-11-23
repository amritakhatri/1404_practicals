"""
Test file for the UnreliableCar class.
"""

from unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class."""
    # Create a reliable and unreliable car
    reliable_car = UnreliableCar("Mostly Reliable", 100, 90)
    unreliable_car = UnreliableCar("Barely Reliable", 100, 20)

    # Drive each car multiple times and display the results
    for i in range(1, 6):
        print(f"Attempt {i}:")
        print(f"{reliable_car.name} drove {reliable_car.drive(10)} km")
        print(f"{unreliable_car.name} drove {unreliable_car.drive(10)} km")
        print()


if __name__ == "__main__":
    main()
