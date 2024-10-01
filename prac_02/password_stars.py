MIN_PASSWORD_LENGTH = 8

def main():
    password = get_password()
    print("Password accepted! Printing asterisks:")
    print_asterisks(password)

def get_password():
    while True:
        password = input("Enter your password: ")
        if len(password) < MIN_PASSWORD_LENGTH:
            print(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long. Try again.")
        else:
            return password

def print_asterisks(password):
    print("*" * len(password))

if __name__ == "__main__":
    main()
