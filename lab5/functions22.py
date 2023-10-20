def movies_above_5_5(movie_list):
    return [movie for movie in movie_list if movie["imdb"] > 5.5]

movies = [
    # Your list of movies here
]

result = movies_above_5_5(movies)
for movie in result:
    print(f"Name: {movie['name']}, IMDB: {movie['imdb']}")
