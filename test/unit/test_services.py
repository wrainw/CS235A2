
import pytest

from authentication.services import AuthenticationException
from movies import services as movies_services
from authentication import services as auth_services


def test_can_add_user(in_memory_repo):
    new_username = 'jz'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    user_as_dict = auth_services.get_user(new_username, in_memory_repo)
    assert user_as_dict['username'] == new_username

    # Check that password has been encrypted.
    assert user_as_dict['password'].startswith('pbkdf2:sha256:')


def test_cannot_add_user_with_existing_name(in_memory_repo):
    username = 'thorke'
    password = 'abcd1A23'
    auth_services.add_user(username, password, in_memory_repo)

    with pytest.raises(auth_services.NameNotUniqueException):
        auth_services.add_user(username, password, in_memory_repo)


def test_authentication_with_valid_credentials(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    try:
        auth_services.authenticate_user(new_username, new_password, in_memory_repo)
    except AuthenticationException:
        assert False


def test_authentication_with_invalid_credentials(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    with pytest.raises(auth_services.AuthenticationException):
        auth_services.authenticate_user(new_username, '0987654321', in_memory_repo)


def test_get_first_actor(in_memory_repo):
    actor = movies_services.get_first_actor(in_memory_repo)

    assert actor.actor_full_name == '50 Cent'


def test_get_last_actor(in_memory_repo):
    actor = movies_services.get_last_actor(in_memory_repo)

    assert actor.actor_full_name == 'Óscar Jaenada'


def test_get_first_genre(in_memory_repo):
    genre = movies_services.get_first_genre(in_memory_repo)

    assert genre.genre_name == 'Action'


def test_get_last_genre(in_memory_repo):
    genre = movies_services.get_last_genre(in_memory_repo)

    assert genre.genre_name == 'Western'


def test_get_first_director(in_memory_repo):
    director = movies_services.get_first_director(in_memory_repo)

    assert director.director_full_name == 'Aamir Khan'


def test_get_last_director(in_memory_repo):
    director = movies_services.get_last_director(in_memory_repo)

    assert director.director_full_name == 'Zackary Adler'


def test_get_movies_by_actor(in_memory_repo):
    movies_dto, prev_actor, next_actor = movies_services.get_movies_by_actor('Óscar Jaenada', in_memory_repo)

    assert len(movies_dto) == 1


def test_get_movies_by_genre(in_memory_repo):
    movies_dto, prev_genre, next_genre = movies_services.get_movies_by_genre('Action', in_memory_repo)

    assert len(movies_dto) == 303


def test_get_movies_by_director(in_memory_repo):
    movies_dto, prev_director, next_director = movies_services.get_movies_by_director('Aamir Khan', in_memory_repo)

    assert len(movies_dto) == 1
