import math
from collections import defaultdict
from collections import Counter

# You may not add any other imports

# For each function, replace "pass" with your code

# --- TASK 1: READING DATA ---

# 1.1
def read_ratings_data(f):
    pass

# 1.2
def read_movie_genre(f):
    pass

# --- TASK 2: PROCESSING DATA ---

# 2.1
def create_genre_dict(d):
    pass

# 2.2
def calculate_average_rating(d):
    pass

# --- TASK 3: RECOMMENDATION ---

# 3.1
def get_popular_movies(d, n=10):
    pass

# 3.2
def filter_movies(d, thres_rating=3):
    pass

# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    pass

# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    pass

# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    pass

# --- TASK 4: USER FOCUSED ---

# 4.1
def read_user_ratings(f):
    pass

# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    pass

# 4.3
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    pass

# --- main function for your testing ---
def main():
    pass

main()
