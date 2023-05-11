from model import db, User, Movie,Rating, connect_to_db

def create_user(email, password):
    '''Create and return a user.'''
    user = User(email=email, password=password)
    return user

def get_users():
    '''Get alls the users in the database'''
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)


def create_movie(title,overview,release_date,poster_path):
    '''Create a new movie'''
    movie = Movie(title=title,overview=overview,release_date=release_date,poster_path=poster_path)
    return movie

def get_movies():
    '''Returns all movies from the database'''
    return Movie.query.all()

def get_movie_by_id(movie_id):
    return Movie.query.get(movie_id)

def create_rating(score,user,movie):
    '''Create rating for a specific movie by a specific user'''
    rating = Rating(score=score,movie=movie,user=user)

    return rating

if __name__ == '__main__':
    from server import app
    connect_to_db(app)