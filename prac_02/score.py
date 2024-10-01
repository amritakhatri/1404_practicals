import random

def main():
    # Asking the user for their score
    user_score = float(input("Enter your score (0-100): "))
    user_result = get_result(user_score)
    print(f"Your result: {user_result}")

    # Generating a random score
    random_score = random.randint(0, 100)
    random_result = get_result(random_score)
    print(f"Random score ({random_score}): {random_result}")

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

if __name__ == "__main__":
    main()
