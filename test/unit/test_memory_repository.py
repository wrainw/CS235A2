
from domain.actor import Actor
from domain.director import Director
from domain.genre import Genre
from domain.movie import Movie
from domain.review import Review
from domain.user import User


def test_repository_can_add_a_user(in_memory_repo):
    user = User('Dave', '123456789')
    in_memory_repo.add_user(user)

    assert in_memory_repo.get_user('dave') is user


def test_repository_does_not_retrieve_a_non_existent_user(in_memory_repo):
    user = in_memory_repo.get_user('prince')
    assert user is None


def test_repository_can_retrieve_movie_count(in_memory_repo):
    number_of_movies = in_memory_repo.get_number_of_movies()

    # Check that the query returned 1000 Movies.
    assert number_of_movies == 1000


def test_repository_can_add_movie(in_memory_repo):
    movie = Movie('abc', 2000)
    in_memory_repo.add_movie(movie)

    assert in_memory_repo.get_movie('abc') is movie


def test_repository_can_retrieve_movie(in_memory_repo):
    movie = in_memory_repo.get_movie('Sing')

    # Check that the movie has the expected title.
    assert movie.title == 'Sing'


def test_repository_does_not_retrieve_a_non_existent_movie(in_memory_repo):
    movie = in_memory_repo.get_movie('def')
    assert movie is None


def test_repository_can_retrieve_movies_by_actor(in_memory_repo):
    movies = in_memory_repo.get_movies_by_actor(Actor('Chris Pratt'))

    assert len(movies) == 7


def test_repository_can_retrieve_movies_by_genre(in_memory_repo):
    movies = in_memory_repo.get_movies_by_genre(Genre('Action'))

    assert len(movies) == 303


def test_repository_can_retrieve_movies_by_director(in_memory_repo):
    movies = in_memory_repo.get_movies_by_director(Director('James Gunn'))

    assert len(movies) == 3


def test_repository_can_get_first_movie(in_memory_repo):
    movie = in_memory_repo.get_first_movie()
    assert movie.title == '(500) Days of Summer'


def test_repository_can_get_last_movie(in_memory_repo):
    movie = in_memory_repo.get_last_movie()
    assert movie.title == 'Zootopia'


def test_repository_get_previous_actor(in_memory_repo):
    actor = in_memory_repo.get_previous_actor(Actor('Chris Pratt'))

    assert actor.actor_full_name == 'Chris Pine'


def test_repository_get_next_actor(in_memory_repo):
    actor = in_memory_repo.get_next_actor(Actor('Chris Pratt'))

    assert actor.actor_full_name == 'Chris Rock'


def test_repository_get_previous_genre(in_memory_repo):
    genre = in_memory_repo.get_previous_genre(Genre('Horror'))

    assert genre.genre_name == 'History'


def test_repository_get_next_genre(in_memory_repo):
    genre = in_memory_repo.get_next_genre(Genre('Horror'))

    assert genre.genre_name == 'Music'


def test_repository_get_previous_director(in_memory_repo):
    director = in_memory_repo.get_previous_director(Director('James Gunn'))

    assert director.director_full_name == 'James Gray'


def test_repository_get_next_director(in_memory_repo):
    director = in_memory_repo.get_next_director(Director('James Gunn'))

    assert director.director_full_name == 'James Lapine'


def test_repository_can_retrieve_comments(in_memory_repo):
    assert len(in_memory_repo.get_reviews()) == 0



