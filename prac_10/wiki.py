""" wiki.py - A program to search for Wikipedia pages and display their details."""


import wikipedia

def main():
    """Main function to prompt user for input and display Wikipedia page details."""
    title = input("Enter page title: ").strip()

    while title:  # Replace while True with a condition based on user input
        title_result, summary_result, url_result = fetch_wikipedia_page(title)

        if summary_result:
            print(f"{title_result}\n{summary_result}\n{url_result}\n")
        else:
            print(title_result)

        # Prompt again for the next title
        title = input("Enter page title: ").strip()

    print("Thank you.")

def fetch_wikipedia_page(title):
    """Fetch and return the title, summary, and URL of the Wikipedia page."""
    try:
        # Attempt to get the page based on the title
        page = wikipedia.page(title)
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
