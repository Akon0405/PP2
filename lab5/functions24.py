def average_imdb_score(movie_list):
    if not movie_list:
        return 0.0  # Return 0.0 if the list is empty to avoid division by zero

    total_score = sum(movie["imdb"] for movie in movie_list)
    average = total_score / len(movie_list)
    return average

movies = [
    # Your list of movies here
]

average_score = average_imdb_score(movies)
print(f"Average IMDB Score: {average_score:.2f}")
