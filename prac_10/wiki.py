""" wiki.py - A program to search for Wikipedia pages and display their details."""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError


def main():
    """Main program loop that prompts for user input and displays the result."""
    print("Welcome to the Wikipedia Page Search Program!")

    while True:
        # Prompt the user for input
        title = input("Enter page title: ").strip()

        # Exit the loop if the input is blank
        if not title:
            print("Thank you.")
            break

        # Fetch the page information
        result_title, summary, url = fetch_wikipedia_page(title)

        # Display the results or errors
        if summary:
            print(f"\n{result_title}\n{summary}\n{url}\n")
        else:
            print(result_title)  # Display the error message


def fetch_wikipedia_page(title):
    """Fetch and return the title, summary, and URL of the Wikipedia page."""
    try:
        # Attempt to get the page based on the title
        page = wikipedia.page(title, autosuggest=False)
        return page.title, page.summary, page.url
    except DisambiguationError as e:
        # Handle disambiguation errors
        return f"We need a more specific title. Try one of the following: {', '.join(e.options)}", None, None
    except PageError:
        # Handle page errors (page not found)
        return f"Page id \"{title}\" does not match any pages. Try another id!", None, None
    except Exception as e:
        # Handle other general errors
        return f"An error occurred: {str(e)}", None, None


if __name__ == "__main__":
    main()

