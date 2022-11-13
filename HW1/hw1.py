import math
from collections import defaultdict
from collections import Counter

# You may not add any other imports

# For each function, replace "pass" with your code

# --- TASK 1: READING DATA ---

# 1.1
def read_ratings_data(f):
    movieRatingFile = open(f, "r")
    movie_to_ratings = dict()

    for line in movieRatingFile:
        movie, rating, _ = line.split('|')
        if movie not in movie_to_ratings.keys():
            movie_to_ratings[movie] = [float(rating)]
        else:
            movie_to_ratings[movie].append(float(rating))
    return movie_to_ratings

# 1.2
def read_movie_genre(f):
    genreMovieFile = open(f, "r")
    movie_to_genre = dict()
    
    for line in genreMovieFile:
        genre, _, movie = line.strip().split('|')
        movie_to_genre[movie] = genre
    return movie_to_genre

# --- TASK 2: PROCESSING DATA ---

# 2.1
def create_genre_dict(d):
    movie_to_genre = d
    genre_to_movies = dict()
    
    for key in movie_to_genre.keys():
        if movie_to_genre[key] not in genre_to_movies:
            genre_to_movies[movie_to_genre[key]] = [key]
        else:
            genre_to_movies[movie_to_genre[key]].append(key)
    return genre_to_movies

# 2.2
def calculate_average_rating(d):
    movie_to_ratings = d
    movie_to_average_rating = dict()
   
    for key in movie_to_ratings.keys():
        sum = 0
        avg = 0
        for value in movie_to_ratings[key]:
            sum = sum + value

        avg = sum/len(movie_to_ratings[key]) 
        movie_to_average_rating[key] = avg
    return movie_to_average_rating

# --- TASK 3: RECOMMENDATION ---

# 3.1
def get_popular_movies(d, n=10):
    sorted_movies_dict = dict()
    popular_movies = dict()
    movie_to_average_rating = d

    if(len(movie_to_average_rating) < n):
        n = len(movie_to_average_rating)

    sorted_movies_dict = sorted(movie_to_average_rating, key = movie_to_average_rating.get, reverse=True)
    
    i = 0
    for key in sorted_movies_dict:
        if(i >= n):
            return popular_movies
        
        popular_movies[key] = movie_to_average_rating[key]
        i = i + 1

    return popular_movies
   
# 3.2
def filter_movies(d, thres_rating=3):
    filtered_movies = dict()
    movie_to_average_rating = d

    for movie, rating in movie_to_average_rating.items():
        if rating >=3: 
            filtered_movies[movie] = rating
    return filtered_movies

# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    
    popular_in_genre = dict()
    selected_genre = genre_to_movies[genre]

    if(len(selected_genre) < n):
        n = len(selected_genre)

    for key in selected_genre:
        popular_in_genre[key] = movie_to_average_rating[key]
    
    popular_in_genre_sorted = sorted(popular_in_genre, key = popular_in_genre.get, reverse=True)

    top_filtered = {}
    i = 0
    for key in popular_in_genre_sorted:
        if (i >= n):
            return top_filtered

        top_filtered[key] = popular_in_genre[key]
        i = i + 1

    return top_filtered

# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    genre_rating = dict()
    genre_Movies = genre_to_movies.get(genre)
    sum = 0; 
    average = 0; 

    for key, value in movie_to_average_rating.items():
        for i in genre_Movies: 
            if i == key: 
                genre_rating[key] = value
    
    for value in genre_rating.values(): 
        sum = sum + value

    average = sum/len(genre_rating)
    return average

# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    popularity_Genre = dict()

    for key in genre_to_movies.keys():
        if key not in popularity_Genre: 
            average_Rating_Genre = get_genre_rating(key,genre_to_movies,movie_to_average_rating)
            popularity_Genre[key] = average_Rating_Genre
    
    genrePopularityRating_Sorted = sorted(popularity_Genre.items(), key= lambda x: x[1], reverse=True)
    
    if len(genrePopularityRating_Sorted) < n: 
        return dict(genrePopularityRating_Sorted)
    else: 
        return dict(genrePopularityRating_Sorted[:n])

# --- TASK 4: USER FOCUSED ---

# 4.1
def read_user_ratings(f):
    movieRatingFile = open(f, "r")
    user_ratings_dict = dict()

    for line in movieRatingFile:
        movie, rating, userID = line.strip().split('|')
        tuple = (movie, rating)
        if userID not in user_ratings_dict.keys():    
            user_ratings_dict[userID] = [tuple]
        else:
            user_ratings_dict[userID].append(tuple)
    return user_ratings_dict

# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    
    top_user_genre = dict()
    movie_count = dict()
    movies_for_user = user_to_movies[user_id]

    for movie, rating in movies_for_user:
        if top_user_genre.get(movie_to_genre[movie]) == None:
            top_user_genre[movie_to_genre[movie]] = float(rating)
            movie_count[movie_to_genre[movie]] = 1
        else:
            top_user_genre[movie_to_genre[movie]] += float(rating)
            movie_count[movie_to_genre[movie]] += 1

    for movie in top_user_genre:
        top_user_genre[movie] = top_user_genre[movie] / movie_count[movie]

    maxMovie = max(top_user_genre, key = top_user_genre.get)
    return maxMovie

# 4.3
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):

    get_genre = get_user_genre(user_id, user_to_movies, movie_to_genre)
    getGenreDict= create_genre_dict(movie_to_genre)
    movies_in_genre = getGenreDict.get(get_genre)
    user_Movies = dict(user_to_movies.get(user_id))
    movies_users_watched = list(user_Movies.keys())

    movie_not_rated = [movies for movies in movies_in_genre if not movies in movies_users_watched]
    movies_not_rated_dict =  {movies: movie_to_average_rating[movies] for movies in movie_not_rated}

    sort_Movies = sorted(movies_not_rated_dict.items(), key= lambda x:x[1], reverse = True)
    
    if len(sort_Movies) < 3: 
        return dict(sort_Movies)
    else: 
        return dict(sort_Movies[:3])

# --- main function for your testing ---
def main():
    f1 = "movieRatingSample.txt"
    f2 = "genreMovieSample.txt"

    movie_to_ratings = read_ratings_data(f1) # 1.1
    movie_to_genre = read_movie_genre(f2) # 1.2
    genre_to_movies = create_genre_dict(movie_to_genre) # 2.1 - parameter from 1.2
    movie_to_average_rating = calculate_average_rating(movie_to_ratings) # 2.2 - parameter from 1.1
    popular_movies = get_popular_movies(movie_to_average_rating) # 3.1
    filtered_movies = filter_movies(movie_to_average_rating) # 3.2
    popular_in_genre = get_popular_in_genre("Action", genre_to_movies, movie_to_average_rating)  # 3.3
    genre_rating = get_genre_rating("Adventure", genre_to_movies, movie_to_average_rating)  # 3.4
    ans = genre_popularity(genre_to_movies, movie_to_average_rating) # 3.5 - parameter from 2.1 and 2.2
    user_to_movie_and_rating = read_user_ratings(f1) # 4.1
    top_genre_for_user = get_user_genre("18", user_to_movie_and_rating, movie_to_genre) # 4.2 - parameter from 4.1 and 1.2
    topRecommended = recommend_movies("18", user_to_movie_and_rating, movie_to_genre,movie_to_average_rating) # 4.2

main()
