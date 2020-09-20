from typing import List, Iterable

from adapters.repository import AbstractRepository
from domain.movie import Movie
from domain.actor import Actor
from domain.director import Director
from domain.genre import Genre


class NonExistentMovieException(Exception):
    pass


class UnknownUserException(Exception):
    pass


# def add_comment(article_id: int, comment_text: str, username: str, repo: AbstractRepository):
#     # Check that the article exists.
#     article = repo.get_article(article_id)
#     if article is None:
#         raise NonExistentArticleException
#
#     user = repo.get_user(username)
#     if user is None:
#         raise UnknownUserException
#
#     # Create comment.
#     comment = make_comment(comment_text, user, article)
#
#     # Update the repository.
#     repo.add_comment(comment)


def get_first_actor(repo: AbstractRepository):
    actors = repo.get_actor()
    return actors[0]


def get_last_actor(repo: AbstractRepository):
    actors = repo.get_actor()
    return actors[-1]


def get_first_genre(repo: AbstractRepository):
    genres = repo.get_genre()
    return genres[0]


def get_last_genre(repo: AbstractRepository):
    genres = repo.get_genre()
    return genres[-1]


def get_first_director(repo: AbstractRepository):
    directors = repo.get_director()
    return directors[0]


def get_last_director(repo: AbstractRepository):
    directors = repo.get_director()
    return directors[-1]


def get_movies_by_actor(actor_full_name, repo: AbstractRepository):
    actor = Actor(actor_full_name)
    movies = repo.get_movies_by_actor(actor)

    movies_dto = list()
    prev_actor = next_actor = None

    if len(movies) > 0:
        prev_actor = repo.get_previous_actor(actor)
        next_actor = repo.get_next_actor(actor)

        # Convert Movies to dictionary form.
        movies_dto = movies_to_dict(movies)

    return movies_dto, prev_actor, next_actor


def get_movies_by_genre(genre_name, repo: AbstractRepository):
    genre = Genre(genre_name)
    movies = repo.get_movies_by_genre(genre)

    movies_dto = list()
    prev_genre = next_genre = None

    if len(movies) > 0:
        prev_genre = repo.get_previous_genre(genre)
        next_genre = repo.get_next_genre(genre)

        # Convert Movies to dictionary form.
        movies_dto = movies_to_dict(movies)

    return movies_dto, prev_genre, next_genre


def get_movies_by_director(director_name, repo: AbstractRepository):
    director = Director(director_name)
    movies = repo.get_movies_by_director(director)

    movies_dto = list()
    prev_director = next_director = None

    if len(movies) > 0:
        prev_director = repo.get_previous_director(director)
        next_director = repo.get_next_director(director)

        # Convert Movies to dictionary form.
        movies_dto = movies_to_dict(movies)

    return movies_dto, prev_director, next_director


# ============================================
# Functions to convert model entities to dicts
# ============================================

def movie_to_dict(movie: Movie):
    actor_string = ''
    for actor in movie.actors:
        actor_string += actor.actor_full_name + ', '
    genre_string = ''
    for genre in movie.genres:
        genre_string += genre.genre_name + ', '

    movie_dict = {
        'title': movie.title,
        'release_year': movie.release_year,
        'description': movie.description,
        'director': movie.director.director_full_name,
        'actors': actor_string,
        'genres': genre_string,
        'runtime_minutes': movie.runtime_minutes,
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]

