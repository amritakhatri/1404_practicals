def main():
    # Dictionary of programming languages and their inventors
    languages = {
        "Python": "Guido van Rossum",
        "Java": "James Gosling",
        "C": "Dennis Ritchie",
        "JavaScript": "Brendan Eich"
    }

    # Display the languages available
    print("Languages available:", ", ".join(languages.keys()))

    # User input to look up an inventor
    language = input("Enter a programming language: ").title()

    # Check and display the inventor or a not-found message
    inventor = languages.get(language)
    if inventor:
        print(f"The inventor of {language} is {inventor}.")
    else:
        print(f"Sorry, {language} is not in the dictionary.")


if __name__ == "__main__":
    main()
