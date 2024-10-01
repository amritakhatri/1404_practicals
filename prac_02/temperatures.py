MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def display_menu():
    print(MENU)
    return input(">>> ").upper()


def main():
    choice = display_menu()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = 5 / 9 * (fahrenheit - 32)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")

        # Display menu again
        choice = display_menu()

    print("Thank you.")


if __name__ == "__main__":
    main()
