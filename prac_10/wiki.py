""" wiki.py - A program to search for Wikipedia pages and display their details."""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

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

# Time taken: 15 mins
