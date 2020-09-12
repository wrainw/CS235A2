import csv
import os
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

#from werkzeug.security import generate_password_hash

from adapters.repository import AbstractRepository, RepositoryException
from adapters.movie_file_csv_reader import MovieFileCSVReader
from domain.actor import Actor
from domain.director import Director
from domain.genre import Genre
from domain.movie import Movie
from domain.review import Review
from domain.user import User


class MemoryRepository(AbstractRepository):
    # Movie ordered by name and year

    def __init__(self):
        self._movies = list()
        self._actors = list()
        self._directors = list()
        self._genres = list()
        self._users = list()
        self._reviews = list()

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username) -> User:
        return next((user for user in self._users if user.user_name == username), None)

    def add_movie(self, movie: Movie):
        insort_left(self._movies, movie)

    def get_movie(self, title: str) -> Movie:
        return next((movie for movie in self._movies if movie.title == title), None)

    def get_movies_by_year(self, target_year: int) -> List[Movie]:
        return [movie for movie in self._movies if movie.release_year == target_year]

    def get_number_of_movies(self):
        return len(self._movies)

    def get_first_movie(self) -> Movie:
        movie = None

        if len(self._movies) > 0:
            movie = self._movies[0]
        return movie

    def get_last_movie(self) -> Movie:
        movie = None

        if len(self._movies) > 0:
            movie = self._movies[-1]
        return movie

    def get_movies_by_actor(self, actor):
        return [movie for movie in self._movies if actor in movie.actors]

    def get_movies_by_genre(self, genre):
        return [movie for movie in self._movies if genre in movie.genres]

    def get_movies_by_director(self, director):
        return [movie for movie in self._movies if movie.director == director]

    def add_actor(self, actor: Actor):
        self._actors.append(actor)

    def get_actor(self) -> List[Actor]:
        return self._actors

    def add_director(self, director: Director):
        self._directors.append(director)

    def get_director(self) -> List[Director]:
        return self._directors

    def add_genre(self, genre: Genre):
        self._genres.append(genre)

    def get_genre(self) -> List[Genre]:
        return self._genres

    def add_review(self, review: Review):
        if review.movie is None:
            raise RepositoryException('Review not correctly attached to a Movie')
        else:
            self._reviews.append(review)

    def get_reviews(self):
        return self._reviews

    # Helper method to return article index.
    def movie_index(self, movie: Movie):
        index = bisect_left(self._movies, movie)
        if index != len(self._movies) and self._movies[index].title == movie.title:
            return index
        raise ValueError


def populate(data_path: str, repo: MemoryRepository):
    file_name = os.path.join(data_path, 'Data1000Movies.csv')
    movie_file_reader = MovieFileCSVReader(file_name)
    movie_file_reader.read_csv_file()
    for movie in movie_file_reader.dataset_of_movies:
        repo.add_movie(movie)
    for actor in movie_file_reader.dataset_of_actors:
        repo.add_actor(actor)
    for director in movie_file_reader.dataset_of_directors:
        repo.add_director(director)
    for genre in movie_file_reader.dataset_of_genres:
        repo.add_genre(genre)
