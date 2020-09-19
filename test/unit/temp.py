import os
from adapters import memory_repository
from adapters.memory_repository import MemoryRepository
from domain.actor import Actor
from domain.director import Director
from domain.genre import Genre
from domain.movie import Movie
from domain.review import Review
from domain.user import User

TEST_DATA_PATH = os.path.join('E:', os.sep, 'git', 'CS235A2', 'adapters', 'data')

repo = MemoryRepository()
memory_repository.populate(TEST_DATA_PATH, repo)

print(len(repo.get_movies_by_actor(Actor('Chris Pratt'))))
print(len(repo.get_movies_by_genre(Genre('Action'))))
print(len(repo.get_movies_by_director(Director('James Gunn'))))
print(repo.get_previous_actor(Actor('Chris Pratt')))
print(repo.get_next_actor(Actor('Chris Pratt')))
print(repo.get_previous_genre(Genre('Horror')))
print(repo.get_next_genre(Genre('Horror')))
print(repo.get_previous_director(Director('James Gunn')))
print(repo.get_next_director(Director('James Gunn')))
