def average_imdb_score_by_category(movie_list, category):
    category_movies = [movie for movie in movie_list if movie["category"] == category]
    
    if not category_movies:
        return 0.0  # Return 0.0 if there are no movies in the specified category

    total_score = sum(movie["imdb"] for movie in category_movies)
    average = total_score / len(category_movies)
    return average

movies = [
]

category_name = "Romance"  # Replace with the category you want to calculate the average for
average_score = average_imdb_score_by_category(movies, category_name)
print(f"Average IMDB Score for {category_name}: {average_score:.2f}")
