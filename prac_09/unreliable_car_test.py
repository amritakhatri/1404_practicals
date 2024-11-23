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
    # Assert tests to validate reliability functionality
    reliable_car = UnreliableCar("Test Reliable", 100, 100)
    unreliable_car = UnreliableCar("Test Unreliable", 100, 0)

    # Test that a fully reliable car always drives
    assert reliable_car.drive(10) == 10, "Fully reliable car failed to drive expected distance"
    assert reliable_car.drive(0) == 0, "Fully reliable car failed to drive 0 distance"

    # Test that a fully unreliable car never drives
    assert unreliable_car.drive(10) == 0, "Fully unreliable car drove when it shouldn't"
    assert unreliable_car.drive(0) == 0, "Fully unreliable car failed edge case for 0 distance"

    print("All tests passed!")


if __name__ == "__main__":
    main()
