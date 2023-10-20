def is_above_5_5(movie):
    return movie["imdb"] > 5.5

movie = {
    "name": "The Help",
    "imdb": 8.0,
    "category": "Drama"
}

result = is_above_5_5(movie)
print(result)  # True
