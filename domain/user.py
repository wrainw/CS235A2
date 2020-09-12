from domainmodel.movie import Movie
from domainmodel.review import Review


class User:

    def __init__(self, user_name, password):
        self._user_name = user_name.strip().lower()
        self._password = password
        self._watched_movies = list()
        self._reviews = list()
        self._time_spent_watching_movies_minutes = 0

    @property
    def user_name(self):
        return self._user_name

    @property
    def password(self):
        return self._password

    @property
    def watched_movies(self):
        return self._watched_movies

    @property
    def reviews(self):
        return self._reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self._time_spent_watching_movies_minutes

    def __repr__(self):
        return f"<User {self._user_name}>"

    def __eq__(self, other):
        return self._user_name == other.user_name

    def __lt__(self, other):
        return self._user_name < other.user_name

    def __hash__(self):
        return hash(self._user_name)

    def watch_movie(self, movie):
        self._watched_movies.append(movie)
        self._time_spent_watching_movies_minutes += movie.get_runtime_minutes()

    def add_review(self, review):
        self._reviews.append(review)


# user1 = User(' Martin', 'pw12345')
# user2 = User('Ian ', 'pw67890')
# user3 = User('Daniel', 'pw87465')
# print(user1)
# print(user2)
# print(user3)
#
# movies = [Movie("Moana", 2016), Movie("Guardians of the Galaxy", 2014)]
# movies[0].runtime_minutes = 107
# movies[1].runtime_minutes = 121
# user = User("Martin", "pw12345")
# print(user.watched_movies)
# print(user.time_spent_watching_movies_minutes)
# for movie in movies:
#     user.watch_movie(movie)
# print(user.watched_movies)
# print(user.time_spent_watching_movies_minutes)