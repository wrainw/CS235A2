import os
from adapters import memory_repository
from adapters.memory_repository import MemoryRepository
from domain.actor import Actor
from domain.director import Director
from domain.genre import Genre
from domain.movie import Movie
from domain.review import Review
from domain.user import User
from movies import services as movies_services
from authentication import services as auth_services

TEST_DATA_PATH = os.path.join('E:', os.sep, 'git', 'CS235A2', 'adapters', 'data')

repo = MemoryRepository()
memory_repository.populate(TEST_DATA_PATH, repo)

# print(len(repo.get_movies_by_actor(Actor('Chris Pratt'))))
# print(len(repo.get_movies_by_genre(Genre('Action'))))
# print(len(repo.get_movies_by_director(Director('James Gunn'))))
# print(repo.get_previous_actor(Actor('Chris Pratt')))
# print(repo.get_next_actor(Actor('Chris Pratt')))
# print(repo.get_previous_genre(Genre('Horror')))
# print(repo.get_next_genre(Genre('Horror')))
# print(repo.get_previous_director(Director('James Gunn')))
# print(repo.get_next_director(Director('James Gunn')))

# actor = movies_services.get_first_actor(repo)
# print(actor.actor_full_name)
# actor = movies_services.get_last_actor(repo)
# print(actor.actor_full_name)
# genre = movies_services.get_first_genre(repo)
# print(genre.genre_name)
# genre = movies_services.get_last_genre(repo)
# print(genre.genre_name)
# director = movies_services.get_first_director(repo)
# print(director.director_full_name)
# director = movies_services.get_last_director(repo)
# print(director.director_full_name)
# movies_dto, prev_actor, next_actor = movies_services.get_movies_by_actor('Óscar Jaenada', repo)
# print(len(movies_dto), prev_actor, next_actor)
# movies_dto, prev_genre, next_genre = movies_services.get_movies_by_genre('Action', repo)
# print(len(movies_dto), prev_genre, next_genre)
# movies_dto, prev_director, next_director = movies_services.get_movies_by_director('Aamir Khan', repo)
# print(len(movies_dto), prev_director, next_director)