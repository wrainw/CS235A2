
from domain.actor import Actor
from domain.director import Director
from domain.genre import Genre
from domain.movie import Movie
from domain.review import Review
from domain.user import User

import pytest


@pytest.fixture()
def actor():
    actor = Actor('Bob')
    actor.add_actor_colleague(Actor('Alice'))
    return actor


@pytest.fixture()
def director():
    director = Director("Taika Waititi")
    return director


@pytest.fixture()
def genre():
    genre = Genre('horror')
    return genre


@pytest.fixture()
def movie():
    movie = Movie('abc', 2000)
    movie.description = 'def'
    movie.runtime_minutes = 120
    return movie


@pytest.fixture()
def review(movie):
    review = Review(movie, 'interesting', 10)
    return review


@pytest.fixture()
def user():
    return User('dbowie', '1234567890')


def test_actor_construction(actor):
    assert actor.actor_full_name == 'Bob'
    assert actor.check_if_this_actor_worked_with(Actor('Alice'))
    assert repr(actor) == '<Actor Bob>'


def test_director_construction(director):
    assert director.director_full_name == 'Taika Waititi'
    assert repr(director) == "<Director Taika Waititi>"


def test_genre_construction(genre):
    assert genre.genre_name == 'horror'
    assert repr(genre) == "<Genre horror>"


def test_review_construction(movie, review):
    assert review.movie == movie
    assert review.review_text == 'interesting'
    assert review.rating == 10


def test_user_construction(user):
    assert user.user_name == 'dbowie'
    assert user.password == '1234567890'
    assert repr(user) == '<User dbowie>'

    for review in user.reviews:
        # User should have an empty list of Comments after construction.
        assert False


def test_movie_construction(movie):
    assert movie.title == 'abc'
    assert movie.release_year == 2000
    assert movie.description == 'def'

    assert movie.runtime_minutes == 120

    assert repr(movie) == '<Movie abc, 2000>'


def test_movie_less_than_operator():
    movie_1 = Movie('abc', 1999)

    movie_2 = Movie('abc', 2000)

    assert movie_1 < movie_2



