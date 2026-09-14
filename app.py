# Import Flask to create our web application
# render_template is used to load HTML files from the templates folder
from flask import Flask, render_template

# Import the movie data from our movies.py file
from data.movies import movies


# Create the Flask application
app = Flask(__name__)


# Home page route
# When a user visits: http://localhost:5000/
# Flask will execute this function
@app.route("/")
def home():

    # Send the movie data to index.html
    # The HTML page will use this data to create movie cards
    return render_template("index.html", movies=movies)


# Movie details route
# <int:movie_id> means the URL will contain a movie ID
# Example: http://localhost:5000/movie/1
@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):

    # Search for the movie whose ID matches the ID in the URL
    movie = next((m for m in movies if m["id"] == movie_id), None)

    # If no movie is found, return a 404 error
    if movie is None:
        return "Movie not found", 404

    # Send the selected movie's data to movie.html
    return render_template("movie.html", movie=movie)


# This block runs the Flask application
# when we execute: python app.py
if __name__ == "__main__":

    # Start the Flask development server
    # debug=True automatically reloads the server when we change code
    app.run(debug=True)