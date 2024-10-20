"""
Emails to Names Program
Estimate: 30 minutes
Actual: 50 minutes
"""

def main():
    emails_to_names = {}
    email = input("Email: ")

    while email != "":
        name = extract_name_from_email(email)
        # Prompt user to confirm or update name
        correct = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if correct not in ("", "y"):
            name = input("Name: ").strip()
        emails_to_names[email] = name
        email = input("Email: ")

    print("\nUser Details:")
    for email, name in emails_to_names.items():
        print(f"{name} ({email})")

def extract_name_from_email(email):
    """Extract the name from the given email."""
    name_part = email.split('@')[0]
    name = " ".join(name_part.split('.')).title()
    return name

if __name__ == "__main__":
    main()
