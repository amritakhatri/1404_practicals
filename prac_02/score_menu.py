import random

def get_result(score):
    if 0 <= score <= 100:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"
    else:
        return "Invalid score"

def show_stars(score):
    return "*" * round(score)  # round score for better star representation

def get_valid_score():
    while True:
        try:
            score = float(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Welcome to the Score Program!")
    user_score = get_valid_score()

    MENU = """
    (G)et a valid score (must be 0-100 inclusive)
    (P)rint result
    (S)how stars
    (Q)uit
    """

    choice = None
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").upper()

        if choice == "G":
            user_score = get_valid_score()
        elif choice == "P":
            user_result = get_result(user_score)
            print(f"Result: {user_result}")
        elif choice == "S":
            stars = show_stars(user_score)
            print(f"Stars: {stars}")
        elif choice == "Q":
            print("Thank you for using the Score Program. Goodbye!")
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
