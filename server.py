"""Server for movie ratings app."""

from flask import Flask, render_template,request,flash,session,redirect,url_for

from model import db, connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'secrettunnel'
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movies')
def all_movies():
    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    '''Info about the specific movie'''
    movie = crud.get_movie_by_id(movie_id)
    return render_template('movie_details.html', movie = movie)

@app.route('/users')
def all_users():
    users = crud.get_users()

    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def show_user(user_id):
    '''Info about the specific movie'''
    user = crud.get_user_by_id(user_id)
    return render_template('user_details.html', user = user)

@app.route('/users', methods=['POST'])
def register_user(email,password):
    """Creates a new user"""
    user = crud.User()

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)
