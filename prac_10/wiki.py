# wiki.py

from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        try:
            # Attempt to fetch the Wikipedia page and pass title and summary to the template
            page = wikipedia.page(query)
            return render_template('results.html', title=page.title, summary=page.summary)
        except wikipedia.exceptions.DisambiguationError as e:
            # Handle disambiguation error
            return render_template('error.html', message="Disambiguation error: Please be more specific with your search.")
        except wikipedia.exceptions.HTTPTimeoutError:
            # Handle request timeout error
            return render_template('error.html', message="Request Timeout: The request to Wikipedia took too long.")
        except wikipedia.exceptions.PageError:
            # Handle page not found error
            return render_template('error.html', message="Page not found: No Wikipedia page matching your search.")
    return render_template('search.html')

@app.route('/about')
def about():
    # Simple about page template
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
