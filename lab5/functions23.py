def movies_by_category(movie_list, category):
    return [movie for movie in movie_list if movie["category"] == category]

movies = [
]

category_name = "Romance"  # Replace with the category you want to filter
result = movies_by_category(movies, category_name)
for movie in result:
    print(f"Name: {movie['name']}, Category: {movie['category']}")
