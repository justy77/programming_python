# list of dictionaries
movies = [
    {"name": "Casablanca", "year": 1942},
    {"name": "Forrest Gump", "year": 1994},
    {"name": "Avatar", "year": 2009},
    {"name": "Finding Nemo", "year": 2003},
    {"name": "Banana Joe", "year": 1984},
    {"name": "Mr. Bean", "year": 1997}
]

old_movies = []
new_movies = []

# movies that were released on year 2000 or later
print("These movies have been released in year 2000 or later:")
for movie in movies:
    if movie['year'] >= 2000:
        new_movies.append(movie['name'])
print(", ".join(new_movies))

# movies that were released before the year 2000
print("\nThese movies have been released before the year 2000:")
for movie in movies:
    if movie['year'] < 2000:
        old_movies.append(movie['name'])
print(", ".join(old_movies))
